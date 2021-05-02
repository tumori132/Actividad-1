import PySimpleGUI as sg
def build():
    """
        Build crea la ventana, en donde habra 3 botones
        solo se puede salir si se aprieta el boton salir
    """
    sg.theme("DarkBlack")
    layout = [[sg.Text(' '), ],
              [sg.Button(button_text='Alcohol en el mundo',size=(70,3),pad=(100,15),key='-OPCION1-')], 
              [sg.Button(button_text='Estadios MLS',size=(70,3),pad=(100,0),key='-OPCION2-')],
              [sg.Text(' '), ],
              [sg.Button('Salir',size=(70,3),pad=(100,2),key='-SALIR-')]
              ]

    window = sg.Window('Menu de inicio', layout, size=(400,300),no_titlebar=True)
    return window

def build1(lista):
    """
        Build de la ventana opcion 1 donde se imprimira
        toda la info sobre el alcohol en el mundo
    """
    sg.theme("DarkBlack")
    layout = [[sg.Text(' ')]
                ]
    for linea in lista:
        layout +=[[sg.Text('Pais: '+linea['country']),sg.Text('Consumo Total: '+linea['total_litres_of_pure_alcohol'])]
            ]
    layout += [[sg.Button('Salir',size=(40,3),pad=(200,10))]]
    window = sg.Window('Paises Consumidores', layout, size=(600,400),no_titlebar=True)
    return window

def build2(lista):
    """
        Build de la ventana opcion 2 donde se imprimira
        toda la info sobre los estadios de la mls
    """
    layout = [[sg.Text(' ')]
                ]
    for linea in lista:
        layout +=[[sg.Text('Equipo: '+linea['ï»¿team']),sg.Text('Nombre: '+linea['stadium']),sg.Text('   Capacidad del estadio: '+linea['stadium_capacity'])]
            ]
    layout += [[sg.Button('Salir',size=(40,3),pad=(200,10))]]
    window = sg.Window('Lista de Estadios MLS', layout, size=(600,400),no_titlebar=True)
    return window