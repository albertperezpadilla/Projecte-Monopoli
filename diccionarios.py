#Diccionarios
#Banca
banca = {
    'diners': 500000,
    'carrers' : ['Lauria', 'Roselló', 'Marina', 'C. de cent', 'Muntaner', 'Aribau', 'Sant Joan', 'Aragó', 'Urquinaona', 'Fontana', 'Les Rambles', 'Pl. Catalunya', 'P. Àngel', 'Via Augusta', 'Balmes', 'Pg. de Gràcia']

}
#Jugadores
jugadors = {
    "groc":  {
        'inicial': 'G',
        'diners': 2000,
        'cartes' : [],
        'carrers': [],
        'total casas': 0,
        'total hoteles': 0,
        'posicio': 23,
        'empressonat': False,
        'torns_empressonat': 0,
    },
    "taronja":  {
        'inicial': 'T',
        'diners': 2000,
        'cartes' : [],
        'carrers': [],
        'total casas': 0,
        'total hoteles': 0,
        'posicio': 22,
        'empressonat': False,
        'torns_empressonat': 0,
    },
    "vermell":  {
        'inicial': 'V',
        'diners': 2000,
        'cartes' : [],
        'carrers': [],
        'total casas': 0,
        'total hoteles': 0,
        'posicio': 22,
        'empressonat': False,
        'torns_empressonat': 0,
    },
    "blau": {
        'inicial': 'B',
        'diners': 2000,
        'cartes' : [],
        'carrers': [],
        'total casas': 2,
        'total hoteles': 2,
        'posicio': 22,
        'empressonat': False,
        'torns_empressonat': 0,
    }
}

#Direccionario de direccionarios de los precios de cada calle
carrers = {
    "Lauria": {
        "Ll. Casa": 10,
        "Ll. Hotel": 15,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 200,
        "Cmp. Hotel": 250,
        "Propietari": "banca",
        "Num. Cases": 0,
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
        "Num. Cases": 0,
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
        "Num. Cases": 0,
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
        "Num. Cases": 0,
        "Num. Hoteles": 0,
        'posicio': 5
    },
    "Muntaner": {
        "Ll. Casa": 20,
        "Ll. Hotel": 20,
        "Cmp. Trrny": 60,
        "Cmp. Casa": 300,
        "Cmp. Hotel": 270,
        "Propietari": "banca",
        "Num. Cases": 0,
        "Num. Hoteles": 0,
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
    "S. Joan": {
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
        "Propietari": "banca",
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
        "Num. Cases": 0,
        "Num. Hoteles": 0,
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
        "Num. Cases": 0,
        "Num. Hoteles": 0,
        'posicio': 22
    },
    "Gracia": {
        "Ll. Casa": 50,
        "Ll. Hotel": 50,
        "Cmp. Trrny": 80,
        "Cmp. Casa": 525,
        "Cmp. Hotel": 360,
        "Propietari": "banca",
        "Num. Cases": 0,
        "Num. Hoteles": 0,
        'posicio': 23
    }
}