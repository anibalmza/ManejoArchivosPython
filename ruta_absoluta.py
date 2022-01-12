import os

print("Directorio de trabajo:",os.getcwd())

absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)

print(f"Este es el path del archivo << {path} >>")
print(f"Este es el nombre del archivo << {filename} >>")
print(path+"/saludo.txt")
print()

f = open(path+"/saludo.txt")
for linea in f:
    print(linea,end="")
    # print(linea)
print()
f.close()