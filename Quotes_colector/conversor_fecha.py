#Convertir de String Fecha a Lista AÑO MES DIA

def convert_date(in_date):
	date=[]
	date.append(int(in_date[:2]))
	date.append(int(in_date[3:5]))
	date.append(int(in_date[6:10]))


#Devuelve una list con 3 valores int [AÑO , MES, DIA]
	
	return date



