import requests, pytest, json
from pytest_html import extras
from dataEspecies import dataConsultaEspecies
from funciones.trello import crearTarjeta

idAgente = "2"

#Devuelve la lista de Agentes
def test_TablasDelSistema_GetAgentes(getAgentes,request,getApiVersion,extra):

        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                    
                 }

        resp = requests.get(getAgentes, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert len(respJson) > 0, "Se devolvió respuesta vacia"
        assert respJson[0]['codigo'] is not None, crearTarjeta(request.node.name, str(payload), resp.text+"\n StatusCode "+str(resp.status_code)) 
        

#Devuelve la lista de Bancos
def test_TablasDelSistema_GetBancos(getBancos,request,getApiVersion,extra):

        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                    
                 }

        resp = requests.get(getBancos, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert len(respJson) > 0, "Se devolvió respuesta vacia"
        assert respJson[0]['codigo'] is not None, crearTarjeta(request.node.name, str(payload), resp.text+"\n StatusCode "+str(resp.status_code)) 

#Devuelve la lista de Depositarios
def test_TablasDelSistema_getDepositarios(getDepositarios,request,getApiVersion,extra):

        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                    
                 }

        resp = requests.get(getDepositarios, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert len(respJson) > 0,crearTarjeta(request.node.name, str(payload), resp.text+"\n StatusCode "+str(resp.status_code)) 
        assert respJson[0]['codigo'] is not None, crearTarjeta(request.node.name, str(payload), resp.text+"\n StatusCode "+str(resp.status_code)) 

#Devuelve la lista de Mercados
def test_TablasDelSistema_getMercados(getMercados,request,getApiVersion,extra):

        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                    
                 }

        resp = requests.get(getMercados, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert respJson[0]['codigo'] is not None, crearTarjeta(request.node.name, str(payload), resp.text+"\n StatusCode "+str(resp.status_code)) 

#Devuelve la lista de Monedas habilitadas.
def test_TablasDelSistema_getMonedas(getMonedas,request,getApiVersion,extra):

        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                    
                 }

        resp = requests.get(getMonedas, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert respJson[0]['codigo'] is not None, crearTarjeta(request.node.name, str(payload), resp.text+"\n StatusCode "+str(resp.status_code)) 

#Devuelve la lista de Paises habilitados.
def test_TablasDelSistema_getPaises(getPaises,request,getApiVersion,extra):

        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                    
                 }

        resp = requests.get(getPaises, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert respJson[0]['codigo'] is not None, crearTarjeta(request.node.name, str(payload), resp.text+"\n StatusCode "+str(resp.status_code)) 

#Consulta de abreviaturas
def test_TablasDelSistema_getTiposAbreviaturas(getTiposAbreviaturas,request,getApiVersion,extra):

        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                    
                 }

        resp = requests.get(getTiposAbreviaturas, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert respJson[0]['codigo'] is not None, crearTarjeta(request.node.name, str(payload), resp.text+"\n StatusCode "+str(resp.status_code)) 


#Devuelve la lista de Tipos de Cuentas Bancarias
def test_TablasDelSistema_getTiposCuentasBancarias(getTiposCuentasBancarias,request,getApiVersion,extra):

        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                    
                 }

        resp = requests.get(getTiposCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert len(respJson) > 0, crearTarjeta(request.node.name, str(payload), resp.text+"\n StatusCode "+str(resp.status_code)) 
        try:
                assert respJson[0]['codigo'] is not None, crearTarjeta(request.node.name, str(payload), resp.text+"\n StatusCode "+str(resp.status_code)) 
        except:
                crearTarjeta(request.node.name, str(payload), resp.text+"\n StatusCode "+str(resp.status_code)) 

#Devuelve la lista de Tipos de Devengamiento de las Cuentas Bancarias
def test_TablasDelSistema_getTiposDevengamientoCuentasBancarias(getTiposDevengamientoCuentasBancarias,request,getApiVersion,extra):

        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                    
                 }

        resp = requests.get(getTiposDevengamientoCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert len(respJson) > 0, "Se devolvió respuesta vacia"
        assert respJson[0]['codigo'] is not None, crearTarjeta(request.node.name, str(payload), resp.text+"\n StatusCode "+str(resp.status_code)) 

#Devuelve la lista de Tipos de Especies
def test_TablasDelSistema_getTiposEspecie(getTiposEspecie,request,getApiVersion,extra):

        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                    
                 }

        resp = requests.get(getTiposEspecie, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert len(respJson) > 0, "Se devolvió respuesta vacia"
        assert respJson[0]['codigo'] is not None, crearTarjeta(request.node.name, str(payload), resp.text+"\n StatusCode "+str(resp.status_code)) 

#Devuelve la lista de Tipos de Operaciones
def test_TablasDelSistema_getTiposOperaciones(getTiposOperaciones,request,getApiVersion,extra):

        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                    
                 }

        resp = requests.get(getTiposOperaciones, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert len(respJson) > 0, "Se devolvió respuesta vacia"
        assert respJson[0]['codigo'] is not None, crearTarjeta(request.node.name, str(payload), resp.text+"\n StatusCode "+str(resp.status_code)) 

#Devuelve la lista de Tipos de Valuaciones
def test_TablasDelSistema_getTiposValuacion(getTiposValuacion,request,getApiVersion,extra):

        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                    
                 }

        resp = requests.get(getTiposValuacion, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert len(respJson) > 0, "Se devolvió respuesta vacia"
        assert respJson[0]['codigo'] is not None, crearTarjeta(request.node.name, str(payload), resp.text+"\n StatusCode "+str(resp.status_code)) 
