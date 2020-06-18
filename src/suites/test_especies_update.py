import requests, pytest, json
from pytest_html import extras
from funciones.trello import crearTarjeta

codigoEspecie = "PR12"
descripcion = "Test"
fechaEmision = "2020-05-28"
fechaVencimiento = "2020-05-28"
moneda = "32"
isinCode = "ARARGE035162"
idTipoEspecie ="INTPUB"
idEmisor = "3"
idEspecie = "PR12"



#206 - Especies - Update -Modificar la descripcion
def test_Especies_206_Modificacion_Descripcion(especiesUpdate,extra,getHeaderApiFondos, request):     
        payload = {
                        "codigoEspecie": codigoEspecie,
                        "idEspecie" : idEspecie,
                        "isinCode" : isinCode,
                        "fechaEmision" : fechaEmision,
                        "fechaVencimiento" : fechaVencimiento, 
                        "moneda" : moneda ,
                        "idTipoEspecie" : idTipoEspecie,
                        "descripcion" : descripcion,
                        "idEmisor" : idEmisor           
                    }
        resp = requests.post(especiesUpdate, json=payload, headers = getHeaderApiFondos) 
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))            
        assert resp.status_code == 200,crearTarjeta(request.node.name, str(payload), resp.text+"\n StatusCode "+str(resp.status_code)+"\n No se realiza la modificacion y el idEspecie existe")

#207	Modificar la descripcion sin campo obligatorio
def test_Especies_207_Modificacion_Descripcion_SinIdEspecie(especiesUpdate,extra,getHeaderApiFondos, request):     
        payload = {
                        "codigoEspecie": codigoEspecie,
                        #"idEspecie" : idEspecie,
                        "isinCode" : isinCode,
                        "fechaEmision" : fechaEmision,
                        "fechaVencimiento" : fechaVencimiento, 
                        "moneda" : moneda ,
                        "idTipoEspecie" : idTipoEspecie,
                        "descripcion" : descripcion,
                        "idEmisor" : idEmisor           
                    }
        resp = requests.post(especiesUpdate, json=payload, headers = getHeaderApiFondos) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code != 200,crearTarjeta(request.node.name, str(payload), resp.text)
        assert "idEspecie" in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg similar a 'idEspecie requerido'")
