import flet as ft
from fletx import Xview
import matplotlib.pyplot as plt
import io
import base64

class page_001(Xview):

    def build(self):

        # Génération du graphique en camembert
        def generate_pie_base64():
            labels = ['A', 'B', 'C']
            sizes = [40, 35, 25]
            colors = ['gold', 'skyblue', 'lightcoral']
            fig, ax = plt.subplots()
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
            ax.axis('equal')
            buf = io.BytesIO()
            plt.savefig(buf, format='png', bbox_inches='tight')
            plt.close(fig)
            buf.seek(0)
            return base64.b64encode(buf.read()).decode('utf-8')

        # Image base64 pour le pie chart
        pie_base64 = generate_pie_base64()


        return ft.View(
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                ft.Column(
                    expand=True,  # << Permet aux enfants d'utiliser expand
                    controls=[
                        ft.Container(
                            content=ft.Text("ceci est la page 1", size=30),
                            alignment=ft.alignment.top_center
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton("Go to previous View", on_click=self.back,
                                                  color=ft.Colors.WHITE,
                                                  bgcolor=ft.Colors.GREEN),
                                ft.ElevatedButton("Go to next View", on_click=lambda e: self.go("/page_002"),
                                                  color=ft.Colors.WHITE,
                                                  bgcolor=ft.Colors.BLUE),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        ft.Container(
                            expand=True,
                            content=ft.ListView(
                                expand=True,
                                spacing=10,
                                padding=10,
                                controls=[
                                    ft.Container(
                                        content=ft.Image(src_base64=pie_base64, width=300, height=300),
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.Colors.AMBER,
                                        width=300,
                                        height=300,
                                        border_radius=10,
                                    ),
                                    ft.Container(
                                        content=ft.Text("Non clickable"),
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.Colors.PURPLE,
                                        width=300,
                                        height=300,
                                        border_radius=10,
                                    ),
                                    ft.Container(
                                        content=ft.Text("Non clickable"),
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.Colors.RED,
                                        width=300,
                                        height=300,
                                        border_radius=10,
                                    ),
                                    ft.Container(
                                        content=ft.Text("Non clickable"),
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.Colors.GREEN,
                                        width=300,
                                        height=300,
                                        border_radius=10,
                                    ),
                                    ft.Container(
                                        content=ft.Text("Non clickable"),
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.Colors.ORANGE,
                                        width=300,
                                        height=300,
                                        border_radius=10,
                                    ),
                                    ft.Container(
                                        content=ft.Text("Non clickable"),
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.Colors.YELLOW,
                                        width=300,
                                        height=300,
                                        border_radius=10,
                                    ),
                                    ft.Container(
                                        content=ft.Text("Non clickable"),
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.Colors.PINK,
                                        width=300,
                                        height=300,
                                        border_radius=10,
                                    ),
                                ]
                            )
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                )
            ]
        )
