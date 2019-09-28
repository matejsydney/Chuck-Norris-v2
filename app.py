
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
    if req.get("result").get("action")=="getjoke":
        res = makeWebhookResultForGetJoke()
    else:
        return {}

    return res


def makeWebhookResultForGetJoke():
#    valueString = data.get('value')
#    joke = valueString.get('joke') - removing this part
    joke = (jokeDict[str(random.randint(1,2))])
    speechText = "<speak>" + joke + '<break time="2s"/>' + " Would you like another joke?" + "</speak>"
    displayText = joke + " Would you like another joke?"
    return {
        "speech": speechText,
        "displayText": displayText,
        # "data": data,
        # "contextOut": [],
        "source": "Heroku live webhook v4.3"
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
