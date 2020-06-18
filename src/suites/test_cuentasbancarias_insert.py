import requests, pytest, json
from pytest_html import extras
from dataEspecies import dataConsultaEspecies
from funciones.sql import sqlQuery
from funciones.trello import crearTarjeta


numFondo = 5
nroCuenta = "2"
idBanco = "MARIVA"
moneda = "32"
esCtaDepositaria = False
idTpCuentaBancaria = "CA"
codTpDevCtaBancaria = "LD"
baseDias =  365
idCuentaBancaria = "TEST_AUTO"

def setup_module():
      sqlQuery("DELETE CTASBANCARIAS WHERE CodInterfaz = '"+idCuentaBancaria+"'")  
      sqlQuery("DELETE CTASBANCARIAS WHERE CodInterfaz = 'TEST_530'")


#501 CuentaBancaria - Insert - Alta con todos los campos
def test_CuentasBancarias_501_AltaConTodosLosCampos(insertCuentasBancarias,extra,getApiVersion,request):
                headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
                payload = {
                                "numFondo": numFondo,
                                "nroCuenta": nroCuenta,
                                "idBanco": idBanco,
                                "moneda": moneda,
                                "esCtaDepositaria": esCtaDepositaria,
                                "idTpCuentaBancaria": idTpCuentaBancaria,
                                "codTpDevCtaBancaria": codTpDevCtaBancaria,
                                "baseDias": baseDias,
                                "idCuentaBancaria": idCuentaBancaria
                                }
                resp = requests.post(insertCuentasBancarias, json=payload, headers = headers) 
                respJson = resp.json()
                extra.append(extras.json(payload, name="Request"))
                extra.append(extras.text(resp.text, name = 'Response'))               
                assert respJson['descripcion'] is not None,crearTarjeta(request.node.name, str(payload), resp.text)

#502 Alta sin numFondo (Fondo)	Nok: Mensaje: El Fondo no puede quedar vacio
def test_CuentasBancarias_502_AltaSinNumFondo(insertCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        #"numFondo": numFondo,
                        "nroCuenta": nroCuenta,
                        "idBanco": idBanco,
                        "moneda": moneda,
                        "esCtaDepositaria": esCtaDepositaria,
                        "idTpCuentaBancaria": idTpCuentaBancaria,
                        "codTpDevCtaBancaria": codTpDevCtaBancaria,
                        "baseDias": baseDias,
                        "idCuentaBancaria": idCuentaBancaria
                        }
        resp = requests.post(insertCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code != 200,crearTarjeta(request.node.name, str(payload), resp.text)
        assert "numFondo" in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg similar a 'numFondo requerido'")



#503  Alta sin nroCuenta(Numero de cuenta bancaria) Nok: Mensaje: El numero decuenta bancaria no puede quedar vacio
def test_CuentasBancarias_503_AltaSinNroCuenta(insertCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo,
                        #"nroCuenta": nroCuenta,
                        "idBanco": idBanco,
                        "moneda": moneda,
                        "esCtaDepositaria": esCtaDepositaria,
                        "idTpCuentaBancaria": idTpCuentaBancaria,
                        "codTpDevCtaBancaria": codTpDevCtaBancaria,
                        "baseDias": baseDias,
                        "idCuentaBancaria": idCuentaBancaria
                        }
        resp = requests.post(insertCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code != 200,crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg 'nroCuenta es requerido")
        assert "nroCuenta" in respJson['error']['Msj'] ,crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg 'nroCuenta es requerido")


#504  Alta sin idBanco ( Cod interfaz del banco) Nok: Mensaje: El idBanco no puede quedar vacio
def test_CuentasBancarias_504_AltaSinIdBanco(insertCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo,
                        "nroCuenta": nroCuenta,
                        #"idBanco": idBanco,
                        "moneda": moneda,
                        "esCtaDepositaria": esCtaDepositaria,
                        "idTpCuentaBancaria": idTpCuentaBancaria,
                        "codTpDevCtaBancaria": codTpDevCtaBancaria,
                        "baseDias": baseDias,
                        "idCuentaBancaria": idCuentaBancaria
                        }
        resp = requests.post(insertCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code != 200,crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg similar a 'idBanco requerido'")
        assert "idBanco" in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg similar a 'idBanco requerido'")

#505	Alta sin idTpCuentaBancaria(Tipo de cuenta bancaria)	Nok: Mensaje: El tipo de cuenta bancaria no puede quedar vacio
def test_CuentasBancarias_505_AltaSinIdTpCuentaBancaria(insertCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo,
                        "nroCuenta": nroCuenta,
                        "idBanco": idBanco,
                        "moneda": moneda,
                        "esCtaDepositaria": esCtaDepositaria,
                        #"idTpCuentaBancaria": idTpCuentaBancaria,
                        "codTpDevCtaBancaria": codTpDevCtaBancaria,
                        "baseDias": baseDias,
                        "idCuentaBancaria": idCuentaBancaria
                        }
        resp = requests.post(insertCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code != 200,crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg similar a 'idTpCuentaBancaria requerido'")
        assert "idTpCuentaBancaria" in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg similar a 'idTpCuentaBancaria requerido'")

#506  Alta sin idMoneda ( Moneda)  Nok: Mensaje: La moneda no puede estar vacia
def test_CuentasBancarias_506_AltaSinIdMoneda(insertCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo,
                        "nroCuenta": nroCuenta,
                        "idBanco": idBanco,
                        #"moneda": moneda,
                        "esCtaDepositaria": esCtaDepositaria,
                        "idTpCuentaBancaria": idTpCuentaBancaria,
                        "codTpDevCtaBancaria": codTpDevCtaBancaria,
                        "baseDias": baseDias,
                        "idCuentaBancaria": idCuentaBancaria
                        }
        resp = requests.post(insertCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code != 200,crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg similar a 'moneda requerido'")
        assert "moneda" in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg similar a 'moneda requerido'")

#507 Alta sin tipo de codTpDevCtaBancaria (Devengamiento -> tipo)	Nok: Mensaje: el tipo de devengamiento no puede estar vacio
def test_CuentasBancarias_507_AltaSinCodTpDevCtaBancaria(insertCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo,
                        "nroCuenta": nroCuenta,
                        "idBanco": idBanco,
                        "moneda": moneda,
                        "esCtaDepositaria": esCtaDepositaria,
                        "idTpCuentaBancaria": idTpCuentaBancaria,
                        #"codTpDevCtaBancaria": codTpDevCtaBancaria,
                        "baseDias": baseDias,
                        "idCuentaBancaria": idCuentaBancaria
                        }
        resp = requests.post(insertCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code != 200,crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg similar a 'codTpDevCtaBancaria requerido'")
        assert "codTpDevCtaBancaria" in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg similar a 'codTpDevCtaBancaria requerido'")

#508	Alta sin campo baseDias (Base Dias)	Nok: Mensaje: La base del dia no puede quedar vacia
def test_CuentasBancarias_508_AltaSinBaseDias(insertCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo,
                        "nroCuenta": nroCuenta,
                        "idBanco": idBanco,
                        "moneda": moneda,
                        "esCtaDepositaria": esCtaDepositaria,
                        "idTpCuentaBancaria": idTpCuentaBancaria,
                        "codTpDevCtaBancaria": codTpDevCtaBancaria,
                        #"baseDias": baseDias,
                        "idCuentaBancaria": idCuentaBancaria
                        }
        resp = requests.post(insertCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code != 200,crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg similar a 'baseDias requerido'")
        assert "baseDias" in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg similar a 'baseDias requerido'")

#509	Alta sin idCuentaBancaria (Codigo de interfaz)	Nok: Mensaje: El codigo de interfaz es obligatorio
def test_CuentasBancarias_509_AltaSinIdCuentaBancaria(insertCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo,
                        "nroCuenta": nroCuenta,
                        "idBanco": idBanco,
                        "moneda": moneda,
                        "esCtaDepositaria": esCtaDepositaria,
                        "idTpCuentaBancaria": idTpCuentaBancaria,
                        "codTpDevCtaBancaria": codTpDevCtaBancaria,
                        "baseDias": baseDias
                        #"idCuentaBancaria": idCuentaBancaria
                        }
        resp = requests.post(insertCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code != 200,crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg similar a 'idCuentaBancaria requerido'")
        assert "idCuentaBancaria" in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg similar a 'idCuentaBancaria requerido'")


#530 Alta codTpDevCtaBancaria  inexistente
def test_CuentasBancarias_530_AltaCodTpDevCtaBancaria(insertCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo,
                        "nroCuenta": nroCuenta,
                        "idBanco": idBanco,
                        "moneda": moneda,
                        "esCtaDepositaria": esCtaDepositaria,
                        "idTpCuentaBancaria": idTpCuentaBancaria,
                        "codTpDevCtaBancaria": "00",
                        "baseDias": baseDias,
                        "idCuentaBancaria": "TEST_530"
                        }
        resp = requests.post(insertCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))   
        assert 'The INSERT' not in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text)
        assert resp.status_code != 200,crearTarjeta(request.node.name, str(payload), resp.text)




#523 Alta con todos los campos (fondo, numero cuenta y banco existente)
def test_CuentasBancarias_523_AltaFondoCuentaBancoExistente(insertCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": 10,
                        "nroCuenta": "7",
                        "idBanco": "MARIVA",
                        "moneda": "32",
                        "esCtaDepositaria": False,
                        "idTpCuentaBancaria": "CA",
                        "codTpDevCtaBancaria": "LD",
                        "baseDias": 365,
                        "idCuentaBancaria": "777",
                        "codMoneda": 0,
                        "codBanco": 0,
                        "codTpCuentaBancaria": 0,
                        "codFondo": 0
                        }
        resp = requests.post(insertCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code != 200
        assert "ya existe" in  respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg 'Ya existe un elemento con el Nro de cuenta, Fondo y Banco")

#524	Alta con codigo de interfaz repetido
def test_CuentasBancarias_524_AltaCodInterfazRepetido(insertCuentasBancarias,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo,
                        "nroCuenta": nroCuenta,
                        "idBanco": idBanco,
                        "moneda": moneda,
                        "esCtaDepositaria": esCtaDepositaria,
                        "idTpCuentaBancaria": idTpCuentaBancaria,
                        "codTpDevCtaBancaria": codTpDevCtaBancaria,
                        "baseDias": baseDias,
                        "idCuentaBancaria": "666"
                        }
        resp = requests.post(insertCuentasBancarias, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code != 200
        assert 'Violation of Unique Key' not in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text)