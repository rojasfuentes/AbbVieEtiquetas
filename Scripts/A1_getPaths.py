import PySimpleGUI as sg

# Establecer el tema
sg.theme('Reddit')

# Función para crear una nueva sección de carga de documentos
def crear_seccion(indice):
    return [
        [
            sg.Text(f'Remisión de pedido {indice}'), sg.Input(key=f'archivo1_{indice}'), sg.FileBrowse(),
            sg.Text(f'Certificado de A. {indice}'), sg.Input(key=f'archivo2_{indice}'), sg.FileBrowse(),
            sg.Text(f'Pz/Contenedor {indice}'), sg.Input(key=f'pz_{indice}', size=(10, 1))
        ]
    ]

# Layout inicial
layout = [
    [sg.Text('Cargar documentos', key='-HEADER-')],
    [
        sg.Text('Remisión de pedido'), sg.Input(key='archivo1_0'), sg.FileBrowse(),
        sg.Text('Certificado de A.'), sg.Input(key='archivo2_0'), sg.FileBrowse(),
        sg.Text('Pz/Contenedor'), sg.Input(key='pz_0', size=(10, 1))
    ],
    [sg.Column([], key='-SECCIONES-')],
    [sg.Button('+', key='Agregar'), sg.Button('Continuar'), sg.Button('Cancelar', button_color=('white', 'red'))]
]

# Crear ventana
window = sg.Window('Carga de Documentos', layout)

# Contador para secciones dinámicas
indice_seccion = 1

# Listas para almacenar los valores de las secciones
listRemisiones = []
listCertificados = []
listPiezas = []

# Loop de eventos
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == 'Cancelar':
        break

    if event == 'Agregar':
        # Agregar una nueva sección al layout debajo de las secciones existentes
        window.extend_layout(window['-SECCIONES-'], crear_seccion(indice_seccion))
        indice_seccion += 1

    if event == 'Continuar':
        for i in range(indice_seccion):
            archivo1 = values[f'archivo1_{i}']
            archivo2 = values[f'archivo2_{i}']
            pz = values[f'pz_{i}']
            listRemisiones.append(archivo1)
            listCertificados.append(archivo2)
            listPiezas.append(pz)
        
        # Imprimir listas en consola
        print('Remisiones:', listRemisiones)
        print('Certificados:', listCertificados)
        print('Cantidades:', listPiezas)
        
        # Cerrar la ventana
        break

window.close()
