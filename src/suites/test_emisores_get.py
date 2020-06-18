import requests, pytest, json
from dataEmisores import dataEmisores
from dataEmisores import dataMoneda
from dataEmisores import dataPais
from pytest_html import extras
from funciones.sql import sqlQuery
from funciones.trello import crearTarjeta

idEmisorDadoBaja = "API"
idEmisor = "BGAL"


#006 - Consulta Emisor dado de Baja
def test_Emisor_106_consultaEmisorDadoDeBaja(emisoresGet,getApiVersion,extra, request):
    headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
    payload = {
                "idEmisor": idEmisorDadoBaja
              }
    resp = requests.post(emisoresGet, json=payload, headers = headers)    
    respJson = resp.json()
    extra.append(extras.json(payload, name="Request"))
    extra.append(extras.text(resp.text, name = 'Response'))

    assert len(respJson) > 0, "Se devolvió respuesta vacia"
    assert respJson[0]['idEmisor'] == idEmisorDadoBaja,crearTarjeta(request.node.name, str(payload), resp.text+"\n Se esperaba que el campo estaAnulado se muestre en True") 



#007 - Consulta Emisor ok
def test_Emisor_107_consultaPorIdEmisor(emisoresGet, extra,getApiVersion, request):
    headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
    payload = {
                "idEmisor": idEmisor
              }
    resp = requests.post(emisoresGet, json=payload, headers = headers)    
    respJson = resp.json()
    extra.append(extras.json(payload, name="Request"))
    extra.append(extras.text(resp.text, name = 'Response'))

    assert len(respJson) > 0, crearTarjeta(request.node.name, str(payload), resp.text)
    assert respJson[0]['idEmisor'] == idEmisor


#012 -  Consulta - Emisor NoExiste
def test_Emisor_112_ConsultaIdEmisorNoExiste(emisoresGet,extra,getApiVersion, request):
    headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
    payload = {
                "idEmisor": "171257272"
              }
    resp = requests.post(emisoresGet, json=payload, headers = headers)    
    respJson = resp.json()
    extra.append(extras.json(payload, name="Request"))
    extra.append(extras.text(resp.text, name = 'Response'))
    assert len(respJson) > 0, crearTarjeta(request.node.name, str(payload), resp.text+"\n Se devolvio respuesta vacia")
    assert "idEmisor" not in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se esperaba un Msj similar a idEmisor es requerido")


#013 - Consulta - Emisor Sin idEmisor
def test_Emisor_113_ConsultaSinIdEmisor(emisoresGet,extra,getApiVersion, request):
    headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
    payload = {
                #"idEmisor": "BGAL"
              }
    resp = requests.post(emisoresGet, json=payload, headers = headers)    
    respJson = resp.json()
    extra.append(extras.json(payload, name="Request"))
    extra.append(extras.text(resp.text, name = 'Response'))
    assert len(respJson) > 0,crearTarjeta(request.node.name, str(payload), resp.text+"\n Se devolvio respuesta vacia")
    #assert respJson[0]['exception']['escoMessage'] != "" 
        



