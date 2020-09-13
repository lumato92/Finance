import requests
import json
import sys
import os
import time

USER="ltorrado@directvla.com.ar"
PASS="directv.55"
global bearer_token
bearer_token=0

_data= {
    'username': USER,
    'password': PASS,
    'grant_type':'password'
}



########### OBTENER TOKEN DE API ######################
def get_TOKEN ():
    global bearer_token
    r=requests.post('https://api.invertironline.com/token', data=_data)

    bearer_token='Bearer '+(str(json.loads(r.text)['access_token']))


##################### Funciones de Consulta ######################  

def estado_cuenta():
    datos={
    'Authorization':bearer_token
    }
    r=requests.get('https://api.invertironline.com/api/estadocuenta', headers=datos)
    '''if r.status_code !=200:
        get_TOKEN()
        estado_cuenta() '''

    with open('estado.json','w', encoding='utf-8') as f:
        json.dump(r.text,f)
    print(str(json.loads(r.text)))

def portfolio():
    datos={
    'Authorization':bearer_token
    }
    r=requests.get('https://api.invertironline.com/api/portafolio', headers=datos)   #Ver como agregar pais
    '''if r.status_code !=200:
        get_TOKEN()
        estado_cuenta() '''

    with open('portafolio.json','w', encoding='utf-8') as f:
        json.dump(r.text,f)
    print(str(json.loads(r.text)))

def operacion (nro):
    datos={
    'Authorization':bearer_token
    }
    r=requests.get('https://api.invertironline.com/api/operaciones/'+nro, headers=datos)   #Ver como agregar pais       
    with open('operacion.json','w', encoding='utf-8') as f:
        json.dump(r.text,f)
    print(str(json.loads(r.text)))

    if not ((json.loads(r.text))['ok']):
        print("Nro Operacion ERRONEO")
    print("hasta ok")

###### TITULOS #############

def FCI():
    datos={
    'Authorization':bearer_token
    }
    r=requests.get('https://api.invertironline.com/api/v2/Titulos/FCI/TipoFondos',headers=datos)   #Ver como agregar pais       
    with open('fci.json','w', encoding='utf-8') as f:
        json.dump(r.text,f)
    print(str(json.loads(r.text)))

def Paneles():

    datos={
    'Authorization':bearer_token
    }
    r=requests.get('https://api.invertironline.com/api/v2/argentina/Titulos/Cotizacion/Paneles/Lider',headers=datos)   #Ver como agregar pais       
    with open('PANEL.json','w', encoding='utf-8') as f:
        json.dump(r.text,f)
    print(str(json.loads(r.text)))


def mostrarpanel():
    hostpanel='https://api.invertironline.com/api/Cotizaciones/bonos/merval/argentina?panelCotizacion.instrumento=acciones&panelCotizacion.panel=merval&panelCotizacion.pais=argentina&api_key='+bearer_token
    body={
        'Authorization':bearer_token,
        'panelCotizacion.instrumento':'acciones',
        'panelCotizacion.panel':'merval',
        'panelCotizacion.pais':'argentina'
        }
    panel = requests.get(hostpanel, headers=body)
    merv=json.loads(panel.text)
    print(merv)
    

get_TOKEN()
print("HASTA ACA OK")
print(bearer_token)
#time.sleep(1)
#estado_cuenta()
#portfolio()
#operacion('6065537')
#FCI()
mostrarpanel()  