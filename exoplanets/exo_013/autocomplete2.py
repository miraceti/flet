import flet as ft

def main(page: ft.Page):
    def on_change(e):
        filtered_options = [
            option for option in suggestions if option.lower().startswith(e.control.value.lower())
        ]
        dropdown.options = [ft.dropdown.Option(option) for option in filtered_options]
        page.update()

    def on_select(e):
        print(f"Suggestion sélectionnée: {dropdown.value}")

    suggestions = ["Python", "Java", "JavaScript", "C#", "C++", "Go", "Swift"]

    text_field = ft.TextField(
        label="Langage de programmation",
        on_change=on_change,
        text_style=ft.TextStyle(size=20),  # Taille du texte personnalisée
    )

    dropdown = ft.Dropdown(
        on_change=on_select,
        width=300  # Ajustez la largeur si nécessaire
    )

    page.add(text_field, dropdown)

ft.app(target=main)

