import flet as ft

def main(page: ft.Page):
    # Liste des suggestions
    suggestions = ["Python", "Java", "JavaScript", "C#", "C++", "Go", "Swift"]

    # Créez une liste pour afficher les suggestions filtrées
    suggestion_list = ft.ListView(height=200)

    # Fonction qui met à jour les suggestions affichées
    def on_text_change(e):
        typed_value = e.control.value.lower()
        suggestion_list.controls.clear()
        
        for suggestion in suggestions:
            if suggestion.lower().startswith(typed_value):
                suggestion_list.controls.append(
                    ft.TextButton(suggestion, on_click=on_suggestion_click)
                )
        page.update()

    # Fonction qui gère le clic sur une suggestion
    def on_suggestion_click(e):
        text_field.value = e.control.text
        suggestion_list.controls.clear()
        page.update()

    # Champ de texte personnalisé avec la taille de police modifiée
    text_field = ft.TextField(
        label="Langage de programmation",
        on_change=on_text_change,
        text_style=ft.TextStyle(size=20),  # Taille du texte modifiée
    )

    # Ajout du champ de texte et de la liste de suggestions à la page
    page.add(text_field, suggestion_list)

ft.app(target=main)

