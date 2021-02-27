import requests

def bancoGalicia(typeAc):
    r = requests.get('https://www.bancogalicia.com/cotizacion/cotizar?currencyId=02&quoteType=SU&quoteId=999')
    jsonResponse = r.json()

    if typeAc == 'buy':
        return float(jsonResponse['buy'].replace(',', '.'))
    elif typeAc == 'sell':
        return float(jsonResponse['sell'].replace(',', '.'))
    else:
        return "error"

def DolarSI(typeAc):
    r = requests.get('https://www.dolarsi.com/api/api.php?type=cotizador')
    jsonResponse = r.json()

    for data in jsonResponse:

        compra = data['casa']['compra']
        venta = data['casa']['venta']
        nombre = data['casa']['nombre']

        if nombre == "Dolar":
            if typeAc == 'buy':
                return float(compra.replace(',', '.'))
            elif typeAc == 'sell':
                return float(venta.replace(',', '.'))
        else:
            return "error"

def afOficial(typeAc):
    V = requests.get('https://mercados.ambito.com/dolar/oficial/variacion')
    jsonResponse = V.json()

    if typeAc == 'buy':
        return float(jsonResponse['compra'].replace(',', '.'))
    elif typeAc == 'sell':
        return float(jsonResponse['venta'].replace(',', '.'))

def afInformal(typeAc):
    I = requests.get('https://mercados.ambito.com/dolar/informal/variacion')
    jsonResponse = I.json()

    if typeAc == 'buy':
        return float(jsonResponse['compra'].replace(',', '.'))
    elif typeAc == 'sell':
        return float(jsonResponse['venta'].replace(',', '.'))

def afTurista(typeAc):
    T = requests.get('https://mercados.ambito.com/dolarturista/variacion')
    jsonResponse = T.json()

    if typeAc == 'buy':
        return float(jsonResponse['compra'].replace(',', '.'))
    elif typeAc == 'sell':
        return float(jsonResponse['venta'].replace(',', '.'))
