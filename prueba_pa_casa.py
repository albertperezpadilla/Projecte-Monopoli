#Aqui haremos el monopoly

import principals as pr
import diccionarios as dic
import tablero as tb
import cartas as ct
import uso_general as ug
import principals as pr
import Monopoly as mp

#Trucos
def trucs(color):
    opcions = ["anar a casella o carrer",
               "afegir cases","afegir hotels",
               "seguent jugador",
               "diners jugador", "diners banca"
               ]
    print("Trucs")
    print(", ".join(opcions))
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
    elif opcio == opcions[1] or opcio == opcions[2]:
        posicio = dic.jugadors[color]['posicio']
        for carrer in dic.carrers:
            if dic.carrers[carrer]['posicio'] == posicio:
                nom_carrer = carrer
                break
        if opcio == opcions[1]:
            x = input("Num. Cases: ")
            while not x.isdigit() or not (1 <= int(x) <= 4) or not ug.comprobarCasas(nom_carrer, x):
                if not x.isdigit():
                    print("Introdueix un número")
                elif not (1 <= int(x) <= 4):
                    print("Introdueix un valor entre 1 i 4")
                else:
                    print("El número de casas supera el límit")
                x = input("Num. Cases: ")
            x = int(x)
            dic.carrers[nom_carrer]["Num. Cases"] += x
        else:
            x = input("Num. Hotels: ")
            while not x.isdigit() or not (1 <= int(x) <= 4) or not ug.comprobarHoteles(nom_carrer, x):
                if not x.isdigit():
                    print("Introdueix un número")
                elif not (1 <= int(x) <= 4):
                    print("Introdueix un valor entre 1 i 4")
                else:
                    print("El número d'hotels supera el límit")
                x = input("Num. Hotels: ")
            x = int(x)
            dic.carrers[nom_carrer]["Num. Hotels"] += x
    elif opcio == opcions[3]:
        seguent = input("Seguent jugador: ")
        tmp = mp.colors
        for i in mp.colors:
            if mp.colors[i] == color:
                del tmp[i]
                break
        

print("hola")