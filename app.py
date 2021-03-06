
from flask import Flask, render_template, request, redirect
import zipToLatLong
import airQuality
import tendayForecast
import motivator
import datetime


app = Flask(__name__)
#app.secret_key = 'monkey'
#images = Images(app)

@app.route('/')
def athlete():
    return render_template('index.html')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():

    if request.method == 'POST':
        result = request.form
        imd = result
        x = dict(imd)
        y = x['Zip']
        y = y[0].encode('utf-8')
        #call zip
        global zip
        zip = zipToLatLong.getzip(y)
        if zip == 'null':
            return redirect('http://localhost:5000/error', code=302)
        #print 'zip',len(zip)
        global aqdata
        #call aq
        now = datetime.datetime.now()
        # '2016-07-31'
        startDate = now.strftime("%Y-%m-%d")
        aqdata = airQuality.airquality(zip[0],zip[1],startDate)
        #10dayforecast
        global twcsummary
        twcsummary = tendayForecast.tenddayforcast(zip[0],zip[1])

        #motivator
        #3 variables
        global z
        #aq = airQuality.aqdata
        #ts = tendayForecast.twcsummary
        z = motivator.motivator(aqdata,twcsummary)

    return render_template("result.html",result = result,zip = zip[2], city = zip[3], state = zip[4], aqdata = aqdata, airstatus = z[3],
                           weatherquote = z[0],today = z[1],week = z[2],bikequote = z[4], wetquote = z[5], tempstatus = z[6], triquote = z[7])


if __name__ == '__main__':
    app.run(debug = True)
