import os

path, _ = os.path.split(os.path.abspath(__file__)) # lo simplificamos en una linea

# print("\nLeyendo texto con read...\n")
print("\nLeyendo texto con read...\n")
archivo = open(path+"/archivo.txt") #abro el archivo

lineas = archivo.read() #devuelve el texto completo
print(lineas)

archivo.close()