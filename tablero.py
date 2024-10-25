#Aqui haremos las funciones del tablero
import random 
import diccionarios as dic
import cartas as ct
import uso_general as ug
import principals as pr
ordenats = False

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
