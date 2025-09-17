import flet as ft


def main(page: ft.Page):
    page.title = "fabrica de programadores"
    page.theme_mode = "dark"
    texto = ft.Text(value="Hola Mundo", color="white", size=30)
    page.window_width = 500
    page.window_height = 900
    page.window.max_width = 500
    entrada = ft.TextField(label="Menu")


    page.add(ft.Row([texto, entrada], alignment = "center"))
ft.app(target=main)