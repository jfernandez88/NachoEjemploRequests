import requests, pytest, json
from pytest_html import extras
from funciones.trello import crearTarjeta
from funciones.sql import sqlQuery


idEmisor = 'J1'
descEmisor = 'EmisorJ1'
moneda = '32'
cuit = '20342114335'
idPais = "ARG"

#108 - Actualizacion - id Emisor NoExiste
def test_Emisor_108_Actualizacion_idEmisorInexistente(emisoresUpdate,getApiVersion, extra, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "descripcion": "Test UpdaTE",
                        "idPais": idPais,
                        "idEmisor": "9999",
                        "moneda": moneda,
                        "esPrivado": False,
                        "cuit": cuit
                  }
        resp = requests.post(emisoresUpdate, json=payload, headers = headers)   
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))
        assert len(respJson) > 0, crearTarjeta(request.node.name, str(payload), resp.text+"\n Se devolvio respuesta vacia")
        assert respJson['error']['Msj'] != '', crearTarjeta(request.node.name, str(payload), resp.text)

#109	Actualizacion	Sin codigo de Emisor	Al intentar actualizar sin enviar el codEmisor, el servicio devolverá una sugerencia similar a 'idEmisor es requerido'
def test_Emisor_109_Actualizacion_SinIdEmisor(emisoresUpdate, getApiVersion, extra, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload =  {
                        #"idEmisor": idEmisor,
                        "moneda": moneda,
                        "esPrivado": False,
                        "cuit": cuit
                   }
                
        resp = requests.post(emisoresUpdate, json=payload, headers = headers)   
        #respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))
        assert resp.status_code != 200


#110 Actualizacion con código y cambio de Moneda es Privado
def test_Emisor_110_Actualizacion_CodMonedaEsPrivado(emisoresUpdate, getApiVersion, extra, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload =  {
                        "idEmisor": idEmisor,
                        "moneda": moneda,
                        "esPrivado": False,
                        "cuit": cuit
                   }
                
        resp = requests.post(emisoresUpdate, json=payload, headers = headers)   
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))
        assert resp.status_code == 200
        assert respJson['codigo'] > 0,crearTarjeta(request.node.name, str(payload), resp.text)

'''
#111 Actualización CuitInvalido
def test_Emisor_111_Actualizacion_CuitInvalido(emisoresUpdate, extra,getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload ={
                        "descripcion": "EmisorJ1",
                        #"idPais": idPais,
                        "idEmisor": idEmisor,
                        "moneda": moneda,
                        "esPrivado": True,
                        "cuit": '111'
                  }
        resp = requests.post(emisoresUpdate, json=payload, headers = headers)   
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))
        assert respJson['error']['Msj'] == 'CUIT inválido.',crearTarjeta(request.node.name, str(payload), resp.text)
'''