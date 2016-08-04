import numbers
import quote


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
        airstatus = "you won't melt"
        #wet run
        #rq = quote.getwrquotes()
        #wr bike
        wq = quote.getwbquotes()
    if isRain[0] != 'rain':
        airstatus = 'Never give up'
        wq = quote.gettriquotes()
    if isinstance( mintmp[0], numbers.Integral ):
        if int(mintmp[0]) < 30:
            tempstatus = 'Yeah its cold'
            brq = quote.getcbquotes()
    if isinstance( mintmp[0], numbers.Integral ):
        if int(mintmp[0]) > 30 and int(mintmp[0]) < 65:
            tempstatus = 'layer and get out there'
            brq = quote.getcbquotes()
    if isinstance( mintmp[0], numbers.Integral ):
        if int(mintmp[0]) > 65 and int(mintmp[0]) < 85:
            tempstatus = 'great day to run'
            #hb hot bike
            brq = quote.gethbquotes()
    if isinstance( mintmp[0], numbers.Integral ):
        if int(mintmp[0]) > 86 and int(mintmp[0]) < 95:
            tempstatus = 'stay hydrated'
            #hb hot bike
            brq = quote.gethbquotes()
    if isinstance( mintmp[0], numbers.Integral ):
        if int(mintmp[0]) > 95:
            tempstatus = 'treadmill may be your best bet'
            #cb hot bike
            brq = quote.gethbquotes()


    if isinstance( maxtmp[0], numbers.Integral ):
        if int(maxtmp[0]) < 30:
            tempstatus = 'Yeah its cold'
    if isinstance( maxtmp[0], numbers.Integral ):
        if int(maxtmp[0]) > 30 and int(mintmp[0]) < 65:
            tempstatus = 'layer and get out there'
    if isinstance( maxtmp[0], numbers.Integral ):
        if int(maxtmp[0]) > 65 and int(maxtmp[0]) < 85:
            tempstatus = 'great day to run'
    if isinstance( maxtmp[0], numbers.Integral ):
        if int(maxtmp[0]) > 86 and int(maxtmp[0]) < 95:
            tempstatus = 'stay hydrated'
    if isinstance( maxtmp[0], numbers.Integral ):
        if int(maxtmp[0]) > 95:
            tempstatus = 'treadmill may be your best bet'
    #print 'hmmm',mintmp, maxtmp

    for line in aq:
        cat = line['Category']
        qt = line['ParameterName']
        num = line['Category']['Number']
    #    print num
        if num == 1:
            aqsumm = 'The air quality is good'
        if num == 2:
            aqsumm = 'The air is moderate'
        if num >= 3:
            aqsumm = 'The air is unhealthy'
    week = ts.iloc[1:8]
    return aqsumm, today, week, airstatus, brq, wq, tempstatus

#aq = airQuality.aqdata
#ts = tendayForecast.twcsummary
#z = motivator(aq,ts)
# summary of results
#print z
#print 'the week in advance'
#print ts.iloc[1:8]

