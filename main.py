import flet as ft

def main(page: ft.Page):
    page.bgcolor = "#FFFFFF"
    page.title = "MENU APP"
    page.window.width = 500
    page.window.height = 900
    page.window.max_width = 500
    page.window.max_height = 900
    
    def handle_dismissal(e):
        print(f"INICIO!")
        print(f"Drawer dismissed!")
    
    def handle_change(e):
        print(f"Selected Index changed: {e.control.selected_index}")
        page.close(drawer)

    drawer = ft.NavigationDrawer(
        on_dismiss=handle_dismissal,
        on_change=handle_change,
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="INICIO",
                icon=ft.Icons.HOME_ROUNDED,
                selected_icon=ft.Icon(ft.Icons.HOME_ROUNDED),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.NOTIFICATIONS_ACTIVE),
                label="NOTIFICAÇÕES",
                selected_icon=ft.Icons.NOTIFICATIONS_ACTIVE,
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.ALIGN_VERTICAL_BOTTOM_SHARP),
                label="DESEMPENHO",
                selected_icon=ft.Icons.ALIGN_VERTICAL_BOTTOM_SHARP,
            ),
            ft.NavigationDrawerDestination(
                label="MATERIAIS",
                icon=ft.Icons.MESSENGER,
                selected_icon=ft.Icon(ft.Icons.MESSENGER),
            ),
            ft.NavigationDrawerDestination(
                label="SUPORTE",
                icon=ft.Icon(ft.Icons.LIVE_HELP_ROUNDED),
                selected_icon=ft.Icon(ft.Icons.LIVE_HELP_ROUNDED),
            ),
            ft.NavigationDrawerDestination(
                label="CONFIGURAÇÕES",
                icon=ft.Icon(ft.Icons.SETTINGS),
                selected_icon=ft.Icon(ft.Icons.SETTINGS),
            ),
            ft.NavigationDrawerDestination(
                label="SAIR",
                icon=ft.Icon(ft.Icons.APP_BLOCKING),
                selected_icon=ft.Icon(ft.Icons.APP_BLOCKING),
            ),
        ],
    )

    def handle_end_drawer_dismissal(e):
        print("End drawer dismissed")

    def handle_end_drawer_change(e):
        print(f"Selected Index changed: {e.control.selected_index}")
        page.close(end_drawer)

    # Coluna para o end_drawer
    col = ft.Column(
        [
            ft.Text("Item 1", size=16, weight=ft.FontWeight.BOLD),
            ft.Text("Item 2", size=16, weight=ft.FontWeight.BOLD),
            ft.Text("Item 3", size=16, weight=ft.FontWeight.BOLD)
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )

    end_drawer = ft.NavigationDrawer(
        position=ft.NavigationDrawerPosition.END,
        on_dismiss=handle_end_drawer_dismissal,
        on_change=handle_end_drawer_change,
        controls=[
            ft.Container(
                content=col,
                padding=20,
                border=ft.border.all(2, ft.Colors.BLACK),
                margin=ft.margin.all(10),
                expand=True
            )
        ],
    )

    # Container principal expandido com borda em todos os lados exceto no topo
    main_container = ft.Container(
        content=ft.Column(
            [
                # Barra de botões no topo - conteúdo centralizado entre os botões
                ft.Row([
                    # Botão menu à esquerda
                    ft.IconButton(
                        icon=ft.Icons.MENU,
                        icon_color="#0A0DA1",
                        icon_size=30,
                        tooltip="Menu Principal",
                        on_click=lambda e: page.open(drawer),
                    ),
                    
                    # Texto centralizado entre os botões
                    ft.Container(
                        content=ft.Text("FÁBRICA DE PROGRAMADORES", 
                                       size=20, 
                                       weight=ft.FontWeight.BOLD,
                                       color="#FFFFFF"),
                        expand=True,
                        alignment=ft.alignment.center
                    ),
                    
                    # Botão settings à direita
                    ft.IconButton(
                        icon=ft.Icons.MORE_VERT,
                        icon_color="#FAFAFA",
                        icon_size=30,
                        tooltip="Menu Lateral",
                        on_click=lambda e: page.open(end_drawer),
                    )
                ], 
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                
                # Conteúdo principal abaixo da barra de botões
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Este é o container expandido com borda nas laterais e inferior.",
                                   size=16,
                                   color="#080404",
                                   text_align=ft.TextAlign.CENTER),
                            ft.Text("A borda superior foi removida conforme solicitado.",
                                   size=16,
                                   color="#2AC9A6",
                                   text_align=ft.TextAlign.CENTER),
                            # Adicione mais conteúdo aqui conforme necessário
                            ft.Container(
                                height=400,
                                bgcolor="#E9E9E9",
                                border_radius=10,
                                padding=20,
                                content=ft.Column([
                                    ft.Text("Área de conteúdo", 
                                           size=18, 
                                           weight=ft.FontWeight.BOLD,
                                           text_align=ft.TextAlign.CENTER),
                                    ft.Divider(),
                                    ft.Text("Você pode adicionar qualquer widget aqui...",
                                           text_align=ft.TextAlign.CENTER)
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                            )
                        ],
                        spacing=20,
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        expand=True
                    ),
                    padding=20,
                    expand=True
                )
            ],
            spacing=0,
            expand=True
        ),
        bgcolor="#D6D6D6",
        border=ft.border.only(
            left=ft.border.BorderSide(2, ft.Colors.BLACK),
            right=ft.border.BorderSide(2, ft.Colors.BLACK),
            bottom=ft.border.BorderSide(2, ft.Colors.BLACK)
        ),
        border_radius=ft.border_radius.only(
            bottom_left=10,
            bottom_right=10
        ),
        margin=ft.margin.only(top=0),
        padding=ft.padding.only(top=0),
        expand=True
    )

    page.add(main_container)

ft.app(target=main)
