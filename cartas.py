#Aqui pondremos funciones de las cartas
import random
import diccionarios as dic
import tablero as tb

#CASILLAS ESPECIALES
#Casilla salida
def sortida(color):
        dic.jugadors[color]['diners'] += 200

#funciones casillas especiales
def casillas_especiales(color):
    pos = dic.jugadors[color]['posicio']
    if pos == 0:
        sortida(color)
    if pos == 6:
        preso(color)
    if pos == 18:
        anar_preso(color)
    if pos == 12:
        tb.afegir_historial(f"{color} ha caigut al Parking")
    if pos in [9,21]:
        caixa(color)
    if pos in [3,15]:
        sort(color)

#ir a prisión
def anar_preso(color):
    dic.jugadors[color]['posicio'] = 6
    preso(color)

#salir prision
def sortida_preso(color):
        dic.jugadors[color]['empressonat'] = False
        dic.jugadors[color]['torns_empressonat'] = 0
        dic.jugadors[color]['cartes'].remove("sortir_presó")

#LOGICA PRESÓ
def preso(color):

    if dic.jugadors[color]['posicio'] == 6:
            #si cae en prisión:
            if not dic.jugadors[color]['empressonat']:
                tb.afegir_historial(f"El jugador {color} ha caigut a la pressó")          
                dic.jugadors[color]['empressonat'] = True
                dic.jugadors[color]['torns_empressonat'] = 3
            else:
                dic.jugadors[color]['torns_empressonat'] -= 1 
            dau1 = random.randint(1, 6)
            dau2 = random.randint(1, 6)
            
            #logica de salida
            if dau1 == dau2 or dic.jugadors[color]['torns_empressonat'] <= 0:
                if "sortir_presó" in dic.jugadors[color]['cartes'] :
                        dic.jugadors[color]['cartes'].remove("sortir_presó")
                sortida_preso(color)
                return
            tb.afegir_historial(f"{color} segueix a la presó, li queden {dic.jugadors[color]['torns_empressonat']} torns.")
            return False
    else:
        dic.jugadors[color]['torns_empressonat'] = 3
        dic.jugadors[color]['empressonat'] = True
        tb.afegir_historial(f"{color} ha anat a la presó.")

#CARTES

#ir salida
def anar_sortida(color):
    dic.jugadors[color]['posicio'] = 0
    sortida(color)
    tb.afegir_historial(f"El jugador {color} ha anat a Sortida, rep +200€")

#tirar pa tra
def tres_enrere(color):
    tb.afegir_historial(f"El jugador {color} ha anat tres caselles enrere")
    dic.jugadors[color]['posicio'] -= 3

#hacienda be like    
def reparacions(color):
    precio = 25 * dic.jugadors[color]["total casas"]
    precio = precio + (100 * dic.jugadors[color]["total hoteles"])
    dic.jugadors[color]["diners"] -= precio
    dic.banca["diners"] += precio
    tb.afegir_historial(f"{color} ha fet reparacions a les seves construccions")
    return dic.banca, dic.jugadors[color]

#eres hacienda
def alcalde(color):
    for jugador in dic.jugadors:
        dic.jugadors[jugador]['diners'] -= 50
        dic.jugadors[color]['diners'] += 200
    tb.afegir_historial(f"{color} ha sigut escollit l'alcalde,rep 150€")
    return

#SUERTE
def sort(color):
    cartes_sort = [f"sortir_presó','{anar_preso(color)}','{anar_sortida(color)}','{tres_enrere(color)}','{reparacions()}','{alcalde(color)}"]
    carta = random.choice(cartes_sort)
    if carta == "sortir_presó":
        dic.jugadors[color]["cartes"].append(carta)
        tb.afegir_historial(f"{color} té la carta de sortir de la presó")    
    return dic.jugadors[color]

#CAIXA
def caixa(color):
    cartes_caixa = [f"sortir_presó','{error_banca(color)}','{despesses_mediques(color)}','{despesses_escolars(color)}','{reparacions_carrers()}','{concurs(color)}"]
    carta = random.choice(cartes_caixa)
    if carta == "sortir_presó":
        dic.jugadors[color]["cartes"].append(carta)
        tb.afegir_historial(f"{color} té la carta de sortir de la presó")    
    return dic.jugadors[color]

#FUNCIONS CAIXA:
def error_banca(color):
    dic.jugadors[color]['diners'] += 150
    tb.afegir_historial("Error de la banca al teu favor, guanyes 150€")
def despesses_mediques(color):
    dic.jugadors[color]['diners'] -= 50
    tb.afegir_historial("Despeses mediques, pagues 50€")
def despesses_escolars(color):
    dic.jugadors[color]['diners'] -= 50
    tb.afegir_historial("Despeses escolars, pagues 50€")
def reparacions_carrers(color):
    dic.jugadors[color]['diners'] -= 40
    tb.afegir_historial("reparacions al carrer, pagues 40€")
def concurs(color):
    dic.jugadors[color]['diners'] += 10
    tb.afegir_historial("Concurs de bellesa, guanyes 10€")