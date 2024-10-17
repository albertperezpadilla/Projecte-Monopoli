#Aqui haremos el monopoly

import random

#Variables del comienzo de la partida

historial = []
banca = {
    'diners': 0,
    'carrers' : ['Lauria', 'Rosselló', 'Marina',' Consell de cent','Muntaner', 'Aribau', 'Sant Joan', 'Aragó','Urquinaona', 'Fontana', 'Les Rambles',' Plaça Catalunya', 'Portal de lÀngel',' Via Augusta', 'Balmes', 'Passeig de Gràcia']
}
jugadors = {
    "groc":  {
        'inicial': 'G',
        'diners': 2000,
        'cartes' : [],
        'carrers': [],
        'total casas': 0,
        'total hoteles': 0,
        'posicio': 0,
    },
    "taronja":  {
        'inicial': 'T',
        'diners': 2000,
        'cartes' : [],
        'carrers': [],
        'total casas': 0,
        'total hoteles': 0,
        'posicio': 0,
    },
    "vermell":  {
        'inicial': 'V',
        'diners': 2000,
        'cartes' : [],
        'carrers': [],
        'total casas': 0,
        'total hoteles': 0,
        'posicio': 0,
    },
    "blau": {
        'inicial': 'B',
        'diners': 2000,
        'cartes' : [],
        'carrers': [],
        'total casas': 2,
        'total hoteles': 2,
        'posicio': 0,
    }
}

#Direccionario de direccionarios de los precios de cada calle
dic_carrers = {
    "Lauria": {
        "Ll. Casa": 10,
        "Ll. Hotel": 15,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 200,
        "Cmp. Hotel": 250,
        "Propietari": "banca",
        "Num. Cases": 1,
        "Num. Hoteles": 0,
        'posicio': 1

    },
    "Roselló": {
        "Ll. Casa": 10,
        "Ll. Hotel": 15,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 225,
        "Cmp. Hotel": 255,
        "Propietari": "banca",
        "Num. Cases": 1,
        "Num. Hoteles": 0,
        'posicio': 2
    },
    "Marina": {
        "Ll. Casa": 15,
        "Ll. Hotel": 15,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 250,
        "Cmp. Hotel": 260,
        "Propietari": "banca",
        "Num. Cases": 1,
        "Num. Hoteles": 0,
        'posicio': 4
    },
    "C. de cent": {
        "Ll. Casa": 15,
        "Ll. Hotel": 20,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 275,
        "Cmp. Hotel": 265,
        "Propietari": "banca",
        "Num. Cases": 1,
        "Num. Hoteles": 1,
        'posicio': 5
    },
    "Muntaner": {
        "Ll. Casa": 20,
        "Ll. Hotel": 20,
        "Cmp. Trrny": 60,
        "Cmp. Casa": 300,
        "Cmp. Hotel": 270,
        "Propietari": "banca",
        "Num. Cases": 1,
        "Num. Hoteles": 1,
        'posicio': 7
    },
    "Aribau": {
        "Ll. Casa": 20,
        "Ll. Hotel": 20,
        "Cmp. Trrny": 60,
        "Cmp. Casa": 325,
        "Cmp. Hotel": 275,
        "Propietari": "banca",
        "Num. Cases": 0,
        "Num. Hoteles": 0,
        'posicio': 8
    },
    "Sant Joan": {
        "Ll. Casa": 25,
        "Ll. Hotel": 25,
        "Cmp. Trrny": 60,
        "Cmp. Casa": 350,
        "Cmp. Hotel": 280,
        "Propietari": "banca",
        "Num. Cases": 0,
        "Num. Hoteles": 0,
        'posicio': 10
    },
    "Aragó": {
        "Ll. Casa": 25,
        "Ll. Hotel": 25,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 375,
        "Cmp. Hotel": 285,
        "Propiedatari": "banca",
        "Num. Cases": 0,
        "Num. Hoteles": 0,
        'posicio': 11
    },
    "Urquinaona": {
        "Ll. Casa": 30,
        "Ll. Hotel": 25,
        "Cmp. Trrny": 70,
        "Cmp. Casa": 400,
        "Cmp. Hotel": 290,
        "Propietari": "banca",
        "Num. Cases": 1,
        "Num. Hoteles": 1,
        'posicio': 13
    },
    "Fontana": {
        "Ll. Casa": 30,
        "Ll. Hotel": 30,
        "Cmp. Trrny": 70,
        "Cmp. Casa": 425,
        "Cmp. Hotel": 300,
        "Propietari": "banca",
        "Num. Cases": 0,
        "Num. Hoteles": 0,
        'posicio': 14
    },
    "Les Rambles": {
        "Ll. Casa": 35,
        "Ll. Hotel": 30,
        "Cmp. Trrny": 70,
        "Cmp. Casa": 450,
        "Cmp. Hotel": 310,
        "Propietari": "banca",
        "Num. Cases": 0,
        "Num. Hoteles": 0,
        'posicio': 16
    },
    "Pl. Catalunya": {
        "Ll. Casa": 35,
        "Ll. Hotel": 30,
        "Cmp. Trrny": 70,
        "Cmp. Casa": 475,
        "Cmp. Hotel": 320,
        "Propietari": "banca",
        "Num. Cases": 0,
        "Num. Hoteles": 0,
        'posicio': 17
    },
    "P. Àngel": {
        "Ll. Casa": 40,
        "Ll. Hotel": 35,
        "Cmp. Trrny": 80,
        "Cmp. Casa": 500,
        "Cmp. Hotel": 330,
        "Propietari": "banca",
        "Num. Cases": 0,
        "Num. Hoteles": 0,
        'posicio': 19
    },
    "Via Augusta": {
        "Ll. Casa": 40,
        "Ll. Hotel": 35,
        "Cmp. Trrny": 80,
        "Cmp. Casa": 525,
        "Cmp. Hotel": 250,
        "Propietari": "banca",
        "Num. Cases": 0,
        "Num. Hoteles": 0,
        'posicio': 20
    },
    "Balmes": {
        "Ll. Casa": 50,
        "Ll. Hotel": 40,
        "Cmp. Trrny": 80,
        "Cmp. Casa": 550,
        "Cmp. Hotel": 350,
        "Propietari": "banca",
        "Num. Cases": 1,
        "Num. Hoteles": 0,
        'posicio': 22
    },
    "Pg. de Gràcia": {
        "Ll. Casa": 50,
        "Ll. Hotel": 50,
        "Cmp. Trrny": 80,
        "Cmp. Casa": 525,
        "Cmp. Hotel": 360,
        "Propietari": "banca",
        "Num. Cases": 1,
        "Num. Hoteles": 1,
        'posicio': 23
    }
}


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
        
    for jugador in jugadors:
        color = jugadors[jugador]['inicial']
        posicio = jugadors[jugador]['posicio']
        t[posicio] += color

    for carrer in dic_carrers:
        num_casa = dic_carrers[carrer]['Num. Cases']
        num_hotels = dic_carrers[carrer]['Num. Hoteles']
        print(num_hotels)
        posicio_carrer = dic_carrers[carrer]['posicio'] # posicion calle
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
                |Parking |Urquinao|Fontana |Sort    |Rambles |Pl.Cat  |Anr pró |    Diners: {banca['diners']}
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
    if jugadors[color]['posicio'] == 0:
        jugadors[color]['diners'] += 200
#sortida("blau")

#FUNCIONES SUPORT


def anar_sortida(color):
    jugadors[color]['posicio'] = 0
    sortida(color)
    print(f"El jugador {color} ha anat a Sortida, rep +200€")
#anar_sortida("blau")

def sort(color):
    cartes_sort = ['sortir_presó','anar_presó','anar_sortida','tres_enrere','reparacions_propietat','alcalde']
    carta = random.choice(cartes_sort)
    jugadors[color]["cartes"].append(carta)
    return jugadors[color]
print(sort("blau")) 

def reparacions(color):
    precio = 25 * jugadors[color]["total casas"]
    precio = precio + (100 * jugadors[color]["total hoteles"])
    jugadors[color]["diners"] -= precio
    banca["diners"] += precio
    

    return banca,jugadors[color]
    #25 por casa
#print("REPARACIONS")
print(reparacions("blau"))
def alcalde(color):
    return