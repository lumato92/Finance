import datetime as dt 
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd 
import pandas_datareader.data as web 
 

style.use('ggplot')
start=dt.datetime(2016,12,22)
end=dt.datetime(2016,12,31)

df=web.DataReader('TSLA','yahoo',start, end)
df.to_csv('tesla.csv')
print(df.head())

print(type(df))

def get_price(ticker,start,To):

	Start=dt.datetime(start[0],start[1],start[2])
	end=dt.datetime(To[0],To[1],To[2])
	stk_q=web.DataReader(ticker, 'yahoo',Start, end)

	return stk_q


'''
From=[0,0,0]
to=[0,0,0]
stock=0
accion=0
From[0]=int(input("Ingrese año"))
From[1]=int(input("Ingrese mes"))
From[2]=int(input("Ingrese dia"))

to[0]=int(input("Ingrese año"))
to[1]=int(input("Ingrese mes"))
to[2]=int(input("Ingrese dia"))

stock=input("Ingrese TICKER")

accion=get_price(stock,From, to)
'''
#print(type(accion))
