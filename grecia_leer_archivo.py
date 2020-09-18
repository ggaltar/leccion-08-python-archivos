# Recorrido e impresión de las líneas de un archivo de texto
with open("maravillas_antiguas.csv", "r") as archivo:
    for linea in archivo:
        if (linea.find("Grecia")!= -1):
            print(linea, end='')