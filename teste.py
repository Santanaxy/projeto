import flet as ft

def main(page: ft.Page):
    page.bgcolor = "#D3D3D3"
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
                label="AMIGOS",
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
                # Barra de botões no topo
                ft.Row([
                    ft.IconButton(
                        icon=ft.Icons.MENU,
                        icon_color=ft.Colors.BLUE_900,
                        icon_size=40,
                        tooltip="Menu Principal",
                        on_click=lambda e: page.open(drawer),
                    ),
                    ft.IconButton(
                        icon=ft.Icons.MORE_VERT,
                        icon_color=ft.Colors.BLUE_900,
                        icon_size=40,
                        tooltip="Menu Lateral",
                        on_click=lambda e: page.open(end_drawer),
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                
                # Conteúdo principal abaixo da barra de botões
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("CONTEÚDO PRINCIPAL", 
                                   size=20, 
                                   weight=ft.FontWeight.BOLD,
                                   color=ft.Colors.BLUE_900),
                            ft.Text("Este é o container expandido com borda nas laterais e inferior.",
                                   size=16,
                                   color=ft.Colors.BLACK87),
                            ft.Text("A borda superior foi removida conforme solicitado.",
                                   size=16,
                                   color=ft.Colors.BLACK87),
                            # Adicione mais conteúdo aqui conforme necessário
                            ft.Container(
                                height=800,
                                bgcolor=ft.Colors.WHITE,
                                border_radius=10,
                                padding=20,
                                content=ft.Column([
                                    ft.Text("Área de conteúdo", size=18),
                                    ft.Divider(),
                                    ft.Text("Você pode adicionar qualquer widget aqui...")
                                ])
                            )
                        ],
                        spacing=20,
                        alignment=ft.MainAxisAlignment.START,
                        expand=True
                    ),
                    padding=20,
                    expand=True
                )
            ],
            spacing=0,
            expand=True
        ),
        bgcolor=ft.Colors.WHITE,
        border=ft.border.only(
            left=ft.border.BorderSide(2, ft.Colors.BLACK),
            right=ft.border.BorderSide(2, ft.Colors.BLACK),
            bottom=ft.border.BorderSide(2, ft.Colors.BLACK)
        ),
        border_radius=ft.border_radius.only(
            bottom_left=10,
            bottom_right=10
        ),
        margin=ft.margin.only(top=0),  # Remove margem superior para ficar colado no topo
        padding=ft.padding.only(top=0),  # Remove padding superior
        expand=True
    )

    page.add(main_container)

ft.app(target=main)
