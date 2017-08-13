# coding: utf-8
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from itertools import chain
from os import environ
import urllib.parse
import logging
import json

try:
    from http import client
except ImportError:
    import httplib as client

from errbot import BotPlugin, botcmd

CONFIG_TEMPLATE = {'PANDASCORE_API_KEY': environ.get('PANDASCORE_API_KEY','your_api_key_here')}
PANDASCORE_API_ROOT = 'api.pandascore.co'

class Pandascore(BotPlugin):
    """
    Basic Pandascore API Err integration
    """

    def activate(self):
        super(Pandascore, self).activate()
        return

    def get_configuration_template(self):
        """
        Defines the configuration structure this plugin supports
        """
        return CONFIG_TEMPLATE

    def configure(self, configuration):
        if configuration is not None and configuration != {}:
            config = dict(chain(CONFIG_TEMPLATE.items(),
                                configuration.items()))
        else:
            config = CONFIG_TEMPLATE
        super().configure(config)
        return

    def query(self, endpoint, params=[]):
        """
        Makes API calls.
        """
        conn = client.HTTPSConnection(PANDASCORE_API_ROOT)
        conn.request('GET', '{endpoint}?token={token}{params}'.format(
            endpoint=endpoint,
            token=self.config['PANDASCORE_API_KEY'],
            params='&' + urllib.parse.urlencode(params) if params else ''
        ))
        return json.loads(conn.getresponse().read().decode())

    @botcmd(template='player')
    def player(self, message, args):
        """
        Fetch and display information about a given player.
        """
        if len(args) == 0:
            return 'You need to give me a name or PandaScore ID.'

        # Sanitize params
        params = {'filter[name]': args.strip('"')} if ('"' in args) else {'search[name]': args}

        # Fetch Pandascore API
        self.log.debug(f'Quering players endpoint with params: {params}')
        res = self.query('/players', params)

        # Handle result(s)
        self.log.debug(f'Got results: {res})')
        if len(res) > 1:
            return f"I found : {', '.join([p['name']+' (id: '+str(p['id'])+')' for p in res])}. Which one should I describe ?"
        elif len(res) == 0:
            return 'Sorry, I didn\'t found anyone with this name.'

        # FIXME: How do we check if the bakend support cards ?
        # # Respond with a card now
        # self.send_card(title=f"{res[0]['first_name']} \"{res[0]['name']}\" {res[0]['last_name']}",
        #                # body=response,
        #                thumbnail=res[0]['image_url'],
        #                fields=(('Game', res[0]['current_videogame']['name']),
        #                        ('Team', res[0]['current_team']['name']),
        #                        ('Role', res[0]['role']),
        #                        ('Pandascore ID', res[0]['id'])),
        #                in_reply_to=message  )

        # Return template context
        return {'player': res[0]}

    @botcmd(template='player')
    def whos(self, message, args):
        """
        Alias for "player".
        """
        return self.player(message, args)

    @botcmd(template='team')
    def team(self, message, args):
        """
        Fetch and display information about a given team.
        """
        self.log.debug(args)
        if len(args) == 0:
            return 'You need to give me a name or PandaScore ID.'

        # Sanitize params
        params = {'filter[name]': args.strip('"')} if ('"' in args) else {'search[name]': args}

        # Fetch Pandascore API
        self.log.debug(f'Quering teams endpoint with params: {params}')
        res = self.query('/teams', params)

        # Handle result(s)
        self.log.debug(f'Got results: {res})')
        if len(res) > 1:
            return f"I found : {', '.join([p['name']+' (id: '+str(p['id'])+')' for p in res])}. Which one should I describe ?"
        elif len(res) == 0:
            return 'Sorry, I didn\'t found any team with this name.'

        return {'team': res[0]}

    @botcmd(template='matches')
    def matches(self, message, args):
        """
        Fetch and display information about last 10 matches in DB. (EXPERIMENTAL)
        """
        # Fetch Pandascore API
        self.log.debug(f'Quering matches endpoint')
        res = self.query('/matches', {'per_page': 10})

        # Handle result(s)
        self.log.debug(f'Got results: {res})')

        # Return template context
        return {'matches': res}
