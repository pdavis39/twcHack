import json
import urllib2
import loadConfig


def airquality(x,y,z):
    startDate = z
    # documentation https://docs.airnowapi.org/forecastsbyzip/docs
    airQKey = loadConfig.airQKey
    lat = x
    long= y
    url = 'http://www.airnowapi.org/aq/forecast/latLong/?format=application/json&latitude='+str(lat)+'&longitude='+str(long)+'&date='+startDate+'&distance=25&API_KEY='+airQKey
    r = urllib2.urlopen(url)
    json_text = r.read().decode('utf-8')
    # Convert it to a Python dictionary
    aqresult = json.loads(json_text)
    if aqresult:
        return aqresult

#aqdata = airquality(39.044855,-77.38701,'2016-08-06')
#print aqdata
#print t
#for line in aqdata:
#    print line['Category'], line['ParameterName']
#    print
#print data['Category'][0]['Name']