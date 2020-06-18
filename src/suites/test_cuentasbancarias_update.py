import requests, pytest, json
from pytest_html import extras
from dataEspecies import dataConsultaEspecies
from funciones.sql import sqlQuery
from funciones.trello import crearTarjeta

numFondo = 5
nroCuenta = "2222"
idBanco = "COLUMBIA"
idTpCuentaBancaria = "8397"
idCuentaBancaria = "2222"
codTpDevCtaBancaria = "ND"


#510	Modificacion	Modificacion sin el campo idCuentaBancaria 
def test_CuentasBancarias_510_ModificarSinIdCuentaBancaria(updateCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "idTpCuentaBancaria": idTpCuentaBancaria,
                        "codTpDevCtaBancaria": codTpDevCtaBancaria,
                        "baseDias": 0,
                        #"idCuentaBancaria": "string"
                }
        resp = requests.post(updateCuentasBancarias, json=payload, headers = headers) 
        #respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code != 200


#511	Modificacion	Modificar la idTpCuentaBancaria en dias mediante idCuentaBancaria 
def test_CuentasBancarias_511_ModificaridTpCuentaBancaria(updateCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "idCuentaBancaria" : idCuentaBancaria,
                        "idTpCuentaBancaria" : idTpCuentaBancaria,
                        "codTpDevCtaBancaria" : codTpDevCtaBancaria,
                        "baseDias" : 365
                }
        resp = requests.post(updateCuentasBancarias, json=payload, headers = headers) 
        #respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert resp.status_code == 200,crearTarjeta(request.node.name, str(payload), resp.text)
    
#512	Modificar la codTpDevCtaBancaria en dias mediante idCuentaBancaria	ok Mensaje:Se a modificaco el campo codTpDevCtaBancaria 
def test_CuentasBancarias_512_Modificar_IdcodTpDevCtaBancaria_BaseDias(updateCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "codTpDevCtaBancaria": "LI",
                        "baseDias": 360,
                        "idCuentaBancaria": "775577"
                 }
        resp = requests.post(updateCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert resp.status_code == 200#,crearTarjeta(request.node.name, str(payload), resp.text)



#525	Modificacion	Modificar la base en dias
def test_CuentasBancarias_525_ModificarBaseEnDias(updateCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "idCuentaBancaria": idCuentaBancaria,
                        "baseDias": 360,
                }
        resp = requests.post(updateCuentasBancarias, json=payload, headers = headers) 
        #respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code == 200

#526    Modificacion base en dias sin el campo idCuentaBancaria "Nok: Mensaje: El campo idCuentaBancaria  es obligatorio
def test_CuentasBancarias_526_ModificarBaseSinIdCuentaBancaria(updateCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "baseDias": 360
                }
        resp = requests.post(updateCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert "idCuentaBancaria" in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se esperaba un Msj similar a idCuentaBancaria es requerido")

#528	Modificacion por valor inexisente
def test_CuentasBancarias_528_ModificarPorValorInexistente(updateCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "idCuentaBancaria": "777",
                        "idTpCuentaBancaria": "JA",
                        "codTpDevCtaBancaria": "LD",
                        "baseDias": 365
                }
        resp = requests.post(updateCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert resp.status_code != 200#,crearTarjeta(request.node.name, str(payload), resp.text)

#531	Modificacion	Modificaicon completa
def test_CuentasBancarias_531_ModificacionCompleta(updateCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "idTpCuentaBancaria": "8398",
                        "codTpDevCtaBancaria": "LI",
                        "baseDias": 360,
                        "idCuentaBancaria": "775577"
                }
        resp = requests.post(updateCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert resp.status_code == 200#,crearTarjeta(request.node.name, str(payload), resp.text)
