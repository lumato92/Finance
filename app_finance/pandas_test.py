import pandas as pd
import sqlite3


#### CREAR DATAFRAME DESDE UNA BASE DE DATOS SQL ###############
connection=sqlite3.connect('C:/Users/ltorrado/Desktop/Apps/Finanzas/app_finance/NASDAQ')
df=pd.read_sql('SELECT * FROM OVERVIEW_NASDAQ ',connection)
connection.close

#### CREAR DATAFRAME DESDE CSV#####

df=pd.read_csv('Ruta del archivo')

### EXPORTAR DATAFRAME A CSV
 
df.to_csv(r'ruta donde ser guardara el .csv', index = False)
