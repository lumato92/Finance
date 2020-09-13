#!/usr/bin/env python3
#Autor:JoséFacundoBogado, dedicado a Clara(I❤U)
import requests
import json
import sys
import os
import time

def borrarPant():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def menu():
    print('FlashTrading 0.1 (pre-alfa)')
    print('''¿Que desea hacer? :
          [0] Estado de Cuenta
          [1] Ver Portafolio
          [2] Consultar la cotización de un titulo
          [3] Ver operaciones
          [4] Comprar/Vender
          [5] Ver Paneles de cotizaciones
          [6] Serie historica
          [7] Calculadora de bonos
          [8] Acerca de...
          [9] Salir
          ''')
    n = input('(Ingrese el número):\t')
    borrarPant()
    if n=='0':
        estado()
    elif n=='1':
        miportafolio()
    elif n=='2':
        consulta()
    elif n=='3':
        operaciones()
    elif n=='5':
        mostrarpanel()
    elif n=='8':
        acercade()
    elif n=='9':
        salir()
    else:
        borrarPant()
        print('\n\n\tERROR: Ingrese el numero de la opción que desee')
        time.sleep(2)
        menu()

def estado():
    print('FlashTrading 0.1 (pre-alfa)')
    data = {
            'Authorization': c,
            }
    r = requests.get("https://api.invertironline.com/api/estadocuenta", headers=data)
    estado = json.loads(r.text)
    n=0
    print(
        '\nEstado de cuenta nº: ', estado['cuentas'][0]['numero'],
        '\n\t\t\t\t[Total en Pesos:$',estado['totalEnPesos'],']\n',
        '\nCuenta',estado['cuentas'][0]['tipo'],
        '\t[Total:\t$',estado['cuentas'][0]['total'],']\n',
        '\n\t\tActivos Valorizados\t\t\t$',estado['cuentas'][0]['titulosValorizados'],
        '\n\t\tComprometido\t\t\t\t$',estado['cuentas'][0]['comprometido'],
        '\n\t\tDisponible para operar\t\t\t$','{:.2f}'.format((estado['cuentas'][0]['saldos'][0]['saldo']+estado['cuentas'][0]['saldos'][1]['saldo']+estado['cuentas'][0]['saldos'][2]['saldo']+estado['cuentas'][0]['saldos'][3]['saldo'])-estado['cuentas'][0]['comprometido']),
        '\n\t\tDisponible en cuenta\t\t\t$','{:.2f}'.format(estado['cuentas'][0]['disponible']),
        '\n\t\t\tSaldo a acreditarse (Inmediato) $',estado['cuentas'][0]['saldos'][1]['saldo'],
        '\n\t\t\tSaldo a acreditarse (24hs)\t$',estado['cuentas'][0]['saldos'][0]['saldo'],
        '\n\t\t\tSaldo a acreditarse (48hs)\t$',estado['cuentas'][0]['saldos'][1]['saldo'],
        '\n\t\t\tSaldo a acreditarse (72hs)\t$',estado['cuentas'][0]['saldos'][2]['saldo'],
        '\n\t\t\tSaldo a acreditarse (+72hs)\t$',estado['cuentas'][0]['saldos'][3]['saldo'],
        '\n\nCuenta',estado['cuentas'][1]['tipo'],
        '\t[Total:\tU$S',estado['cuentas'][1]['total'],']\n',
        '\n\t\tActivos Valorizados\t\t\tU$S',estado['cuentas'][1]['titulosValorizados'],
        '\n\t\tComprometido\t\t\t\tU$S',estado['cuentas'][1]['comprometido'],
        '\n\t\tDisponible para operar\t\t\t$','{:.4f}'.format(estado['cuentas'][1]['saldos'][1]['saldo']+estado['cuentas'][1]['saldos'][2]['saldo']+estado['cuentas'][1]['saldos'][3]['saldo']-estado['cuentas'][1]['comprometido']),
        '\n\t\tDisponible en cuenta\t\t\tU$S',estado['cuentas'][1]['disponible'],
        '\n\t\t\tSaldo a acreditarse (Inmediato) U$S',estado['cuentas'][1]['saldos'][1]['saldo'],
        '\n\t\t\tSaldo a acreditarse (24hs)\tU$S',estado['cuentas'][1]['saldos'][0]['saldo'],
        '\n\t\t\tSaldo a acreditarse (48hs)\tU$S',estado['cuentas'][1]['saldos'][1]['saldo'],
        '\n\t\t\tSaldo a acreditarse (72hs)\tU$S',estado['cuentas'][1]['saldos'][2]['saldo'],
        '\n\t\t\tSaldo a acreditarse (+72hs)\tU$S',estado['cuentas'][1]['saldos'][3]['saldo'],'\n',

        )
    #+estado['cuentas'][0]['saldos'][1]['saldo']+estado['cuentas'][0]['saldos'][2]['saldo']+estado['cuentas'][0]['saldos'][3]['saldo']-estado['cuentas'][0]['comprometido'],
    a=input('presione enter para ir al menu de opciones')
    borrarPant()
    menu()

def miportafolio():
    print('FlashTrading 0.1 (pre-alfa)')
    data = {
        'Authorization': c,
        }
    r = requests.get("https://api.invertironline.com/api/portafolio", headers=data)
    port = json.loads(r.text)
    print('Portafolio:')
    n=0
    while n< len(port['activos']):
        ls = port['activos'][n]['titulo']['descripcion']
        ls2 = port['activos'][n]['ultimoPrecio']
        ls3 = port['activos'][n]['cantidad']
        ls4 = port['activos'][n]['titulo']['moneda']
        ls5 = port['activos'][n]['gananciaPorcentaje']
        ls6 = port['activos'][n]['valorizado']
        ls7 = port['activos'][n]['titulo']['simbolo']
        ls8 = port['activos'][n]['variacionDiaria']
        ls9 = port['activos'][n]['gananciaDinero']
        print(ls,'\n\t\tSimbolo:\t\t',ls7,'\n\t\tNominales:\t\t',ls3,'\n\t\tCotización:\t\t $',
             ls2,ls4,'\n\t\tVariacion desde Compra:\t',ls5,'%','\n\t\tValorizado:\t\t $',ls6,ls4,
            '\n\t\tVariación Diaria:\t',ls8,'%','\n\t\tGanancia Nominal:\t $',ls9,ls4,'\n')
        n+=1
    a=input('presione enter para ir al menu de opciones')
    borrarPant()
    menu()

def consulta():
    print('FlashTrading 0.1 (pre-alfa)\n\n')
    merc='bcba'
    simb=input('\nIngrese el simbolo del titulo que desea consultar\n(ejemplo: pamp, alua, cres):\t')
    host='https://api.invertironline.com/api/'+merc+'/Titulos/'+simb+'/cotizacion'
    host2='https://api.invertironline.com/api/'+merc+'/Titulos/'+simb
    data = {
            'Authorization': c,
            'mercado':merc,
            'simbolo':simb,
            'model.simbolo':simb,
            'model.mercado':merc
            }
    r = requests.get(host, headers=data)
    r2 = requests.get(host2, headers=data)
    borrarPant()
    cotizacion=json.loads(r.text)
    datos=json.loads(r2.text)
    print(datos['descripcion'],' - [',datos['simbolo'],']\n',
          '\núltimo precio: \t$',cotizacion['ultimoPrecio'],'\t\tApertura: $',cotizacion['apertura'],'\tMáximo: $',cotizacion['maximo'],'\tMínimo: $',cotizacion['minimo'],
          '\nCierre Anterior: ',cotizacion['cierreAnterior'],
          '\nVariación:\t', cotizacion['variacion'],'%',
          '\n')
    print('-CAJA DE PUNTAS-\n')
    print('\tCOMPRA\t\tVENTA')
    print('Cantidad','Precio','\tPrecio','  Cantidad')
    n=0
    while n< len(cotizacion['puntas']):
        print('{:^8}'.format(str(int(cotizacion['puntas'][n]['cantidadCompra']))),'$',cotizacion['puntas'][n]['precioCompra'],
        '\t{:9}'.format('$'+str(cotizacion['puntas'][n]['precioVenta'])),'{:^8}'.format(str(int(cotizacion['puntas'][n]['cantidadVenta']))))
        n+=1
    k=input('presione enter para volver al menú')
    borrarPant()
    menu()

def mostrarpanel():
    hostpanel='https://api.invertironline.com/api/Cotizaciones/acciones/merval/argentina?panelCotizacion.instrumento=acciones&panelCotizacion.panel=merval&panelCotizacion.pais=argentina&api_key='+c
    body={
        'Authorization':c,
        'panelCotizacion.instrumento':'acciones',
        'panelCotizacion.panel':'merval',
        'panelCotizacion.pais':'argentina'
        }
    panel = requests.get(hostpanel, headers=body)
    merv=json.loads(panel.text)
    n=0
    borrarPant()
    print('''
----------------------------------[[MERVAL]]-----------------------------------------------
-------------------------------------------------------------------------------------------
         Último   Variación -----Compra----Puntas----Venta-----  Apertura  Máximo   Mínimo    Cierre    Cantidad     Monto
Simbolo  Precio       %     Cantidad  Precio - Precio  Cantidad                              Anterior   Operaciones  Operado
''')
    while n<len(merv['titulos']):
        print('{:8}'.format(merv['titulos'][n]['simbolo']),'{:9}'.format('$ '+str(merv['titulos'][n]['ultimoPrecio'])),'{:^9}'.format(str(merv['titulos'][n]['variacionPorcentual'])+'%'),
        '{:^7}'.format(str(int(merv['titulos'][n]['puntas']['cantidadCompra']))),'{:9}'.format('$'+str(merv['titulos'][n]['puntas']['precioCompra'])),
        '{:>7}'.format('$'+str(merv['titulos'][n]['puntas']['precioVenta'])),'{:^10}'.format(str(int(merv['titulos'][n]['puntas']['cantidadVenta']))),
        '{:8}'.format('$ '+str(merv['titulos'][n]['apertura'])),'{:8}'.format('$ '+str(merv['titulos'][n]['maximo'])),'{:9}'.format('$ '+str(merv['titulos'][n]['minimo'])),
        '{:9}'.format('$ '+str(merv['titulos'][n]['ultimoCierre'])),'{:12}'.format(str(int(merv['titulos'][n]['cantidadOperaciones']))),'{:9}'.format('$ '+str(merv['titulos'][n]['volumen']))
        )
        n+=1
    w=input('presione enter para volver al menú')
    menu()

def operaciones():
    print('FlashTrading 0.1 (pre-alfa)\n')
    print('''Seleccione que tipo de operaciones desea:
            [1] Todas
            [2] Pendientes
            [3] Terminadas
            [4] Canceladas
    ''')
    tipo=input('Ingrese la opción:  ')
    if tipo=='1':
        tipo='todas'
    elif tipo=='2':
        tipo="pendientes"
    elif tipo=='3':
        tipo='terminadas'
    elif tipo=='4':
        tipo='canceladas'
    else:
        borrarPant()
        print('Error. Ingrese un numero del 1 al 4')
        time.sleep(2)
        operaciones()
    borrarPant()
    #print(tipo)
    print('Ingrese la fecha desde la que desea consultar. (formato "aaaa-mm-dd", ejemplo: 2018-07-24)')
    print('***Si deja vacio se tomara el último mes por defecto')
    fechadesde=input()
    print('\nIngrese la fecha hasta la que desea consultar. (formato "aaaa-mm-dd", ejemplo: 2019-01-06)')
    print('***Si deja vacio se tomara hoy por defecto')
    fechahasta=input()
    data = {
        'Authorization': c,
        'filtro.numero':'',
        'filtro.estado':tipo,
        'filtro.fechaDesde':fechadesde,
        'filtro.fechaHasta':fechahasta
        }
    url='https://api.invertironline.com/api/operaciones?filtro.estado='+tipo+'&filtro.fechaDesde='+fechadesde+'&filtro.fechaHasta='+fechahasta
    r = requests.get(url, headers=data)
    operetas = json.loads(r.text)
    n=0
    print('''
    | Nº de   |Fecha de  |  Tipo  |  Estado   | Símbolo  | Cantidad   |  Precio  |  Fecha   |   Monto    |  Precio  |
    |trans.   | orden    |        |           |          | /Monto     |  orden   |  Operada |   Operado  |  operado |
    ---------------------------------------------------------------------------------------------------------------''')
    while n<len(operetas):
        if operetas[n]['estado']=='en_Proceso':
            operetas[n]['estado']='Pendiente'
        if operetas[n]['estado']=='cancelada_Por_Vencimiento_Validez':
            operetas[n]['estado']='Cancelada'
        if operetas[n]['tipo']=='Suscripción FCI':
            operetas[n]['tipo']='Sus. FCI'
        if operetas[n]['tipo']=='Pago de Renta':
            operetas[n]['tipo']='Renta'
        if operetas[n]['tipo']=='Rescate FCI':
            operetas[n]['tipo']='Rescate'
        print('    ',operetas[n]['numero'],'', operetas[n]['fechaOrden'][:10],
        '{:^8}'.format(operetas[n]['tipo']),'{:^11}'.format(operetas[n]['estado']),'{:^10}'.format(operetas[n]['simbolo']),
        '$','{:10}'.format(str(operetas[n]['monto'])),'{:^10}'.format('$ '+str(operetas[n]['precio'])),
        '{:^10.10}'.format(str(operetas[n]['fechaOperada'])),'{:^12.12}'.format('$ '+str(operetas[n]['montoOperado'])),
        '$',operetas[n]['precioOperado']
        )
        n+=1
    print('\n\n')
    k=input('Presione [Enter] para volver al menu principal.')
    menu()

def acercade():
    print('''
          FlashTrading 0.1 ((pre-alfa)) - TRADEANDO COMO UN CAMPEÓN
          ==============================================================
          ♜♞♝♚♛♝♞♜    Creado con ❤ por JoséFacundoBogado
          ♟♟♟♟♟♟♟♟
          ▓░▓░▓░▓░▓  ---contacto:
          ░▓░▓░▓░▓░         facundobogado@gmail.com
          ▓░▓░▓░▓░▓     analistabursatil.formosa@gmail.com
          ░▓░▓░▓░▓░ https://www.facebook.com/economia.mercados.7
          ♙♙♙♙♙♙♙♙ =====================================================
          ♖♘♗♔♕♗♘♖
          Licencia GPL - "Porque lo mejor de la vida es gratis!"
                  (https://www.gnu.org/licenses/gpl.html)
        ***Este software no posee ninguna garantia en su funcionamiento.
        Esto es totalmente libre y gratuito, y pueden sentirse libres de
        modificar y redistribuirlo siempre y cuando se aclare la fuente.
        ***Este programa no esta relacionado en absoluto con la empresa
        InvertirOnline.
        ***Este programa ni guarda, ni envia información a terceros.
        Sus datos de inicio de sesión sólo seran enviados al servidor de
        la API oficial de InvertirOnline.
                  ♖♘♗♔♕♗♘♖
                                            ---Clara(I❤U)---
          ''')
    k=input('presione enter para volver al menu')
    borrarPant()
    menu()

def salir():
    print('FlashTrading 0.1 (pre-alfa)')
    print('''
                 """""""
                 ^-O-O-^
            ---ooO--U--Ooo-----
             Muchas Gracias
              Hasta luego!
                    JoséFacundoBogado
          ''')
    time.sleep(1)
    exit()

if len(sys.argv) == 3:
    _user = sys.argv[1]
    _pass = sys.argv[2]
    _data = {
        'username':_user,
        'password':_pass,
        'grant_type':'password'
        }
    r = requests.post("https://api.invertironline.com/token", data=_data)
    c = 'Bearer '+str(json.loads(r.text)['access_token'])
    borrarPant()
    print('Bienvenido a FlashTrading 0.1 (pre-alfa)\nun script para operar en InvertirOnline\n\n\n               ***NO POSEO RELACION CON INVERTIRONLINE\n               ***SIN GARANTIA, ÚSESE BAJO SU RESPONSABILIDAD\n\n\n\n\tcreado por Facundo Bogado(c) para consumo humano, NO COMERCIAL\nLicencia GPL (https://www.gnu.org/licenses/gpl.html) Derechos reservados.\n\n\n\t\t\t\t\t\t---dedicado a Clara(I❤U)\n')
    print(str(json.loads(r.text)['access_token'])) #active este codigo si necesita copiar la bearer token
    time.sleep(1)
    borrarPant()
    estado()

else:
    print('FlashTrading 0.1 (pre-alfa)\n\n')
    print('Bienvenidos: introduzca usuario y contraseña\n')
    _user = input('Ingrese su usuario:  ')
    _pass = input('Ingrese su contraseña:  ')
    _data = {
        'username':_user,
        'password':_pass,
        'grant_type':'password'
        }
    r = requests.post("https://api.invertironline.com/token", data=_data)
    c = 'Bearer '+str(json.loads(r.text)['access_token'])
    print('Bienvenido a FlashTrading 0.1 (pre-alfa)\nun script para operar en InvertirOnline\n\n\n               ***NO POSEO RELACION CON INVERTIRONLINE\n               ***SIN GARANTIA, ÚSESE BAJO SU RESPONSABILIDAD\n\n\n\n\tcreado por Facundo Bogado(c) para consumo humano, NO COMERCIAL\nLicencia GPL (https://www.gnu.org/licenses/gpl.html) Derechos reservados.\n\n\n\t\t\t\t\t\t---dedicado a Clara(I❤U)\n')
    print(str(json.loads(r.text)['access_token'])) #active este codigo si necesita copiar la bearer token
    time.sleep(1)
    #borrarPant()
    estado()