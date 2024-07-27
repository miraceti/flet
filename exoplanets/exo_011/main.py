import flet as ft

def main(page: ft.Page):
    page.title = "Containers - clickable and not"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    grid_distances = ft.GridView(
            expand=True,
            max_extent=150,
            runs_count=0,
            spacing=12,
            run_spacing=5,
            horizontal=True,
        )

    distance_list = [["10", str("d10")],
                     ["20", str("d20")],
                     ["30", str("d30")],
                     ["40", str("d40")],
                     ["50", str("d50")],
                     ["60", str("d60")],
                     ["70", str("d70")],
                     ["80", str("d80")],
                     ["90", str("d90")],
                     ["100", str("d100")],
                     ]
    for i in distance_list:
        __ = ft.Container(
            width=100,
            height=100,
            bgcolor='blue10',
            border_radius=15,
            alignment=ft.alignment.center,
            content = ft.Text( f'{i}',color='black', weight='bold' ),
        )
        grid_distances.controls.append(__)

        for x in i:
            __.content = ft.Column(
                alignment='center',
                horizontal_alignment='center',
                controls=[
                    ft.Text(f'{i[0]}', size=11, color='black54'),
                    ft.Text(f'{i[1]}', size=16,color='black', weight='bold'),
                ]
            )

    page.add(
        ft.Row(
            [
                ft.Container(
                        height=50,
                        content=grid_distances,
                    ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

ft.app(target=main)