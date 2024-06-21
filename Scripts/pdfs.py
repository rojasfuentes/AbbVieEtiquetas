import os
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.errors import PdfReadError
from tkinter import Tk, filedialog

def seleccionar_carpeta():
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter
    carpeta = filedialog.askdirectory(title="Selecciona una carpeta con archivos PDF")
    return carpeta

def procesar_pdfs(carpeta_entrada, carpeta_salida):
    # Crear la carpeta de salida si no existe
    os.makedirs(carpeta_salida, exist_ok=True)

    # Obtener la lista de archivos PDF en la carpeta seleccionada
    archivos_pdf = [f for f in os.listdir(carpeta_entrada) if f.endswith('.pdf')]

    # Nueva lista para almacenar las rutas de los nuevos archivos PDF
    nuevas_rutas = []

    for pdf_file in archivos_pdf:
        pdf_path = os.path.join(carpeta_entrada, pdf_file)
        try:
            # Leer el archivo PDF
            reader = PdfReader(pdf_path)
            
            # Verificar si el PDF tiene al menos una página
            if len(reader.pages) > 0:
                # Crear un nuevo archivo PDF con la primera página
                writer = PdfWriter()
                writer.add_page(reader.pages[0])
                
                # Crear la ruta del nuevo archivo
                new_pdf_path = os.path.join(carpeta_salida, f"FirstPage_{pdf_file}")
                
                # Guardar el nuevo archivo PDF
                with open(new_pdf_path, 'wb') as new_pdf_file:
                    writer.write(new_pdf_file)
                
                # Añadir la ruta del nuevo archivo a la lista
                nuevas_rutas.append(new_pdf_path)
            else:
                print(f"El archivo {pdf_path} no tiene páginas.")
        
        except PdfReadError as e:
            print(f"Error al leer el archivo {pdf_path}: {e}")
        except Exception as e:
            print(f"Se produjo un error con el archivo {pdf_path}: {e}")

    return nuevas_rutas

if __name__ == "__main__":
    # Seleccionar carpeta de entrada
    carpeta_entrada = seleccionar_carpeta()
    if not carpeta_entrada:
        print("No se seleccionó ninguna carpeta.")
    else:
        # Definir la carpeta de salida
        carpeta_salida = os.path.join(carpeta_entrada, 'FirstPages')
        
        # Procesar los PDFs
        nuevas_rutas = procesar_pdfs(carpeta_entrada, carpeta_salida)
        
        # Imprimir la lista de nuevas rutas
        print("Nuevos archivos PDF creados en las siguientes rutas:")
        for ruta in nuevas_rutas:
            print(ruta)
