import os
path, _ = os.path.split(os.path.abspath(__file__)) # lo simplificamos en una linea

print("\nescribir en el archivo de texto\n")
with open(path+"/archivox.txt","x+") as archivo: #abro el archivo modo write

    archivo.write("\n") # agrego un salto de linea antes de agregar contenido

    archivo.write("Hola mi nombre es Anibal\n") #noten el salto de linea

    archivo.write("mi apellido es Vargas...") #aca no hay salto de linea

    archivo.write("creacion archivo modo exclusivo\n") #aca si, pasa a la tercer linea

    archivo.write("no se creara si ya existe\n")

    edad = 38
    archivo.write(f"mi edad es: {edad}") #la ultima linea no necesita \n

archivo.close()
# pueden probar ejecutando el codigo y viendo como crea el archivo
# despues cambien alguna linea y vean como el archivo se sobreescribe