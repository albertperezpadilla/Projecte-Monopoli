#Aqui haremos el monopoly

import random
import diccionarios as dic

#Variables del comienzo de la partida

historial = []

def mostrar_historial():
    global historial
    for i in historial:
        print(i + '\n')
    if len(historial) > 14:  
        historial.pop(0)
def afegir_historial(accio):
    historial.append(accio)
def ordre_jugades():
        colors = ['G','T','V','B']
        random.shuffle(colors)
        return colors           

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


    print(f"""
                +--------+----{casa[13]}+----{casa[14]}+--------+----{casa[16]}+---{casa[17]}+---------+   "Banca":
                |Parking |Urquinao|Fontana |Sort    |Rambles |Pl.Cat  |Anr pró |    Diners: {dic.banca['diners']}
                |{t[12]}  |{t[13]}  |{t[14]}  |{t[15]}  |{t[16]}  |{t[17]}  |{t[18]}  |
                +--------+--------+--------+--------+--------+--------+--------+jugador blau:
                |Aragó  {casa[11]}                                            | Angel {casa[19]}    
                |{t[11]} {hotel[11]}                                            |{t[19]} {hotel[19]}  
                +--------+                                            +--------+          
                |S.Joan {casa[10]}                                            |Augusta{casa[20]}
                |{t[10]} {hotel[10]}                                            |{t[20]} {hotel[20]}
                +--------+                                            +--------+
                |Caixa   |                                            |Caixa   |
                |{t[9]}  |                                            |{t[21]}  |
                +--------+                                            +--------+
                |Aribau {casa[8]}                                            |Balmes {casa[22]}
                |{t[8]} {hotel[8]}                                            |{t[22]} {hotel[22]}
                +--------+                                            +--------+
                |Muntan {casa[7]}                                            |Gracia {casa[23]}
                |{t[7]} {hotel[7]}                                            |{t[23]} {hotel[23]}
                +--------+----{casa[5]}+----{casa[4]}+--------+----{casa[2]}+----{casa[1]}+--------+
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