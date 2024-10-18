historial = ['Han tret 2', 'Comprat Parking', 'AAA', '20900000000000000000000000000000000000000']

def afegir_historial(accio):
    historial.append(accio)
    if len(historial) > 14:
        historial.pop(0)

def dibuixa_historial():
    global historial
    historial_bien = []
    
    # mirar que no se pase de 14
    for i in range(14):
        if i < len(historial):
            comanda = historial[i]
            llarg = len(comanda)
            espacios = 41 - llarg
            historial_bien.append(comanda + (' ' * espacios))
        else:
            historial_bien.append(' ' * 41)

    return historial_bien

def taulellDibuixar():
    log = dibuixa_historial() 
    
    print(f"""
            +--------+--------+--------+--------+--------+--------+--------+
            |Parking |Urqinoa |Fontan  |Sort    |Rambles |Pl.Cat  |Anr pró |
            |        |        |        |        |        |        |        |
            +--------+--------+--------+--------+--------+--------+--------+
            |Aragó   |> {log[0]} | Angel  |
            |        |{log[1]}   |        |
            +--------+{log[2]}   +--------+
            |S.Joan  |{log[3]}   |Augusta |
            |        |> {log[4]} |        |
            +--------+ {log[5]}  +--------+
            |Caixa   |{log[6]}   |Caixa   |
            |        |{log[7]}   |        |
            +--------+> {log[8]} +--------+
            |Aribau  |{log[9]}   |Balmes  |
            |        |{log[10]}   |        |
            +--------+> {log[11]} +--------+
            |Muntan  |{log[12]}   |Gracia  |
            |        |{log[13]}   |        |
            +--------+--------+--------+--------+--------+--------+--------+
            |        |        |        |        |        |        |        |
            |Presó   |Consell |Marina  |Sort    |Rosell  |Lauria  |Sortida |
            +--------+--------+--------+--------+--------+--------+--------+
    """)

taulellDibuixar()
