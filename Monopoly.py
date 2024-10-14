#Aqui haremos el monopoly

import random

#Variables del comienzo de la partida
banc = 0
if banc < 500000:
    banc += 1000000

dgroc = 2000
dtaronja = 2000
dvermell = 2000
dblau= 2000

#JUGADORS

banca = {
    'diners': banc,
    'carrers' : ['Lauria', 'Rosselló', 'Marina',' Consell de cent','Muntaner', 'Aribau', 'Sant Joan', 'Aragó','Urquinaona', 'Fontana', 'Les Rambles',' Plaça Catalunya', 'Portal de lÀngel',' Via Augusta', 'Balmes', 'Passeig de Gràcia']
}

jugador_groc =  {
        'color': 'groc',
        'diners': dgroc,
        'cartes' : [],
        'carrers': [],
}

jugador_taronja =  {
        'color': 'taronja',
        'diners': dtaronja,
        'cartes' : [],
        'carrers': [],
}

jugador_vermell =  {
        'color': 'vermell',
        'diners': dvermell,
        'cartes' : [],
        'carrers': [],
}

jugador_blau =  {
        'color': 'blau',
        'diners': dblau,
        'cartes' : [],
        'carrers': [],
}

#Direccionario de direccionarios de los precios de cada calle
llista_preus = {
    "Lauria": {
        "Ll. Casa": 10,
        "Ll. Hotel": 15,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 200,
        "Cmp. Hotel": 250,
        "Propietari": banca
    },
    "Roselló": {
        "Ll. Casa": 10,
        "Ll. Hotel": 15,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 225,
        "Cmp. Hotel": 255,
        "Propietari": banca
    },
    "Marina": {
        "Ll. Casa": 15,
        "Ll. Hotel": 15,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 250,
        "Cmp. Hotel": 260,
        "Propietari": banca
    },
    "C. de cent": {
        "Ll. Casa": 15,
        "Ll. Hotel": 20,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 275,
        "Cmp. Hotel": 265,
        "Propietari": banca
    },
    "Muntaner": {
        "Ll. Casa": 20,
        "Ll. Hotel": 20,
        "Cmp. Trrny": 60,
        "Cmp. Casa": 300,
        "Cmp. Hotel": 270,
        "Propietari": banca
    },
    "Aribau": {
        "Ll. Casa": 20,
        "Ll. Hotel": 20,
        "Cmp. Trrny": 60,
        "Cmp. Casa": 325,
        "Cmp. Hotel": 275,
        "Propietari": banca
    },
    "Sant Joan": {
        "Ll. Casa": 25,
        "Ll. Hotel": 25,
        "Cmp. Trrny": 60,
        "Cmp. Casa": 350,
        "Cmp. Hotel": 280,
        "Propietari": banca
    },
    "Aragó": {
        "Ll. Casa": 25,
        "Ll. Hotel": 25,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 375,
        "Cmp. Hotel": 285,
        "Propiedatari": banca
    },
    "Urquinaona": {
        "Ll. Casa": 30,
        "Ll. Hotel": 25,
        "Cmp. Trrny": 70,
        "Cmp. Casa": 400,
        "Cmp. Hotel": 290,
        "Propietari": banca
    },
    "Fontana": {
        "Ll. Casa": 30,
        "Ll. Hotel": 30,
        "Cmp. Trrny": 70,
        "Cmp. Casa": 425,
        "Cmp. Hotel": 300,
        "Propietari": banca
    },
    "Les Rambles": {
        "Ll. Casa": 35,
        "Ll. Hotel": 30,
        "Cmp. Trrny": 70,
        "Cmp. Casa": 450,
        "Cmp. Hotel": 310,
        "Propietari": banca
    },
    "Pl. Catalunya": {
        "Ll. Casa": 35,
        "Ll. Hotel": 30,
        "Cmp. Trrny": 70,
        "Cmp. Casa": 475,
        "Cmp. Hotel": 320,
        "Propietari": banca
    },
    "P. Àngel": {
        "Ll. Casa": 40,
        "Ll. Hotel": 35,
        "Cmp. Trrny": 80,
        "Cmp. Casa": 500,
        "Cmp. Hotel": 330,
        "Propietari": banca
    },
    "Via Augusta": {
        "Ll. Casa": 40,
        "Ll. Hotel": 35,
        "Cmp. Trrny": 80,
        "Cmp. Casa": 525,
        "Cmp. Hotel": 250,
        "Propietari": banca
    },
    "Balmes": {
        "Ll. Casa": 50,
        "Ll. Hotel": 40,
        "Cmp. Trrny": 80,
        "Cmp. Casa": 550,
        "Cmp. Hotel": 350
    },
    "Pg. de Gràcia": {
        "Ll. Casa": 50,
        "Ll. Hotel": 50,
        "Cmp. Trrny": 80,
        "Cmp. Casa": 525,
        "Cmp. Hotel": 360,
        "Propietari": banca
    }
}

