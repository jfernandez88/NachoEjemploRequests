import requests, pytest, json
from pytest_html import extras
from dataEspecies import dataConsultaEspecies
from funciones.sql import sqlQuery
from funciones.trello import crearTarjeta


#401    Alta con todos los campos obligatorios	"ok: Mensaje:Se agregado existosamente el Plazo Fijo Num de operacion"
def test_plazoFijo_401_Alta_TodosCampos(insertPlazoFijo,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": 10,
                        "numOperFinanciera": 123456,
                        "fechaConcertacion": "2020-06-16",
                        "fechaLiquidacion": "2020-06-30",
                        "idBanco": "MARIVA",
                        "codTipoDevengamiento": "LI",
                        "moneda": "32",
                        "Importe": 300,
                        "gastos": 1000,
                        "factorConversion": 1,
                        "codTipoTasaBancaria": "TN",
                        "baseDias": 360,
                        "pfPrecancelable": True,
                        "pfPrecancelableInmediato": False,
                        "pfRenovable": False,
                        "pfTransferible": False,
                        "codTipoOrden": "OC",
                        "devengaConUltimaTasa": False,
                        "idPlazoFijo": "QAAutomation_Test",
                        "idCuentaBancaria": "TEST_AUTO",
                        "codCAFCI": "CAFCI API",
                        "tasas": [
                                        {
                                        "fechaDesde": "2020-06-16",
                                        "fechaHasta": "2020-06-25",
                                        "tasa": 5
                                        },
                                                {
                                        "fechaDesde": "2020-06-26",
                                        "fechaHasta": "2020-06-29",
                                        "tasa": 10
                                        }
                                 ]
                        }
        resp = requests.post(insertPlazoFijo, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code == 200, crearTarjeta(request.node.name, str(payload), resp.text)
        #assert respJson['codigo'] > 0