import flet as ft

# Simulons une grande liste de dictionnaires
data = [
    {"name": f"Language {i}", "description": f"Description for language {i}"} 
    for i in range(1, 5001)
]

def main(page: ft.Page):
    suggestion_list = ft.ListView(height=200)

    def on_text_change(e):
        # Filtrer les données en fonction de la saisie
        query = e.control.value.lower()
        filtered_data = [item for item in data if query in item["name"].lower()]
        
        # Limiter les résultats à 10 éléments
        suggestion_list.controls.clear()
        for item in filtered_data[:10]:
            suggestion_list.controls.append(
                ft.TextButton(item["name"], on_click=lambda e, item=item: select_item(e, item))
            )
        page.update()

    def select_item(e, item):
        text_field.value = item["name"]
        suggestion_list.controls.clear()
        page.update()

    text_field = ft.TextField(
        label="Langage de programmation",
        on_change=on_text_change,
        text_style=ft.TextStyle(size=20),
    )

    page.add(text_field, suggestion_list)

ft.app(target=main)

