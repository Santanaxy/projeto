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
        expand=False
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

    page.add(
        ft.Row([
            ft.IconButton(
                icon=ft.Icons.MENU,
                icon_color=ft.Colors.BLUE_900,
                icon_size=40,
                tooltip="Menu Principal",
                on_click=lambda e: page.open(drawer),
            ),
            ft.IconButton(
                icon=ft.Icons.SETTINGS,
                icon_color=ft.Colors.BLUE_900,
                icon_size=40,
                tooltip="Menu Lateral",
                on_click=lambda e: page.open(end_drawer),
            )
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    )

ft.app(target=main)
