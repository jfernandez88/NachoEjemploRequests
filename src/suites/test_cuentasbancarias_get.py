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
idCuentaBancariaAnulada = "666"

#513 Consulta - Debe devolverse todas las cuentas activas del fondo - numFondo
def test_CuentasBancarias_513_ConsultaPornumFondo(getCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo
                        #"nroCuenta": nroCuenta,
                        #"idBanco": idBanco,
                        #"idTpCuentaBancaria": idTpCuentaBancaria,
                        #"idCuentaBancaria": idCuentaBancaria
                  }
        resp = requests.post(getCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 

        assert len(respJson) > 0,crearTarjeta(request.node.name, str(payload), resp.text)
        for row in respJson:
                assert row['fondo']['numFondo'] == numFondo,crearTarjeta(request.node.name, str(payload), resp.text)


#514 Consulta - Consultar por numero de cuenta - nroCuenta
def test_CuentasBancarias_514_ConsultaPornroCuenta(getCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "nroCuenta": nroCuenta
                  }
        resp = requests.post(getCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 

        assert len(respJson) > 0,crearTarjeta(request.node.name, str(payload), resp.text)
        for row in respJson:
                assert row['nroCuenta'] == nroCuenta,crearTarjeta(request.node.name, str(payload), resp.text)
 

#515 Consulta Consulta por codigo de interfaz - idBanco
def test_CuentasBancarias_515_ConsultaPorIdBanco(getCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "idBanco": idBanco
                  }
        resp = requests.post(getCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert len(respJson) > 0,crearTarjeta(request.node.name, str(payload), resp.text)
        for row in respJson:
                assert row['banco']['idBanco'] == idBanco,crearTarjeta(request.node.name, str(payload), resp.text)


#516	Consulta por tipo de cuenta bancaria - idTpCuentaBancaria
def test_CuentasBancarias_516_ConsultaPoridTpCuentaBancaria(getCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "idTpCuentaBancaria": idTpCuentaBancaria
                  }
        resp = requests.post(getCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert len(respJson) > 0,crearTarjeta(request.node.name, str(payload), resp.text)
        assert respJson[0]['tipoCuentaBancaria']['idTipoCuentaBancaria'] == idTpCuentaBancaria,crearTarjeta(request.node.name, str(payload), resp.text)

#517	Consult	 de la cuenta por codigo de interfaz - idCuentaBancaria
def test_CuentasBancarias_517_ConsultaPoridCuentaBancaria(getCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "idCuentaBancaria": idCuentaBancaria
                  }
        resp = requests.post(getCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert len(respJson) > 0,crearTarjeta(request.node.name, str(payload), resp.text)
        for row in respJson:
                assert row['idCuentaBancaria'] == idCuentaBancaria,crearTarjeta(request.node.name, str(payload), resp.text)


#521	Consulta de cuenta bancaria anulada por cualquier metodo
def test_CuentasBancarias_521_ConsultaCuentaBancariaAnulada(getCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "idCuentaBancaria": idCuentaBancariaAnulada
                  }
        resp = requests.post(getCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert len(respJson) > 0, crearTarjeta(request.node.name, str(payload), resp.text)

#522	Consulta	Consulta de cuenta bancaria sin datos
def test_CuentasBancarias_522_ConsultaCuentaBancariaSinDatos(getCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        
                  }
        resp = requests.post(getCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert  "The API query failed" not in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Agregar validación por no enviar datos")
        assert resp.status_code != 200