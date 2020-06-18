import requests

url = "https://api.trello.com/1/cards"
headerTrello = {
        "key": "asasas", 
        "token":"asassaas"
        }
idList = "asasas"
idListEnCorrecion = "asassa"

#Crea una tarjeta siempre y cuando el check devuelva un true
def crearTarjeta(name, request, response):
        if(checkCrearTarjeta(name) and checkCrearTarjetaEnCorreccion(name)):
                print("Creando tarjeta en trello..")
                trelloCard = {
                        "idList": idList,
                        "name": name,
                        "desc":"[Tarjeta creada automaticamente] \n REQUEST: "+request+"\n \n RESPONSE:"+response
                }
                resp = requests.post(url, json=trelloCard, params = headerTrello) 
                print("Se creo tarjeta en la lista Bug de Trello - statusCode "+str(resp.status_code))


#Revisa si existe una tarjeta, de ser asi devuelve false para crearla
def checkCrearTarjeta(name):
    url = "https://api.trello.com/1/lists/"+idList+"/cards"
    resp = requests.get(url, headerTrello)
    respJson = resp.json()
    tarjeta = [aux for aux in respJson if aux['name'] == name ]
    if(len(tarjeta) > 0):
        print("Ya existe una tarjeta en Bug para "+name)
        return False
    return True

def checkCrearTarjetaEnCorreccion(name):
    url = "https://api.trello.com/1/lists/"+idListEnCorrecion+"/cards"
    resp = requests.get(url, headerTrello)
    respJson = resp.json()
    tarjeta = [aux for aux in respJson if aux['name'] == name ]
    if(len(tarjeta) > 0):
        print("Ya existe una tarjeta en Correcion para "+name)
        return False
    return True

