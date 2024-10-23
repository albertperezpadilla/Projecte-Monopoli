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

def comprobar_bancarrota():
    bancarrota = 0
    for jugador in dic.jugadors:
        if dic.jugadors[jugador]["diners"] <= 0:
            bancarrota += 1
    return bancarrota
#Hay que cambiar el bucle para que funcione con las deudas y no cuando sea 0
def jugar_partida():
    colors = tb.ordre_jugadors() 
    pr.taulellDibuixar()  
    iniciar = input("Començar? Si/No: ") 
    if iniciar.lower() == "si": 
        while True:  
            diners_banca()
            for color in colors:
                if comprobar_bancarrota() == 3:
                    print(f"El jugador {color} ha guanyat!")
                    return  
                
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
