# coding: utf-8
from errbot.backends.test import testbot

import pandascore


class TestPandascorePlugin(object):
    extra_plugin_dir = '.'

    def test_pandascore_player_no_args(self, testbot):
        testbot.push_message('!player')
        assert ('You need to give me a name or PandaScore ID.'
                in testbot.pop_message())

    def test_pandascore_player(self, testbot):
        testbot.push_message('!player "Faker"')
        assert ('Sanghyeok "Faker" Lee is a LoL player for SK telecom T1, as a mid. PandaScore ID : 585'
                in testbot.pop_message())

    def test_pandascore_player_wrong_arg(self, testbot):
        testbot.push_message('!player "notaplayer"')
        assert ('Sorry, I didn\'t found anyone with this name.'
                in testbot.pop_message())

    def test_pandascore_player_whos_alias(self, testbot):
        testbot.push_message('!whos "Faker"')
        assert ('Sanghyeok "Faker" Lee is a LoL player for SK telecom T1, as a mid. PandaScore ID : 585'
                in testbot.pop_message())

    def test_pandascore_team_no_args(self, testbot):
        testbot.push_message('!team')
        assert ('You need to give me a name or PandaScore ID.'
                in testbot.pop_message())

    def test_pandascore_team_wrong_arg(self, testbot):
        testbot.push_message('!team "notateam"')
        assert ('Sorry, I didn\'t found any team with this name.'
                in testbot.pop_message())
