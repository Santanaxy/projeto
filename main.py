import flet as ft


import flet as ft

def main(page: ft.Page):
    page.bgcolor = '#5B11BD'
    page.title = "MENU APP"
    page.window_width = 500
    page.window_height = 900
    page.window_maximizable = False

    sidebar = ft.Container(
        width=70,
        bgcolor="#C50202",
        border_radius=ft.border_radius.only(top_right=10, bottom_right=20),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.IconButton(ft.Icons.HOME, icon_color="white"),
                ft.IconButton(ft.Icons.SEARCH, icon_color="white"),
                ft.IconButton(ft.Icons.FAVORITE, icon_color="white"),
            ],
            spacing=5
        ),
        padding=ft.padding.only(left=0, top=10, right=10, bottom=10),  # Menos espaço à esquerda
        margin=0,
        expand=False,
    )

    page.add(
        ft.Row(
            controls=[
                sidebar,
                ft.Container(expand=True)  # Espaço para o conteúdo principal
            ],
            expand=True,
            spacing=0  # Garante que não há espaço entre sidebar e conteúdo
        )
    )

ft.app(target=main)