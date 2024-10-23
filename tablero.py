#Aqui haremos las funciones del tablero
import random 
import diccionarios as dic
import cartas as ct
import uso_general as ug
import principals as pr
ordenats = False
historial = []
def afegir_historial(accio):
    historial.append(accio)
    if len(historial) > 14:
        historial.pop(0)

def dibuixa_historial():
    global historial
    historial_bien = []

    # mirar que no se pase de 14
    for i in range(14):
        if i < len(historial):
            comanda = historial[i]
            llarg = len(comanda)
            espacios = 41 - llarg
            historial_bien.append(comanda + (' ' * espacios))
        else:
            historial_bien.append(' ' * 41)

    return historial_bien
def ordre_jugadors():
    global ordenats
    global colors 
    if not ordenats:
        colors = ['groc', 'taronja', 'vermell', 'blau']
        random.shuffle(colors)
        ordenats = True  
    return colors

def mostrar_info(color):
    carrers = dic.jugadors[color]["carrers"]
    cartes = dic.jugadors[color]["cartes"]
    diners = dic.jugadors[color]["diners"]
    if len(carrers) == 0:
        carrers = "Res"
    if len(cartes) == 0:
        cartes = "Res"
    info =  [carrers ,diners, cartes]
    return info
blau = mostrar_info("blau")
taronja = mostrar_info("taronja")
vermell = mostrar_info("vermell")
groc = mostrar_info("blau")
