import flet as ft
from fletx import Xview

class page_002(Xview):
    def build(self):
        return ft.View(
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Text("ceci est la page 2", size=30),
                            alignment=ft.alignment.top_center
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton("Go to previous View", on_click=lambda e: self.go("/page_001"),
                                                  color=ft.colors.WHITE,
                                                    bgcolor=ft.colors.GREEN),
                                ft.ElevatedButton("Go to next View", on_click=lambda e: self.go("/page_003"),
                                                    color=ft.colors.WHITE,
                                                    bgcolor=ft.colors.BLUE),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        ft.Row(
                            controls=[
                                ft.Tabs(
                                    selected_index=0,
                                    animation_duration=300,
                                    tabs=[
                                        ft.Tab(text="t1", icon=ft.Icon(name=ft.Icons.FAVORITE, color=ft.Colors.PINK),
                                                
                                                ),     
                                        
                                        ft.Tab(text="t2", 
                                               icon=ft.Icon(name=ft.Icons.LOCAL_FIRE_DEPARTMENT, color=ft.Colors.RED),
                                               
                                               
                                        ),
                                        ft.Tab(text="t3", icon=ft.Icon(name=ft.Icons.LOCAL_CAFE, color=ft.Colors.GREEN),
                                               
                                        ),
                                        ft.Tab( text="t4", 
                                                icon=ft.Icon(name=ft.Icons.LOCAL_PHONE, color=ft.Colors.BLUE),


                                        ),
                                        ft.Tab(text="t5", icon=ft.Icon(name=ft.Icons.LOCAL_BAR, color=ft.Colors.ORANGE),
                                               
                                               ),
                                        ft.Tab(text="t6", icon=ft.Icon(name=ft.Icons.LOCAL_AIRPORT, color=ft.Colors.PURPLE),
                                               
                                               ),
                                        ft.Tab(text="t7", icon=ft.Icon(name=ft.Icons.ELECTRIC_BIKE, color=ft.Colors.YELLOW),
                                               
                                               ),
                                    ],
                                    expand=1,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                ),
            ],
        )

