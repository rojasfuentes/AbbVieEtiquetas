from A1_getPaths import listCertificados
import os
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.errors import PdfReadError

# Lista de rutas de archivos PDF
#listCertificados = [
#    'C:/Users/JFROJAS/Desktop/Abbvie Etiquetas/Documents/(BIRMEX) Certificado Venclexta 100mg 1214866.pdf',
#    'C:/Users/JFROJAS/Desktop/Abbvie Etiquetas/Documents/5. CERTIFICADO BOTOX C7994C3.pdf',
#    'C:/Users/JFROJAS/Desktop/Abbvie Etiquetas/Documents/Certificado Humira 1213620.pdf'
#]

# Ruta fija donde se guardarán los nuevos archivos PDF
output_folder = 'C:/Users/JFROJAS/Desktop/Abbvie Etiquetas V2/FirstPages/'

# Crear la carpeta de salida si no existe
os.makedirs(output_folder, exist_ok=True)

# Nueva lista para almacenar las rutas de los nuevos archivos PDF
nuevas_rutas = []

for pdf_path in listCertificados:
    try:
        # Leer el archivo PDF
        reader = PdfReader(pdf_path)
        
        # Verificar si el PDF tiene al menos una página
        if len(reader.pages) > 0:
            # Crear un nuevo archivo PDF con la primera página
            writer = PdfWriter()
            writer.add_page(reader.pages[0])
            
            # Crear la ruta del nuevo archivo
            base_name = os.path.basename(pdf_path)
            new_pdf_path = os.path.join(output_folder, f"FirstPage_{base_name}")
            
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

# Imprimir la lista de nuevas rutas
print(nuevas_rutas)
