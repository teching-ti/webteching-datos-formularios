import tkinter as tk
import os
from tkinter import messagebox
from tkinter import filedialog
from proceso import procesar_archivos

def buscar_archivos():
    archivos = filedialog.askopenfilenames(
        title="Seleccionar los archivos",
        filetypes=[("Archivos CSV", "*.csv")]
    )
    mostrar_archivos_seleccionados(archivos)

def mostrar_archivos_seleccionados(archivos):
    if archivos:
        archivos_seleccionados_label.config(text=",".join(archivos))
        btn_generar_documento["state"] = "normal"
    else:
        archivos_seleccionados_label.config(text="Operación cancelada")
    window.update_idletasks()
    window.geometry(f"480x{frame.winfo_reqheight()}")

def generar_archivos():
    archivos_para_comprobar = archivos_seleccionados_label.cget("text")
    lista = archivos_para_comprobar.split(",")
    for nombre in lista:
        nombre_archivo = os.path.basename(nombre)
        
        if not nombre_archivo.startswith("nf-subs-"):
            messagebox.showwarning(title="Mensaje Error", message=f"No se fha podido generar el archivo resultante.\nEl archivo {nombre_archivo} no proviene de los formularios de teching.")
            return
            
    messagebox.showinfo(title="Mensaje", message="El archivo ha sido generado de manera exitosa.")
    procesar_archivos(archivos_para_comprobar)

def cerrar():
    global window
    window.quit()

window = tk.Tk()
window.geometry("480x240")
window.title("Teching forms to .xlsx")

frame = tk.Frame(window)
frame.pack(expand=True, fill='both')


btn_seleccionar = tk.Button(frame, text="Abrir archivos CSV", command=buscar_archivos)
btn_seleccionar.pack(padx=50, pady=50)

archivos_seleccionados_label = tk.Label(frame, text="")
archivos_seleccionados_label.pack(pady=10)

btn_generar_documento = tk.Button(frame, text="Generar", command=generar_archivos, state="disabled")
btn_generar_documento.pack(padx=10, pady=10)

window.mainloop()