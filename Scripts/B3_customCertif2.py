from B3_firstPages import nuevas_rutas
from google.cloud import documentai_v1 as documentai
import pandas as pd
from tqdm import tqdm

# Lista de archivos a procesar
list_certificados =nuevas_rutas 
                #['C:/Users/JFROJAS/Desktop/Abbvie Etiquetas V2/FirstPages/FirstPage_(BIRMEX) Certificado Venclexta 100mg 1214866.pdf', 
                #   'C:/Users/JFROJAS/Desktop/Abbvie Etiquetas V2/FirstPages/FirstPage_5. CERTIFICADO BOTOX C7994C3.pdf', 
                #   'C:/Users/JFROJAS/Desktop/Abbvie Etiquetas V2/FirstPages/FirstPage_Certificado Humira 1213620.pdf']

# Listas para almacenar la información
llist_fCaducidad = []
list_fFabricacion = []



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
PROCESSOR_ID = "9f12789f1e777d7d"  # Create processor in Cloud Console
MIME_TYPE = "application/pdf"

for file_path in tqdm(list_certificados, desc="Processing files"):
    document = online_process(
        project_id=PROJECT_ID,
        location=LOCATION,
        processor_id=PROCESSOR_ID,
        file_path=file_path,
        mime_type=MIME_TYPE,
        
    )

#print(document.entities)
    # Iterar sobre las entidades del documento y agregar valores a las listas correspondientes
    for entity in document.entities:
        if entity.type_ == "fecha-caducidad":
            llist_fCaducidad.append(entity.mention_text)
        elif entity.type_ == "fecha-fabricacion":
            list_fFabricacion.append(entity.mention_text)
        
# Imprimir las listas en la consola
print("Fecha de caducidad:", llist_fCaducidad)
print("Fecha de fabricación:", list_fFabricacion)



