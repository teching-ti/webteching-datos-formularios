from flet import *
import flet as ft
import os
from proceso import procesar_archivos

def main(page: ft.Page):
    page.bgcolor = ft.colors.SECONDARY
    page.title = "Teching forms to .xlsx"
    page.window_width = 540
    page.window_maximizable = False
    page.window_center()

    def dialog_picker(e:FilePickerResultEvent):
        selected_files.value = (
            ",\n".join(map(lambda f: f.path, e.files)) if e.files else "Se canceló la operación."
        )
        selected_files.update()
        btnGenerar.disabled = False
        btnGenerar.update()
    
    selected_files = ft.Text(color=ft.colors.BLACK, selectable=True)

    pick_files_dialog = FilePicker(on_result=dialog_picker)
    page.overlay.append(pick_files_dialog)

    confirmation = ft.Text(color=ft.colors.BLACK)
    def generar_archivo():
        archivos_para_comprobar = selected_files.value.replace("\n", "")
        lista = archivos_para_comprobar.split(",")

        for nombre in lista:
            nombre_archivo = os.path.basename(nombre)

            if not nombre_archivo.startswith("nf-subs-"):
                dialog_open()
                return
            
        procesar_archivos(archivos_para_comprobar)
        confirmation.value = "Archivos generados"
        confirmation.update()

    alerta = AlertDialog(
        title=Text("Se presenta un error, primero debe seleccionar los archivos correctos"),
        on_dismiss=lambda event: True
    )

    def dialog_open():
        page.dialog = alerta
        alerta.open = True
        page.update()

    btnSeleccionar =  ElevatedButton("Seleccionar archivos", 
                           style=ft.ButtonStyle(
                               color={
                                    ft.MaterialState.HOVERED: ft.colors.WHITE,
                                    ft.MaterialState.DEFAULT: ft.colors.BLACK,
                                },
                                bgcolor={
                                    ft.MaterialState.HOVERED: ft.colors.GREY,
                                    ft.MaterialState.DEFAULT: ft.colors.BLUE_50
                                }
                               ),
                            on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=True, allowed_extensions= ["csv"]),
                            )

    btnGenerar = ElevatedButton("Generar Resultado",
                           style=ft.ButtonStyle(
                               color={
                                    ft.MaterialState.HOVERED: ft.colors.WHITE,
                                    ft.MaterialState.DEFAULT: ft.colors.BLACK,
                                },
                                bgcolor={
                                    ft.MaterialState.HOVERED: ft.colors.GREY,
                                    ft.MaterialState.DEFAULT: ft.colors.BLUE_50
                                }
                               ),
                            on_click=lambda _: generar_archivo(),
                            disabled=True
                            )
    
    page.add(
        Row([btnSeleccionar, 
            btnGenerar,
        ], alignment="CENTER"),
        ResponsiveRow([
            selected_files,
        ], alignment="CENTER"),
        Row([
            confirmation,
        ], alignment="CENTER")
    )

ft.app(target=main)