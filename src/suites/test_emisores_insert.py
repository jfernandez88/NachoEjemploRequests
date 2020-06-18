import requests, pytest, json
from random import randrange
from pytest_html import extras
from funciones.sql import sqlQuery
from funciones.trello import crearTarjeta

descripcion = "TEST EMISOR"
idPais = "ARG"
idEmisor = "TEST QA_AUTOMATION"
moneda = "32"
esPrivado = False
cuit = "20342114335"


def setup_module():
      sqlQuery("DELETE FROM EMISORES where Descripcion = 'TEST EMISOR'")  


#001 - Emisor - Alta - Todos los campos
def test_Emisor_101_AltaTodosLosCampos(emisoresInsert, extra,getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "descripcion": descripcion,
                        "idPais": idPais,
                        "idEmisor": idEmisor,
                        "moneda": moneda,
                        "esPrivado": esPrivado,
                        "cuit": cuit
                }
        resp = requests.post(emisoresInsert, json=payload, headers = headers)   
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))
        respJson = resp.json()
        assert resp.status_code == 200, "ERROR "+str(resp.status_code)
        assert respJson['codigo'] > 0,crearTarjeta(request.node.name, str(payload), resp.text)

#005 Alta codInterfaz Existente
def test_Emisor_105_AltaCodInterfazExistente(emisoresInsert,extra,getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "descripcion": descripcion,
                        "idPais": idPais,
                        "idEmisor": idEmisor,
                        "moneda": moneda,
                        "esPrivado": False,
                        "cuit": cuit
                }
        resp = requests.post(emisoresInsert, json=payload, headers = headers)   
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))
        assert respJson['error']['Msj'] != '', crearTarjeta(request.node.name, str(payload), resp.text)