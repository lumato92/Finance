import json
import sqlite3
import alpha_vantage
import time


SECTORS=['Communication Services','Consumer Discretionary','Consumer Staples','Energy','Financials','Health Care','Information Technology','Materials','Real Estate','Utilities','Industrials']

ROUTE="sp500.json"
ROUTE_1="C:/Users/ltorrado/Desktop/Apps/Finanzas/app_finance/OverView_final/"
DOWNLOAD_DIR_JSON="C:/Users/ltorrado/Desktop/Apps/Finanzas/JSON_DATA/SP500/"
DOWNLOAD_DIR_JSON_BALANCE="C:/Users/ltorrado/Desktop/Apps/Finanzas/JSON_DATA/SP500/Balance_sheet/"
#-------------DATABASE--------------------------------
def conect_db(): #Funcion Conectar DB
	conexcion_db=sqlite3.connect("SP500")
	cursor_db=conexcion_db.cursor()
	try:
		cursor_db.execute('''

		CREATE TABLE SP500(
		
		NAME VARCHAR(50),
		SECTOR VARCHAR(50),
		SYMBOL VARCHAR(20))
		''')

	except sqlite3.OperationalError:

		print("La Base de Datos ya esta creada")

	conexcion_db.close()


def overview_db():
	conexcion_db=sqlite3.connect("OVERVIEW_SP500")
	cursor_db=conexcion_db.cursor()
	
	cursor_db.execute('''

		CREATE TABLE OVERVIEW_SP500(
		
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
		'''
		)


	conexcion_db.close()

def new_db_entry(data):
	conexcion_db=sqlite3.connect("SP500")
	cursor_db=conexcion_db.cursor()
	#ingreso=[nombre_gui.get(),pass_gui.get(),apellido_gui.get(),direccion_gui.get()]
	

	cursor_db.execute("INSERT INTO SP500 VALUES (?,?,?)", data)
	conexcion_db.commit()
	conexcion_db.close()
	return
	#messagebox.showinfo("CRUD", "Se realizo el ingreso con exito")

def search_db_sector(a):
	conexcion_db=sqlite3.connect("SP500")
	cursor_db=conexcion_db.cursor()
	cursor_db.execute("SELECT NAME, SYMBOL FROM SP500 WHERE SECTOR='Financials'")
	read=list(cursor_db.fetchall())
	conexcion_db.close()


	return read


def carga_json(a):
	
	for item in a:
		print(item[1])
		temp=alpha_vantage.StockTimeSeries(item[1]).overview()
			#with open(item[0]+'.json', 'w') as json_file:
    		#json.dump(temp, json_file)

def carga_ini(ROUTE):
	with open(ROUTE) as f:
	    d = json.load(f)
	    print(type(d))
	count=0    
	for index in range(len(d)):
		count=count+1
		#new_db_entry(list(d[index].values()))
		print(list(d[index].values()))
		print("registro nro",count)





def carga_over(SECTORS):

	
		a=search_db_sector(SECTORS)
		for element in a:
			
			temp=alpha_vantage.StockTimeSeries(element[1]).overview()
			with open(element[0]+'.json','w') as json_file:
				json.dump(temp, json_file)
			time.sleep(20)
	
		print("Carga Completa")



def carga_OVERVIEW_2(company):


	with open(ROUTE_1+company+'.json') as f:
		d = list(json.load(f).values())
		
		db_entry_overview(d)
		


def search_db_sector_overview():
	conexcion_db=sqlite3.connect("SP500")
	cursor_db=conexcion_db.cursor()
	cursor_db.execute("SELECT NAME, SYMBOL FROM SP500 WHERE SECTOR='Consumer Staples'")
	read=list(cursor_db.fetchall())
	conexcion_db.close()


	return read


def get_company_list():
	conexcion_db=sqlite3.connect("SP500")
	cursor_db=conexcion_db.cursor()
	cursor_db.execute("SELECT NAME, SYMBOL FROM SP500")
	read=list(cursor_db.fetchall())
	conexcion_db.close()


	return read

def overview_download(TICKER):

			
	temp=alpha_vantage.StockTimeSeries(element[1]).overview()
	with open(DOWNLOAD_DIR_JSON+element[0]+'.json','w') as json_file:
		json.dump(temp, json_file)
		time.sleep(12)
	
	print("Carga Completa")

def balancesheet_download(TICKER):
	temp=alpha_vantage.StockTimeSeries(element[1]).balance_sheet()
	with open(DOWNLOAD_DIR_JSON_BALANCE+element[0]+'.json','w') as json_file:
		json.dump(temp, json_file)
		time.sleep(12)
	
	print(element[0]," Carga Completa")

def db_entry_overview(data):
	conexcion_db=sqlite3.connect("OVERVIEW_SP500")
	cursor_db=conexcion_db.cursor()
	
	
	try:
		cursor_db.execute("INSERT INTO OVERVIEW_SP500 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data)
		conexcion_db.commit()
		conexcion_db.close()
	except:
		pass
	return





'''
company=get_company_list()
for element in company:
	(empresa,)=element
	carga_OVERVIEW_2(empresa)
	print(empresa)
'''

lista=get_company_list()

for element in lista:
	balancesheet_download(list(element))

