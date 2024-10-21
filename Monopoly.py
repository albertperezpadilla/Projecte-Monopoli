#Aqui haremos el monopoly

import random
import diccionarios as dic

#Variables del comienzo de la partida

historial = []
ordenats = False

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



def ordre_jugades():
        colors = ['G','T','V','B']
        random.shuffle(colors)
        return colors           
    
def mostrar_info(color):
    carrers = dic.jugadors[color]["carrers"]
    cartes = dic.jugadors[color]["cartes"]
    diners = dic.jugadors[color]["diners"]
    if len(carrers) == 0:
        carrers = "Res"
    if len(cartes) == 0:
        cartes = "Res"
    return f'''
            Carrers: {carrers}
            Cartes: {cartes}
            Diners: {diners} '''

print(ordre_jugades())

def taulellDibuixar():
    t = []
    casa = []
    hotel = []
    for i in range(0, 24):
        t.append("")
        casa.append("")
        hotel.append("")  # Casillas vacías 
        
    for jugador in dic.jugadors:
        color = dic.jugadors[jugador]['inicial']
        posicio = dic.jugadors[jugador]['posicio']
        t[posicio] += color

    for carrer in dic.carrers:
        num_casa = dic.carrers[carrer]['Num. Cases']
        num_hotels = dic.carrers[carrer]['Num. Hoteles']
        print(num_hotels)
        posicio_carrer = dic.carrers[carrer]['posicio'] # posicion calle
        if num_hotels == 0 and num_casa > 0:
            casa[posicio_carrer] = "--" + str(num_casa) + "C" 
        elif num_casa > 0 and num_hotels > 0:
            casa[posicio_carrer] = str(num_hotels) + "H" + (str(num_casa)) + "C"
        else:
            casa[posicio_carrer] = "----"

        #HOTELES CASAS LADOS:
        if posicio_carrer in [7, 8, 10, 11, 19, 20, 22, 23]:
            if  num_casa > 0:
                casa[posicio_carrer] = str(num_casa) + "C" 
            if num_hotels > 0:
                hotel[posicio_carrer] = str(num_hotels) + "H" 

            else:
                casa[posicio_carrer] = " |"
                hotel[posicio_carrer] = " |"
    # Ajuste de espacios para los jugadores
    for i in range(len(t)):
        t[i] = t[i].ljust(6)
    




    log = dibuixa_historial() 

    print(f"""
                +--------+----{casa[13]}+----{casa[14]}+--------+----{casa[16]}+---{casa[17]}+---------+   "Banca":
                |Parking |Urquinao|Fontana |Sort    |Rambles |Pl.Cat  |Anr pró |    Diners: {dic.banca['diners']}
                |{t[12]}  |{t[13]}  |{t[14]}  |{t[15]}  |{t[16]}  |{t[17]}  |{t[18]}  |
                +--------+--------+--------+--------+--------+--------+--------+jugador blau: 
                |Aragó  {casa[11]}> {log[0]} | Angel {casa[19]}    
                |{t[11]} {hotel[11]}{log[1]}   |{t[19]} {hotel[19]}  
                +--------+{log[2]}   +--------+          
                |S.Joan {casa[10]}{log[3]}   |Augusta{casa[20]}
                |{t[10]} {hotel[10]}> {log[4]} |{t[20]} {hotel[20]}
                +--------+{log[5]}   +--------+
                |Caixa   |{log[6]}   |Caixa   |
                |{t[9]}  |{log[7]}   |{t[21]}  |
                +--------+> {log[8]} +--------+
                |Aribau {casa[8]}{log[9]}   |Balmes {casa[22]}
                |{t[8]} {hotel[8]}{log[10]}   |{t[22]} {hotel[22]}
                +--------+> {log[11]} +--------+
                |Muntan {casa[7]}{log[12]}   |Gracia {casa[23]}
                |{t[7]} {hotel[7]}{log[13]}   |{t[23]} {hotel[23]}
                +--------+----{casa[5]}+----{casa[4]}+--------+----{casa[2]}+----{casa[1]}+--------+
                |{t[6]}  |{t[5]}  |{t[4]}  |{t[3]}  |{t[2]}  |{t[1]}  |{t[0]}  |
                |Presó   |Consell |Marina  |Sort    |Rosell  |Lauria  |Sortida |
                +--------+--------+--------+--------+--------+--------+--------+
    """)

taulellDibuixar()

def tirar_dados(color):
    dau1 = random.randint(1,6)
    dau2 = random.randint(1,6)
    suma = dau1 + dau2
    dic.jugadors[color]['posicio'] += suma 
    afegir_historial(f"{color} ha tret {suma}")

#CASILLAS ESPECIALES
def sortida(color):
        dic.jugadors[color]['diners'] += 200

def casillas_especiales(color):
    pos = dic.jugadors[color]['posicio']
    if pos == 0:
        sortida(color)
    if pos == 6:
        preso(color)
    if pos == 18:
        anar_preso(color)
    if pos == 12:
        afegir_historial(f"{color} ha caigut al Parking")
    if pos in [9,21]:
        caixa(color)
    if pos in [3,15]:
        sort(color)


#CARTES
'''- Sortir de la presó: quan cau a la presó podrà seguir jugant (i perdrà aquesta opció)
- Anar a la presó: el jugador va a la presó sense cobrar la sortida i sense jugar 3 torns
- Anar a la sortida: el jugador va a la sortida i cobra els 200€
- Anar tres espais endarrera'''

#TRES ESPAIS ENRERRE:
def tres_enrere(color):
    afegir_historial(f"El jugador {color} ha anat tres caselles enrere")
    dic.jugadors[color]['posicio'] -= 3       

#LOGICA PRESÓ
def preso(color):

    if dic.jugadors[color]['posicio'] == 6:
            afegir_historial(f"El jugador {color} ha caigut a la pressó")          
            dic.jugadors[color]['empressonat'] = True
            dic.jugadors[color]['torns_empressonat'] -= 1 
            dau1 = random.randint(1, 6)
            dau2 = random.randint(1, 6)
            if dau1 == dau2:
                dic.jugadors[color]['empressonat'] = False
                dic.jugadors[color]['torns_empressonat'] = 0

            if dic.jugadors[color]['torns_empressonat'] <= 0:
                dic.jugadors[color]['empressonat'] = False
                dic.jugadors[color]['torns_empressonat'] = 0
            else:
                afegir_historial(f"{color} segueix a la presó, li queden {dic.jugadors[color]['torns_empressonat']} torns.")
                return False
    else:
        dic.jugadors[color]['torns_empressonat'] = 3
        dic.jugadors[color]['empressonat'] = True
        afegir_historial(f"{color} ha anat a la presó.")


def anar_preso(color):
    dic.jugadors[color]['posicio'] = 6
    preso(color)

def sortir_preso(color):
        dic.jugadors[color]['empressonat'] = False
        dic.jugadors[color]['torns_empressonat'] = 0
        dic.jugadors[color]['cartes'].remove("sortir_presó")
#sortida("blau")

#FUNCIONES SUPORT


def anar_sortida(color):
    dic.jugadors[color]['posicio'] = 0
    sortida(color)
    afegir_historial(f"El jugador {color} ha anat a Sortida, rep +200€")
#anar_sortida("blau")

    
def reparacions(color):
    precio = 25 * dic.jugadors[color]["total casas"]
    precio = precio + (100 * dic.jugadors[color]["total hoteles"])
    dic.jugadors[color]["diners"] -= precio
    dic.banca["diners"] += precio
    afegir_historial(f"{color} ha fet reparacions a les seves construccions")    

    return dic.banca, dic.jugadors[color]
def alcalde(color):
    for jugador in dic.jugadors:
        dic.jugadors[jugador]['diners'] -= 50
        dic.jugadors[color]['diners'] += 200
    afegir_historial(f"{color} ha sigut escollit l'alcalde,rep 150€")
    return
#SUERTE
def sort(color):
    cartes_sort = [f"sortir_presó','{anar_preso(color)}','{anar_sortida(color)}','{tres_enrere(color)}','{reparacions()}','{alcalde(color)}"]
    carta = random.choice(cartes_sort)
    if carta == "sortir_presó":
        dic.jugadors[color]["cartes"].append(carta)
        afegir_historial(f"{color} té la carta de sortir de la presó")    
    return dic.jugadors[color]
#CAIXA

'''- Sortir de la presó: quan cau a la presó podrà seguir jugant (i perdrà aquesta opció)
- Anar a la presó: el jugador va a la presó sense cobrar la sortida i sense jugar 3 torns
- Error de la banca al teu favor, guanyes 150€
- Despeses mèdiques, pagues 50€
- Despeses escolars, pagues 50€
- Reparacions al carrer, pagues 40€
- Concurs de bellesa, guanyes 10€'''
def caixa(color):
    cartes_caixa = [f"sortir_presó','{error_banca(color)}','{despesses_mediques(color)}','{despesses_escolars(color)}','{reparacions_carrers()}','{concurs(color)}"]
    carta = random.choice(cartes_caixa)
    if carta == "sortir_presó":
        dic.jugadors[color]["cartes"].append(carta)
        afegir_historial(f"{color} té la carta de sortir de la presó")    
    return dic.jugadors[color]
#FUNCIONS CAIXA:
def error_banca(color):
    dic.jugadors[color]['diners'] += 150
    afegir_historial("Error de la banca al teu favor, guanyes 150€")
def despesses_mediques(color):
    dic.jugadors[color]['diners'] -= 50
    afegir_historial("Despeses mediques, pagues 50€")
def despesses_escolars(color):
    dic.jugadors[color]['diners'] -= 50
    afegir_historial("Despeses escolars, pagues 50€")
def reparacions_carrers(color):
    dic.jugadors[color]['diners'] -= 40
    afegir_historial("reparacions al carrer, pagues 40€")
def concurs(color):
    dic.jugadors[color]['diners'] += 10
    afegir_historial("Concurs de bellesa, guanyes 10€")
#Alquiler a pagar
def totalPagar(posicio):
    for dades_carrer in dic.carrers.values():
        if dades_carrer['posicio'] == posicio:
            ll_casas = dades_carrer["Ll. Casa"] * dades_carrer["Num. Cases"]
            ll_hotels = dades_carrer["Ll. Hotel"] * dades_carrer["Num. Hoteles"]
            total_lloguer = ll_casas + ll_hotels
            return total_lloguer
#Valor vender todas las propiedades a otro jugador/banca
def totalVendre(color):
    preu_total = 0
    carrers_color = dic.jugadors[color]['carrers']
    for carrer in carrers_color:
        preu_terreny = dic.carrers[carrer]['Cmp. Trrny']
        num_cases = dic.carrers[carrer]['Num. Cases']
        num_hotels = dic.carrers[carrer]['Num. Hoteles']
        preu_cases = num_cases * dic.carrers[carrer]['Cmp. Casa']
        preu_hotels = num_hotels * dic.carrers[carrer]['Cmp. Hotel']
        preu_total += preu_terreny + preu_cases + preu_hotels
    return preu_total
    
#Opciones del jugador
#funcion para saber comprobar si una calle tiene propietario o no
def opcions_jugador(color):
    posicio = dic.jugadors[color]['posicio']
    opcions = ["passar"]
    for carrer in dic.carrers:
        if dic.carrers[carrer]['posicio'] == posicio:
            nom_carrer = carrer
            break
    if posicio != 12:
        if posicio not in [0, 3, 6, 9, 12, 15, 18, 21]:
            if dic.carrers[nom_carrer]["Propietari"] == "banca":
                opcions.append("comprar terreny")
            elif dic.carrers[nom_carrer]["Propietari"] == color:
                if dic.carrers[nom_carrer]["Num. Cases"] < 4:
                    opcions.append("comprar casa")
                if dic.carrers[nom_carrer]["Num. Hoteles"] < 2:
                    opcions.append("comprar hotel")
                opcions.append("preus")
            else:
                if totalPagar(posicio) > dic.jugadors[color]['diners']:
                    opcions.append("preu jugador")
                    opcions.append("preu banc")
                    opcions.append("vendre al banc")
                    tmp = dic.jugadors.copy()
                    del tmp[color]
                    for jugador in tmp:
                        if tmp[jugador]['diners'] >= totalVendre(color) * 0.9:
                            opcions.append(f"vendre a {tmp[jugador]['inicial']}")
    return opcions

