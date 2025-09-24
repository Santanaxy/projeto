import flet as ft

def home(page: ft.Page):
    page.bgcolor = "#FFFFFF"
    page.title = "MENU APP"
    page.window.width = 500
    page.window.height = 900
    page.window.max_width = 500
    page.window.max_height = 900

    # Variável para controlar o item selecionado no menu
    selected_index = 0

    # Variável para controlar o índice do carrossel
    carousel_index = 0

    # Variável para controlar o auto-play
    auto_play_enabled = True

    # Variável para a foto de perfil
    profile_image = "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=200"  # Imagem padrão

    # Lista de imagens para o carrossel (URLs de exemplo)
    carousel_images = [
        "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=400",
        "https://images.unsplash.com/photo-1555099962-4199c345e5dd?w=400",
        "https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=400",
        "https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=400"
    ]

    # Funções para o auto-play
    def start_auto_play():
        if auto_play_enabled:
            page.run_thread(auto_play_loop)

    def auto_play_loop():
        import time
        global auto_play_enabled, carousel_index
        
        while auto_play_enabled and page:
            time.sleep(3)
            if auto_play_enabled and page:
                carousel_index = (carousel_index + 1) % len(carousel_images)
                page.run_task(update_carousel_and_refresh)

    def update_carousel_and_refresh():
        update_carousel()
        page.update()

    # Funções para o FilePicker
    def on_file_result(e: ft.FilePickerResultEvent):
        if e.files and e.files[0].path:
            # Aqui você pode processar o arquivo selecionado
            # Por enquanto, vamos usar uma imagem de placeholder
            profile_photo.src = "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200"
            page.update()
            print(f"Arquivo selecionado: {e.files[0].name}")

    file_picker = ft.FilePicker(on_result=on_file_result)
    page.overlay.append(file_picker)

    # Função para abrir o seletor de arquivos
    def pick_file(e):
        file_picker.pick_files(allow_multiple=False, file_type=ft.FilePickerFileType.IMAGE)

    # Funções para o carrossel
    def next_image(e):
        nonlocal carousel_index
        carousel_index = (carousel_index + 1) % len(carousel_images)
        update_carousel()
        page.update()

    def previous_image(e):
        nonlocal carousel_index
        carousel_index = (carousel_index - 1) % len(carousel_images)
        update_carousel()
        page.update()

    def update_carousel():
        carousel_image.src = carousel_images[carousel_index]
        carousel_indicator.content = ft.Row(
            [ft.Container(
                width=10,
                height=10,
                border_radius=5,
                bgcolor="#0A0DA1" if i == carousel_index else "#CCCCCC",
                animate=ft.Animation(300, curve=ft.AnimationCurve.EASE_IN_OUT)
            ) for i in range(len(carousel_images))],
            alignment=ft.MainAxisAlignment.CENTER
        )

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
        elevation=20,
        controls=[
            ft.Container(height=5),
            ft.NavigationDrawerDestination(
                label="INICIO",
                icon=ft.Icons.HOME_ROUNDED,
                selected_icon=ft.Icon(ft.Icons.HOME_ROUNDED),
            ),
            ft.NavigationDrawerDestination(
                label="SUPORTE",
                icon=ft.Icon(ft.Icons.LIVE_HELP_ROUNDED),
                selected_icon=ft.Icon(ft.Icons.LIVE_HELP_ROUNDED),
            ),
            # Container expansível para empurrar o SAIR para o final
            
            # Divisor visual
            ft.Divider(height=680, thickness=1),
            # SAIR no final do menu
             ft.Container(expand=True),
            ft.NavigationDrawerDestination(
                label="SAIR",
                icon=ft.Icon(ft.Icons.EXIT_TO_APP, color=ft.Colors.RED_400),
                selected_icon=ft.Icon(ft.Icons.EXIT_TO_APP, color=ft.Colors.RED_400),
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

    # Componentes do carrossel
    carousel_image = ft.Image(
        src=carousel_images[0],
        width=400,
        height=200,
        fit=ft.ImageFit.COVER,
        border_radius=15
    )

    carousel_indicator = ft.Container(
        content=ft.Row(
            [ft.Container(
                width=10,
                height=10,
                border_radius=5,
                bgcolor="#0A0DA1" if i == 0 else "#CCCCCC"
            ) for i in range(len(carousel_images))],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        padding=10
    )

    # Componentes da foto de perfil (layout horizontal/deitado)
    profile_photo = ft.Image(
        src=profile_image,
        width=80,
        height=80,
        fit=ft.ImageFit.COVER,
        border_radius=40  # Torna a imagem circular
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
                            
                            # FOTO DE PERFIL NA HORIZONTAL (ACIMA DO CARROSSEL)
                            ft.Container(
                                content=ft.Row([
                                    # Container da foto de perfil
                                    ft.Container(
                                        content=ft.Stack([
                                            # Foto de perfil
                                            profile_photo,
                                            
                                            # Ícone de câmera para adicionar foto
                                            ft.Container(
                                                content=ft.IconButton(
                                                    icon=ft.Icons.CAMERA_ALT,
                                                    icon_size=16,
                                                    icon_color=ft.Colors.WHITE,
                                                    on_click=pick_file,
                                                    tooltip="Adicionar Foto",
                                                    style=ft.ButtonStyle(
                                                        bgcolor={"": "#0A0DA1"},
                                                        shape=ft.CircleBorder(),
                                                        padding=8
                                                    )
                                                ),
                                                alignment=ft.alignment.bottom_right,
                                            )
                                        ]),
                                        width=90,
                                        height=90,
                                        border=ft.border.all(2, "#0A0DA1"),
                                        border_radius=45,  # Torna o container circular
                                        padding=5,
                                        margin=ft.margin.only(right=15),
                                        shadow=ft.BoxShadow(
                                            spread_radius=1,
                                            blur_radius=8,
                                            color=ft.Colors.BLACK26,
                                            offset=ft.Offset(0, 2)
                                        )
                                    ),
                                    
                                    # Informações do usuário (lado direito da foto)
                                    ft.Column([
                                        ft.Text("Usuário",
                                               size=16,
                                               weight=ft.FontWeight.BOLD,
                                               color="#080404"),
                                        ft.Text("Programador Iniciante",
                                               size=12,
                                               color="#666666"),
                                        ft.Container(
                                            content=ft.ElevatedButton(
                                                content=ft.Row([
                                                    ft.Icon(ft.Icons.EDIT, size=14, color=ft.Colors.WHITE),
                                                    ft.Text("Editar Perfil", size=11, color=ft.Colors.WHITE),
                                                ], alignment=ft.MainAxisAlignment.CENTER),
                                                on_click=pick_file,
                                                style=ft.ButtonStyle(
                                                    bgcolor={"": "#2AC9A6"},
                                                    padding=ft.padding.symmetric(horizontal=12, vertical=8),
                                                    shape=ft.RoundedRectangleBorder(radius=8)
                                                ),
                                                height=30
                                            ),
                                            margin=ft.margin.only(top=5)
                                        )
                                    ], spacing=3, expand=True)
                                ], 
                                alignment=ft.MainAxisAlignment.START,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER),
                                margin=ft.margin.symmetric(horizontal=15, vertical=10),
                                padding=15,
                                bgcolor="#F8F9FA",
                                border_radius=15,
                                border=ft.border.all(1, "#E0E0E0")
                            ),
                            
                            # CARROSSEL DE FOTOS (ABAIXO DA FOTO DE PERFIL) - COM AUTO-PLAY
                            ft.Container(
                                content=ft.Column([
                                    # Container do carrossel
                                    ft.Container(
                                        content=ft.Stack([
                                            # Imagem do carrossel
                                            carousel_image,
                                            
                                            # Botão anterior
                                            ft.Container(
                                                content=ft.IconButton(
                                                    icon=ft.Icons.ARROW_BACK_IOS_NEW,
                                                    icon_color=ft.Colors.WHITE,
                                                    icon_size=20,
                                                    on_click=previous_image,
                                                    style=ft.ButtonStyle(
                                                        bgcolor={"": ft.Colors.BLACK54},
                                                        shape=ft.RoundedRectangleBorder(radius=10)
                                                    )
                                                ),
                                                alignment=ft.alignment.center_left,
                                                padding=10
                                            ),
                                            
                                            # Botão próximo
                                            ft.Container(
                                                content=ft.IconButton(
                                                    icon=ft.Icons.ARROW_FORWARD_IOS,
                                                    icon_color=ft.Colors.WHITE,
                                                    icon_size=20,
                                                    on_click=next_image,
                                                    style=ft.ButtonStyle(
                                                        bgcolor={"": ft.Colors.BLACK54},
                                                        shape=ft.RoundedRectangleBorder(radius=10)
                                                    )
                                                ),
                                                alignment=ft.alignment.center_right,
                                                padding=10
                                            ),
                                        ]),
                                        width=400,
                                        height=200,
                                        margin=ft.margin.symmetric(vertical=10),
                                        border_radius=15,
                                        shadow=ft.BoxShadow(
                                            spread_radius=1,
                                            blur_radius=15,
                                            color=ft.Colors.BLACK12,
                                            offset=ft.Offset(0, 3)
                                        )
                                    ),
                                    
                                    # Indicadores do carrossel
                                    carousel_indicator,
                                    
                                    # Texto abaixo do carrossel
                                    ft.Text("Explore nossos cursos e materiais!",
                                           size=14,
                                           color="#2AC9A6",
                                           text_align=ft.TextAlign.CENTER),
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                                margin=ft.margin.symmetric(horizontal=15, vertical=5)
                            ),
                            
                            # Área de conteúdo expansível
                            ft.Container(
                                height=300,
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
                                    ft.Text("Perfil e carrossel integrados!", 
                                           size=16,
                                           text_align=ft.TextAlign.CENTER),
                                    ft.Text("Carrossel automático a cada 3 segundos", 
                                           size=14,
                                           color="#0A0DA1",
                                           text_align=ft.TextAlign.CENTER),
                                    ft.Text("Recursos disponíveis:", 
                                           size=14,
                                           weight=ft.FontWeight.BOLD,
                                           color="#0A0DA1"),
                                    ft.Text("• Perfil personalizável", 
                                           size=14,
                                           color="#666666"),
                                    ft.Text("• Carrossel de conteúdos automático", 
                                           size=14,
                                           color="#666666"),
                                    ft.Text("• Navegação intuitiva", 
                                           size=14,
                                           color="#666666"),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=15)
                            )
                        ],
                        spacing=10,
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
    
    # Iniciar o auto-play do carrossel
    start_auto_play()

ft.app(target=home)
