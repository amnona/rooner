#!/usr/bin/env python

from roon import RoonApi

appinfo = {"extension_id": "python_roon_test",
           "display_name": "Python library for Roon",
           "display_version": "1.0.0",
           "publisher": "marcelveldt",
           "email": "mygreat@emailaddress.com"}


def get_roon_api():
    token = None
    try:
        token = open('mytokenfile').read()
    except:
        print('no token found. please accept new extension in roon')
    # get all zones (as dict)
    # print(roonapi.zones)

    # get all outputs (as dict)
    # print(roonapi.outputs)

    roon_api = RoonApi(appinfo, token, host='192.168.0.10')

    # save the token for next time
    with open('mytokenfile', 'w') as f:
        f.write(roonapi.token)

    return roon_api


print('connecting to roon api')
roonapi = get_roon_api()
print('connected to roon.')

# get all zones (as dict)
print('zones:')
print(roonapi.zones)

# get all outputs (as dict)
print('outputs:')
print(roonapi.outputs)

roonapi.play_genre(zone_or_output_id='1601a1017231251ef045b9767880bc709941', genre_name='Classical', shuffle=True)
