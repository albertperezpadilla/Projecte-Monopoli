#Aqui pondremos las funciones de uso general
import diccionarios as dic
import tablero as tb
import principals as pr
import historial as h
#Mostrar Preu:

def actualiztar_tauler():
    pr.clearScreen() 
    pr.taulellDibuixar()


def mostrarPreu(color):
    pos_jugador = dic.jugadors[color]["posicio"]

    for carrer in dic.carrers:
        pos_carrer = dic.carrers[carrer]["posicio"]
        preu_carrer = dic.carrers[carrer]["Cmp. Trrny"]
        preu_casa = dic.carrers[carrer]["Cmp. Casa"]
        preu_hotel = dic.carrers[carrer]["Cmp. Hotel"]
        propietari = dic.carrers[carrer]['Propietari']
        if pos_jugador == pos_carrer and propietari =="banca":
            h.afegir_historial(f"  Preu {carrer}:{preu_carrer}€")
        elif pos_jugador == pos_carrer and propietari == color:
            h.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" - Preu Casa: {preu_casa}")
            h.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" - Preu Hotel: {preu_hotel}")

            # Verificar si no se puede edificar
            if pos_jugador in [0, 3, 6, 9, 12, 15, 18, 21]:
                h.afegir_historial("  Aqui no es pot edificar!")

    actualiztar_tauler() 


def comprarTerreny(color):
    pos_jugador = dic.jugadors[color]["posicio"]
    diners_jugador = dic.jugadors[color]["diners"]

    for carrer in dic.carrers:
        pos_carrer = dic.carrers[carrer]["posicio"]
        preu_carrer = dic.carrers[carrer]["Cmp. Trrny"]
        propietari = dic.carrers[carrer]["Propietari"]
        if pos_jugador == pos_carrer and int(diners_jugador) >= int(preu_carrer) and propietari == "banca":
            h.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" ha comprat {carrer}")
            print(dic.jugadors[color]["diners"])
            dic.jugadors[color]["diners"] = int(dic.jugadors[color]["diners"]) - preu_carrer


            dic.banca["diners"] += int(preu_carrer)
            dic.carrers[carrer]["Propietari"] = color
            dic.jugadors[color]["carrers"].append(carrer)
            dic.banca["carrers"].remove(carrer)
            if '(Res)' in dic.jugadors[color]['carrers']:
                dic.jugadors[color]['carrers'].remove('(Res)')
            break
            
        elif pos_jugador == pos_carrer and propietari != "banca":
            h.afegir_historial(f"  Aquesta casella ja té propietari: {propietari}.")
        elif pos_jugador in [0, 3, 6, 9, 12, 15, 18, 21]:
            h.afegir_historial("  Aquesta casella no està a la venda.")

    actualiztar_tauler()

def edificarCasa(color):
    pos_jugador = dic.jugadors[color]["posicio"]
    diners_jugador = dic.jugadors[color]["diners"]

    if pos_jugador in [0, 3, 6, 9, 12, 15, 18, 21]:
        h.afegir_historial("  A aquesta casella no es pot edificar.")
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
                            h.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" ha comprat una casa.")
                            dic.jugadors[color]["diners"] -= preu_casa
                            dic.banca["diners"] += preu_casa
                            dic.carrers[carrer]["Num. Cases"] += 1
                            dic.jugadors[color]["total casas"] += 1
                        else:
                            h.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" no té diners per comprar una casa.")
                    else:
                        h.afegir_historial(f"  No pots construir mes cases.")
            else:
                h.afegir_historial(f"  No es teu! Es de: {propietari}.")
                break


    actualiztar_tauler()
                
def edificarHotel(color):
    pos_jugador = dic.jugadors[color]["posicio"]
    diners_jugador = dic.jugadors[color]["diners"]

    if pos_jugador in [0, 3, 6, 9, 12, 15, 18, 21]:
        h.afegir_historial("  A aquesta casella no es pot edificar.")
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
                            h.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" ha comprat un hotel.")
                            dic.jugadors[color]["diners"] -= preu_hotel
                            dic.banca["diners"] += preu_hotel
                            dic.carrers[carrer]["Num. Hoteles"] += 1
                            dic.jugadors[color]["total hoteles"] += 1
                            dic.carrers[carrer]["Num. Cases"] -= 2
                            dic.jugadors[color]["total casas"] -= 1
                            print(dic.carrers[carrer]["Num. Hoteles"])
                        elif num_cases < 2:
                            h.afegir_historial(f"  Falten cases per un hotel")
                        else:
                            h.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" no té diners per comprar un hotel.")
                    else:
                        h.afegir_historial(f"  No pots construir mes hotels.")
            else:
                h.afegir_historial(f"  No es teu! Es de: {propietari}.")
                break


    actualiztar_tauler()

#Alquiler a pagar
def totalPagar(color):
    posicion_actual = dic.jugadors[color]['posicio']
    diners_actuals = int(dic.jugadors[color]['diners'])
    total_lloguer = 0  # Inicializar el total a pagar

    for dades_carrer in dic.carrers.values():
        if dades_carrer['posicio'] == posicion_actual:
            propietari = dades_carrer['Propietari']
            if propietari != "banca" and propietari != color:
                num_cases = dades_carrer["Num. Cases"]
                num_hotels = dades_carrer["Num. Hoteles"]

                if num_cases == 0 and num_hotels == 0:
                    h.afegir_historial("  No hi ha cases ni hotels.")
                else:
                    ll_casas = dades_carrer["Ll. Casa"] * num_cases
                    ll_hotels = dades_carrer["Ll. Hotel"] * num_hotels
                    total_lloguer = ll_casas + ll_hotels

                    # Comprobar si el jugador tiene suficiente dinero
                    if int(total_lloguer) > int(diners_actuals):
                        h.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" no pot pagar a \"{dic.jugadors[propietari]['inicial']}\".")
                    else:
                        # Actualizar el dinero del propietario
                        dic.jugadors[propietari]['diners'] += total_lloguer
                        (diners_actuals) -= int(total_lloguer)  
                        dic.jugadors[color]['diners'] = diners_actuals 
                        h.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" paga {total_lloguer} a \"{dic.jugadors[propietari]['inicial']}\"")
                        
    actualiztar_tauler()
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

    return preu_total  # Retorna el precio total


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

def vendre_banc(color):
    propietats = dic.jugadors[color]['carrers']
    diners_jugador = dic.jugadors[color]['diners']
    propietats_banca = dic.banca['carrers']
    if len(propietats) == 0:
        print(f"  \"{dic.jugadors[color]['inicial']}\" no te propietats")
        verificar_bancarrota(color)
    else:
        for carrer in propietats:
            propietats_banca.append(carrer)
            quantitat = totalVendre(color) * 0.5
            diners_jugador += quantitat
            propietats.remove(carrer)
            dic.carrers[carrer]['Num. Cases'] = 0
            dic.carrers[carrer]['Num. Hoteles'] = 0
            print(dic.carrers[carrer]['Propietari'])
            dic.carrers[carrer]['Propietari'] = "banca"
            print(dic.carrers[carrer]['Propietari'])
        return diners_jugador

def vendre_a_jugador(venedor, nou_propietari):
    import tablero as tb
    propietats = dic.jugadors[venedor]['carrers']
    diners_jugador = dic.jugadors[nou_propietari]['diners']
    propietats_venedor = dic.jugadors[nou_propietari]['carrers']
    print("Propietats:", propietats)
    print("Propietats Venedor:", propietats_venedor)
    if len(propietats) == 0:
        print(f"  \"{dic.jugadors[venedor]['inicial']}\" no te propietats")
        verificar_bancarrota(venedor)
    else:
        for carrer in propietats: 
                propietats_venedor.append(carrer)
                quantitat = totalVendre(venedor) * 0.9
                diners_jugador += quantitat
                propietats.remove(carrer)
                dic.carrers[carrer]['Propietari'] = nou_propietari
                h.afegir_historial(f"{  dic.jugadors[venedor]['inicial']} ha venut tot a {dic.jugadors[nou_propietari]['inicial']}") 
        return diners_jugador

def verificar_bancarrota(color):
        if totalPagar(color) > dic.jugadors[color]['diners'] and dic.jugadors[color]['total casas'] == 0 and dic.jugadors[color]['total hoteles'] == 0:
            h.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" está en bancarrota")
            actualiztar_tauler()
            return True
        else:
            return False



def fer_opcions(color):
        while True:
            opcions = pr.opcions_jugador(color)
            print(f"Juga \"{dic.jugadors[color]['inicial']}\", opcions: {', '.join(opcions)}")

            opcio = input("Opció: ")
            if opcio == "trucs":
                pr.trucs(color)
            elif opcio in opcions:
                if dic.jugadors[color]["posicio"] == 12:
                    break
                if opcio == "passar":
                    h.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" passa el torn.")
                    break  
                elif opcio == "comprar terreny":
                    comprarTerreny(color)
                elif opcio == "comprar casa":
                    edificarCasa(color)
                    continue  
                elif opcio == "comprar hotel":
                    edificarHotel(color)
                elif opcio == "preus":
                    mostrarPreu(color)
                elif opcio == "preu jugador":
                    h.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" guanyará: {totalVendre(color) * 0.9}")
                    actualiztar_tauler()
                elif opcio == "preu banc":
                    h.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" guanyará: {totalVendre(color) * 0.5}")
                    actualiztar_tauler()
                elif opcio == "vendre al banc":
                        if verificar_bancarrota(color):
                            h.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" està en bancarrota")
                            break
                        else:
                            vendre_banc(color)
                tmp = dic.jugadors.copy()
                del tmp[color]
                for jugador in tmp:
                    if opcio == f"vendre a {jugador}":
                        if verificar_bancarrota(color):
                            h.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" està en bancarrota")
                            break
                        else:            
                            if jugador == 'G':
                                vendre_a_jugador(color,"groc")
                                actualiztar_tauler()

                            elif jugador == 'T':
                                vendre_a_jugador(color,"taronja")
                            elif jugador == 'V':
                                vendre_a_jugador(color,"vermell")
                            elif jugador == 'B':
                                vendre_a_jugador(color,"blau")

            else:
                print("Aquesta opció no està disponible")