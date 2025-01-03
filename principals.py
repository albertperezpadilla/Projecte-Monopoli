#Aqui pondremos las funciones principales
import tablero as tb
import diccionarios as dic
import cartas as ct
import uso_general as ug
import os,copy
import historial as h
colors_modificats = False
ordenats = False
icolor = 0
isiguiente = 0
siguiente = ""

def clearScreen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def obtenirCartes(color):
    cartes = dic.jugadors[color]['cartes'] 
    if len(cartes) == 0:
        cartes.append("(Res)")
        return cartes
    else:
        return cartes
def obtenirCarrers(color):
    carrer = dic.jugadors[color]['carrers']
    if len(carrer) == 0:
        return ["(Res)"]
    if "(Res)" in carrer:
        carrer.remove("(Res)")
    
    return carrer


def tirar_dados(color):
    #dau1 = random.randint(1,6)
    #dau2 = random.randint(1,6)'''
    dau1 = 2
    dau2 = 0
    suma = dau1 + dau2
    dic.jugadors[color]['posicio'] += suma 
    h.afegir_historial(f"> Juga \"{dic.jugadors[color]['inicial']}\", ha sortit {dau1} i {dau2}")



def taulellDibuixar():
    t = []
    casa = []
    hotel = []
    for i in range(0, 24):
        t.append("")
        casa.append("")
        hotel.append("")  # Casillas vacías 
    
    global colors
    colors = tb.ordre_jugadors()
    global ordenats
    for color in colors:
        inicial = dic.jugadors[color]['inicial']
        posicio = dic.jugadors[color]['posicio']
        print(f"Jugador: {color}, Posición: {posicio}")  
        
        # Si la posición es mayor a 23, reiniciamos la posición al rango 0-23
        if posicio > 23:
            dic.jugadors[color]['posicio'] = posicio % 24
            posicio = dic.jugadors[color]['posicio']
            print(f"Jugador {color} ha dado la vuelta, nueva posición: {posicio}")
        
        t[posicio] += inicial  # Añadimos el jugador en la casilla correspondiente
        
        for carrer in dic.carrers:
            if posicio == dic.carrers[carrer]['posicio']:
                print(carrer)
        
        # Verificamos si el jugador está en la casilla 0 (la salida)



    for carrer in dic.carrers:
        num_casa = dic.carrers[carrer]['Num. Cases']
        num_hotels = dic.carrers[carrer]['Num. Hoteles']
        posicio_carrer = dic.carrers[carrer]['posicio'] # posicion calle
        if num_hotels == 0 and num_casa > 0:
            casa[posicio_carrer] = "--" + str(num_casa) + "C" 
        elif num_casa > 0 and num_hotels > 0:
            casa[posicio_carrer] = str(num_hotels) + "H" + (str(num_casa)) + "C"
        elif num_casa == 0 and num_hotels > 0:
            casa[posicio_carrer] = str(num_hotels) + "H" + "--"
        else:
            casa[posicio_carrer] = "----"

        #HOTELES CASAS LADOS:
        if posicio_carrer in [7, 8, 10, 11, 19, 20, 22, 23]:
            if num_casa > 0:
                casa[posicio_carrer] = str(num_casa) + "C"
            else:
                casa[posicio_carrer] = " |"
            
            if num_hotels > 0:
                hotel[posicio_carrer] = str(num_hotels) + "H"
            else:
                hotel[posicio_carrer] = " |"

    # Ajuste de espacios para los jugadores
    for i in range(len(t)):
        t[i] = t[i].ljust(6)
    log = h.dibuixa_historial() 
    print(f"""
                +--------+----{casa[13]}+----{casa[14]}+--------+----{casa[16]}+---{casa[17]}+---------+ Banca:
                |Parking |Urquinao|Fontana |Sort    |Rambles |Pl.Cat  |Anr pró | Diners: {dic.banca['diners']}
                |{t[12]}  |{t[13]}  |{t[14]}  |{t[15]}  |{t[16]}  |{t[17]}  |{t[18]}  |
                +--------+--------+--------+--------+--------+--------+--------+ Jugador {colors[0].capitalize()}: 
                |Aragó  {casa[11]}{log[0]}   | Angel {casa[19]} Carrers: {(", ").join(obtenirCarrers(colors[0]))}
                |{t[11]} {hotel[11]}{log[1]}   |{t[19]} {hotel[19]} Diners: {dic.jugadors[colors[0]]['diners']}  
                +--------+{log[2]}   +--------+ Especial: {(", ").join(obtenirCartes(colors[0]))}          
                |S.Joan {casa[10]}{log[3]}   |Augusta{casa[20]} 
                |{t[10]} {hotel[10]}{log[4]}   |{t[20]} {hotel[20]} Jugador {colors[1].capitalize()}:
                +--------+{log[5]}   +--------+ Carrers: {(", ").join(obtenirCarrers(colors[1]))}
                |Caixa   |{log[6]}   |Caixa   | Diners: {dic.jugadors[colors[1]]['diners']}
                |{t[9]}  |{log[7]}   |{t[21]}  | Especial: {(", ").join(obtenirCartes(colors[1]))} 
                +--------+{log[8]}   +--------+ 
                |Aribau {casa[8]}{log[9]}   |Balmes {casa[22]} Jugador {colors[2].capitalize()}: 
                |{t[8]} {hotel[8]}{log[10]}   |{t[22]} {hotel[22]} Carrers: {(", ").join(obtenirCarrers(colors[2]))}
                +--------+{log[11]}   +--------+ Diners: {dic.jugadors[colors[2]]['diners']}
                |Muntan {casa[7]}{log[12]}   |Gracia {casa[23]} Especial: {(", ").join(obtenirCartes(colors[2]))}
                |{t[7]} {hotel[7]}{log[13]}   |{t[23]} {hotel[23]} 
                +--------+----{casa[5]}+----{casa[4]}+--------+----{casa[2]}+----{casa[1]}+--------+ Jugador {colors[3].capitalize()}:
                |{t[6]}  |{t[5]}  |{t[4]}  |{t[3]}  |{t[2]}  |{t[1]}  |{t[0]}  | Carrers: {(", ").join(obtenirCarrers(colors[3]))}
                |Presó   |Consell |Marina  |Sort    |Rosell  |Lauria  |Sortida | Diners: {dic.jugadors[colors[3]]['diners']}
                +--------+--------+--------+--------+--------+--------+--------+ Especial: {(", ").join(obtenirCartes(colors[3]))}
    """)



#Opciones del jugador
#funcion para saber comprobar si una calle tiene propietario o no
def opcions_jugador(color):
    posicio = dic.jugadors[color]['posicio']
    opcions = ["passar"]
    
    if posicio in [0, 3, 6, 9, 12, 15, 18, 21]:
        return opcions

    for carrer in dic.carrers:
        if dic.carrers[carrer]['posicio'] == posicio:
            nom_carrer = carrer
            break
    if posicio != 12:
        if posicio not in [0, 3, 6, 9, 15, 18, 21]:
            if dic.carrers[nom_carrer]["Propietari"] == "banca":
                opcions.append("comprar terreny")
                opcions.append("preus")
            elif dic.carrers[nom_carrer]["Propietari"] == color:
                if dic.carrers[nom_carrer]["Num. Cases"] < 4:
                    opcions.append("comprar casa")
                if dic.carrers[nom_carrer]["Num. Hoteles"] < 2:
                    opcions.append("comprar hotel")
                opcions.append("preus")
            else:
                if int(ug.totalPagar(color)) > int(dic.jugadors[color]['diners']):
                    opcions.append("preu jugador")
                    opcions.append("preu banc")
                    opcions.append("vendre al banc")
                    tmp = dic.jugadors.copy()
                    del tmp[color]
                    for jugador in tmp:
                        if int(tmp[jugador]['diners']) >= int(ug.totalVendre(color)) * 0.9:
                            opcions.append(f"vendre a {tmp[jugador]['inicial']}")
        return opcions
    
    

#Trucos
def trucs(color):
    opcions = ["anar a casella o carrer",
               "afegir cases", "afegir hotels",
               "seguent jugador",
               "diners jugador", "diners banca",
               "sortir"
               ]
    ug.actualiztar_tauler()
    print("Trucs:")
    print("opcions: ",", ".join(opcions))
    opcio = input("Opcio: ")
    while opcio not in opcions:
        print("Opció incorrecte")
        opcio = input("Opcio: ").lower()
    if opcio == opcions[0]:  
        ug.actualiztar_tauler()
        print("Digues el nom del carrer al que vols anar:")
        nom_carrer = input("Anar a carrer: ")  
        if nom_carrer in dic.carrers:  
            posicio = dic.carrers[nom_carrer]['posicio'] 
            dic.jugadors[color]['posicio'] = posicio  
            ug.actualiztar_tauler()
        elif nom_carrer.lower() == "presó":
            dic.jugadors[color]['posicio'] = 6
            ct.anar_preso(color)
        elif nom_carrer.lower() == "parking":
            dic.jugadors[color]['posicio'] = 12
        elif nom_carrer.lower() == "sort":
            suerte = input("Selecciona una de las dos casellas: ")
            while int(suerte) not in [1,2]:
                print("Opció incorrecte, escriu un numero de l'1 al 2")
                suerte = input("Selecciona una de las dos casellas: ")
            if int(suerte) == 1:
                dic.jugadors[color]['posicio'] = 3
                ct.sort(color)
            elif int(suerte) == 2:
                dic.jugadors[color]['posicio'] = 15
                ct.sort(color)
        elif nom_carrer.lower() == "caixa":
            caja = input("Selecciona una de las dos casellas: ")
            while int(caja) not in [1,2]:
                print("Opció incorrecte, escriu un numero de l'1 al 2")
                suerte = input("Selecciona una de las dos casellas: ")
            if int(caja) == 1:
                dic.jugadors[color]['posicio'] = 9
                ct.caixa(color)
            elif int(caja) == 2:
                dic.jugadors[color]['posicio'] = 21
                ct.caixa(color)
        else:
            print(f"El carrer '{nom_carrer}' no existeix.")  
        ug.actualiztar_tauler()

    elif opcio == opcions[1] or opcio == opcions[2]:
        ug.actualiztar_tauler()
        posicio = dic.jugadors[color]['posicio']
        if posicio not in [0, 3, 6, 9, 12, 15, 18, 21]:
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
                        print("El número de cases supera el límit")
                    x = input("Num. Cases: ")
                x = int(x)
                dic.carrers[nom_carrer]["Num. Cases"] += x
                ug.actualiztar_tauler()  

            else:
                x = input("Num. Hoteles: ")
                while not x.isdigit() or not (1 <= int(x) <= 2) or not ug.comprobarHoteles(nom_carrer, x):
                    if not x.isdigit():
                        print("Introdueix un número")
                    elif not (1 <= int(x) <= 2):
                        print("Introdueix un valor entre 1 i 2")
                    else:
                        print("El número d'hotels supera el límit")
                    x = input("Num. Hoteles: ")
                x = int(x)
                dic.carrers[nom_carrer]["Num. Hoteles"] += x
                ug.actualiztar_tauler() 
        else:
            print("No pots contriur en una casella especial")

    elif opcio == opcions[3]:
        global icolor, isiguiente, colors_modificats, siguiente
        siguiente = input("Color: ").lower()
        if siguiente in colors:
                isiguiente = colors.index(siguiente)
                del colors[isiguiente]
                icolor = colors.index(color)
                colors.insert(icolor + 1, siguiente)
                colors_modificats = True
        else:
            print(f"El color no existeix")

    elif opcio == opcions[4]:
        jugador = input("Jugador: ").lower()
        while not jugador in colors:
            print("Jugador incorrecte")
            jugador = input("Jugador: ").lower()
        diners = input("Diners: ")
        while not diners.isdigit():
            print("Introdueix un número")
            diners = input("Diners: ")
        dic.jugadors[jugador]['diners'] = diners
        ug.actualiztar_tauler()  

    elif opcio == opcions[5]:
        diners = input("Diners: ")
        while not diners.isdigit():
            print("Introdueix un número")
            diners = input("Diners: ")
        dic.banca['diners'] = diners
        ug.actualiztar_tauler()  

    elif opcio == opcions[6]:
        ug.actualiztar_tauler()  
        return
