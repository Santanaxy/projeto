import flet as ft
import os

def main(page: ft.Page):
    
    page.title = "MENU APP"
    page.window.width = 500
    page.window.height = 900
    page.window.max_width = 500
    page.window.max_height = 900
    page.padding = 0  # Remover qualquer padding da página
    page.bgcolor = "transparent"  # Tornar o fundo da página transparente
    
    # Obter o diretório atual do script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    gif_path = os.path.join(current_dir, "img", "purple.gif")
    
    # Verificar se o arquivo existe
    if not os.path.exists(gif_path):
        print(f"AVISO: Arquivo GIF não encontrado em: {gif_path}")
        # Usar um GIF online como fallback
        gif_src = "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif"
    else:
        gif_src = gif_path
    
    # CODIGO PARA COLOCAR O GIF DE Fundo cobrindo toda a tela
    gif_bg = ft.Container(
        content=ft.Image(
            src=gif_src,
            fit=ft.ImageFit.COVER,
            width=page.window.width,
            height=page.window.height,
        ),
        expand=True,
        alignment=ft.alignment.center,
    )
    
    def handle_dismissal(e):
        print(f"INICIO!")
        print(f"Drawer dismissed!")
    
    def handle_change(e):
        print(f"Selected Index changed: {e.control.selected_index}")
        page.close(drawer)

#AQUI E A BARRA DE MENU LATERAL ESQUERDA
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
            ft.Divider(thickness=1),
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
    #AQUI SÃO AS MENSAGENS QUE APARECE NO MEU MENU LATERAL ESQUERDO 
    def handle_end_drawer_dismissal(e):
        print("End drawer dismissed")

    def handle_end_drawer_change(e):
        print(f"Selected Index changed: {e.control.selected_index}")
        page.close(end_drawer)
    #AQUI E A BARRA DE MENU LATERAL DIREITA
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
    #AQUI E O CONTAINER DA FOTO DE PERFIL DO USUARIO QUE FICA NA TELA PRINCIPAL
    circular_container = ft.Container(
        width=100,
        height=100,
        content=ft.Image(
            src="https://images.unsplash.com/photo-1494790108755-2616b612b786?ixlib=rb-1.2.1&auto=format&fit=crop&w=200&q=80", #AQUI VAI SER O LINK DA FOTO DE PERFIL DO USUARIO
            fit=ft.ImageFit.COVER,
        ),
        border=ft.border.all(5, "#ff006e"),
        border_radius=100,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
    )

    # AQUI SÃO OS CODIGOS DA BARRA SUPERIOR E DO CONTEUDO PRINCIPAL
    top_bar = ft.Container(
        content=ft.Row([
            ft.IconButton(
                icon=ft.Icons.MENU,
                icon_color="#FFFFFF",
                icon_size=30,
                tooltip="Menu Principal",
                on_click=lambda e: page.open(drawer),
            ),
            ft.Container(
                content=ft.Text("FÁBRICA DE PROGRAMADORES", 
                               size=20, 
                               weight=ft.FontWeight.BOLD,
                               color="#FFFFFF"),
                expand=True,
                alignment=ft.alignment.center
            ),
            ft.IconButton(
                icon=ft.Icons.MORE_VERT,
                icon_color="#FFFFFF",
                icon_size=30,
                tooltip="Menu Lateral",
                on_click=lambda e: page.open(end_drawer),
            )
        ], 
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        bgcolor="#80000000",  # Preto semi-transparente
        padding=10,
        border_radius=ft.border_radius.only(
            bottom_left=10,
            bottom_right=10
        )
    )

    # AQUI E O CONTEUDO PRINCIPAL DA TELA DE MENU DO USUARIO
    content_area = ft.Container(
        content=ft.Column(
            [
                ft.Text("Bem-vindo ao App!",
                       size=16,
                       color="#FFFFFF",
                       text_align=ft.TextAlign.CENTER),
                ft.Row([
                    circular_container,
                    ft.Text("Perfil do Usuário", 
                           size=20, 
                           weight=ft.FontWeight.BOLD,
                           color="#FFFFFF")
                ], 
                alignment=ft.MainAxisAlignment.START,
                spacing=10),
                ft.Text("A CALABRESA ACABOU !",
                       size=16,
                       color="#FFFFFF",
                       text_align=ft.TextAlign.CENTER),
                ft.Container(
                    height=400,
                    bgcolor="#80000000",  # Preto semi-transparente
                    border_radius=10,
                    padding=20,
                    content=ft.Column([
                        ft.Text("ÁREA DO ALUNO", 
                               size=18, 
                               weight=ft.FontWeight.BOLD,
                               color="#FFFFFF",
                               text_align=ft.TextAlign.CENTER),
                        ft.Divider(color="#FFFFFF"),
                        ft.Text("Você pode adicionar qualquer BOSTA AQUI.",
                               color="#FFFFFF",
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

    # AQUI E O CODIGO DE LAYOUT PRINCIPAL COM FUNDO DE GIF E IMPORPANTE TER PRA RODAR O GIF DE FUNDO
    main_layout = ft.Stack(
        [
            gif_bg,  # GIF de fundo cobrindo toda a tela
            ft.Column(
                [
                    top_bar,
                    content_area
                ],
                expand=True
            )
        ],
        expand=True
    )

    # Container principal sem margens ou padding
    page_container = ft.Container(
        content=main_layout,
        expand=True,
        padding=0,
        margin=0,
    )

    page.add(page_container)

if __name__ == "__main__":
    ft.app(target=main, assets_dir="img")