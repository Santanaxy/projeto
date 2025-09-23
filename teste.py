import flet as ft

def main(page: ft.Page):
    # Configuração da página - IMPLANTADO
    page.bgcolor = "#FFFFFF"
    page.title = "MENU APP"
    page.window.width = 500
    page.window.height = 900
    page.window.max_width = 500
    page.window.max_height = 900
    page.padding = 0
    page.spacing = 0
    
    # Cores - Adicionando cores para o menu azul escuro
    PRIMARY_COLOR = "#4361ee"
    DARK_BLUE = "#1e3a8a"  # Azul escuro principal
    DARKER_BLUE = "#1e40af"  # Azul mais escuro para hover
    ACCENT_BLUE = "#60a5fa"  # Azul claro para destaque
    BACKGROUND_COLOR = "#FFFFFF"
    TEXT_COLOR = "#2b2d42"
    LIGHT_GRAY = "#f8f9fa"
    MENU_TEXT_COLOR = "#e0f2fe"  # Texto claro para contraste
    
    # Variável para controlar o item selecionado no menu
    selected_index = 0
    
    def menu_item_clicked(e):
        nonlocal selected_index
        selected_index = e.control.data
        update_menu_style()
        print(f"Menu item clicked: {e.control.data}")
    
    def update_menu_style():
        for i, item in enumerate(menu_items.controls):
            if i == selected_index:
                # Item selecionado - destaque
                item.bgcolor = ACCENT_BLUE
                item.content.controls[0].content.color = DARK_BLUE  # Ícone
                item.content.controls[1].color = DARK_BLUE  # Texto
                item.content.controls[1].weight = ft.FontWeight.BOLD
                item.shadow = ft.BoxShadow(
                    spread_radius=2,
                    blur_radius=15,
                    color=ft.Colors.BLUE_300,
                    offset=ft.Offset(0, -3),
                )
            else:
                # Item não selecionado
                item.bgcolor = ft.Colors.TRANSPARENT
                item.content.controls[0].content.color = MENU_TEXT_COLOR  # Ícone
                item.content.controls[1].color = MENU_TEXT_COLOR  # Texto
                item.content.controls[1].weight = ft.FontWeight.NORMAL
                item.shadow = None
        page.update()
    
    # Função para criar itens do menu
    def create_menu_item(icon, label, index):
        icon_container = ft.Container(
            content=ft.Icon(icon, size=24, color=MENU_TEXT_COLOR),
            width=40,
            height=40,
            alignment=ft.alignment.center
        )
        
        text = ft.Text(
            label, 
            size=11, 
            color=MENU_TEXT_COLOR,
            text_align=ft.TextAlign.CENTER
        )
        
        column = ft.Column(
            [icon_container, text],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5,
            height=70
        )
        
        return ft.Container(
            content=column,
            padding=10,
            border_radius=15,
            data=index,
            on_click=menu_item_clicked,
            animate=ft.Animation(300, curve=ft.AnimationCurve.EASE_OUT),
        )
    
    # Criar menu horizontal inferior
    menu_items = ft.Row(
        controls=[
            create_menu_item(ft.Icons.HOME, "Início", 0),
            create_menu_item(ft.Icons.NOTIFICATIONS, "Notificações", 1),
            create_menu_item(ft.Icons.CALENDAR_MONTH, "Calendário", 2),
            create_menu_item(ft.Icons.PERSON, "Perfil", 3),
            create_menu_item(ft.Icons.SETTINGS, "Config", 4),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        expand=True
    )
    
    # Menu inferior azul escuro
    bottom_menu = ft.Container(
        content=ft.Column([
            # Linha decorativa superior
            ft.Container(
                width=60,
                height=4,
                bgcolor=ACCENT_BLUE,
                border_radius=2,
                margin=ft.margin.only(bottom=8)
            ),
            menu_items
        ]),
        bgcolor=DARK_BLUE,
        padding=ft.padding.symmetric(vertical=10, horizontal=5),
        border_radius=ft.border_radius.only(
            top_left=25,
            top_right=25
        ),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=25,
            color=ft.Colors.BLACK45,
            offset=ft.Offset(0, -5),
        )
    )
    
    # Função para abrir diálogo
    def open_dialog(e):
        page.dialog = dialog
        dialog.open = True
        page.update()
    
    def close_dialog(e):
        dialog.open = False
        page.update()
    
    # Criar diálogo
    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Basic dialog title", size=20, weight=ft.FontWeight.BOLD),
        content=ft.Text(
            "A dialog is a type of mental window that appears in front of app content "
            "to provide critical information, or prompt for a decision to be made.",
            size=14,
            color=ft.Colors.BLACK54
        ),
        actions=[
            ft.TextButton("Cancel", on_click=close_dialog),
            ft.TextButton("OK", on_click=close_dialog),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    
    # Criar calendário estilo grid
    def create_calendar():
        # Dias da semana
        week_days = ["S", "M", "T", "W", "T", "F", "S"]
        
        # Dias do mês
        month_days = [
            "", "", "", "", "1", "2", "3",
            "4", "5", "6", "7", "8", "9", "10",
            "11", "12", "13", "14", "15", "16", "17",
            "18", "19", "20", "21", "22", "23", "24",
            "25", "26", "27", "28", "29", "30", "31"
        ]
        
        # Criar grid 7x6 (semanas x dias)
        calendar_grid = ft.GridView(
            max_extent=40,  # Tamanho de cada célula
            runs_count=7,   # 7 colunas (dias da semana)
            spacing=5,      # Espaçamento entre células
            run_spacing=5,  # Espaçamento entre linhas
            height=200,     # Altura fixa do calendário
        )
        
        # Adicionar dias da semana
        for day in week_days:
            calendar_grid.controls.append(
                ft.Container(
                    content=ft.Text(
                        day, 
                        size=14, 
                        weight=ft.FontWeight.BOLD, 
                        color=TEXT_COLOR,
                        text_align=ft.TextAlign.CENTER
                    ),
                    alignment=ft.alignment.center,
                    bgcolor=LIGHT_GRAY,
                    border_radius=8,
                    padding=8,
                )
            )
        
        # Adicionar dias do mês
        for day in month_days:
            if day == "9":  # Destacar o dia 9 como exemplo
                bgcolor = PRIMARY_COLOR
                text_color = ft.Colors.WHITE
            else:
                bgcolor = LIGHT_GRAY if day else ft.Colors.TRANSPARENT
                text_color = TEXT_COLOR if day else ft.Colors.TRANSPARENT
            
            calendar_grid.controls.append(
                ft.Container(
                    content=ft.Text(
                        day, 
                        size=14, 
                        color=text_color,
                        text_align=ft.TextAlign.CENTER
                    ),
                    alignment=ft.alignment.center,
                    bgcolor=bgcolor,
                    border_radius=8,
                    padding=8,
                )
            )
        
        return calendar_grid
    
    # Layout principal
    main_content = ft.Container(
        content=ft.Column(
            [
                # Header com horário
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "9:41",
                                size=32,
                                weight=ft.FontWeight.BOLD,
                                color=TEXT_COLOR,
                                text_align=ft.TextAlign.CENTER
                            ),
                            ft.Text(
                                "Titulo do banner",
                                size=18,
                                color=TEXT_COLOR,
                                text_align=ft.TextAlign.CENTER
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=5
                    ),
                    padding=30,
                    margin=ft.margin.only(bottom=20),
                    bgcolor=LIGHT_GRAY,
                ),
                
                # Calendário
                ft.Container(
                    content=ft.Column(
                        [
                            create_calendar()
                        ]
                    ),
                    padding=20,
                    margin=ft.margin.only(bottom=20),
                    bgcolor=BACKGROUND_COLOR,
                    border_radius=15,
                ),
                
                # Divisor
                ft.Divider(height=1, color="#E0E0E0", thickness=1),
                
                # Seção do diálogo
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "Basic dialog title",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=TEXT_COLOR
                            ),
                            ft.Text(
                                "A dialog is a type of mental window that appears in front of app content "
                                "to provide critical information, or prompt for a decision to be made.",
                                size=14,
                                color=ft.Colors.BLACK54
                            ),
                            ft.Container(
                                content=ft.ElevatedButton(
                                    content=ft.Text(
                                        "Abrir Diálogo",
                                        color=ft.Colors.WHITE,
                                        size=14
                                    ),
                                    bgcolor=PRIMARY_COLOR,
                                    on_click=open_dialog,
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                        padding=20
                                    )
                                ),
                                margin=ft.margin.only(top=20),
                                alignment=ft.alignment.center
                            )
                        ],
                        spacing=15
                    ),
                    padding=30,
                    bgcolor=BACKGROUND_COLOR,
                ),
                
                # Espaço para o menu inferior
                ft.Container(height=20),
            ],
            scroll=ft.ScrollMode.ADAPTIVE,
            spacing=0
        ),
        # Container expandido com bordas ovais
       
    )
    
    # Layout principal com menu inferior
    page_content = ft.Stack(
        [
            # Conteúdo principal
            main_content,
            
            # Menu inferior fixo
            ft.Container(
                content=bottom_menu,
                bottom=0,
                left=0,
                right=0,
                height=90
            )
        ],
        expand=True
    )
    
    page_container = ft.Container(
        content=page_content,
        expand=True,
        bgcolor="#E5E5E5",
        padding=0,
        margin=0,
    )
    
    page.add(page_container)
    
    # Inicializar estilo do menu
    update_menu_style()

ft.app(target=main)