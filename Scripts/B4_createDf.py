from B1_customProcesorRemisiones import list_descripcion, list_direccion_destino, list_licitacion, list_registro_sanitario, list_operador_logistico, list_estado_destino, list_contrato, list_direccion_entrega, list_denominacion, list_lote, list_remision, list_clave, list_procedencia, list_orden_reposicion, list_almacen
from B2_cantidades import resultadosCant
from B3_customCertif2 import llist_fCaducidad, list_fFabricacion
import pandas as pd

# Se asume que las listas y diccionarios necesarios ya han sido importados o definidos previamente
list_descripcion2 = []

for descripcion in list_descripcion:
    partes = descripcion.split(',',1)
    if len(partes) > 1:
        list_descripcion2.append(partes[1].strip())
    else:
        list_descripcion2.append("")
# Diccionario de productos con información adicional
productos = {
    "010 000 4420 00 00": {
        "Codigo de barras": "7501201400581",
        "Leyenda de temperatura": "Conservese a no mas de 25° C"
    },
    "010 000 5666 00 00": {
        "Codigo de barras": "7501201405043",
        "Leyenda de temperatura": "Conservese de 2° a 8° C"
    },
    "010 000 6119 00 00": {
        "Codigo de barras": "7501201401533",
        "Leyenda de temperatura": "Conservese entre 15° C y 30° C"
    },
    "010 000 1101 00 00": {
        "Codigo de barras": "8054083016467",
        "Leyenda de temperatura": "Conservese a no mas de 25° C"
    },
    "010 000 5097 00 00": {
        "Codigo de barras": "8054083005140",
        "Leyenda de temperatura": "Conservese de 2° a 8° C"
    },
    "010 000 1100 00 00": {
        "Codigo de barras": "8054083019215",
        "Leyenda de temperatura": "Conservese a no mas de 30° C"
    },
    "010 000 6164 00 00": {
        "Codigo de barras": "8054083016054",
        "Leyenda de temperatura": "Conservese a no mas de 30° C"
    },
    "010 000 4512 03 00": {
        "Codigo de barras": "8054083020518",
        "Leyenda de temperatura": "Conservese de 2° a 8° C"
    },
    "010 000 6226 00 00": {
        "Codigo de barras": "8054083020136",
        "Leyenda de temperatura": "Conservese a no mas de 30° C"
    }
}

# Listas de ejemplo
cantidades = resultadosCant

# Crear y almacenar dataframes en un diccionario
dataframes = {}
for i in range(len(list_operador_logistico)):
    df_name = f"df{i+1}"
    num_rows = len(cantidades[i])
    
    data = {
        'OPE_LOG': [list_operador_logistico[i]] * num_rows,
        'DIRTEXTUL': [list_direccion_entrega[i]] * num_rows,
        'LICITACION': [list_licitacion[i]] * num_rows,
        'CONTRATO': [list_contrato[i]] * num_rows,
        'CLAVE': [list_clave[i]] * num_rows,
        'DENOMINACI': [list_denominacion[i]] * num_rows,
        'DESCRIPCIO': [list_descripcion2[i]] * num_rows,
        'EDODES': [list_estado_destino[i]] * num_rows,
        'ORDREP': [list_orden_reposicion[i]] * num_rows,
        'REMISION': [list_remision[i]] * num_rows,
        'list_almacen': [list_almacen[i]] * num_rows,
        'DIRDESTFIN': [list_direccion_destino[i]] * num_rows,
        'CANTIDAD': cantidades[i],
        'FAB': [list_fFabricacion[i]] * num_rows,
        'CAD': [llist_fCaducidad[i]] * num_rows,
        'LOTE': [list_lote[i]] * num_rows,
        'BARRAS': [productos[list_clave[i]]["Codigo de barras"]] * num_rows,
        'SANITARIO': [list_registro_sanitario[i]] * num_rows,
        'PROCED': [list_procedencia[i]] * num_rows,
        'CONSERVESE': [productos[list_clave[i]]["Leyenda de temperatura"]] * num_rows,
        'DISTRIBUID': ["AbbVie Farmaceuticos S.A. de C.V. Sub Indice 51 Avenida Industria Automotriz, No 128, Lote C, Edificio A-2, Parque Industrial El Coecillo, Toluca, C.P. 50246, Estado de México"] * num_rows
    }
    
    dataframes[df_name] = pd.DataFrame(data)

# Guardar cada dataframe en un archivo Excel diferente
for name, df in dataframes.items():
    # Obtener el índice del diccionario para usar en list_remision
    idx = int(name[2:]) - 1  # Convertir 'df1' a 0, 'df2' a 1, etc.
    nombre_remision = list_remision[idx]
    df.to_excel(f"{nombre_remision}.xlsx", index=False)

print("Todos los dataframes han sido guardados en archivos Excel.")
