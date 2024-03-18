import os
#import shutil
import pandas as pd
#from openpyxl import workbook
#from openpyxl.utils.dataframe import dataframe_to_rows

def procesar_archivos(archivos_seleccionados_text):
    
    proyecto_path = os.path.dirname(os.path.abspath(__file__))

    documentos_generados_path = os.path.join(proyecto_path, "documentos_generados")

    if not os.path.exists(documentos_generados_path):
        os.makedirs(documentos_generados_path)

    archivos_seleccionados = archivos_seleccionados_text.split(",")

    # Buscar el nombre adecuado para el archivo Excel
    numero_archivo = 1

    excel_filename = os.path.join(documentos_generados_path, f"resultados_{numero_archivo}.xlsx")
    while os.path.exists(excel_filename):
        numero_archivo += 1
        excel_filename = os.path.join(documentos_generados_path, f"resultados_{numero_archivo}.xlsx")

    with pd.ExcelWriter(excel_filename, engine='xlsxwriter') as writer:
        df_resultados = pd.DataFrame()

        for archivo in archivos_seleccionados:
            if archivo:

                df = pd.read_csv(archivo)
                if not df.empty:

                    df.rename(columns={'Fecha de envío': 'Fecha'}, inplace=True)

                    columna_a_eliminar = "Doy mi consentimiento para que esta web almacene la información que envío para que puedan responder a mi petición."
                    if columna_a_eliminar in df.columns:
                        df.drop(columna_a_eliminar, axis=1, inplace=True)

                    nombre_archivo = os.path.splitext(os.path.basename(archivo))[0]

                    if nombre_archivo.startswith("nf-subs-") and nombre_archivo[8:].isdigit():
                        numero = nombre_archivo[8:]

                        diccionario_productos = {"2": "Concentrador de datos multifunción inteligente ADD GRUP DC2S", 
                                                 "5": "HEYI MSQ",
                                                 "7": "Analizador de Red ISKRA iMC784",
                                                 "8": "Advanticsys Concentrador UCM-316",
                                                 "9": "DATA LOGGER SPC-31",
                                                 "10": "LECTOR ÓPTICO EMH OKK-USB",
                                                 "11": "Luminaria Cronos",
                                                 "12": "Medidor Digital EMH DIZ-G",
                                                 "13": "Medidor KLEA 320P Tipo Panel",
                                                 "14": "Medidor KLEMSAN POWYS 3000",
                                                 "15": "Medidor Multifunción EMH LZQJ-XC Clase 0.2S",
                                                 "16": "Medidor Multifunción EMH LZQJ-XC Clase 0.5S",
                                                 "17": "Medidor Multifunción EMH LZQJ-XC Clase 1",
                                                 "18": "Medidor multifunción y multitarifa monofásico ADD GRUP AD11",
                                                 "19": "Medidor multifunción y multitarifa trifásico ADD GRUP ADD13A",
                                                 "20": "Modem Celular FOUR FAITH F-R100-FL",
                                                 "21": "MODEM CELULAR FOUR FAITH F2816",
                                                 "22": "Modem Celular FOUR FAITH F3X26Q",
                                                 "23": "Modem Celular INTERBIN MK-9XC4G",
                                                 "24": "Relé de Protección Multifunción ZIV IRL",
                                                 "25": "ROUTER F8926-L",
                                                 "26": "Router ZIV SIP-3",
                                                 "27": "Terminal LORA F8L10T",
                                                 "28": "Transformadores de Corriente HEYI ELECTRICAL",
                                                 "29": "ZIV Concentrador de Datos 4CCT",
                                                 "30": "ZIV Medidor Monofásico 5CTME2C",
                                                 "31": "Lectores Ópticos Bluetooth BLUSKY BSC 1162",
                                                 "32": "Lectores Ópticos Bluetooth BLUSKY BSC 1163",
                                                 "33": "Puente Modbus RS485 Inalámbrico"
                                                 }
                    
                        nombre_producto = diccionario_productos.get(numero, nombre_archivo)
                        df['Producto'] = nombre_producto

                        df_resultados = pd.concat([df_resultados, df], ignore_index=True)

                    df_resultados.to_excel(writer, sheet_name='HojaPrincipal', index=False)