from pysmash import api, brackets, utils
ENTRANT_PREFIX = 'entrant/'

def show_id(entrant_id):
    uri = ENTRANT_PREFIX + entrant_id

    response = api.get(uri)

    player_id = response.get(u'entities').get(u'player')[0].get(u'id')

    return player_id
