from pyzipcode import ZipCodeDatabase
import datetime

def getzip(x):
    zcdb = ZipCodeDatabase()
    zipcode = zcdb[x]
    now = datetime.datetime.now()
    # '2016-07-31'
    startDate = now.strftime("%Y-%m-%d")
    #print startDate
   # zip = zipcode.zip
    city = zipcode.city
    state = zipcode.state
    long = zipcode.longitude
    lat = zipcode.latitude
    return lat, long, startDate, city, state

#zip = getzip(20165)
#print zip
