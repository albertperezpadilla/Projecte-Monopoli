#Aqui pondremos las funciones de uso general
import diccionarios as dic
import tablero as tb
import principals as pr
#Mostrar Preu:

def actualiztar_tauler():
    pr.clearScreen() 
    pr.taulellDibuixar()


def mostarPreu(color):
    pos_jugador = dic.jugadors[color]["posicio"]

    for carrer in dic.carrers:
        pos_carrer = dic.carrers[carrer]["posicio"]
        preu_casa = dic.carrers[carrer]["Cmp. Casa"]
        preu_hotel = dic.carrers[carrer]["Cmp. Hotel"]
        
        if pos_jugador == pos_carrer:
            tb.afegir_historial(f"Jugador: {color} - Preu Casa: {preu_casa}")
            tb.afegir_historial(f"Jugador: {color} - Preu Hotel: {preu_hotel}")

            # Verificar si no se puede edificar
            if pos_jugador in [0, 3, 6, 9, 12, 15, 18, 21]:
                tb.afegir_historial("Aquí no se puede edificar!")

    actualiztar_tauler() 


def comprarTerreny(color):
    pos_jugador = dic.jugadors[color]["posicio"]
    diners_jugador = dic.jugadors[color]["diners"]

    for carrer in dic.carrers:
        pos_carrer = dic.carrers[carrer]["posicio"]
        preu_carrer = dic.carrers[carrer]["Cmp. Trrny"]
        propietari = dic.carrers[carrer]["Propietari"]
        if pos_jugador == pos_carrer and diners_jugador >= preu_carrer and propietari == "banca":
            tb.afegir_historial(f"Jugador: {color} ha comprat {carrer}")
            dic.jugadors[color]["diners"] -= preu_carrer
            dic.banca["diners"] += preu_carrer
            dic.carrers[carrer]["Propietari"] = color
            dic.jugadors[color]["carrers"].append(carrer)
            dic.banca["carrers"].remove(carrer)
            break
            
        elif pos_jugador == pos_carrer and propietari != "banca":
            tb.afegir_historial(f"Aquesta casella ja té propietari: {propietari}.")
        elif pos_jugador in [0, 3, 6, 9, 12, 15, 18, 21]:
            tb.afegir_historial("Aquesta casella no està a la venda.")

    actualiztar_tauler()


def edificarCasa(color):
    pos_jugador = dic.jugadors[color]["posicio"]
    diners_jugador = dic.jugadors[color]["diners"]

    if pos_jugador in [0, 3, 6, 9, 12, 15, 18, 21]:
        tb.afegir_historial("A aquesta casella no es pot edificar.")
        return
    
    # Revisar si el jugador puede edificar en su posición actual
    for carrer in dic.carrers:
        pos_carrer = dic.carrers[carrer]["posicio"]
        preu_casa = dic.carrers[carrer]["Cmp. Casa"]
        propietari = dic.carrers[carrer]["Propietari"]
        
        if pos_jugador == pos_carrer:
            if propietari == color:
                    if comprobarCasas(carrer, 1):
                        if diners_jugador >= preu_casa:
                            tb.afegir_historial(f"{color} ha comprat una casa.")
                            dic.jugadors[color]["diners"] -= preu_casa
                            dic.banca["diners"] += preu_casa
                            dic.carrers[carrer]["Num. Cases"] += 1
                            dic.jugadors[color]["total casas"] += 1
                        else:
                            tb.afegir_historial(f"{color} no té diners per comprar una casa.")
                    else:
                        tb.afegir_historial(f"No pots construir mes cases.")
            else:
                tb.afegir_historial(f"No es teu! Es de: {propietari}.")
                break


    actualiztar_tauler()
                
def edificarHotel(color):
    pos_jugador = dic.jugadors[color]["posicio"]
    diners_jugador = dic.jugadors[color]["diners"]

    if pos_jugador in [0, 3, 6, 9, 12, 15, 18, 21]:
        tb.afegir_historial("A aquesta casella no es pot edificar.")
        return
    
    # Revisar si el jugador puede edificar en su posición actual
    for carrer in dic.carrers:
        pos_carrer = dic.carrers[carrer]["posicio"]
        preu_hotel = dic.carrers[carrer]["Cmp. Hotel"]
        propietari = dic.carrers[carrer]["Propietari"]
        num_cases =dic.carrers[carrer]["Num. Cases"] 
        if pos_jugador == pos_carrer:
            if propietari == color:
                    if comprobarHoteles(carrer, 1):
                        if diners_jugador >= preu_hotel and num_cases >= 2:
                            tb.afegir_historial(f"{color} ha comprat un hotel.")
                            dic.jugadors[color]["diners"] -= preu_hotel
                            dic.banca["diners"] += preu_hotel
                            dic.carrers[carrer]["Num. Hoteles"] += 1
                            dic.jugadors[color]["total hoteles"] += 1
                            dic.carrers[carrer]["Num. Cases"] -= 2
                            dic.jugadors[color]["total casas"] -= 1
                            print(dic.carrers[carrer]["Num. Hoteles"])
                        elif num_cases < 2:
                            tb.afegir_historial(f"Falten cases per un hotel")
                        else:
                            tb.afegir_historial(f"{color} no té diners per comprar un hotel.")
                    else:
                        tb.afegir_historial(f"No pots construir mes hotels.")
            else:
                tb.afegir_historial(f"No es teu! Es de: {propietari}.")
                break


    actualiztar_tauler()

#Alquiler a pagar
def totalPagar(color):
    pos = dic.jugadors[color]['posicio']
    diners = dic.jugadors[color]['diners']
    total_lloguer = 0  # Inicializar el total a pagar
    
    for dades_carrer in dic.carrers.values():
        if dades_carrer['posicio'] == pos:
            propietari = dades_carrer['Propietari']
            if propietari != "banca" and propietari != color:
                num_cases = dades_carrer["Num. Cases"]
                num_hotels = dades_carrer["Num. Hoteles"]
                
                if num_cases == 0 and num_hotels == 0:
                    tb.afegir_historial(f"No hi ha cases ni hotels.")
                else:
                    ll_casas = dades_carrer["Ll. Casa"] * num_cases
                    ll_hotels = dades_carrer["Ll. Hotel"] * num_hotels
                    total_lloguer = ll_casas + ll_hotels

                    # Actualizar dinero solo si hay un alquiler a pagar
                    if diners >= total_lloguer:
                        diners -= total_lloguer
                        dic.jugadors[propietari]['diners'] += total_lloguer
                        tb.afegir_historial(f"{color} paga {total_lloguer} a {propietari}")
                    else:
                        tb.afegir_historial(f"{color} no té diners suficients per pagar {total_lloguer} a {propietari}.")
    
    dic.jugadors[color]['diners'] = diners 
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

#Comprobar numero de casas i hoteles
def comprobarCasas(nom_carrer, x):
    x = int(x)
    if dic.carrers[nom_carrer]["Num. Cases"] + x <= 4:
        return True
    return False

def comprobarHoteles(nom_carrer, x):
    x = int(x)
    if dic.carrers[nom_carrer]["Num. Hoteles"] + x <= 2:
        return True
    return False

def fer_opcions(color):
        while True:
            opcions = pr.opcions_jugador(color)
            print(f"Juga \"{color}\", {opcions}")
            opcio = input("Opció: ")
            if opcio == "trucs":
                pr.trucs(color)
            elif opcio in opcions:
                if dic.jugadors[color]["posicio"] == 12:
                    break
                if opcio == "passar":
                    tb.afegir_historial(f"{color} passa el torn.")
                    break  
                elif opcio == "comprar terreny":
                    comprarTerreny(color)
                elif opcio == "comprar casa":
                    edificarCasa(color)
                    continue  
                elif opcio == "comprar hotel":
                    edificarHotel(color)
                    
                elif opcio == "preus":
                    mostarPreu(color)
            else:
                print("Aquesta opció no esta disponible")