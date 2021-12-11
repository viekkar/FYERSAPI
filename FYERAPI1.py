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

app_id = ur app id"

app_secret = "ur secret id"

app_session = accessToken.SessionModel(app_id, app_secret)

response = app_session.auth()


print(response)


