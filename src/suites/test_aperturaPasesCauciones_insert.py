import requests, pytest, json
from pytest_html import extras
from dataEspecies import dataConsultaEspecies
from funciones.sql import sqlQuery
from funciones.trello import crearTarjeta


#701	Alta exitosa
def test_AperturaPasesCausiones_701_Alta_Completa(insertAperturaPasesCausiones,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": 5,
                        "codTipoOperacion": "APCC",
                        "idAgente": "22",
                        "codTpDevengamiento": "DE",
                        "monedaConcertacion": "1",
                        "monedaLiquidacion": "2",
                        "monedaGastos": "2",
                        "idEspecie": "AJ12",
                        "idPasesCauciones": "QAAUTOMATION",
                        "boletoContadoFechaConcert": "2020-06-16T17:33:13.041Z",
                        "boletoContadoFechaLiquid": "2020-07-16T17:33:13.041Z",
                        "boletoContadoNumero": "2",
                        "boletoContadoCantidad": 1,
                        "boletoContadoPrecio": 1,
                        "boletoFuturoFechaConcert": "2020-06-16T17:33:13.041Z",
                        "boletoFuturoFechaLiquid": "2020-07-16T17:33:13.041Z",
                        "boletoFuturoNumero": "2",
                        "boletoFuturoCantidad": 1,
                        "boletoFuturoPrecio": 1,
                        "tipoCambioConcertacion":10,
                        "tipoCambioLiquidacion": 2,
                        "tipoCambioGastos": 1,
                        "cantidad": 1,
                        "precio": 1,
                        "arancel": 1,
                        "impuesto": 2,
                        "derechoBolsa": 1,
                        "derechoMercado": 2
                }
        resp = requests.post(insertAperturaPasesCausiones, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code == 200#, crearTarjeta(request.node.name, str(payload), resp.text)
        assert respJson['codigo'] > 0


#729	Alta con idPasesCauciones existente
def test_AperturaPasesCausiones_729_Alta_ConIdPasesCaucionesExistente(insertAperturaPasesCausiones,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": 5,
                        "codTipoOperacion": "APCC",
                        "idAgente": "22",
                        "codTpDevengamiento": "DE",
                        "monedaConcertacion": "1",
                        "monedaLiquidacion": "2",
                        "monedaGastos": "2",
                        "idEspecie": "AJ12",
                        "idPasesCauciones": "QAAUTOMATION",
                        "boletoContadoFechaConcert": "2020-06-16T17:33:13.041Z",
                        "boletoContadoFechaLiquid": "2020-07-16T17:33:13.041Z",
                        "boletoContadoNumero": "2",
                        "boletoContadoCantidad": 1,
                        "boletoContadoPrecio": 1,
                        "boletoFuturoFechaConcert": "2020-06-16T17:33:13.041Z",
                        "boletoFuturoFechaLiquid": "2020-07-16T17:33:13.041Z",
                        "boletoFuturoNumero": "2",
                        "boletoFuturoCantidad": 1,
                        "boletoFuturoPrecio": 1,
                        "tipoCambioConcertacion":10,
                        "tipoCambioLiquidacion": 2,
                        "tipoCambioGastos": 1,
                        "cantidad": 1,
                        "precio": 1,
                        "arancel": 1,
                        "impuesto": 2,
                        "derechoBolsa": 1,
                        "derechoMercado": 2
                }
        resp = requests.post(insertAperturaPasesCausiones, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code != 200, crearTarjeta(request.node.name, str(payload), resp.text+"\n \n se esperaba un msg de error por idPasesCauciones existente")
