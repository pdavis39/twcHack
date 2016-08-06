from pyzipcode import ZipCodeDatabase
import datetime

def getzip(x):
    zcdb = ZipCodeDatabase()
    try:
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
    except IndexError:
        zipcode = 'null'
        return zipcode




#zip = getzip(22804)
#print zip
