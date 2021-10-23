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


app = Flask(__name__)
token = "gAAAAABhcjk1i4pXTT7_pLH6gFeU-kbEGrHjRmOghFrUYYmfjYofGzOnDYsRqBcXGCsWKBuLjjeV4ClQ-_QytgW5AF-G7POwoFYBhAhG-St3uNbSnpADK9o="




@app.route('/buy', methods=['POST'])
def buy():
	if request.method == 'POST':
		#print(request.json) 
		req_data = request.get_json()

		stocks = req_data['stocks']
		trigger_prices = req_data['trigger_prices']


		stocklist = (stocks.split(','))[0]
		trigger_prices = (trigger_prices.split(','))[0]
		print(stocklist)
		print(trigger_prices)
		risk = (int(100))
		stopLoss = round((float(int(float(trigger_prices))*(float(0.003)))), 1)
		print(stopLoss)
		takeProfit = round((float(int(float(trigger_prices))*(float(0.02)))), 1)
		print(takeProfit)
		qty = (int(risk/stopLoss))
		print(qty)
		
		
		is_async = False

		fyers = fyersModel.FyersModel(is_async)
	
		print(fyers.place_orders(
    		token = token,
    		data = {
    		"symbol" : "NSE:"+stocklist+"-EQ",
    		"qty" : qty,
    		"type" : 2,
    		"side" : 1,
    		"productType" : "BO",
    		"limitPrice" : 0,
    		"stopPrice" : 0,
    		"disclosedQty" : 0,
    		"validity" : "DAY",
    		"offlineOrder" : "False",
    		"stopLoss" : stopLoss,
    		"takeProfit" : takeProfit,
    		}

		)
		)

		return 'success', 200
	else:
		abort(400)









@app.route('/sell', methods=['POST'])
def sell():
	if request.method == 'POST':
		#print(request.json) 
		req_data = request.get_json()

		stocks = req_data['stocks']
		trigger_prices = req_data['trigger_prices']

        
		stocklist = (stocks.split(','))[0]
		trigger_prices = (trigger_prices.split(','))[0]



		print(stocklist)
		print(trigger_prices)
		risk = (int(100))
		stopLoss = round((float(int(float(trigger_prices))*(float(0.003)))), 1)
		print(stopLoss)
		takeProfit = round((float(int(float(trigger_prices))*(float(0.02)))), 1)
		print(takeProfit)
		qty = (int(risk/stopLoss))
		print(qty)
		
		
		is_async = False

		fyers = fyersModel.FyersModel(is_async)

		print(fyers.place_orders(
    		token = token,
    		data = {
    		"symbol" : "NSE:"+stocklist+"-EQ",
    		"qty" : qty,
    		"type" : 2,
    		"side" : -1,
    		"productType" : "BO",
    		"limitPrice" : 0,
    		"stopPrice" : 0,
    		"disclosedQty" : 0,
    		"validity" : "DAY",
    		"offlineOrder" : "False",
    		"stopLoss" : stopLoss,
    		"takeProfit" : takeProfit,
    		}

		)
		)

		return 'success', 200
	else:
		abort(400)





if __name__ == '__main__':
	app.run()
