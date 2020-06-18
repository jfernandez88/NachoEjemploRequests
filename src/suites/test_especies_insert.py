import requests, pytest, json
from pytest_html import extras
from funciones.sql import sqlQuery
from funciones.trello import crearTarjeta



#003 Especies - Alta con todos los datos
def test_Especies_203_AltaConTodosLosDatos(especiesInsert,extra,getApiVersion, request):
    headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
    payload = {
                "abreviaturasInternal": [
                    {
                    "codTipoAbreviatura": "BL",
                    "descripcion": "abrev j3",
                    "esDefault": True,
                    "moneda": "32",
                    "unidadCotizacion": 1,
                    "idMercado": "INTBOLSA"
                    }
                ],
                "codigoEspecie": "Espj1",
                "descripcion": "especie 1",
                "fechaEmision": "2020-05-18",
                "fechaVencimiento": "2020-05-18",
                "moneda": "32",
                "isinCode": "444",
                "idTipoEspecie": "INTPUB",
                "idEmisor": "BGAL",
                "idEspecie": "9988"
                }
    resp = requests.post(especiesInsert, json=payload, headers = headers)
    extra.append(extras.json(payload, name="Request"))
    extra.append(extras.text(resp.text, name = 'Response'))     
    assert resp.status_code == 200, crearTarjeta(request.node.name, str(payload), resp.text+"\n StatusCode "+str(resp.status_code)) 

    
#204  Alta scodigoEspecie  vacio	Al no enviar codEspecie el servicio debe devolver msg acorde solicitando el mismo
def test_Especies_204_AltaSinCodEspecie(especiesInsert,extra,getApiVersion, request):
    headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
    payload = {
                "abreviaturasInternal": [
                    {
                    "codTipoAbreviatura": "BL",
                    "descripcion": "abrev j3",
                    "esDefault": True,
                    "moneda": "32",
                    "unidadCotizacion": 1,
                    "idMercado": "INTBOLSA"
                    }
                ],
                #"codigoEspecie": "Espj1",
                "descripcion": "especie 1",
                "fechaEmision": "2020-05-18",
                "fechaVencimiento": "2020-05-18",
                "moneda": "32",
                "isinCode": "444",
                "idTipoEspecie": "INTPUB",
                "idEmisor": "BGAL",
                "idEspecie": "9988"
                }
    resp = requests.post(especiesInsert, json=payload, headers = headers)
    extra.append(extras.json(payload, name="Request"))
    extra.append(extras.text(resp.text, name = 'Response'))
    respJson = resp.json()
    assert resp.status_code != 200,crearTarjeta(request.node.name, str(payload), resp.text)
    assert "codigoEspecie" in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg similar a 'codigoEspecie requerido'")
     