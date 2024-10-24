#Aqui pondremos funciones de las cartas
import random
import diccionarios as dic
import tablero as tb

#CASILLAS ESPECIALES
def sortida(color):
        dic.jugadors[color]['diners'] += 200
        tb.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" ha pasat per sortida +200")

def anar_preso(color):
    dic.jugadors[color]['posicio'] = 6
    preso(color)
def sortida_preso(color):
        dic.jugadors[color]['empressonat'] = False
        dic.jugadors[color]['torns_empressonat'] = 0
        dic.jugadors[color]['posicio'] += 1
        tb.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" surt de la pressó")
#LOGICA PRESÓ
def preso(color):
    if dic.jugadors[color]['posicio'] == 6:
            #si cae en prisión:
            if not dic.jugadors[color]['empressonat']:
                tb.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" ha entrat a la pressó")          
                dic.jugadors[color]['empressonat'] = True
                dic.jugadors[color]['torns_empressonat'] = 3
            else:
                dic.jugadors[color]['torns_empressonat'] -= 1 
            dau1 = random.randint(1, 6)
            dau2 = random.randint(1, 6)
            
            #logica de salida
            if dau1 == dau2:
                tb.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" ha tret {dau1} i {dau2} (dobles).")
                sortida_preso(color)
            elif dic.jugadors[color]['torns_empressonat'] <= 0:
                sortida_preso(color)
            if "sortir_presó" in dic.jugadors[color]['cartes'] :
                dic.jugadors[color]['cartes'].remove("sortir_presó")
                sortida_preso(color)
                return
            tb.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" és a la pressó, {dic.jugadors[color]['torns_empressonat']} torns sense tirar")
            return False
    else:
        dic.jugadors[color]['torns_empressonat'] = 3
        dic.jugadors[color]['empressonat'] = True
        tb.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" ha anat a la presó.")


#CARTES
def anar_sortida(color):
    dic.jugadors[color]['posicio'] = 0
    sortida(color)
    tb.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" ha anat a Sortida, rep +200€")
def tres_enrere(color):
    tb.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" ha anat tres caselles enrere")
    dic.jugadors[color]['posicio'] -= 3       
def reparacions(color):
    precio = 25 * dic.jugadors[color]["total casas"]
    precio = precio + (100 * dic.jugadors[color]["total hoteles"])
    dic.jugadors[color]["diners"] -= precio
    dic.banca["diners"] += precio
    tb.afegir_historial(f" \"{dic.jugadors[color]['inicial']}\" repara construccions")
    return dic.banca, dic.jugadors[color]
def alcalde(color):
    for jugador in dic.jugadors:
        dic.jugadors[jugador]['diners'] -= 50
        dic.jugadors[color]['diners'] += 200
    tb.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" ha sigut escollit l'alcalde,rep 150€")
    return
#SUERTE
def sort(color):
    cartes_sort = ["sortir_presó","anar_preso","anar_sortida","tres_enrere","reparacions","alcalde"]  
    carta = random.choice(cartes_sort)
    if carta == "sortir_presó":
        dic.jugadors[color]["cartes"].append(carta)
        tb.afegir_historial(f"{color} té la carta de sortir de la presó")
    elif carta == "anar_preso":
        anar_preso(color)
    elif carta == "anar_sortida":
        anar_sortida(color)
    elif carta == "tres_enrere":
        tres_enrere(color)
    elif carta == "reparacions":
        reparacions(color)
    elif carta == "alcalde":
        alcalde(color)

    return dic.jugadors[color]


#FUNCIONS CAIXA:
def error_banca(color):
    dic.jugadors[color]['diners'] += 150
    tb.afegir_historial("Error de la banca, guanyes 150€")
def despesses_mediques(color):
    dic.jugadors[color]['diners'] -= 50
    tb.afegir_historial("Despeses mediques, pagues 50€")
def despesses_escolars(color):
    dic.jugadors[color]['diners'] -= 50
    tb.afegir_historial("Despeses escolars, pagues 50€")
def reparacions_carrers(color):
    dic.jugadors[color]['diners'] -= 40
    tb.afegir_historial("Reparacions al carrer, pagues 40€")
def concurs(color):
    dic.jugadors[color]['diners'] += 10
    tb.afegir_historial("Concurs de bellesa, guanyes 10€")

#CAIXA
def caixa(color):
    cartes_caixa = [
        "sortir_presó","error_banca","despesses_mediques","despesses_escolars","reparacions_carrers","concurs"]
    
    carta = random.choice(cartes_caixa)
    if carta == "sortir_presó":
        dic.jugadors[color]["cartes"].append(carta)
        if '(Res)' in dic.jugadors[color]['cartes']:
            dic.jugadors[color]['cartes'].remove('(Res)')
        tb.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" té la carta de sortir de la presó")
    elif carta == "error_banca":
        error_banca(color)
    elif carta == "despesses_mediques":
        despesses_mediques(color)
    elif carta == "despesses_escolars":
        despesses_escolars(color)
    elif carta == "reparacions_carrers":
        reparacions_carrers(color)
    elif carta == "concurs":
        concurs(color)

    return dic.jugadors[color]

def casillas_especiales(color):
    pos_actual = dic.jugadors[color]['posicio']
    if pos_actual > 23 or pos_actual == 0:
        sortida(color)
        dic.jugadors[color]['posicio'] = pos_actual % 24

    # Otras casillas especiales
    if pos_actual == 6:
        preso(color)
    if pos_actual == 18:
        anar_preso(color)
    if pos_actual == 12:
        tb.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" ha caigut al Parking")
    if pos_actual in [9, 21]:
        caixa(color)
    if pos_actual in [3, 15]:
        sort(color)

    # Actualiza la posición anterior al final de la función
    dic.jugadors[color]['posicio_anterior'] = pos_actual
