# Aquí haremos el monopoly
import copy
import diccionarios as dic
import tablero as tb
import cartas as ct
import uso_general as ug
import principals as pr

def diners_banca():
    banca = dic.banca["diners"]
    if banca < 500000:
        banca += 1000000
    ug.actualiztar_tauler() 

#Hay que cambiar el bucle para que funcione con las deudas y no cuando sea 0
def jugar_partida():
    colors = tb.ordre_jugadors()
    pr.taulellDibuixar()  
    iniciar = input("Començar? Si/No: ")
    bancarrota = 0
    if iniciar.lower() == "si": 
        while True:  
            diners_banca()
            if pr.colors_modificats:
                del colors[pr.icolor + 1]
                colors.insert(pr.isiguiente, pr.siguiente)
                pr.colors_modificats = False
            for color in colors:
                pr.clearScreen()  
                pr.taulellDibuixar() 

                if dic.jugadors[color]['empressonat']:
                    ct.anar_preso(color)
                else:
                    pr.tirar_dados(color)
                    if dic.jugadors[color]["posicio"] == 6:
                        ct.anar_preso(color)
                    else:
                        posicio_perdre = dic.jugadors[color]['posicio']
                        if posicio_perdre not in [0, 3, 6, 9, 12, 15, 18, 21]:
                            for carrer in dic.carrers:
                                if not dic.carrers[carrer]['posicio'] == posicio_perdre:
                                    nom_carrer = carrer
                                    break
                            if dic.carrers[nom_carrer]["Propietari"] != color and dic.carrers[nom_carrer]["Propietari"] != "banca":
                                if ug.totalPagar(color) > dic.jugadors[color]['diners'] and dic.jugadors[color]['total casas'] == 0 and dic.jugadors[color]['total hoteles'] == 0:
                                    bancarrota += 1
                                    tb.afegir_historial(f"  \"{dic.jugadors[color]['inicial']}\" está en bancarrota")
                                    colors.remove(color)
                        ct.casillas_especiales(color)
                        ug.totalPagar(color)
                        pr.taulellDibuixar()              
                        ug.fer_opcions(color)
                
      
jugar_partida()
