{% for match in matches: %}
"{{match['name']}}" (league: {{match['league']['name']}} - game: {{match['videogame']['name']}}). PandaScore ID : {{match['id']}}
{% endfor %}
