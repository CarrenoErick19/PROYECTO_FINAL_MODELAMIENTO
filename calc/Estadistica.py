import matplotlib.pyplot as plt
import pandas as pd
import io
import base64

class Estadistica:

    def __init__(self):
        self.df = pd.read_excel('info/datos.xlsx')
    
    def datosExcel(self):

        return self.df

    def graficoTotalFacturadodecompraventa(self):
        img = io.BytesIO()

        metodo = self.df['Sube/Baja'].unique()
        totalf = []
        for i in metodo:
            suma = self.df.loc[self.df['Sube/Baja'] == i, ['%var']].sum()[0]
            totalf.append(suma)

        plt.figure(figsize=(10,5))
        plt.bar(metodo, totalf, color='teal')
        plt.title('Totales de acuerdo a subidas y bajadas')
        plt.xticks(rotation=10)
        plt.ylabel('Subidas y Bajadas de valor')
        plt.xlabel('Sube o Baja')
        plt.savefig(img, format='png')
        img.seek(0)

        img_url = base64.b64encode(img.getvalue()).decode()
        return img_url

    def graficoFrecuenciadelCliente(self):

        img = io.BytesIO()

        cliente = self.df['Frecuente']
        plt.figure(figsize=(10,5))
        plt.hist(cliente, bins=None, color='gray')
        plt.title('Inversores frecuentes')
        plt.xticks(rotation=10)
        plt.ylabel('Frecuencia')
        plt.xlabel('Frecuente')

        plt.savefig(img, format='png')
        img.seek(0)

        img_url = base64.b64encode(img.getvalue()).decode()
        return img_url
        
    def graficodeprecioporproveedor(self):

        img = io.BytesIO()

        proveedor = self.df['Ultimo'].unique()
        precio = []
        for i in proveedor:
            suma = self.df.loc[self.df['Ultimo'] == i, ['Maximo']].sum()[0]
            precio.append(suma)

        plt.figure(figsize=(10,5))
        plt.bar(proveedor, precio, color = 'brown')
        plt.title('frecuencia del ultimo inversor')
        plt.xticks(rotation=10)
        plt.ylabel('Precio del Etherium')
        plt.xlabel('Ultimo')
        plt.savefig(img, format='png')
        img.seek(0)

        img_url = base64.b64encode(img.getvalue()).decode()
        return img_url

    def graficoFrecuenciadelproducto(self):

        img = io.BytesIO()

        x = self.df['Tipo_cliente']
        plt.figure(figsize=(10,5))
        plt.hist(x, bins=None, color='green')
        plt.title('Tipo de clientes inversores')
        plt.xticks(rotation=10)
        plt.ylabel('Frecuencia')
        plt.xlabel('Tipo_cliente')

        plt.savefig(img, format='png')
        img.seek(0)

        img_url = base64.b64encode(img.getvalue()).decode()
        return img_url
