import requests, pytest, json
from pytest_html import extras
from dataEspecies import dataConsultaEspecies
from funciones.sql import sqlQuery
from funciones.trello import crearTarjeta


idBanco = "MARIVA"
moneda = "32"
monedaInex = "inexistente"

#421	Consulta por idBanco	ok: Resultado: Se deben devolver todos los PF con ese ID
def test_plazoFijo_421_Consulta_PorIdBanco(getPlazoFijo,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                    "idBanco": idBanco
                   }
        resp = requests.post(getPlazoFijo, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code == 200
        for row in respJson:
            assert row['banco']['idBanco'] == idBanco,crearTarjeta(request.node.name, str(payload), resp.text)

#422	Consulta	Consulta por moneda
def test_plazoFijo_422_Consulta_PorMoneda(getPlazoFijo,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                    "moneda": moneda
                   }
        resp = requests.post(getPlazoFijo, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code == 200
        for row in respJson:
            assert row['moneda']['idMoneda'] == 'ARS',crearTarjeta(request.node.name, str(payload), resp.text)

#423 Consulta por rango de fechas fechaConcertacion y fechaLiquidacion
def test_plazoFijo_423_Consulta_PorFechaConcertFechaLiq(getPlazoFijo,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                      "fechaConcertacion": "2014-09-16",
                      "fechaLiquidacion":  "2015-03-16"
                   }
        resp = requests.post(getPlazoFijo, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code == 200
        for row in respJson:
            assert row['fechaConcertacion'] == '2014-09-16T00:00:00'#,crearTarjeta(request.node.name, str(payload), resp.text)
            assert row['fechaLiquidacion'] == '2015-03-16T00:00:00'

#424	Consulta por idPlazoFijo (codigo de interfaz)