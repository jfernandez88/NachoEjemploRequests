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

def setup_module():
      sqlQuery("UPDATE CTASBANCARIAS SET EstaAnulado = 0 WHERE CodInterfaz = '"+idCuentaBancaria+"'")  


#518 Baja de cuenta por idCuentaBancaria
def test_CuentasBancarias_518_BajaPorIdCuntaBancaria(deleteCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version":getApiVersion, "Content-Type":"application/json"}
        payload = {
                    "idCuentaBancaria": idCuentaBancaria,
                  }
        resp = requests.post(deleteCuentasBancarias, json=payload, headers = headers)
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))
        respJson = resp.json()     
        assert respJson['codigo'] != 0,crearTarjeta(request.node.name, str(payload), resp.text)

#519 Baja de cuenta por idCuentaBancaria - NOK
def test_CuentasBancarias_519_BajaPorIdCuntaBancariaInexistente(deleteCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version":getApiVersion, "Content-Type":"application/json"}
        payload = {
                    "idCuentaBancaria": "ASASAS",
                  }
        resp = requests.post(deleteCuentasBancarias, json=payload, headers = headers)
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))
        #respJson = resp.json()     
        assert resp.status_code != 200,crearTarjeta(request.node.name, str(payload), resp.text)


def test_CuentasBancarias_520_BajaPorSinIdCuntaBancaria(deleteCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version":getApiVersion, "Content-Type":"application/json"}
        payload = {
                    
                  }
        resp = requests.post(deleteCuentasBancarias, json=payload, headers = headers)
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))
        #respJson = resp.json()     
        assert resp.status_code != 200

