# Aquí haremos el monopoly
import random
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
    if iniciar.lower() == "si": 
        while True:  
            diners_banca()
            bancarrota = 0
            for color in colors:
                posicio_perdre = dic.jugadors[color]['posicio']
                if posicio_perdre not in [0, 3, 6, 9, 12, 15, 18, 21]:
                    for carrer in dic.carrers:
                        if not dic.carrers[carrer]['posicio'] == posicio_perdre:
                            nom_carrer = carrer
                            break
                    if dic.carrers[nom_carrer]["Propietari"] != color and dic.carrers[nom_carrer]["Propietari"] != "banca":
                        if ug.totalPagar(posicio_perdre) > dic.jugadors[color]['diners'] and dic.jugadors[color]['total casas'] == 0 and dic.jugadors[color]['total hoteles'] == 0:
                            bancarrota += 1
                            tb.afegir_historial()
                            colors.remove(color)
                
                pr.clearScreen()  
                pr.taulellDibuixar() 

                if dic.jugadors[color]['empressonat']:
                    ct.anar_preso(color)
                else:
                    pr.tirar_dados(color)

                ct.casillas_especiales(color)
                pr.taulellDibuixar()              

                ug.fer_opcions(color)
                
      
jugar_partida()
