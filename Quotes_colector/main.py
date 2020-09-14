from conversor_fecha import convert_date
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter.filedialog import asksaveasfile 

import pandas as pd 
import pandas_datareader.data as web
import datetime as dt 

def get_data(route):
	ticker=ticker_gui.get()
	inicio=convert_date(fecha_ini.get())
	fin=convert_date(fecha_fin.get())

	quote=get_price(ticker,inicio,fin)
	quote.to_csv(route)

def get_price(ticker,start,To):

	Start=dt.datetime(start[2],start[0],start[1])
	end=dt.datetime(To[2],To[0],To[1])
	stk_q=web.DataReader(ticker, 'yahoo',Start, end)

	return stk_q
def save():
	files = [('CSV Files', '*.csv')]
	file = asksaveasfile(mode='a',filetypes = files, defaultextension = files, initialfile=ticker_gui.get())
	get_data(file.name)

root=Tk()
root.title("Get Quotes")
root.geometry("400x400")


ticker_gui=StringVar()
fecha_ini=StringVar()
fecha_fin=StringVar()
label3=Label(root, text="Ingrese fecha Final: ", font=("Helvetica", 10)).grid(row=4,column=0)
label0=Label(root,text="Descargar cotizacion acciones", font=("Helvetica", 16), anchor="center").grid(row=0, column=0, columnspan=2)
label1=Label(root,text="Ingrese TICKER: ",anchor="w", font=("Helvetica", 10)).grid(row=1, column=0)
entry1=Entry(root,textvariable=ticker_gui).grid(row=1, column=1)
label2=Label(root, text="Ingrese fecha Inicial: ", font=("Helvetica", 10)).grid(row=2,column=0)
fecha_st= DateEntry(root, width=12, background='darkblue',foreground='white', borderwidth=2, textvariable=fecha_ini, date_pattern='mm/dd/yyyy').grid(row=3,column=0)
label2=Label(root, text="Ingrese fecha Inicial: ", font=("Helvetica", 10)).grid(row=4,column=0)
fecha_end= DateEntry(root, width=12, background='darkblue',foreground='white', borderwidth=2, textvariable=fecha_fin, date_pattern='mm/dd/yyyy').grid(row=5,column=0)
boton_obtener=Button(root, text="Generar CSV", command=save).grid(row=6, column=0)



root.mainloop()