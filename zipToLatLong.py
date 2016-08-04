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
   # zip_city = zipcode.city
   # zip_state = zipcode.state
    long = zipcode.longitude
    lat = zipcode.latitude
    return lat, long, startDate,

#zip = getzip(20165)
#print zip
