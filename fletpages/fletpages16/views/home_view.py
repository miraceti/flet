import flet as ft
from fletx import Xview
import maindata as md

class HomeView(Xview):
    def __init__(self, page=None, state=None, params=None):
        print("Initializing HomeView")
        super().__init__(page=page, state=state, params=params)
        self.page = page
        self.state = state
        self.params = params

    def build(self):
        print("Building the view")

        # Conteneur pour le texte de la version
        version_bubble = ft.Container(
            content=ft.Text("Version de l'application: 16.b",
                weight=ft.FontWeight.BOLD,  # Texte en gras
                color=ft.colors.BLACK,  # Texte en noir
                ),
            bgcolor=ft.colors.BLUE_50,
            padding=10,
            border_radius=ft.border_radius.all(10),
            visible=False,  # Initialement invisible
        )

        def show_version(e):
            # Basculer la visibilité du conteneur
            version_bubble.visible = not version_bubble.visible
            self.page.update()

        # Bouton pour afficher/masquer la version
        show_version_button = ft.TextButton(
            "À propos",
            icon=ft.icons.INFO_OUTLINE,
            on_click=show_version
        )

        # Utiliser un Row pour aligner le bouton et la bulle horizontalement
        about_row = ft.Row(
            controls=[
                show_version_button,
                version_bubble
            ],
            alignment=ft.MainAxisAlignment.START,
        )

        return ft.View(
            controls=[
                ft.Container(
                    content=ft.Stack(
                        controls=[
                            ft.Image(
                                src="exo1.jpg",
                                expand=True,
                                fit=ft.ImageFit.COVER,
                            ),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text(
                                            "Nombre d'exoplanètes découvertes à ce jour",
                                            size=30,
                                            color=ft.Colors.WHITE,
                                            text_align=ft.TextAlign.CENTER,
                                        ),
                                        ft.Text(
                                            str(md.nb_exoplanets),
                                            size=30,
                                            color=ft.Colors.RED,
                                            bgcolor=ft.Colors.BLACK,
                                            weight=ft.FontWeight.BOLD,
                                            text_align=ft.TextAlign.CENTER,
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.ElevatedButton(
                                                    "Go to Next View",
                                                    on_click=lambda e: self.go("/page_001"),
                                                    color=ft.Colors.WHITE,
                                                    bgcolor=ft.Colors.BLUE
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.END,
                                        )
                                    ],
                                    spacing=30,
                                    alignment=ft.MainAxisAlignment.START,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                padding=40,
                                alignment=ft.alignment.top_center,
                            ),
                            ft.Container(
                                content=about_row,
                                left=10,
                                bottom=10,
                            )
                        ]
                    ),
                    expand=True,
                )
            ]
        )
