#Aqui haremos el monopoly

import random
import diccionarios as dic

#Variables del comienzo de la partida

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
def taulellDibuixar():
    t = []
    casa = []
    hotel = []
    for i in range(0, 24):
        t.append("")
        casa.append("")
        hotel.append("")  # Casillas vacías 
    colors = ordre_jugadors()
    global ordenats
    for color in colors:
        inicial = dic.jugadors[color]['inicial']
        posicio = dic.jugadors[color]['posicio']
        posicio = posicio % 24
        t[posicio] += inicial
 
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
                +--------+--------+--------+--------+--------+--------+--------+>jugador blau: 
                |Aragó  {casa[11]}> {log[0]} | Angel {casa[19]}Carrers:{blau[0]}
                |{t[11]} {hotel[11]}{log[1]}   |{t[19]} {hotel[19]}Diners:{blau[1]}  
                +--------+{log[2]}   +--------+Cartes:{blau[2]}          
                |S.Joan {casa[10]}{log[3]}   |Augusta{casa[20]}>jugador Vermell:
                |{t[10]} {hotel[10]}> {log[4]} |{t[20]} {hotel[20]}Carrers:{vermell[0]}
                +--------+{log[5]}   +--------+Diners:{vermell[1]} 
                |Caixa   |{log[6]}   |Caixa   |Cartes:{vermell[2]} 
                |{t[9]}  |{log[7]}   |{t[21]}  |>jugador Groc:
                +--------+> {log[8]} +--------+Carrers:{groc[0]}
                |Aribau {casa[8]}{log[9]}   |Balmes {casa[22]}Diners:{groc[1]} 
                |{t[8]} {hotel[8]}{log[10]}   |{t[22]} {hotel[22]}Cartes:{groc[2]} 
                +--------+> {log[11]} +--------+>jugador Taronja:
                |Muntan {casa[7]}{log[12]}   |Gracia {casa[23]}Carrers:{taronja[0]}
                |{t[7]} {hotel[7]}{log[13]}   |{t[23]} {hotel[23]}Diners:{taronja[1]} 
                +--------+----{casa[5]}+----{casa[4]}+--------+----{casa[2]}+----{casa[1]}+--------+Cartes:{taronja[2]} 
                |{t[6]}  |{t[5]}  |{t[4]}  |{t[3]}  |{t[2]}  |{t[1]}  |{t[0]}  |
                |Presó   |Consell |Marina  |Sort    |Rosell  |Lauria  |Sortida |
                +--------+--------+--------+--------+--------+--------+--------+
    """)
taulellDibuixar()
#CASILLAS ESPECIALES
def sortida(color):
    if dic.jugadors[color]['posicio'] == 0:
        dic.jugadors[color]['diners'] += 200
#sortida("blau")

#FUNCIONES SUPORT


def anar_sortida(color):
    dic.jugadors[color]['posicio'] = 0
    sortida(color)
    print(f"El jugador {color} ha anat a Sortida, rep +200€")
#anar_sortida("blau")

def sort(color):
    cartes_sort = ['sortir_presó','anar_presó','anar_sortida','tres_enrere','reparacions_propietat','alcalde']
    carta = random.choice(cartes_sort)
    dic.jugadors[color]["cartes"].append(carta)
    return dic.jugadors[color]
print(sort("blau")) 

def reparacions(color):
    precio = 25 * dic.jugadors[color]["total casas"]
    precio = precio + (100 * dic.jugadors[color]["total hoteles"])
    dic.jugadors[color]["diners"] -= precio
    dic.banca["diners"] += precio
    

    return dic.banca, dic.jugadors[color]
    #25 por casa
#print("REPARACIONS")
print(reparacions("blau"))
def alcalde(color):
    return

#Hay que ordenar bien las funciones
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
def trucs():
    opcions = ["anar a casella o carrer",
               "afegir cases","afegir hotels",
               "seguent jugador",
               "diners jugador", "diners banca"
               ]
    print(opcions)
    opcio = input("Opcio: ")
    while opcio not in opcions:
        print("Opció incorrecte")
        opcio = input("Opcio: ").lower()
        if opcio == opcions[0]:
            print("Digues el nom del carrer al que vols anar: ")
            nom_carrer = input("Anar a carrer")
            for carrer in dic.carrers:
                if dic.carrers[carrer] == nom_carrer:
                    posicio = dic.carrers[carrer]['posicio']
                    break 
            dic.jugadors['posicio'] = posicio
        elif opcio == opcions[1]:
            print("tmp")
print("hola")