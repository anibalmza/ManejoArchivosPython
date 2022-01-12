import os

path, _ = os.path.split(os.path.abspath(__file__)) # lo simplificamos en una linea
#=======================================================
print("\nLeyendo lineas con while...\n") #\n")

archivo = open(path+"/archivo.txt") #abro el archivo

linea = archivo.readline() #leo la primera linea
contador=1
while linea != '':
    print(contador,linea) #muestro el numero de linea y su contenido
    linea = archivo.readline() #leo la siguiente linea
    contador+=1 #incremento el numero de linea

archivo.close()