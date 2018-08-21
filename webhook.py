import json
import os
import requests
from flask import Flask
from flask import request
from flask import make_response
# flask app should start in global layout
app=Flask(__name__)
@app.route('/webhook',methods=['POST'])
def webhook():
speech="hot"
return{
"speech":speech,
"displayText":speech,
"source":"apiai-weather-webhook"
}
if __name__=='__main__':
port=int(os.getenv('PORT',5000))
print("Starting app on port %d" % port)
app.run(debug=False,port=port,host='0.0.0.0')
