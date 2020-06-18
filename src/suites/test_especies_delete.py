import requests, pytest, json
from pytest_html import extras
from funciones.trello import crearTarjeta
from funciones.sql import *

idEspecie = 'RO15'

#def setup_module():
      #sqlQuery("UPDATE ESPECIES SET EstaAnulado = 0 WHERE CodInterfaz = '"+idEspecie+"'")  


#210 - Especies - Baja de especie codigo de interfaz incorrecto
def test_Especies_210_BajaCodInterfazIncorrecto(especiesDelete,extra, getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                       
                }
        resp = requests.get(especiesDelete, json=payload, headers = headers) 
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        respJson = resp.json()   
        assert resp.status_code != 200,crearTarjeta(request.node.name, str(payload),resp.text+"\n \n Se espera el msg similar a 'idEspecie requerido'")
        assert "idEspecie" in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg similar a 'idEspecie requerido'")

#211	Baja de especie idEspecie inexistente
def test_Especies_211_BajaIdEspecieInexistente(especiesDelete,extra, getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "idEspecie": "ASASS"
                }
        resp = requests.get(especiesDelete, json=payload, headers = headers) 
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        respJson = resp.json() 
        assert resp.status_code != 200,crearTarjeta(request.node.name, str(payload), resp.text)
        assert "idEspecie" in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg similar a 'idEspecie no existe'")


#212 - Especies - Delete - Anular idEspecie
def test_Especies_212_AnularIdEspecie(especiesDelete,extra,getApiVersion, request):
        headers = {"api-version":getApiVersion, "Content-Type":"application/json"}
        payload = {
                    "idEspecie": idEspecie
                  }
        resp = requests.get(especiesDelete, json=payload, headers = headers)
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))     
        assert resp.status_code == 200,crearTarjeta(request.node.name, str(payload), resp.text)

