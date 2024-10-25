historial = []
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