#Aqui pondremos las funciones principales
import tablero as tb
import diccionarios as dic
import cartas as ct
import uso_general as ug
import random

#Dibujar el tablero
def taulellDibuixar():
    t = []
    casa = []
    hotel = []
    for i in range(0, 24):
        t.append("")
        casa.append("")
        hotel.append("")  # Casillas vacías 
    colors = tb.ordre_jugadors()
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
    log = tb.dibuixa_historial() 
    print(f"""
                +--------+----{casa[13]}+----{casa[14]}+--------+----{casa[16]}+---{casa[17]}+---------+   "Banca":
                |Parking |Urquinao|Fontana |Sort    |Rambles |Pl.Cat  |Anr pró |    Diners: {dic.banca['diners']}
                |{t[12]}  |{t[13]}  |{t[14]}  |{t[15]}  |{t[16]}  |{t[17]}  |{t[18]}  |
                +--------+--------+--------+--------+--------+--------+--------+>jugador blau: 
                |Aragó  {casa[11]}> {log[0]} | Angel {casa[19]}Carrers:{dic.blau['carrers']}
                |{t[11]} {hotel[11]}{log[1]}   |{t[19]} {hotel[19]}Diners:{dic.blau['diners']}  
                +--------+{log[2]}   +--------+Cartes:{dic.blau['cartes']}          
                |S.Joan {casa[10]}{log[3]}   |Augusta{casa[20]}>jugador Vermell:
                |{t[10]} {hotel[10]}> {log[4]} |{t[20]} {hotel[20]}Carrers:{dic.vermell['carrers']}
                +--------+{log[5]}   +--------+Diners:{dic.vermell['diners']} 
                |Caixa   |{log[6]}   |Caixa   |Cartes:{dic.vermell['cartes']} 
                |{t[9]}  |{log[7]}   |{t[21]}  |>jugador Groc:
                +--------+> {log[8]} +--------+Carrers:{dic.groc['carrers']}
                |Aribau {casa[8]}{log[9]}   |Balmes {casa[22]}Diners:{dic.groc['diners']} 
                |{t[8]} {hotel[8]}{log[10]}   |{t[22]} {hotel[22]}Cartes:{dic.groc['cartes']} 
                +--------+> {log[11]} +--------+>jugador Taronja:
                |Muntan {casa[7]}{log[12]}   |Gracia {casa[23]}Carrers:{dic.taronja['carrers']}
                |{t[7]} {hotel[7]}{log[13]}   |{t[23]} {hotel[23]}Diners:{dic.taronja['diners']} 
                +--------+----{casa[5]}+----{casa[4]}+--------+----{casa[2]}+----{casa[1]}+--------+Cartes:{dic.taronja['cartes']} 
                |{t[6]}  |{t[5]}  |{t[4]}  |{t[3]}  |{t[2]}  |{t[1]}  |{t[0]}  |
                |Presó   |Consell |Marina  |Sort    |Rosell  |Lauria  |Sortida |
                +--------+--------+--------+--------+--------+--------+--------+
    """)
def tirar_dados(color):
    dau1 = random.randint(1,6)
    dau2 = random.randint(1,6)
    suma = dau1 + dau2
    dic.jugadors[color]['posicio'] += suma 
    tb.afegir_historial(f"{color} ha tret {suma}")

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
                if ug.totalPagar(posicio) > dic.jugadors[color]['diners']:
                    opcions.append("preu jugador")
                    opcions.append("preu banc")
                    opcions.append("vendre al banc")
                    tmp = dic.jugadors.copy()
                    del tmp[color]
                    for jugador in tmp:
                        if tmp[jugador]['diners'] >= ug.totalVendre(color) * 0.9:
                            opcions.append(f"vendre a {tmp[jugador]['inicial']}")
        return opcions
