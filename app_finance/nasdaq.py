import json
import sqlite3
import alpha_vantage
import time



def conect_db(): #Funcion Conectar DB
	conexcion_db=sqlite3.connect("NASDAQ")
	cursor_db=conexcion_db.cursor()
	try:
		cursor_db.execute('''

		CREATE TABLE NASDAQ(
		
		NAME VARCHAR(50),
		SYMBOL VARCHAR(8))
		''')

	except sqlite3.OperationalError:

		print("La Base de Datos ya esta creada")

	conexcion_db.close()

def create_db_overview(): #Funcion Conectar DB
	conexcion_db=sqlite3.connect("NASDAQ")
	cursor_db=conexcion_db.cursor()
	try:
		cursor_db.execute('''


		CREATE TABLE OVERVIEW_NASDAQ(
		
		SYMBOL VARCHAR(5),
		ASSET_TYPE VARCHAR(15),
		NAME VARCHAR(40),
		DESCRIPTION VARCHAR(2500),
		EXCHANGE VARCHAR(15),
		CURRENCY VARCHAR(5),
		COUNTRY VARCHAR(5),
		SECTOR VARCHAR(15),
		INDUSTRY VARCHAR(20),
		ADDRESS VARCHAR(50),
		FULLTIMEEMPLOYEES VARCHAR(8),
		FISCALYEAREND VARCHAR(15),
		LATESTQUARTER VARCHAR(10),
		MARKETCAPITALIZATION VARCHAR(15),
		EBITDA VARCHAR(15),
		PER_RATIO VARCHAR(15),
		PEG_RATIO VARCHAR(15),
		BOOKVALUE VARCHAR(10),
		DIVIDEND_PER_SHARE VARCHAR(10),
		DIVIDEND_YIELD VARCHAR(10),
		EPS VARCHAR(10),
		REVENUE_PER_SHARE_TTM VARCHAR(10),
		PROFIT_MARGIN VARCHAR(12),
		OPERATING_MARGIN_TTM VARCHAR(10),
		RETURN_ON_ASSET_TTM VARCHAR(10),
		RETURN_ON_EQUITY_TTM VARCHAR(10),
		REVENUE_TTM VARCHAR(20),
		GROSSPROFIT_TTM VARCHAR(25),
		DILUTED_EPS_TTM VARCHAR(10),
		QUARTERLY_EARNINGS_GROWTH_YOY VARCHAR(10),
		QUARTERLY_RENEVUE_GROWTH_YOY VARCHAR(10),
		ANALYST_TARGET_PRICE VARCHAR(10),
		TRAILING_PE VARCHAR(15),
		FOWARD_PE VARCHAR(15),
		PRICE_TO_SALE_RATIO_TTM VARCHAR(15),
		PRICE_TO_BOOK_RATIO VARCHAR(15),
		EV_TO_REVENUE VARCHAR(15),
		EV_TO_EBITDA VARCHAR(15),
		BETA VARCHAR(15),
		C52WEEKHIGH VARCHAR(10),
		C52WEEKLOW VARCHAR(10),
		C50DAYMOVINGAVERAGE VARCHAR(15),
		C200DAYMOVINGAVERAGE VARCHAR(15),
		SHARES_OUTSTANDING VARCHAR(20),
		SHARES_FLOAT VARCHAR(20),
		SHARES_SHORT VARCHAR(20),
		SHARES_SHORTPRIORMONTH VARCHAR(20),
		SHORT_RATIO VARCHAR(10),
		SHORT_PERCENT_OUTSTANDING VARCHAR(10),
		SHORT_PERCENT_FLOAT VARCHAR(10),
		PERCENT_INSIDERS VARCHAR(10),
		PERCENT_INSTITUTIONS VARCHAR(10),
		FOWARD_ANNUAL_DIVIDEND_RATE VARCHAR(10),
		FOWARD_ANNUAL_DIVIDEND_YIELD VARCHAR(10),
		PAYOUT_RATIO VARCHAR(10),
		DIVIDEND_DATE VARCHAR(15),
		EX_DIVIDEND_DATE VARCHAR(15),
		LAST_SPLIT_FACTOR VARCHAR(5),
		LAST_SPLIT_DATE VARCHAR(10) )
		''')
	except sqlite3.OperationalError:

		print("La Base de Datos ya esta creada")

	conexcion_db.close()


def new_db_entry(data):
	conexcion_db=sqlite3.connect("NASDAQ")
	cursor_db=conexcion_db.cursor()
	
	cursor_db.execute("INSERT INTO NASDAQ VALUES (?,?)", data)
	conexcion_db.commit()
	conexcion_db.close()
	return


def carga_ini():	
	with open('nasdaq.json') as f:
		d = json.load(f)
		for index in range(len(d)):
			new_db_entry(list(d[index].values()))

def get_overview():
	conexcion_db=sqlite3.connect("NASDAQ")
	cursor_db=conexcion_db.cursor()
	cursor_db.execute("SELECT SYMBOL FROM NASDAQ ")
	read=cursor_db.fetchall()
	
	count=0
	for i in range (2000,2500):
		(symbol,)=read[i]
		count=count+1
		print(symbol,count)
		temp=alpha_vantage.StockTimeSeries(symbol).overview()
		with open(symbol+'.json','w') as json_file:
			json.dump(temp, json_file)
			time.sleep(12)		
		#print(len(read))

def db_entry_overview(data):
	conexcion_db=sqlite3.connect("NASDAQ")
	cursor_db=conexcion_db.cursor()
	#ingreso=[nombre_gui.get(),pass_gui.get(),apellido_gui.get(),direccion_gui.get()]
	
	try:
		cursor_db.execute("INSERT INTO OVERVIEW_NASDAQ VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data)
		conexcion_db.commit()
		conexcion_db.close()
	except:
		pass
	return
def carga_OVERVIEW():
	conexcion_db=sqlite3.connect("NASDAQ")
	cursor_db=conexcion_db.cursor()
	cursor_db.execute("SELECT SYMBOL FROM NASDAQ ")
	read=cursor_db.fetchall()
	
	for i in range (1501,1999):
		(symbol,)=read[i]
		with open(symbol+'.json') as f:
			d = list(json.load(f).values())
		
			db_entry_overview(d)


get_overview()

#carga_OVERVIEW()