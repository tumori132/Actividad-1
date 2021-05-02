import PySimpleGUI as sg
import json
import csv
import Window

def prom(datos):
    """
        prom saca el promedio de capacidad de la lista con
        los 10 estadios mas grandes de la MLS
    """
    return sum(int(linea['stadium_capacity']) for linea in datos)/ float(len(datos))

def guardar_archivo(ruta,datos):
    """
        Crea el archivo en la ruta que recibe y la lista 
        dentro  
    """
    with open (ruta,"w",encoding="utf8")as file:
        json.dump(datos,file,indent=4,ensure_ascii=False)

def abrir_archivo(ruta,clave):
    """
        Abre el archivo con los datos y hace una lista con los
        10 diccionarios que mas tengan en el campo clave
    """
    arch = open(ruta,'r')
    data = list(csv.DictReader(arch))
    lista = (sorted(data, key= lambda data: float(data[clave]), reverse= True)[:10])
    return lista

def start():
    """ comienzo la window1 con el loop y cuando termina se cierra """
    window1 = loop()
    try:
        window1.close()
    except:
        pass

def loop ():
    """ Loop de el programa , solo va a terminar si
        se apreta el boton salir
    """
    window1 = Window.build()
    while True:
        event, values = window1.read()

        if event == '-SALIR-':
            break

        if event == 'Salir':
            window1.close()
            window1 = Window.build()

        if event == '-OPCION1-':
            sg.popup('Entraste a Alcohol en el mundo','A continuacion veras los 10 paises que consumen mas alcohol','MENSAJE: el consumo total per capita es en litros total de alcohol')
            datos = abrir_archivo('./drinks.csv','total_litres_of_pure_alcohol')
            guardar_archivo('./listaAlcohol.json',datos)
            window1.close()
            window1 = Window.build1(datos)

        if event == '-OPCION2-':
            sg.popup('Entraste a estadios de la MLS','A continuacion los 10 estadios mas grandes de la MLS')
            datos = abrir_archivo('./mls.csv','stadium_capacity')
            promedio = prom(datos)
            guardar_archivo('./listaMLS.json',datos)
            window1.close()
            window1 = Window.build2(datos,promedio)