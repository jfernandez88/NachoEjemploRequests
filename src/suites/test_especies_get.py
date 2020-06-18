import requests, pytest, json
from pytest_html import extras
from dataEspecies import dataConsultaEspecies
from funciones.trello import crearTarjeta

idEspecie = "PR12"
codigoEspecie = "2"
idMoneda = "ARS"
isinCode = "ARARGE035162"
idTipoEspecie = "35"
idEmisor = 'AJ12'


#001 - Especies - Consulta por codigo de interfaz especie
def test_Especies_201_ConsultaPorCodInterfaz(especiesGet,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                    "idEspecie": idEspecie
                    #"codigoEspecie": "string",
                    #"isinCode": "string",
                    #"moneda": "string",
                    #"idTipoEspecie": "string",
                    #"idEmisor": "string"
                }
        resp = requests.post(especiesGet, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert len(respJson) > 0, "Se devolvió respuesta vacia"
        assert respJson[0]['idEspecie'] == idEspecie

#013 - Especies - Consulta por codigoEspecie
def test_Especies_213_ConsultaPorCodEspecie(especiesGet,extra,getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                    "codigoEspecie": codigoEspecie
                }
        resp = requests.post(especiesGet, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert len(respJson) > 0, crearTarjeta(request.node.name, str(payload), resp.text+"\n Se devolvio respuesta vacia")
        assert respJson[0]['codigoEspecie'] == codigoEspecie


#014 - Especies - Consulta por isinCode
def test_Especies_214_ConsultaPorIsinCode(especiesGet,extra,getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                    "isinCode": isinCode
                }
        resp = requests.post(especiesGet, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert len(respJson) > 0, crearTarjeta(request.node.name, str(payload), resp.text+"\n Se devolvio respuesta vacia")
        assert respJson[0]['isinCode'] == isinCode

#015 - Especies - Consulta por moneda
def test_Especies_215_ConsultaPorMoneda(especiesGet,extra,getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                    "moneda": idMoneda
                }
        resp = requests.post(especiesGet, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert len(respJson) > 0, crearTarjeta(request.node.name, str(payload), resp.text+"\n Se devolvio respuesta vacia")
        assert respJson[0]['moneda'] == idMoneda

#016 - Especies - Consulta por idTipoEspecie
def test_Especies_216_ConsultaPoridTipoEspecie(especiesGet,extra,getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                    "idTipoEspecie": idTipoEspecie
                }
        resp = requests.post(especiesGet, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert len(respJson) > 0, crearTarjeta(request.node.name, str(payload), resp.text+"\n Se devolvio respuesta vacia")
        assert respJson[0]['idTipoEspecie'] == idTipoEspecie


#017 - Especies - Consulta por idEmisor
def test_Especies_217_ConsultaPorIdEmisor(especiesGet,extra,getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                    "idEmisor": idEmisor
                }
        resp = requests.post(especiesGet, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert len(respJson) > 0, crearTarjeta(request.node.name, str(payload), resp.text+"\n Se devolvio respuesta vacia")
        assert respJson[0]['idEmisor'] == idEmisor

#018 - Especies - Consulta sin campos
def test_Especies_218_ConsultaSinCampos(especiesGet,extra,getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                    
                }
        resp = requests.post(especiesGet, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert len(respJson) > 0, crearTarjeta(request.node.name, str(payload), resp.text+"\n Se devolvio respuesta vacia")
        