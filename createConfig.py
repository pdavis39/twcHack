import json

config = {'twcKey': <insert key here>, 'airQKey': <insert key here>}

with open('/Users/paul/Documents/twcHack/config.json', 'w') as f:
    json.dump(config, f)


