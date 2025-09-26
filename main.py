import flet as ft

class App:
    def __init__(self):
        self.primary_color = "#1E5FE9"
        self.secondary_color = "#2AC9A6"
        self.carousel_images = [
            "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=400",
            "https://images.unsplash.com/photo-1555099962-4199c345e5dd?w=400",
            "https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=400",
            "https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=400"
        ]
        self.carousel_index = 0
        self.selected_index = 0
        self.auto_play_enabled = True
        self.drawer_open = False

    def create_drawer(self, page):
        
        """ANIMAÇÃO DO MENU LATERAL DO APLICATIVO"""
        
        def toggle_drawer(e):
            self.drawer_open = not self.drawer_open
            drawer.width = 280 if self.drawer_open else 0
            overlay.opacity = 0.4 if self.drawer_open else 0
            overlay.visible = self.drawer_open
            page.update()

        def menu_clicked(e):
            item_text = e.control.content.controls[1].value
            print(f"Item {item_text} clicado!")
            toggle_drawer(e)

        # Overlay
        overlay = ft.Container(
            expand=True, bgcolor="black", opacity=0, visible=False,
            on_click=toggle_drawer, animate_opacity=300
        )

        # mensagem dos button do menu lateral 
        drawer = ft.Container(
            width=0, height=page.height, bgcolor="white",
            content=ft.Column([
                # Header do drawer
                ft.Container(
                    content=ft.Row([
                        ft.Text("MENU", size=20, weight="bold", color="white" ),
                    ], alignment="center"),
                    bgcolor=self.primary_color, padding=15, height=70,border_radius=3, margin=1
                ),
                         #  """ICONES E TEXTOS DA ABA DO MENU LATERAL """
                
                ft.Container(
                    content=ft.Column([
                        self.create_menu_item("HOME", "INÍCIO", menu_clicked),
                        ft.Divider(height=1),
                        self.create_menu_item("SUPPORT", "SUPORTE", menu_clicked),
                        ft.Divider(height=1),
                        ft.Container(expand=True),  # Espaço flexível
                        self.create_menu_item("EXIT_TO_APP", "SAIR", menu_clicked, is_exit=True),
                    ], spacing=0),
                    padding=10, expand=True
                )
            ], spacing=0),
            animate=300, right=0, top=0,
            shadow=ft.BoxShadow(blur_radius=20, color=ft.Colors.BLACK54)
        )

        return overlay, drawer, toggle_drawer

    def create_menu_item(self, icon, text, on_click, is_exit=False):
        """Cria um item do menu"""
        color = "#ef4444" if is_exit else self.primary_color
        bg_color = "#fee2e2" if is_exit else "#e0e7ff"
        
        """return dos itens do meenu lateral"""
        
        return ft.Container(
            content=ft.Row([
                ft.Container(
                    content=ft.Icon(icon, color=color, size=20),
                    bgcolor=bg_color, padding=10, border_radius=10, width=40, height=40
                ),
                ft.Text(text, weight="bold", color=color, size=16)
            ], spacing=15),
            padding=15, on_click=on_click, border_radius=10,
            bgcolor={"": "transparent", "hovered": "#f1f5f9"}
        )

    def create_header(self, toggle_drawer):
        
        """modificar o cabeçalho do aplicativo"""
        
        return ft.Container(
            content=ft.Row([
                ft.IconButton(
                    icon="MENU", icon_color="#FFFFFF", icon_size=30,
                    on_click=toggle_drawer, tooltip="Abrir Menu"
                ),
                ft.Text("FÁBRICA DE PROGRAMADORES", size=22, weight="bold", 
                       color="#ffffff", text_align=ft.TextAlign.CENTER, expand=True),
            ], alignment=ft.MainAxisAlignment.START),
            bgcolor=self.primary_color, padding=20, height=70, border_radius=10, margin=1
        )

    def create_profile_section(self, pick_file):
        
        """mudar a seção de perfil do aplicativo"""
        
        return ft.Container(
            content=ft.Row([
                ft.Stack([
                    ft.Image(
                        src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=200",
                        width=110, height=110, fit=ft.ImageFit.COVER, border_radius=110
                    ),
                    ft.Container(
                        content=ft.IconButton(
                            icon="CAMERA_ALT", icon_size=20, icon_color="white",
                            on_click=pick_file, tooltip="Adicionar Foto",
                            style=ft.ButtonStyle(bgcolor={"": self.primary_color}, shape=ft.CircleBorder())
                        ),
                        alignment=ft.alignment.bottom_right,
                    )
                ]),
                ft.Column([
                    ft.Text("Usuário", size=18, weight=ft.FontWeight.BOLD, color="#000000"),
                    ft.Text("Programador Iniciante", size=12, color="#000000"),
                    ft.ElevatedButton(
                        "Editar Perfil", icon="EDIT", height=30,
                        style=ft.ButtonStyle(bgcolor={"WHITE": self.secondary_color}, padding=10)
                    )
                ], spacing=3, expand=True)
            ], alignment=ft.MainAxisAlignment.START),
             padding=15, border_radius=15, margin=10
        )

    def create_carousel(self, next_image, previous_image):
        
        """carrosel de imagens do aplicativo"""
        
        carousel_image = ft.Image(
            src=self.carousel_images[0],
            width=400, height=200, fit=ft.ImageFit.COVER, border_radius=15
        )
        """""container do carrosel e função de atualizar o carrosel"""
        def update_carousel():
            carousel_image.src = self.carousel_images[self.carousel_index]

        carousel = ft.Container(
            content=ft.Stack([
                carousel_image,
                ft.Container(
                    content=ft.IconButton(
                        icon="ARROW_BACK_IOS_NEW", icon_color="#ededed",
                        on_click=previous_image,
                        style=ft.ButtonStyle(bgcolor={"": ft.Colors.BLACK54})
                    ), alignment=ft.alignment.center_left
                ),
                ft.Container(
                    content=ft.IconButton(
                        icon="ARROW_FORWARD_IOS", icon_color="#efefef",
                        on_click=next_image,
                        style=ft.ButtonStyle(bgcolor={"": ft.Colors.BLACK54})
                    ), alignment=ft.alignment.center_right
                ),
            ]), width=400, height=200, margin=10, border_radius=15
        )
        
        """"return o carrosel e a função de atualizar o carrosel"""
        
        
        return carousel, update_carousel

    def create_bottom_menu(self, menu_item_clicked):
        
        """aplicação do menu inferior"""
        
        def create_menu_item(icon, label, index):
            return ft.Container(
                content=ft.Column([
                    ft.Icon(icon, size=28, color="#012643"),
                    ft.Text(label, size=11, color="#012643", text_align=ft.TextAlign.CENTER)
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=3),
                padding=10, border_radius=10, data=index, on_click=menu_item_clicked,
                width=70, height=65, animate=200
            )
        
        """"retorun o menu inferior (icones e textos)"""
        
        return ft.Container(
            content=ft.Row([
                create_menu_item("HOME", "Home", 0),
                create_menu_item("NOTIFICATIONS", "Notificações", 1),
                create_menu_item("BOOK", "Materiais", 2),
                create_menu_item("TRENDING_UP", "Desempenho", 3),
                create_menu_item("PERSON", "Perfil", 4),
            ], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
            bgcolor="#F5F5F5", padding=10, height=80
        )

    def main(self, page: ft.Page):
        
        """modificicar a pagina do aplicativo"""
        # Configuração da página
        page.bgcolor = "#ffffff"
        page.title = "FÁBRICA DE PROGRAMADORES"
        page.window.width = 500
        page.window.height = 900
        page.window.max_width = 500
        page.window.max_height = 900

        """"File Picker(button de adicionar foto de perfil)"""
        
        file_picker = ft.FilePicker()
        page.overlay.append(file_picker)

        def pick_file(e):
            file_picker.pick_files(allow_multiple=False)

        # Carrossel functions
        def next_image(e):
            self.carousel_index = (self.carousel_index + 1) % len(self.carousel_images)
            update_carousel()
            page.update()

        def previous_image(e):
            self.carousel_index = (self.carousel_index - 1) % len(self.carousel_images)
            update_carousel()
            page.update()

        # Menu função 
        def menu_item_clicked(e):
            self.selected_index = e.control.data
            page.update()

        """"todos os componentes da página para rodar o layout do aplicativo"""
        
        overlay, drawer, toggle_drawer = self.create_drawer(page)
        header = self.create_header(toggle_drawer)
        profile_section = self.create_profile_section(pick_file)
        carousel, update_carousel = self.create_carousel(next_image, previous_image)
        bottom_menu = self.create_bottom_menu(menu_item_clicked)

        """Conteúdo principal da página"""
        
        content = ft.Column([
            header,
            ft.Container(
                content=ft.Column([
                    ft.Text("Bem-vindo à Fábrica de Programadores!", size=18, 
                           weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    profile_section,
                    carousel,
                    ft.Text("Explore nossos cursos e materiais!", size=14, 
                           color=self.secondary_color, text_align=ft.TextAlign.CENTER),
                    ft.Container(
                        content=ft.Column([
                            ft.Text("Área de conteúdo principal", size=18, 
                                   weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            ft.Divider(height=20, color=self.primary_color),
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        height=300, bgcolor="#E9E9E9", padding=25, border_radius=15, margin=10
                    )
                ], scroll=ft.ScrollMode.ADAPTIVE, expand=True),
                padding=15, expand=True
            )
        ], expand=True)

        # Layout final
        page.add(
            ft.Stack([
                content,
                overlay,
                drawer,
                ft.Container(content=bottom_menu, bottom=0, left=0, right=0)
            ], expand=True)
        )

        """função de rodar o carrosel automaticamente"""
        
        def auto_play():
            import time
            while self.auto_play_enabled:
                time.sleep(3)
                if self.auto_play_enabled:
                    self.carousel_index = (self.carousel_index + 1) % len(self.carousel_images)
                    page.run_task(lambda: update_carousel() or page.update())

        page.run_thread(auto_play)

# Executar aplicação
app = App()
ft.app(target=app.main)