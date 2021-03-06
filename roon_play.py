#!/usr/bin/env python

from roonapi import RoonApi
from flask import Flask
import os

cdir = os.path.dirname(os.path.abspath(__file__))
token_file = os.path.join(cdir, 'mytokenfile')
app = Flask(__name__)


@app.route('/')
def main():
    return 'your mother was a hamster'


@app.route('/toggle')
def toggle():
    roonapi.playback_control(zone_or_output_id='16012da7c6f9d962e8ccb70a736cf19c2ca0', control='playpause')
    return 'toggle'


appinfo = {"extension_id": "python_roon_test",
           "display_name": "Python library for Roon",
           "display_version": "1.0.0",
           "publisher": "marcelveldt",
           "email": "mygreat@emailaddress.com"}


def get_roon_api():
    token = None
    try:
        token = open(token_file).read()
    except:
        print('no token found. please accept new extension in roon')
    # get all zones (as dict)
    # print(roonapi.zones)

    # get all outputs (as dict)
    # print(roonapi.outputs)

    roon_api = RoonApi(appinfo, token, host='192.168.0.9')

    # save the token for next time
    with open(token_file, 'w') as f:
        f.write(roon_api.token)

    return roon_api


print('connecting to roon api')
roonapi = get_roon_api()
print('connected to roon.')

app.run(port=5000)

print('almost')
roonapi.playback_control(zone_or_output_id='16012da7c6f9d962e8ccb70a736cf19c2ca0', control='playpause')
print('ready')

# # get all zones (as dict)
# print('zones:')
# print(roonapi.zones)

# # get all outputs (as dict)
# print('outputs:')
# print(roonapi.outputs)
