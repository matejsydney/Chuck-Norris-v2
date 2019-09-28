
from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# MY ADDITION - joke list needs to be .py file to work
import random
from jokeList import jokeDict

#picking random starts with first number and ends with the last one- converted to string
#randomJoke = str(random.randint(1,4))
#jokeReturn = (jokeDict[randomJoke])
# MY ADDITION THE ABOVE NOT NEEDED  2




# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
#    if req.get("result").get("action")=="yahooWeatherForecast":
#        baseurl = "https://query.yahooapis.com/v1/public/yql?"
#        yql_query = makeYqlQuery(req)
#        if yql_query is None:
#            return {}
#        yql_url = baseurl + urlencode({'q': yql_query}) + "&format=json"
#        result = urlopen(yql_url).read()
#        data = json.loads(result)
#        res = makeWebhookResult(data)
    if req.get("result").get("action")=="getjoke":
#        baseurl = "http://api.icndb.com/jokes/random"
#        result = urlopen(baseurl).read()
#        data = json.loads(result)
        res = makeWebhookResultForGetJoke()
    else:
        return {}

    return res


def makeWebhookResultForGetJoke():
#    valueString = data.get('value')
#    joke = valueString.get('joke') - removing this part
    joke = (jokeDict[str(random.randint(1,186))])
    speechText = "<speak>" + joke + '<break time="2s"/>' + " Would you like another joke?" + "</speak>"
    displayText = joke + " Would you like another joke?"
    return {
        "speech": speechText,
        "displayText": displayText,
        # "data": data,
        # "contextOut": [],
        "source": "Heroku live webhook v4.3"
    }
'''
def makeYqlQuery(req):
    result = req.get("result")
    parameters = result.get("parameters")
    city = parameters.get("geo-city")
    if city is None:
        return None

    return "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='" + city + "') and u='c'"


def makeWebhookResult(data):
    query = data.get('query')
    if query is None:
        return {}

    result = query.get('results')
    if result is None:
        return {}

    channel = result.get('channel')
    if channel is None:
        return {}

    item = channel.get('item')
    location = channel.get('location')
    units = channel.get('units')
    if (location is None) or (item is None) or (units is None):
        return {}

    condition = item.get('condition')
    if condition is None:
        return {}

    # print(json.dumps(item, indent=4))

    speech = "Todays C2 weather in " + location.get('city') + ": " + condition.get('text') + \
             ", And the temperature feels " + condition.get('temp') + " " + units.get('temperature')

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }
'''

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
