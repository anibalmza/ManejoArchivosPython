import os

path, _ = os.path.split(os.path.abspath(__file__)) # lo simplificamos en una linea

print("\nLeyendo lineas con readlines...\n")
archivo = open(path+"/archivo.txt") #abro el archivo

lineas = archivo.readlines()    #devuelve una lista
print(lineas)

archivo.close()