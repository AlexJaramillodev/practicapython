import pandas as pd

from generators.generadorDecibelios import generarDatosRuido

def construirDataRuido(): 
    #creando un datFrame
    datosRuido = generarDatosRuido()
    dataFrameRuido = pd.DataFrame(datosRuido, columns=['id', 'nivelRuido', 'comuna'])
    dataFrameRuido.to_csv('datosRuido.csv', index=False)
    print(dataFrameRuido)

construirDataRuido()
