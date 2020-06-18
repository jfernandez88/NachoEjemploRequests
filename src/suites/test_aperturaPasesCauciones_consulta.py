import requests, pytest, json
from pytest_html import extras
from dataEspecies import dataConsultaEspecies
from funciones.sql import sqlQuery
from funciones.trello import crearTarjeta

numFondo = 3
idPasesCauciones = "QAAUTOMATION"
idAgente = "22"
idEspecie = "AJ12"


#724	Consulta	Consulta exitosa por numFondo	Se devuelven datos unicamente del numFondo enviado
def test_AperPasesCausiones_724_Consulta_PorNumFondo(getAperturaPasesCausiones,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "numFondo": numFondo
                }
        resp = requests.post(getAperturaPasesCausiones, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code == 200
        assert len(respJson) > 0
        for row in respJson:
                assert row['fondo']['numFondo'] == numFondo,crearTarjeta(request.node.name, str(payload), resp.text)

#725	Consulta	Consulta exitosa por idAgente	Se devuelven datos unicamente del idAgente enviado
def test_AperPasesCausiones_725_Consulta_PorIdAgente(getAperturaPasesCausiones,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "idAgente": idAgente
                }
        resp = requests.post(getAperturaPasesCausiones, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code == 200
        assert len(respJson) > 0
        for row in respJson:
                assert row['fondo']['numFondo']  != 0,crearTarjeta(request.node.name, str(payload), resp.text)

#726	Consulta por idEspecie	Se devuelven datos unicamente del idEspecie enviado
def test_AperPasesCausiones_726_Consulta_PoridEspecie(getAperturaPasesCausiones,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "idEspecie": idEspecie
                }
        resp = requests.post(getAperturaPasesCausiones, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert resp.status_code == 200
        assert len(respJson) > 0,crearTarjeta(request.node.name, str(payload), resp.text)


#727	Consulta	Consulta por idPasesCauciones	Se devuelven datos unicamente del idPasesCauciones enviado
def test_AperPasesCausiones_727_Consulta_PoridPasesCauciones(getAperturaPasesCausiones,extra,getApiVersion,request):
        headers = {"api-version": getApiVersion, "Content-Type":"application/json"}
        payload = {
                        "idPasesCauciones": idPasesCauciones
                }
        resp = requests.post(getAperturaPasesCausiones, json=payload, headers = headers) 
        respJson = resp.json()
        extra.append(extras.json(payload, name="Request"))
        extra.append(extras.text(resp.text, name = 'Response')) 
        assert len(respJson) > 0,crearTarjeta(request.node.name, str(payload), resp.text)


        '''
        for row in respJson:
                assert row['fondo']['numFondo'] == numFondo,crearTarjeta(request.node.name, str(payload), resp.text)
        '''

#728	Consulta	Consulta completa por numFondo,idAgente, idEspecie, idPasesCausiones	Se devuelven datos unicamente del numFondo,idAgente, idEspecie, idPasesCausiones enviado


