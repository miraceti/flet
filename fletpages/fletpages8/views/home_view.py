import flet as ft
from fletx import Xview
import maindata as md

class HomeView(Xview):
    def build(self):
        return ft.View(
            controls=[
                ft.Container(
                    #width=400,  # Largeur fixe
                    #height=700,  # Hauteur fixe
                    content=ft.Stack(
                        controls=[
                            # ✅ Image de fond locale
                            ft.Image(
                                src="exo1.jpg",
                                #width=400,
                                #height=700,
                                expand=True,
                                fit=ft.ImageFit.COVER,
                            ),
                            # ✅ Contenu par-dessus l'image
                            ft.Container(
                                #width=400,
                                #height=700,
                                content=ft.Column(
                                    controls=[
                                        ft.Text(
                                            "Nombre d'exoplanètes découvertes à ce jour",
                                            size=30,
                                            color=ft.colors.WHITE,
                                            text_align=ft.TextAlign.CENTER,
                                        ),
                                        ft.Text(
                                            str(md.nb_exoplanets),
                                            size=30,
                                            color=ft.colors.RED,
                                            bgcolor=ft.colors.BLACK,
                                            weight=ft.FontWeight.BOLD,
                                            text_align=ft.TextAlign.CENTER,
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.ElevatedButton(
                                                    "Go to Next View",
                                                    on_click=lambda e: self.go("/page_001"),
                                                    color=ft.colors.WHITE,
                                                    bgcolor=ft.colors.BLUE
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
                            )
                        ]
                    ),
                    expand=True,
                )
            ]
        )
