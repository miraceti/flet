from flet import Page, Row, Column, Text, Container, colors, alignment, padding

def main(page: Page):
    texts = ["3 premières planetes les plus proches"] * 5
    
    column_controls = [
        Container(
            content=Text(text, size=10, weight='bold', color=colors.WHITE70),
            padding=padding.only(bottom=10)  # Ajoute un espacement inférieur
        ) for text in texts
    ]
    
    content = Row(
        controls=[
            Column(
                expand=True,
                horizontal_alignment='center',
                alignment=alignment.center,
                controls=column_controls
            )
        ]
    )
    
    page.add(content)

# Appel de la fonction principale pour lancer l'application
if __name__ == "__main__":
    from flet import app
    app(target=main)
