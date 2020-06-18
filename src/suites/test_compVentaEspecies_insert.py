import requests, pytest, json
from pytest_html import extras
from dataEspecies import dataConsultaEspecies
from funciones.trello import crearTarjeta
from funciones.sql import sqlQuery

 
numFondo = 5
codTipoOperacion = "C"
idAgente = "CITI"
nroBoleto = "1212"
fechaConcertacion = "2020-06-09"
fechaLiquidacion = "2020-06-09"
idEspecie = "AJ12"
monedaConcertacion = "32"
monedaLiquidacion = "32"
monedaGastos = "32"
tipoCambioConcertacion = 1
tipoCambioLiquidacion = 1
tipoCambioGastos = 1
idDepositario = "ROFEX"
idMercadoOperacion = "INTBOLSA"
idCompraVentaEspecie = "QAAutomation_TEST"
cantidad = 10
precio = 10
arancel = 0
impuesto = 0
derechoBolsa = 0
derechoMercado = 0
gastosSEC = 0

#617	Alta	Alta con todos los campos	ok
def test_CompVentaEspecies_617_AltaConTodosLosCampos(insertCompraVentaEspecies,extra,getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo,
                        "codTipoOperacion": codTipoOperacion,
                        "idAgente": idAgente ,
                        "nroBoleto": "1212",
                        "fechaConcertacion":fechaConcertacion,
                        "fechaLiquidacion": fechaLiquidacion,
                        "idEspecie": idEspecie,
                        "monedaConcertacion": monedaConcertacion,
                        "monedaLiquidacion": monedaLiquidacion,
                        "monedaGastos": monedaGastos,
                        "tipoCambioConcertacion": tipoCambioConcertacion,
                        "tipoCambioLiquidacion": tipoCambioLiquidacion,
                        "tipoCambioGastos": tipoCambioGastos,
                        "idDepositario": idDepositario,
                        "idMercadoOperacion": idMercadoOperacion,
                        "idCompraVentaEspecie": idCompraVentaEspecie,
                        "cantidad": cantidad,
                        "precio": precio,
                        "arancel": arancel,
                        "impuesto": impuesto,
                        "derechoBolsa": derechoBolsa,
                        "derechoMercado": derechoMercado,
                        "gastosSEC": gastosSEC
                }
        resp = requests.post(insertCompraVentaEspecies, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        codigo = respJson['codigo']
        sqlQuery("DELETE TITULOS Where CodOperBursatil = "+str(codigo))
        sqlQuery("DELETE OPERBURSATILESIT WHERE CodOperBursatil = "+str(codigo))
        sqlQuery("DELETE  OPERBURSATILES WHERE CodOperBursatil = "+str(codigo))
        assert 'error' not in resp.text, crearTarjeta(request.node.name, str(payload), resp.text) 
        assert respJson['codigo'] != 0,crearTarjeta(request.node.name, str(payload), resp.text+"\n \n El codigo esta vacio") 

#601	Alta	Sin numFondo (numero de Fondo)	Nok: Mensaje: El Fondo no puede quedar vacio
def test_CompVentaEspecies_601_AltaSinNumFondo(insertCompraVentaEspecies,extra,getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        #"numFondo": numFondo,
                        "codTipoOperacion": codTipoOperacion,
                        "idAgente": idAgente ,
                        "nroBoleto": "1212",
                        "fechaConcertacion":fechaConcertacion,
                        "fechaLiquidacion": fechaLiquidacion,
                        "idEspecie": idEspecie,
                        "monedaConcertacion": monedaConcertacion,
                        "monedaLiquidacion": monedaLiquidacion,
                        "monedaGastos": monedaGastos,
                        "tipoCambioConcertacion": tipoCambioConcertacion,
                        "tipoCambioLiquidacion": tipoCambioLiquidacion,
                        "tipoCambioGastos": tipoCambioGastos,
                        "idDepositario": idDepositario,
                        "idMercadoOperacion": idMercadoOperacion,
                        "idCompraVentaEspecie": idCompraVentaEspecie,
                        "cantidad": cantidad,
                        "precio": precio,
                        "arancel": arancel,
                        "impuesto": impuesto,
                        "derechoBolsa": derechoBolsa,
                        "derechoMercado": derechoMercado,
                        "gastosSEC": gastosSEC
                }

        resp = requests.post(insertCompraVentaEspecies, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert 'Fondo' in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se esperaba un msj similar a numFondo es requerido")

#602	Alta	Sin codTipoOperacion (Tipo de operacion)	Nok: Mensaje: El tipo de operacion ingresada es invalida
def test_CompVentaEspecies_602_AltaSinCodTipoOperacion(insertCompraVentaEspecies,extra,getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo,
                        #"codTipoOperacion": codTipoOperacion,
                        "idAgente": idAgente ,
                        "nroBoleto": "1212",
                        "fechaConcertacion":fechaConcertacion,
                        "fechaLiquidacion": fechaLiquidacion,
                        "idEspecie": idEspecie,
                        "monedaConcertacion": monedaConcertacion,
                        "monedaLiquidacion": monedaLiquidacion,
                        "monedaGastos": monedaGastos,
                        "tipoCambioConcertacion": tipoCambioConcertacion,
                        "tipoCambioLiquidacion": tipoCambioLiquidacion,
                        "tipoCambioGastos": tipoCambioGastos,
                        "idDepositario": idDepositario,
                        "idMercadoOperacion": idMercadoOperacion,
                        "idCompraVentaEspecie": idCompraVentaEspecie,
                        "cantidad": cantidad,
                        "precio": precio,
                        "arancel": arancel,
                        "impuesto": impuesto,
                        "derechoBolsa": derechoBolsa,
                        "derechoMercado": derechoMercado,
                        "gastosSEC": gastosSEC
                }

        resp = requests.post(insertCompraVentaEspecies, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert 'Operacion' in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se esperaba un msj similar a codTipoOperacion es requerido")


#603 Alta Sin nroBoleto	Nok: Mensaje: El N° de boleto ingresado es invalido
def test_CompVentaEspecies_603_AltaSinNroBoleto(insertCompraVentaEspecies,extra,getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo,
                        "codTipoOperacion": codTipoOperacion,
                        "idAgente": idAgente ,
                        #"nroBoleto": "1212",
                        "fechaConcertacion":fechaConcertacion,
                        "fechaLiquidacion": fechaLiquidacion,
                        "idEspecie": idEspecie,
                        "monedaConcertacion": monedaConcertacion,
                        "monedaLiquidacion": monedaLiquidacion,
                        "monedaGastos": monedaGastos,
                        "tipoCambioConcertacion": tipoCambioConcertacion,
                        "tipoCambioLiquidacion": tipoCambioLiquidacion,
                        "tipoCambioGastos": tipoCambioGastos,
                        "idDepositario": idDepositario,
                        "idMercadoOperacion": idMercadoOperacion,
                        "idCompraVentaEspecie": idCompraVentaEspecie,
                        "cantidad": cantidad,
                        "precio": precio,
                        "arancel": arancel,
                        "impuesto": impuesto,
                        "derechoBolsa": derechoBolsa,
                        "derechoMercado": derechoMercado,
                        "gastosSEC": gastosSEC
                }

        resp = requests.post(insertCompraVentaEspecies, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert 'nroBoleto' in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se esperaba un msj similar a nroBoleto es requerido")

#604	Alta	Sin idAgente (Cod interfaz de agente)	Nok: Mensaje: El Agente no puede quedar vacio
def test_CompVentaEspecies_604_AltaSinIdAgente(insertCompraVentaEspecies,extra,getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo,
                        "codTipoOperacion": codTipoOperacion,
                        #"idAgente": idAgente ,
                        "nroBoleto": "1212",
                        "fechaConcertacion":fechaConcertacion,
                        "fechaLiquidacion": fechaLiquidacion,
                        "idEspecie": idEspecie,
                        "monedaConcertacion": monedaConcertacion,
                        "monedaLiquidacion": monedaLiquidacion,
                        "monedaGastos": monedaGastos,
                        "tipoCambioConcertacion": tipoCambioConcertacion,
                        "tipoCambioLiquidacion": tipoCambioLiquidacion,
                        "tipoCambioGastos": tipoCambioGastos,
                        "idDepositario": idDepositario,
                        "idMercadoOperacion": idMercadoOperacion,
                        "idCompraVentaEspecie": idCompraVentaEspecie,
                        "cantidad": cantidad,
                        "precio": precio,
                        "arancel": arancel,
                        "impuesto": impuesto,
                        "derechoBolsa": derechoBolsa,
                        "derechoMercado": derechoMercado,
                        "gastosSEC": gastosSEC
                }

        resp = requests.post(insertCompraVentaEspecies, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert 'Agente' in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg similar a 'El campo idAgente es requerido")



#605	Alta	Sin fechaConcertacion (Fecha de concertacion)  +Logica dia no habil	Nok: Mensaje: La fecha de concertacion es invalida
def test_CompVentaEspecies_605_AltaSinFechaConcertacion(insertCompraVentaEspecies,extra,getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo,
                        "codTipoOperacion": codTipoOperacion,
                        "idAgente": idAgente ,
                        "nroBoleto": "1212",
                        #"fechaConcertacion":fechaConcertacion,
                        "fechaLiquidacion": fechaLiquidacion,
                        "idEspecie": idEspecie,
                        "monedaConcertacion": monedaConcertacion,
                        "monedaLiquidacion": monedaLiquidacion,
                        "monedaGastos": monedaGastos,
                        "tipoCambioConcertacion": tipoCambioConcertacion,
                        "tipoCambioLiquidacion": tipoCambioLiquidacion,
                        "tipoCambioGastos": tipoCambioGastos,
                        "idDepositario": idDepositario,
                        "idMercadoOperacion": idMercadoOperacion,
                        "idCompraVentaEspecie": idCompraVentaEspecie,
                        "cantidad": cantidad,
                        "precio": precio,
                        "arancel": arancel,
                        "impuesto": impuesto,
                        "derechoBolsa": derechoBolsa,
                        "derechoMercado": derechoMercado,
                        "gastosSEC": gastosSEC
                }

        resp = requests.post(insertCompraVentaEspecies, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert 'fechaConcertacion' in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg similar a fechaConcertacion es requerida")

#606	Alta	Sin fechaLiquidacion ( Fecha de liquidacion)  +Logica dia no habil	Nok: Mensaje: La fecha de liquidacion es invalida
def test_CompVentaEspecies_606_AltaSinFechaLiquidacion(insertCompraVentaEspecies,extra,getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo,
                        "codTipoOperacion": codTipoOperacion,
                        "idAgente": idAgente ,
                        "nroBoleto": "1212",
                        "fechaConcertacion":fechaConcertacion,
                        #"fechaLiquidacion": fechaLiquidacion,
                        "idEspecie": idEspecie,
                        "monedaConcertacion": monedaConcertacion,
                        "monedaLiquidacion": monedaLiquidacion,
                        "monedaGastos": monedaGastos,
                        "tipoCambioConcertacion": tipoCambioConcertacion,
                        "tipoCambioLiquidacion": tipoCambioLiquidacion,
                        "tipoCambioGastos": tipoCambioGastos,
                        "idDepositario": idDepositario,
                        "idMercadoOperacion": idMercadoOperacion,
                        "idCompraVentaEspecie": idCompraVentaEspecie,
                        "cantidad": cantidad,
                        "precio": precio,
                        "arancel": arancel,
                        "impuesto": impuesto,
                        "derechoBolsa": derechoBolsa,
                        "derechoMercado": derechoMercado,
                        "gastosSEC": gastosSEC
                }

        resp = requests.post(insertCompraVentaEspecies, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert 'fechaLiquidacion' in respJson['error']['Msj'] ,crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera el msg similar a fechaLiquidacion es requerida")


#607	Alta	Sin idEspecie (Cod inf especie) +Contabilidad	Nok: Mensaje: La especie no puede quedar vacia
def test_CompVentaEspecies_607_AltaSinIdEspecie(insertCompraVentaEspecies,extra,getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo,
                        "codTipoOperacion": codTipoOperacion,
                        "idAgente": idAgente ,
                        "nroBoleto": "1212",
                        "fechaConcertacion":fechaConcertacion,
                        "fechaLiquidacion": fechaLiquidacion,
                        #"idEspecie": idEspecie,
                        "monedaConcertacion": monedaConcertacion,
                        "monedaLiquidacion": monedaLiquidacion,
                        "monedaGastos": monedaGastos,
                        "tipoCambioConcertacion": tipoCambioConcertacion,
                        "tipoCambioLiquidacion": tipoCambioLiquidacion,
                        "tipoCambioGastos": tipoCambioGastos,
                        "idDepositario": idDepositario,
                        "idMercadoOperacion": idMercadoOperacion,
                        "idCompraVentaEspecie": idCompraVentaEspecie,
                        "cantidad": cantidad,
                        "precio": precio,
                        "arancel": arancel,
                        "impuesto": impuesto,
                        "derechoBolsa": derechoBolsa,
                        "derechoMercado": derechoMercado,
                        "gastosSEC": gastosSEC
                }

        resp = requests.post(insertCompraVentaEspecies, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert 'idEspecie' in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera un Msj similar a 'idEspecie' es requerido")


#608	Alta	Sin monedaLiquidacion (Moneda de liquidacion)	Nok: Mensaje: La moneda de liquidacion ingresada es invalida
def test_CompVentaEspecies_608_AltaSinMonedaLiquidacion(insertCompraVentaEspecies,extra,getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo,
                        "codTipoOperacion": codTipoOperacion,
                        "idAgente": idAgente ,
                        "nroBoleto": "1212",
                        "fechaConcertacion":fechaConcertacion,
                        "fechaLiquidacion": fechaLiquidacion,
                        "idEspecie": idEspecie,
                        "monedaConcertacion": monedaConcertacion,
                        #"monedaLiquidacion": monedaLiquidacion,
                        "monedaGastos": monedaGastos,
                        "tipoCambioConcertacion": tipoCambioConcertacion,
                        "tipoCambioLiquidacion": tipoCambioLiquidacion,
                        "tipoCambioGastos": tipoCambioGastos,
                        "idDepositario": idDepositario,
                        "idMercadoOperacion": idMercadoOperacion,
                        "idCompraVentaEspecie": idCompraVentaEspecie,
                        "cantidad": cantidad,
                        "precio": precio,
                        "arancel": arancel,
                        "impuesto": impuesto,
                        "derechoBolsa": derechoBolsa,
                        "derechoMercado": derechoMercado,
                        "gastosSEC": gastosSEC
                }

        resp = requests.post(insertCompraVentaEspecies, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert 'Moneda' in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera un Msj similar a 'monedaLiquidacion' es requerido")


#609	Alta	Sin monedaConcertacion 	Nok: Mensaje: La moneda de concertacion ingresada es invalida
def test_CompVentaEspecies_609_AltaSinMonedaConcertacion(insertCompraVentaEspecies,extra,getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo,
                        "codTipoOperacion": codTipoOperacion,
                        "idAgente": idAgente ,
                        "nroBoleto": "1212",
                        "fechaConcertacion":fechaConcertacion,
                        "fechaLiquidacion": fechaLiquidacion,
                        "idEspecie": idEspecie,
                        #"monedaConcertacion": monedaConcertacion,
                        "monedaLiquidacion": monedaLiquidacion,
                        "monedaGastos": monedaGastos,
                        "tipoCambioConcertacion": tipoCambioConcertacion,
                        "tipoCambioLiquidacion": tipoCambioLiquidacion,
                        "tipoCambioGastos": tipoCambioGastos,
                        "idDepositario": idDepositario,
                        "idMercadoOperacion": idMercadoOperacion,
                        "idCompraVentaEspecie": idCompraVentaEspecie,
                        "cantidad": cantidad,
                        "precio": precio,
                        "arancel": arancel,
                        "impuesto": impuesto,
                        "derechoBolsa": derechoBolsa,
                        "derechoMercado": derechoMercado,
                        "gastosSEC": gastosSEC
                }

        resp = requests.post(insertCompraVentaEspecies, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert 'concertacion' in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera un Msj similar a 'monedaConcertacion' es requerido")

#610	Alta	Sin monedaGastos (Moneda de Gasto)
def test_CompVentaEspecies_610_AltaSinMonedaGastos(insertCompraVentaEspecies,extra,getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo,
                        "codTipoOperacion": codTipoOperacion,
                        "idAgente": idAgente ,
                        "nroBoleto": "1212",
                        "fechaConcertacion":fechaConcertacion,
                        "fechaLiquidacion": fechaLiquidacion,
                        "idEspecie": idEspecie,
                        "monedaConcertacion": monedaConcertacion,
                        "monedaLiquidacion": monedaLiquidacion,
                        #"monedaGastos": monedaGastos,
                        "tipoCambioConcertacion": tipoCambioConcertacion,
                        "tipoCambioLiquidacion": tipoCambioLiquidacion,
                        "tipoCambioGastos": tipoCambioGastos,
                        "idDepositario": idDepositario,
                        "idMercadoOperacion": idMercadoOperacion,
                        "idCompraVentaEspecie": idCompraVentaEspecie,
                        "cantidad": cantidad,
                        "precio": precio,
                        "arancel": arancel,
                        "impuesto": impuesto,
                        "derechoBolsa": derechoBolsa,
                        "derechoMercado": derechoMercado,
                        "gastosSEC": gastosSEC
                }

        resp = requests.post(insertCompraVentaEspecies, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert 'Moneda' in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera un Msj similar a 'monedaGastos' es requerido")


#613	Alta	Sin idDepositario (Codigo de interfaz de depositaria)	Nok: Mensaje: El depositario no puede quedar vacio
def test_CompVentaEspecies_613_AltaSinIdDepositario(insertCompraVentaEspecies,extra,getApiVersion, request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo,
                        "codTipoOperacion": codTipoOperacion,
                        "idAgente": idAgente ,
                        "nroBoleto": "1212",
                        "fechaConcertacion":fechaConcertacion,
                        "fechaLiquidacion": fechaLiquidacion,
                        "idEspecie": idEspecie,
                        "monedaConcertacion": monedaConcertacion,
                        "monedaLiquidacion": monedaLiquidacion,
                        "monedaGastos": monedaGastos,
                        "tipoCambioConcertacion": tipoCambioConcertacion,
                        "tipoCambioLiquidacion": tipoCambioLiquidacion,
                        "tipoCambioGastos": tipoCambioGastos,
                        #"idDepositario": idDepositario,
                        "idMercadoOperacion": idMercadoOperacion,
                        "idCompraVentaEspecie": idCompraVentaEspecie,
                        "cantidad": cantidad,
                        "precio": precio,
                        "arancel": arancel,
                        "impuesto": impuesto,
                        "derechoBolsa": derechoBolsa,
                        "derechoMercado": derechoMercado,
                        "gastosSEC": gastosSEC
                }

        resp = requests.post(insertCompraVentaEspecies, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response'))  
        assert 'Depositario' in respJson['error']['Msj'],crearTarjeta(request.node.name, str(payload), resp.text+"\n \n Se espera un Msj similar a 'idDepositario' es requerido")
