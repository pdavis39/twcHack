import json

with open('/Users/paul/Documents/twcHack/config.json', 'r') as f:
    config = json.load(f)

    twckey = config['twcKey']
    print twckey

    airQKey = config["airQKey"]
    print airQKey