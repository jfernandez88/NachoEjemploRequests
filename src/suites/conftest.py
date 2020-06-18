import pytest, pyodbc

Ambiente = "192.168.22.14:6003"
BaseDeDatos = "v21server21 vfAlfa_Nueva"
apiVersion = "1"

#API VERSION
@pytest.fixture
def getApiVersion():
	return "1"

@pytest.fixture
def getHeaderApiFondos():
    header = {"api-version": apiVersion, "Content-Type":"application/json"}
    return   header  

#URL EMISORES
@pytest.fixture
def emisoresInsert():
	return "http://"+Ambiente+"/api/fondos/v1/insert-emisor"

@pytest.fixture
def emisoresGet():
	return "http://"+Ambiente+"/api/fondos/v1/get-Emisor"

@pytest.fixture
def emisoresUpdate():
	return "http://"+Ambiente+"/api/fondos/v1/update-emisor"

@pytest.fixture
def emisoresDelete():
	return "http://"+Ambiente+"/api/fondos/v1/delete-emisor"
    
#URL ESPECIES
@pytest.fixture
def especiesInsert():
	return "http://"+Ambiente+"/api/fondos/v1/insert-especie"

@pytest.fixture
def especiesGet():
	return "http://"+Ambiente+"/api/fondos/v1/get-especies"

@pytest.fixture
def especiesUpdate():
	return "http://"+Ambiente+"/api/fondos/v1/update-especie"

@pytest.fixture
def especiesDelete():
	return "http://"+Ambiente+"/api/fondos/v1/delete-Especie"


#URL CUENTAS BANCARIAS
@pytest.fixture
def getCuentasBancarias():
    return "http://"+Ambiente+"/api/fondos/v1/get-cuentas-bancarias"

@pytest.fixture
def deleteCuentasBancarias():
    return "http://"+Ambiente+"/api/fondos/v1/delete-cuenta-bancaria"

@pytest.fixture
def updateCuentasBancarias():
    return "http://"+Ambiente+"/api/fondos/v1/update-cuenta-bancaria"

@pytest.fixture
def insertCuentasBancarias():
    return "http://"+Ambiente+"/api/fondos/v1/insert-cuenta-bancaria"

# URL COMPRA Y VENTA DE ESPECIES
@pytest.fixture
def getCompraVentaEspecies():
    return "http://"+Ambiente+"/api/fondos/v1/getCompraVentaEspecie"

@pytest.fixture
def insertCompraVentaEspecies():
    return "http://"+Ambiente+"/api/fondos/v1/insert-compra-venta-especie"



#URL Tablas del sistema
@pytest.fixture
def getAgentes():
    return "http://"+Ambiente+"/api/fondos/v1/get-agentes"
@pytest.fixture
def getBancos():
    return "http://"+Ambiente+"/api/fondos/v1/get-bancos"
@pytest.fixture
def getDepositarios():
    return "http://"+Ambiente+"/api/fondos/v1/get-depositarios"
@pytest.fixture
def getMercados():
    return "http://"+Ambiente+"/api/fondos/v1/get-mercados"
@pytest.fixture
def getMonedas():
    return "http://"+Ambiente+"/api/fondos/v1/get-monedas"
@pytest.fixture
def getPaises():
    return "http://"+Ambiente+"/api/fondos/v1/get-paises"
@pytest.fixture
def getTiposAbreviaturas():
    return "http://"+Ambiente+"/api/fondos/v1/get-tipos-abreviatura"
@pytest.fixture
def getTiposCuentasBancarias():
    return "http://"+Ambiente+"/api/fondos/v1/get-tipos-cuentas-bancarias"

@pytest.fixture
def getTiposDevengamientoCuentasBancarias():
    return "http://"+Ambiente+"/api/fondos/v1/get-tipos-devengamiento-cuentas-bancarias"

@pytest.fixture
def getTiposEspecie():
    return "http://"+Ambiente+"/api/fondos/v1/get-tipos-especie"

@pytest.fixture
def getTiposOperaciones():
    return "http://"+Ambiente+"/api/fondos/v1/get-tipos-operaciones"

@pytest.fixture
def getTiposValuacion():
    return "http://"+Ambiente+"/api/fondos/v1/get-tipos-valuacion"



#URL DE CAUCIONES
@pytest.fixture
def getAperturaPasesCausiones():
    return "http://"+Ambiente+"/api/fondos/v1/get-apertura-pase-cauciones"

@pytest.fixture
def insertAperturaPasesCausiones():
    return "http://"+Ambiente+"/api/fondos/v1/insert-aperPaseCaucion"

#URL Plazo Fijo
@pytest.fixture
def insertPlazoFijo():
    return "http://"+Ambiente+"/api/fondos/v1/insert-plazo-fijo"
@pytest.fixture
def getPlazoFijo():
    return "http://"+Ambiente+"/api/fondos/v1/get-plazo-fijos"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        #extra.append(pytest_html.extras.url('http://www.example.com/'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Detalle del fallo:</div>'))
        report.extra = extra


def pytest_html_report_title(report):
   report.title = "REPORTE: QA AUTOMATION - ApiFondos"


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend("Ambiente: http://"+Ambiente+"/swagger/index.html?urls.primaryName=VisualFondos%20v%201 \n BaseDeDatos: "+BaseDeDatos)


