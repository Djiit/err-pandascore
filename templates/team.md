{{team['name']}} ({{team['acronym']}}) is a {{team['current_videogame']['name']}} team. PandaScore ID: {{team['id']}}. Roster :
{% for player in team['players'] %}
* {{player['first_name']}} "{{player['name']}}" {{player['last_name']}}. PandaScore ID: {{player['id']}}{% endfor %}
