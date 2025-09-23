import flet as ft

def main(page: ft.Page):
    page.bgcolor = "#FFFFFF"
    page.title = "MENU APP"
    page.window.width = 500
    page.window.height = 900
    page.window.max_width = 500
    page.window.max_height = 900

    # Variável para controlar o item selecionado no menu
    selected_index = 0

    # Funções para o menu lateral direito
    def handle_change(e):
        print(f"Selected Index changed: {e.control.selected_index}")
        page.close(end_drawer)

    def handle_dismissal(e):
        print(f"Drawer dismissed!")

    def open_end_drawer(e):
        page.open(end_drawer)

    # Menu lateral DIREITO
    end_drawer = ft.NavigationDrawer(
        position=ft.NavigationDrawerPosition.END,  # Define como menu lateral DIREITO
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
                icon=ft.Icons.BOOK,  # Ícone mais apropriado para Materiais
                selected_icon=ft.Icon(ft.Icons.BOOK),
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
                icon=ft.Icon(ft.Icons.EXIT_TO_APP),  # Ícone mais apropriado para Sair
                selected_icon=ft.Icon(ft.Icons.EXIT_TO_APP),
            ),
        ],
    )

    # Funções para o menu inferior
    def menu_item_clicked(e):
        nonlocal selected_index
        selected_index = e.control.data
        update_menu_style()
        print(f"Menu item selecionado: {e.control.data} - {e.control.tooltip}")

    def update_menu_style():
        for i, item in enumerate(menu_items.controls):
            if i == selected_index:
                # Item selecionado - destaque
                item.bgcolor = "#0A0DA1"
                item.content.controls[0].color = ft.Colors.WHITE
                item.content.controls[1].color = ft.Colors.WHITE
                item.content.controls[1].weight = ft.FontWeight.BOLD
            else:
                # Item não selecionado
                item.bgcolor = ft.Colors.TRANSPARENT
                item.content.controls[0].color = "#666666"
                item.content.controls[1].color = "#666666"
                item.content.controls[1].weight = ft.FontWeight.NORMAL
        page.update()

    # Função para criar itens do menu
    def create_menu_item(icon, label, index, tooltip):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Icon(icon, size=28, color="#666666"),
                    ft.Text(label, size=11, color="#666666", text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=3,
            ),
            padding=10,
            border_radius=10,
            data=index,
            tooltip=tooltip,
            on_click=menu_item_clicked,
            animate=ft.Animation(200, curve=ft.AnimationCurve.EASE_OUT),
            width=70,
            height=65,
        )

    # Criar menu horizontal inferior
    menu_items = ft.Row(
        controls=[
            create_menu_item(ft.Icons.HOME, "Home", 0, "Página Inicial"),
            create_menu_item(ft.Icons.NOTIFICATIONS, "Notificações", 1, "Ver Notificações"),
            create_menu_item(ft.Icons.BOOK, "Materiais", 2, "Materiais de Estudo"),
            create_menu_item(ft.Icons.TRENDING_UP, "Desempenho", 3, "Ver Desempenho"),
            create_menu_item(ft.Icons.PERSON, "Perfil", 4, "Meu Perfil"),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Menu inferior
    bottom_menu = ft.Container(
        content=menu_items,
        bgcolor="#F5F5F5",
        padding=ft.padding.symmetric(vertical=10, horizontal=5),
        border_radius=0,
        border=ft.border.only(top=ft.border.BorderSide(1, "#E0E0E0")),
        height=80
    )

    # Conteúdo principal
    main_content = ft.Container(
        content=ft.Column(
            [
                # Header com título e botão para abrir menu lateral DIREITO
                ft.Container(
                    content=ft.Row([
                        # Título centralizado
                        ft.Container(
                            content=ft.Text("FÁBRICA DE PROGRAMADORES", 
                                           size=22, 
                                           weight=ft.FontWeight.BOLD,
                                           color="#0A0DA1",
                                           text_align=ft.TextAlign.CENTER),
                            alignment=ft.alignment.center,
                            expand=True
                        ),
                        
                        # Botão para abrir menu lateral DIREITO
                        ft.Container(
                            content=ft.IconButton(
                                icon=ft.Icons.MENU,
                                icon_color="#0A0DA1",
                                icon_size=30,
                                tooltip="Abrir Menu Lateral",
                                on_click=open_end_drawer,
                            ),
                            margin=ft.margin.only(left=10)
                        )
                    ], 
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    bgcolor="#E9E9E9",
                    padding=20,
                    border_radius=ft.border_radius.only(bottom_left=15, bottom_right=15),
                    height=80
                ),
                
                # Conteúdo principal scrollável
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Bem-vindo à Fábrica de Programadores!",
                                   size=18,
                                   weight=ft.FontWeight.BOLD,
                                   color="#080404",
                                   text_align=ft.TextAlign.CENTER),
                            ft.Text("Agora com menu lateral direito funcional!",
                                   size=16,
                                   color="#2AC9A6",
                                   text_align=ft.TextAlign.CENTER),
                            
                            # Área de conteúdo expansível
                            ft.Container(
                                height=550,
                                bgcolor="#E9E9E9",
                                border_radius=15,
                                padding=25,
                                margin=ft.margin.symmetric(horizontal=15),
                                content=ft.Column([
                                    ft.Text("Área de conteúdo principal", 
                                           size=18, 
                                           weight=ft.FontWeight.BOLD,
                                           text_align=ft.TextAlign.CENTER),
                                    ft.Divider(height=20, color="#CCCCCC"),
                                    ft.Text("Menu lateral direito implantado com sucesso!", 
                                           size=16,
                                           text_align=ft.TextAlign.CENTER),
                                    ft.Text("Clique no ícone ☰ no canto superior direito", 
                                           size=14,
                                           color="#0A0DA1",
                                           text_align=ft.TextAlign.CENTER),
                                    ft.Text("Itens do menu lateral:", 
                                           size=14,
                                           weight=ft.FontWeight.BOLD,
                                           color="#0A0DA1"),
                                    ft.Text("• INICIO - Página inicial", 
                                           size=14,
                                           color="#666666"),
                                    ft.Text("• NOTIFICAÇÕES - Alertas e avisos", 
                                           size=14,
                                           color="#666666"),
                                    ft.Text("• DESEMPENHO - Estatísticas", 
                                           size=14,
                                           color="#666666"),
                                    ft.Text("• MATERIAIS - Conteúdo de estudo", 
                                           size=14,
                                           color="#666666"),
                                    ft.Text("• SUPORTE - Ajuda técnica", 
                                           size=14,
                                           color="#666666"),
                                    ft.Text("• CONFIGURAÇÕES - Configurações do app", 
                                           size=14,
                                           color="#666666"),
                                    ft.Text("• SAIR - Encerrar aplicação", 
                                           size=14,
                                           color="#FF0000"),
                                    ft.Divider(height=20, color="#CCCCCC"),
                                    ft.Text("Clique nos ícones do menu inferior para testar!",
                                           size=14,
                                           weight=ft.FontWeight.BOLD,
                                           color="#2AC9A6",
                                           text_align=ft.TextAlign.CENTER),
                                    
                                    # Espaço adicional para demonstrar scroll
                                    ft.Container(
                                        height=150,
                                        bgcolor="#D9D9D9",
                                        border_radius=10,
                                        padding=15,
                                        content=ft.Column([
                                            ft.Text("Conteúdo adicional",
                                                   size=14,
                                                   weight=ft.FontWeight.BOLD,
                                                   text_align=ft.TextAlign.CENTER),
                                            ft.Text("Mais conteúdo pode ser adicionado aqui...",
                                                   size=12,
                                                   text_align=ft.TextAlign.CENTER)
                                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                                    )
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=15)
                            )
                        ],
                        spacing=20,
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        expand=True,
                        scroll=ft.ScrollMode.ADAPTIVE
                    ),
                    padding=15,
                    expand=True
                )
            ],
            spacing=0,
            expand=True
        ),
        bgcolor="#FFFFFF",
        expand=True
    )

    # Layout principal com Stack para menu inferior fixo
    page_content = ft.Stack(
        [
            # Conteúdo principal
            main_content,
            
            # Menu inferior fixo na base
            ft.Container(
                content=bottom_menu,
                bottom=0,
                left=0,
                right=0,
            )
        ],
        expand=True
    )

    page.add(page_content)
    
    # Inicializar estilo do menu
    update_menu_style()

ft.app(target=main)