import flet as ft

def main(page):
    # Criação do NavigationRail
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.FAVORITE_BORDER,
                selected_icon=ft.Icons.FAVORITE,
                label="First",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.BOOKMARK_BORDER),
                selected_icon=ft.Icon(ft.Icons.BOOKMARK),
                label="Second",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.SETTINGS_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.SETTINGS),
                label_content=ft.Text("Settings"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
        visible=False  # Inicialmente o NavigationRail está invisível
    )

    # Função que alterna a visibilidade do NavigationRail
    def toggle_navigation_rail(e):
        rail.visible = not rail.visible
        page.update()  # Atualiza a interface após a mudança

    # Criação do botão para alternar a visibilidade
    toggle_button = ft.ElevatedButton(
        text="Open Navigation Rail", 
        on_click=toggle_navigation_rail
    )

    # Adiciona o botão e o NavigationRail à página
    page.add(ft.Column([toggle_button, rail]))  # O botão e o NavigationRail estão na coluna

    # Defina o título da página
    page.title = "Toggle NavigationRail"
    
    # Ajuste de tamanho da página
    page.width = 800
    page.height = 600

# Run the app
ft.app(target=main)