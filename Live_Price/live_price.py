import requests
from bs4 import BeautifulSoup

URL_YAHOO="https://finance.yahoo.com/quote/"#?p=TSLA"
'''
req=requests.get(URL_YAHOO)
soup=BeautifulSoup(req.content,"html.parser")
dat=soup.findAll('span',{'class': 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)'})

for element in dat:
	print(element.text)

'''
class Stock_data():
	def __init__(self, ticker):
		self.__ticker=ticker
		self.req=0
		self.src=0
		self.soup=0
		self.__raw_dat=[]
		self.__quote_price=0
		self.__info_table=0
		self.__out=[]

	def connect_url(self):
		self.req=requests.get(URL_YAHOO+self.__ticker)
		self.src=self.req.content

	def live_price(self):
		self.connect_url()
		self.soup=BeautifulSoup(self.src,"html.parser")
		self.__raw_dat=self.soup.find('span',{'class': 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)'})
		self.__quote_price=self.__raw_dat.text
		return self.__quote_price

	def information_table(self):
		self.connect_url()
		self.soup=BeautifulSoup(self.src,"html.parser")
		self.__raw_dat.append(self.soup.findAll('td',attrs={'data-test': 'PREV_CLOSE-value'}))#'table',{'class': 'W(100%) M(0) Bdcl(c)'})
		self.__raw_dat.append(self.soup.findAll('td',attrs={'data-test': 'OPEN-value'}))
		self.__raw_dat.append(self.soup.findAll('td',attrs={'data-test': 'BID-value'}))
		self.__raw_dat.append(self.soup.findAll('td',attrs={'data-test': 'ASK-value'}))
		self.__raw_dat.append(self.soup.findAll('td',attrs={'data-test': 'TD_VOLUME-value'}))

		self.__info_table=self.conversor(self.__raw_dat)
		return self.__info_table
		
	def conversor(self,a):
		for elements in a:
			for b in elements:
				self.__out.append(b.getText())

		return self.__out

#codigo=Stock_data("KO")

print(Stock_data("CSCO").live_price())
print(Stock_data("KO").information_table())

