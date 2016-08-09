import numbers
import quote
import math


# qoutes - https://github.com/gbigwood/Quote-generator/blob/master/src/randomquotes.py
# air quality
# Forecasted AQI category number:
# 1 = Good, 2 = Moderate, 3 = Unhealthy for Sensitive Groups, 4 = Unhealthy, 5 = Very Unhealthy, 6 = Hazardous, 7 = Unavailable
# check messages
def motivator(aq,ts):
    #print 'Today'
    today = ts.iloc[:1]
    mintmp = ts.iloc[:1]['min_temp']
    maxtmp = ts.iloc[:1]['max_temp']
    isRain = ts.iloc[:1]['day.precip_type']

    # same thing to check for snow....
    if isRain[0] == 'rain':
        airstatus = "You won't melt, get out and train"
        wq = quote.getwbquotes()
    if isRain[0] != 'rain':
        airstatus = 'Weather is fine, get out and train'
        wq = quote.gettriquotes()

    if math.isnan(mintmp[0]):
        tempstatus = 'just do it'
        brq = quote.gethbquotes()
    else:


        if int(mintmp[0]) < 30:
            tempstatus = 'Yeah its cold'
            brq = quote.getcbquotes()

        if int(mintmp[0]) > 30 and int(mintmp[0]) < 65:
            tempstatus = 'layer and get out there'
            brq = quote.getcbquotes()

        if int(mintmp[0]) > 65 and int(mintmp[0]) < 85:
            tempstatus = 'great day to run'
            #hb hot bike
            brq = quote.gethbquotes()

        if int(mintmp[0]) > 86 and int(mintmp[0]) < 95:
            tempstatus = 'stay hydrated'
            #hb hot bike
            brq = quote.gethbquotes()

        if int(mintmp[0]) > 95:
            tempstatus = 'treadmill may be your best bet'
            #cb hot bike
            brq = quote.gethbquotes()

    if math.isnan(maxtmp[0]):
        tempstatus = 'just do it'
        brq = quote.gethbquotes()
    else:
        if int(maxtmp[0]) < 30:
            tempstatus = 'Yeah its cold'
            brq = quote.getcbquotes()

        if int(maxtmp[0]) > 30 and int(mintmp[0]) < 65:
            tempstatus = 'layer and get out there'
            brq = quote.gethbquotes()

        if int(maxtmp[0]) > 65 and int(maxtmp[0]) < 85:
            tempstatus = 'great day to run'
            brq = quote.gethbquotes()

        if int(maxtmp[0]) > 86 and int(maxtmp[0]) < 95:
            tempstatus = 'stay hydrated'
            brq = quote.gethbquotes()

        if int(maxtmp[0]) > 95:
            tempstatus = 'treadmill may be your best bet'
            brq = quote.gethbquotes()


    #print 'hmmm',mintmp, maxtmp

    if aq:
        for line in aq:
            # Category 0 = no service

            #cat = line['Category']
            #qt = line['ParameterName']
            if line['Category']['Number']:
                num = line['Category']['Number']
            else:
                num = 0
           # print num
            if num == 0:
                aqsumm = 'Air quality sensors not available'
            if num == 1:
                aqsumm = 'The air quality is good'
            if num == 2:
                aqsumm = 'The air is moderate'
            if num >= 3:
                aqsumm = 'The air is unhealthy'
    else:
        aqsumm = 'Air quality sensors not unavailable'
    week = ts.iloc[1:8]
    tq = quote.gettriquotes()
    return aqsumm, today, week, airstatus, brq, wq, tempstatus, tq

#aq = airQuality.aqdata
#ts = tendayForecast.twcsummary
#z = motivator(aq,ts)
# summary of results
#print z
#print 'the week in advance'
#print ts.iloc[1:8]

