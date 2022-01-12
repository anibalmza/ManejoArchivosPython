import os

path, _ = os.path.split(os.path.abspath(__file__)) # lo simplificamos en una linea
#=======================================================
print("\nLeyendo lineas con for...\n")
archivo = open(path+"/archivo.txt") #abro el archivo

contador=1
for linea in archivo:    
    print(contador,linea) #muestro el numero de linea y su contenido
    contador+=1 #incremento el contador de lineas en 1

archivo.close()