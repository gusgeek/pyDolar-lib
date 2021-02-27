import requests

def test():
    print('hola')

def bancoGalicia():
    r = requests.get('https://www.bancogalicia.com/cotizacion/cotizar?currencyId=02&quoteType=SU&quoteId=999')
    jsonResponse = r.json()

    for key, value in jsonResponse.items():

        if key == 'error':
            print('Disculpe pero en este momento no es posible conseguir la cotizacion \nIntente nuevamente mas tarde')
        else:
            if key == 'buy':
                print(f'        Dolar Compra es de {value}')

            elif key == 'sell':
                print(f'        Dolar Venta es de {value}')

def DolarSI():
    r = requests.get('https://www.dolarsi.com/api/api.php?type=cotizador')
    jsonResponse = r.json()
    for data in jsonResponse:

        compra = data['casa']['compra']
        venta = data['casa']['venta']
        nombre = data['casa']['nombre']

        print(f"\n *** {nombre} ***")
        print(f" COMPRA {compra} - VENTA {venta}\n")

def AmbitoFinanciero():
    V = requests.get('https://mercados.ambito.com/dolar/oficial/variacion')
    jsonResponse = V.json()

    print(f"\n *** Variacion USD las {jsonResponse['fecha']} ***")
    print(f"         COMPRA {jsonResponse['compra']} - VENTA {jsonResponse['venta']}\n")

    I = requests.get('https://mercados.ambito.com/dolar/informal/variacion')
    jsonResponse = I.json()

    print(f"\n *** USD Informal las {jsonResponse['fecha']} ***")
    print(f"         COMPRA {jsonResponse['compra']} - VENTA {jsonResponse['venta']}\n")

    T = requests.get('https://mercados.ambito.com/dolarturista/variacion')
    jsonResponse = T.json()

    print(f"\n *** USD Turista las {jsonResponse['fecha']} ***")
    print(f"         COMPRA {jsonResponse['compra']} - VENTA {jsonResponse['venta']}\n")
