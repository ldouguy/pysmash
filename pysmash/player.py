from pysmash import api, brackets, utils
PLAYER_PREFIX = 'player/'

def show_region(player_id):
    uri = PLAYER_PREFIX + str(player_id)

    response = api.get(uri)

    region = response.get(u'entities').get(u'player').get(u'region')
    state = response.get(u'entities').get(u'player').get(u'state')
    country = response.get(u'entities').get(u'player').get(u'country')

    result = region

    if region is None and state is None:
        result = country

    if region is None:
        result = state

    return result

def show_gamerTag(player_id):
    uri = PLAYER_PREFIX + str(player_id)

    response = api.get(uri)

    gamerTag = response.get(u'entities').get(u'player').get(u'gamerTag')

    return gamerTag 
