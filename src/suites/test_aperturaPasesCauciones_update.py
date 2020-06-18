import requests, pytest, json
from pytest_html import extras
from dataEspecies import dataConsultaEspecies
from funciones.sql import sqlQuery
from funciones.trello import crearTarjeta


idPasesCauciones = ""
boletoContadoNumero = ""
boletoFuturoFechaLiquid = ""
boletoFuturoNumero = ""

def test_AperPasesCausiones__700_Modificar_PorNumFondo(getAperturaPasesCausiones,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload =  {
                        "numFondo": 5,
                        "numOperFinanciera": 123456,
                        "fechaConcertacion": "2020-06-16",
                        "fechaLiquidacion": "2020-06-30",
                    
                 }
                
        resp = requests.post(getAperturaPasesCausiones, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code == 200