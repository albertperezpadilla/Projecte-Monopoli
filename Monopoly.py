#Aqui haremos el monopoly

import random

#Variables del comienzo de la partida
banca = {
    'diners': 0,
    'carrers' : ['Lauria', 'Rosselló', 'Marina',' Consell de cent','Muntaner', 'Aribau', 'Sant Joan', 'Aragó','Urquinaona', 'Fontana', 'Les Rambles',' Plaça Catalunya', 'Portal de lÀngel',' Via Augusta', 'Balmes', 'Passeig de Gràcia']
}

jugador_groc =  {
        'color': 'groc',
        'diners': 2000,
        'cartes' : [],
        'carrers': [],
}

jugador_taronja =  {
        'color': 'taronja',
        'diners': 2000,
        'cartes' : [],
        'carrers': [],
}

jugador_vermell =  {
        'color': 'vermell',
        'diners': 2000,
        'cartes' : [],
        'carrers': [],
}

jugador_blau =  {
        'color': 'blau',
        'diners': 2000,
        'cartes' : [],
        'carrers': [],
}

#Direccionario de direccionarios de los precios de cada calle
dic_carrers = {
    "Lauria": {
        "Ll. Casa": 10,
        "Ll. Hotel": 15,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 200,
        "Cmp. Hotel": 250,
        "Propietari": banca,
        "Num. Cases": 0,
        "Num. Hoteles": 0
    },
    "Roselló": {
        "Ll. Casa": 10,
        "Ll. Hotel": 15,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 225,
        "Cmp. Hotel": 255,
        "Propietari": banca,
        "Num. Cases": 0,
        "Num. Hoteles": 0
    },
    "Marina": {
        "Ll. Casa": 15,
        "Ll. Hotel": 15,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 250,
        "Cmp. Hotel": 260,
        "Propietari": banca,
        "Num. Cases": 0,
        "Num. Hoteles": 0
    },
    "C. de cent": {
        "Ll. Casa": 15,
        "Ll. Hotel": 20,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 275,
        "Cmp. Hotel": 265,
        "Propietari": banca,
        "Num. Cases": 0,
        "Num. Hoteles": 0
    },
    "Muntaner": {
        "Ll. Casa": 20,
        "Ll. Hotel": 20,
        "Cmp. Trrny": 60,
        "Cmp. Casa": 300,
        "Cmp. Hotel": 270,
        "Propietari": banca,
        "Num. Cases": 0,
        "Num. Hoteles": 0
    },
    "Aribau": {
        "Ll. Casa": 20,
        "Ll. Hotel": 20,
        "Cmp. Trrny": 60,
        "Cmp. Casa": 325,
        "Cmp. Hotel": 275,
        "Propietari": banca,
        "Num. Cases": 0,
        "Num. Hoteles": 0
    },
    "Sant Joan": {
        "Ll. Casa": 25,
        "Ll. Hotel": 25,
        "Cmp. Trrny": 60,
        "Cmp. Casa": 350,
        "Cmp. Hotel": 280,
        "Propietari": banca,
        "Num. Cases": 0,
        "Num. Hoteles": 0
    },
    "Aragó": {
        "Ll. Casa": 25,
        "Ll. Hotel": 25,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 375,
        "Cmp. Hotel": 285,
        "Propiedatari": banca,
        "Num. Cases": 0,
        "Num. Hoteles": 0
    },
    "Urquinaona": {
        "Ll. Casa": 30,
        "Ll. Hotel": 25,
        "Cmp. Trrny": 70,
        "Cmp. Casa": 400,
        "Cmp. Hotel": 290,
        "Propietari": banca,
        "Num. Cases": 0,
        "Num. Hoteles": 0
    },
    "Fontana": {
        "Ll. Casa": 30,
        "Ll. Hotel": 30,
        "Cmp. Trrny": 70,
        "Cmp. Casa": 425,
        "Cmp. Hotel": 300,
        "Propietari": banca,
        "Num. Cases": 0,
        "Num. Hoteles": 0
    },
    "Les Rambles": {
        "Ll. Casa": 35,
        "Ll. Hotel": 30,
        "Cmp. Trrny": 70,
        "Cmp. Casa": 450,
        "Cmp. Hotel": 310,
        "Propietari": banca,
        "Num. Cases": 0,
        "Num. Hoteles": 0
    },
    "Pl. Catalunya": {
        "Ll. Casa": 35,
        "Ll. Hotel": 30,
        "Cmp. Trrny": 70,
        "Cmp. Casa": 475,
        "Cmp. Hotel": 320,
        "Propietari": banca,
        "Num. Cases": 0,
        "Num. Hoteles": 0
    },
    "P. Àngel": {
        "Ll. Casa": 40,
        "Ll. Hotel": 35,
        "Cmp. Trrny": 80,
        "Cmp. Casa": 500,
        "Cmp. Hotel": 330,
        "Propietari": banca,
        "Num. Cases": 0,
        "Num. Hoteles": 0
    },
    "Via Augusta": {
        "Ll. Casa": 40,
        "Ll. Hotel": 35,
        "Cmp. Trrny": 80,
        "Cmp. Casa": 525,
        "Cmp. Hotel": 250,
        "Propietari": banca,
        "Num. Cases": 0,
        "Num. Hoteles": 0
    },
    "Balmes": {
        "Ll. Casa": 50,
        "Ll. Hotel": 40,
        "Cmp. Trrny": 80,
        "Cmp. Casa": 550,
        "Cmp. Hotel": 350,
        "Propietari": banca,
        "Num. Cases": 0,
        "Num. Hoteles": 0
    },
    "Pg. de Gràcia": {
        "Ll. Casa": 50,
        "Ll. Hotel": 50,
        "Cmp. Trrny": 80,
        "Cmp. Casa": 525,
        "Cmp. Hotel": 360,
        "Propietari": banca,
        "Num. Cases": 0,
        "Num. Hoteles": 0
    }
}

