import requests
import json
import csv



API_KEY_posta='43DJZJPQSKUIKFC5'
API_KEY='QH5NIU2RPGLEQ4ZT'
API_KEY_1='Q0U22HFMNKRGJSUN'
class StockTimeSeries():

	def __init__(self, ticker):

		self.__symbol=ticker


	def intraday(self, interval, datatype=json):
		global API_KEY

		req=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+self.__symbol+'&interval='+interval+'&apikey='+API_KEY)

		print(json.loads(req.text))

	def dailyAdjusted(self, outputsize='compact', datatype='json'):
		global API_KEY
		req=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+self.__symbol+'&outputsize='+outputsize+'&apikey='+API_KEY+'&datatype='+datatype)

		if datatype=='json':
			print(json.loads(req.text))
		else:
			cr=csv.reader(req)

	def weekly (self, datatype='json'):
		global API_KEY
		
		req=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol='+self.__symbol+'&apikey='+API_KEY+'&datatype='+datatype)

		if datatype=='json':
			print(json.loads(req.text))
		else:
			cr=csv.reader(req)

	def weeklyAdj (self, datatype='json'):
		#global API_KEY
		req=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol='+self.__symbol+'&apikey='+API_KEY+'&datatype='+datatype)

		if datatype=='json':
			print(json.loads(req.text))
		else:
			cr=csv.reader(req)


	def monthly (self, datatype='json'):
		global API_KEY
		req=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol='+self.__symbol+'&apikey='+API_KEY+'&datatype='+datatype)

		if datatype=='json':
			print(json.loads(req.text))
		else:
			cr=csv.reader(req)


	def monthlyAdj (self, datatype='json'):
		global API_KEY
		req=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol='+self.__symbol+'&apikey='+API_KEY+'&datatype='+datatype)

		if datatype=='json':
			print(json.loads(req.text))
		else:
			cr=csv.reader(req)			

	def quote (self, datatype='json'):
		global API_KEY
		req=requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='+self.__symbol+'&apikey='+API_KEY+'&datatype='+datatype)

		if datatype=='json':
			print(json.loads(req.text))
		else:
			cr=csv.reader(req)		

	def overview(self):

		global API_KEY

		req=requests.get('https://www.alphavantage.co/query?function=OVERVIEW&symbol='+self.__symbol+'&apikey='+API_KEY)
		
		return(json.loads(req.text))

	def income_statement(self):
		
		req=requests.get('https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol='+self.__symbol+'&apikey='+API_KEY)
		print(json.loads(req.text))

	def balance_sheet(self):
		req=requests.get('https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol='+self.__symbol+'&apikey='+API_KEY)
		return(json.loads(req.text))

			
