from fyers_api import accessToken
from flask import Flask, request, abort
import requests
import json
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import math
import datetime
import decimal
from fyers_api import fyersModel
from decimal import Decimal
from fyers_api import fyersModel

app_id = "5SNVZTE1PX"

app_secret = "WEGE5ZFCCG"

app_session = accessToken.SessionModel(app_id, app_secret)

response = app_session.auth()


print(response)
# json_object = json.dumps(response)  
# print(json_object) 

# stocks = json_object["authorization_code"]
# print(stocks)

# y = json_object

# print(y)
# # print(type(y))

# last = y.strip('{"code": 200, "data": {"authorization_code": ')

# first = last.strip('"}, "message": ""}')

# final = "e"+first
# # print(final)


# add = "https://api.fyers.in/api/v1/genrateToken?authorization_code="+final+"&appId=5SNVZTE1PX"


# response = requests.get(add)

# # print response
# # print(response)

# # print url
# print(response.text)


