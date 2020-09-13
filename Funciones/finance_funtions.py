

def future_value(pv, irate, periods):
	'''Objetivo: estimar valor futuro
	formula= valor actual x (tasa) ^ periodos
	Ej: future_value(100, 0,15 , 2)'''
	return( pv*(1+irate)**periods)

def present_value (fv, r, perdiods):
	''' Devuelve el valor presente'''	
	return (fv/(1+r)**perdiods)

def npv_f(rate, cashflow):
	nvp=0

	for i in range (0,len(cashflow)):
		nvp+=present_value(cashflow[i],rate,i)

	return nvp
def npv_r(cashflow):
	r=0

	while(r<1.0):
		r+=0.000001
		npv=npv_f(r,cashflow)
		#print(npv)
		if(abs(npv)<=0.0001):
			print(r)

flujo_caja=[-100,-30,10, 40, 50, 45, 20]
flujo_caja1=(500, -500, -500, -500, 1000)
#print(npv_f(0.035, flujo_caja))
print(npv_r(flujo_caja1))

'''
cashFlows=(550,-500,-500,-500,1000)
r=0
while(r<1.0):
	r+=0.000001
	npv=npv_f(r,cashFlows)
	if(abs(npv)<=0.0001):
		print(r) '''