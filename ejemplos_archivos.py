import os.path

dias = ["lunes", "martes", "miercoles    ", "  jueves ", "viernes", "sabado", "domingo"]
nombre_archivo = "/home/viky/kk"


if os.path.exists(nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        for dia in dias:
            archivo.write(dia + "\n")


try:
    with open(nombre_archivo, "r") as archivo:
        linea = "kk"
        while linea:
            linea = archivo.readline().strip()
            if linea != "miercoles":
                print (linea)
except FileNotFoundError:
    print("Cuidado, el archivo no existe")