import flet as ft

def main(page: ft.Page):
    BG = "#041955"
    FWG = "#97b4ff"
    FG = "#3450a1"
    PINK = "#ff0feb"

    # Menu Icon no topo
    first_page = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Icon(name=ft.icons.MENU)
                        )
                    ]
                )
            ]
        )
    )

    # Um container centralizado
    page_2 = ft.Container(
        width=300,
        height=300,
        bgcolor=FG,
        border_radius=20,
        padding=10,
        content=ft.Column(
            controls=[
                first_page
            ]
        )
    )

    # Stack com os elementos
    container = ft.Container(
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=40,
        content=ft.Stack(
            controls=[
                page_2
            ]
        )
    )

    page.add(container)

ft.app(target=main)