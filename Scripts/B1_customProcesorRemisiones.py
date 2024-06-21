from A1_getPaths import listRemisiones
from google.cloud import documentai_v1 as documentai
import pandas as pd
from tqdm import tqdm

# Lista de archivos a procesar
#listRemisiones = [
#    'C:/Users/JFROJAS/Desktop/Abbvie Etiquetas/Documents/(BIRMEX) REMISION 50245619.pdf', 
#    'C:/Users/JFROJAS/Desktop/Abbvie Etiquetas/Documents/1. REMISIÓN 50308517.pdf', 
#    'C:/Users/JFROJAS/Desktop/Abbvie Etiquetas/Documents/Remision 50343223.pdf'
#]

# Listas para almacenar la información
list_descripcion = []
list_direccion_destino = []
list_licitacion = []
list_registro_sanitario = []
list_operador_logistico = []
list_estado_destino = []
list_contrato = []
list_direccion_entrega = []
list_denominacion = []
list_lote = []
list_remision = []
list_cantidad = []
list_clave = []
list_almacen = []
list_procedencia = []
list_orden_reposicion = []

def online_process(
    project_id: str,
    location: str,
    processor_id: str,
    file_path: str,
    mime_type: str,
) -> documentai.Document:
    """
    Processes a document using the Document AI Online Processing API.
    """

    opts = {"api_endpoint": f"{location}-documentai.googleapis.com"}

    # Instantiates a client
    documentai_client = documentai.DocumentProcessorServiceClient(client_options=opts)

    # The full resource name of the processor
    resource_name = documentai_client.processor_path(project_id, location, processor_id)

    # Read the file into memory
    with open(file_path, "rb") as file:
        file_content = file.read()

    # Load Binary Data into Document AI RawDocument Object
    raw_document = documentai.RawDocument(content=file_content, mime_type=mime_type)

    # Configure the process request
    request = documentai.ProcessRequest(name=resource_name, raw_document=raw_document)

    # Use the Document AI client to process the sample form
    result = documentai_client.process_document(request=request)

    return result.document

PROJECT_ID = "abbvie-etiquetas"
LOCATION = "us"  # Format is 'us' or 'eu'
PROCESSOR_ID = "d92aa61ee7de8075"  # Create processor in Cloud Console
MIME_TYPE = "application/pdf"

for file_path in tqdm(listRemisiones, desc="Processing files"):
    document = online_process(
        project_id=PROJECT_ID,
        location=LOCATION,
        processor_id=PROCESSOR_ID,
        file_path=file_path,
        mime_type=MIME_TYPE,
    )

    # Iterar sobre las entidades del documento y agregar valores a las listas correspondientes
    for entity in document.entities:
        if entity.type_ == "descripcion":
            list_descripcion.append(entity.mention_text)
        elif entity.type_ == "direccion-destino":
            list_direccion_destino.append(entity.mention_text)
        elif entity.type_ == "licitacion":
            list_licitacion.append(entity.mention_text)
        elif entity.type_ == "registro-sanitario":
            list_registro_sanitario.append(entity.mention_text)
        elif entity.type_ == "operador-logistico":
            list_operador_logistico.append(entity.mention_text)
        elif entity.type_ == "estado-destino":
            list_estado_destino.append(entity.mention_text)
        elif entity.type_ == "contrato":
            list_contrato.append(entity.mention_text)
        elif entity.type_ == "direccion-entrega":
            list_direccion_entrega.append(entity.mention_text)
        elif entity.type_ == "denominacion":
            list_denominacion.append(entity.mention_text)
        elif entity.type_ == "lote":
            list_lote.append(entity.mention_text)
        elif entity.type_ == "remision":
            list_remision.append(entity.mention_text)
        elif entity.type_ == "cantidad":
            list_cantidad.append(entity.mention_text)
        elif entity.type_ == "clave":
            list_clave.append(entity.mention_text)
        elif entity.type_ == "almacen":
            list_almacen.append(entity.mention_text)
        elif entity.type_ == "procedencia":
            list_procedencia.append(entity.mention_text)
        elif entity.type_ == "orden-reposicion":
            list_orden_reposicion.append(entity.mention_text)

# Imprimir las listas en la consola
#print("Descripción:", list_descripcion)
#print("Dirección Destino:", list_direccion_destino)
#print("Licitación:", list_licitacion)
#print("Registro Sanitario:", list_registro_sanitario)
#print("Operador Logístico:", list_operador_logistico)
#print("Estado Destino:", list_estado_destino)
#print("Contrato:", list_contrato)
#print("Dirección Entrega:", list_direccion_entrega)
#print("Denominación:", list_denominacion)
#print("Lote:", list_lote)
#print("Remisión:", list_remision)
#print("Cantidad:", list_cantidad)
#print("Clave:", list_clave)
#print("Almacen:", list_almacen)
#print("Procedencia:", list_procedencia)
#print("Orden Reposición:", list_orden_reposicion)
