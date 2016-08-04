import datetime
import json
import os
import urllib2
import pandas as pd
from pandas.io.json import json_normalize
import loadConfig


#t = tenddayforcast(39.044855,-77.38701,'2016-08-02')
#x = 39.044855
#y = -77.38701
#z = '2016-08-02'
def tenddayforcast(x,y):
    os.chdir('/Users/paul/Dropbox/dev/twc/sandbox')
    os.getcwd()
    twcKey = loadConfig.twckey

    fieldnames = [
        'lat','long','sunset','class','expire_time_gmt','expire_date','expire_time','fcst_valid','fcst_date','fcst_time','fcst_valid_local','num','max_temp',
        'min_temp','torcon','stormcon','blurb','blurb_author','dow','lunar_phase_code','lunar_phase',
        'lunar_phase_day','sunrise','sunset','moonrise','moonset','snow_range', 'snow_phrase', 'narrative',
        'qualifier_code', 'snow_qpf', 'qualifier', 'qpf', 'snow_code'

                                                          'day.fcst_valid_local','day.phrase_22char','day.golf_category','day.temp_phrase','day.fcst_valid',
        'day.golf_index','day.daypart_name','day.snow_phrase', 'day.accumulation_phrase', 'day.precip_type',
        'day.pop', 'day.alt_daypart_name','day.hi','day.narrative','day.wspd','day.qualifier_code','day.wxman','day.uv_index_raw','day.pop_phrase','day.qualifier',
        'day.uv_index','day.wind_phrase','day.qpf','day.clds','day.temp','day.uv_warning','day.snow_code','day.uv_warning', \
        'day.wdir_cardinal','day.subphrase_pt1','day.wc','day.wdir','day.thunder_enum','day.subphrase_pt3','day.rh','day.snow_range',
        'day.icon_code','day.subphrase_pt2','day.icon_extd','day.long_daypart_name','day.day.ind','day.phrase_12char','day.snow_qpf',
        'day.thunder_enum_phrase','day.shortcast','day.uv_desc','day.num','day.phrase_32char','day.vocal_key',

        'night.fcst_valid_local','night.phrase_22char','night.golf_category','night.temp_phrase','night.fcst_valid',
        'night.hi','night.narrative','night.wspd','night.qualifier_code','night.wxman','night.uv_index_raw','night.pop_phrase',
        'night.qualifier','night.uv_index','night.wind_phrase','night.qpf','night.clds','night.temp','night.uv_warning','night.snow_code',
        'night.uv_warning','night.wdir_cardinal','night.subphrase_pt1','night.wc','night.wdir','night.thunder_enum','night.subphrase_pt3',
        'night.rh','night.snow_range','night.icon_code','night.subphrase_pt2','night.icon_extd','night.long_daypart_name','night.day.ind',
        'night.phrase_12char','night.snow_qpf','night.thunder_enum_phrase','night.shortcast','night.uv_desc','night.num','night.phrase_32char',
        'night.vocal_key', 'night.alt_daypart_name','night.precip_type', 'night.pop','night.golf_index', 'night.daypart_name','night.accumulation_phrase',
        'night.snow_phrase'

    ]
    df=pd.DataFrame(columns=fieldnames)

    filename = "Weather_10dayforecast_latlong_" + datetime.datetime.today().strftime("%m%d%Y")+".csv"
    filename

    #for index,row in latlong.iterrows():
    #    try:
    lat = x
    #print(lat)
    long= y
    #print(long)
    url = "https://api.weather.com/v1/geocode/" + "%s" %lat + "/" + "%s" %long + "/forecast/daily/10day.json?language=en-US&units=e&apiKey="+twcKey
    #print(url)
    #result = json_normalize(data)

    r = urllib2.urlopen(url)
    json_text = r.read().decode('utf-8')
    # Convert it to a Python dictionary
    data = json.loads(json_text)


    # Function to flatten day & night nested variables

    for forecast in data['forecasts']:
        forecast['long'] = long
        forecast['lat'] = lat


    if df.empty:
        df = pd.DataFrame(json_normalize(data['forecasts']),columns=fieldnames)
        df.head(5)

    else:
        df2=pd.DataFrame(json_normalize(data['forecasts']),columns=fieldnames)
        df=df.append(df2)
        df.head(5)

     #   except urllib2.URLError as error:
     #       print('Error while retrieving data for ', url)


    df.reset_index(inplace=True,drop=True)
    df['fcst_valid'] = df['fcst_valid'].astype('datetime64[s]')
    df['expire_time_gmt'] = df['expire_time_gmt'].astype('datetime64[s]')
    df['fcst_date'] = df.fcst_valid.dt.date
    df['fcst_time'] = df.fcst_valid.dt.time
    df['expire_date'] = df.expire_time_gmt.dt.date
    df['expire_time'] = df.expire_time_gmt.dt.time

    df = df.sort_values(by = ['lat','long','expire_time_gmt'],ascending=True)
    df.to_csv(filename,index=False, header=True, index_label = False)

    #print df['lunar_phase'], df['min_temp'], df['max_temp'], df['dow'], df['narrative']
    twcsummary = df[['dow','lunar_phase', 'min_temp', 'max_temp', 'day.phrase_22char', 'day.wind_phrase','day.precip_type']]
    #print twcsummary
    return twcsummary

#twcsummary = tenddayforcast(39.044855,-77.38701)
#print twcsummary
#print("***** Finished******")