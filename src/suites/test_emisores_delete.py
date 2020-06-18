import requests, pytest, json
from pytest_html import extras
from dataEmisores import deleteEmisores
from funciones.sql import *
from funciones.trello import crearTarjeta

idEmisor = 'J1'
descEmisor = 'EmisorJ1'

def setup_module():
      sqlQuery("UPDATE EMISORES SET EstaAnulado = 0 WHERE CodInterfaz = '"+idEmisor+"'")  


#103 - Emisor - Baja- Exitosa
def test_Emisor_103_BajaExitosa(emisoresUpdate,emisoresDelete, getApiVersion, extra,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                 "idEmisor": idEmisor
                }
        resp = requests.post(emisoresDelete, json=payload, headers = headers)   
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))
        respJson = resp.json()
        assert respJson['codigo'] > 0 ,crearTarjeta(request.node.name, str(payload), resp.text)
 
def test_Emisor_114_Baja_idEmisorInexistente(emisoresDelete, getApiVersion, extra, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                 "idEmisor": "14141"
                }
        resp = requests.post(emisoresDelete, json=payload, headers = headers)   
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))
        respJson = resp.json()
        assert respJson['error']['Msj'] == 'Codigo de Interfaz invalido.',crearTarjeta(request.node.name, str(payload), resp.text)

def test_Emisor_115_Baja_sinCampoIdEmisor(emisoresDelete, getApiVersion, extra, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                 
                }
        resp = requests.post(emisoresDelete, json=payload, headers = headers)   
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))
        respJson = resp.json()
        assert 'idEmisor' in  respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text + "\n \n Se esperaba un msj similar a idEmisor es requerido")