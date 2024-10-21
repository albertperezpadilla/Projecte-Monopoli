#Aqui pondremos las funciones de uso general
import diccionarios as dic

#Alquiler a pagar
def totalPagar(posicio):
    for dades_carrer in dic.carrers.values():
        if dades_carrer['posicio'] == posicio:
            ll_casas = dades_carrer["Ll. Casa"] * dades_carrer["Num. Cases"]
            ll_hotels = dades_carrer["Ll. Hotel"] * dades_carrer["Num. Hoteles"]
            total_lloguer = ll_casas + ll_hotels
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