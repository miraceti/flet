import flet
from flet import (
    UserControl, Page, Column, Row, icons,
    Container, Text, padding, alignment,
    LinearGradient, IconButton, GridView,
    transform, animation, colors, Stack
)
import flet as ft
from urllib.request import urlopen
import json
import datetime

# Exoplanet data fetching
urlexo1 = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+count(pl_name)+as+nbe+from+ps+where+default_flag=1&format=json"
data = json.loads(urlopen(urlexo1).read().decode("utf-8"))
nb_exoplanets = data[0]['nbe']

now = datetime.date.today()
y0 = now.year

# Data fetching with multiple fields
urlexo7 = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,hostname,pl_letter,pl_bmasse,pl_bmassj,pl_rade,pl_radj,pl_orbper,pl_dens,pl_trandur,pl_ratror,sy_snum,sy_pnum,sy_mnum,st_mass,st_lum,st_age,st_dens,sy_dist,disc_year,disc_telescope,discoverymethod+from+ps+where+default_flag=1&format=json"
list7 = json.loads(urlopen(urlexo7).read().decode("utf-8"))

# Number of planets discovered per year
y0 = datetime.date.today().year
year_counts = {y: 0 for y in range(y0 - 9, y0 + 1)}
for planet in list7:
    disc_year = planet['disc_year']
    if disc_year is not None and disc_year in year_counts:
        year_counts[disc_year] += 1

# Number of planets by distance
distance_counts = {f'{i}0-{i+1}0': 0 for i in range(10)}
for planet in list7:
    distance = planet['sy_dist']
    if distance is not None:
        bucket = min(int(distance // 10), 9)
        distance_counts[f'{bucket}0-{bucket+1}0'] += 1

col1 = "col1"
col2 = "col2"
col3 = "col3"

class Exoplanet(Stack):

    def colnom_0(self, e):
        self.datatable.columns[0].label = "col01"
        self.datatable.update()

    def hover_animation(self, e):
        if e.data == 'true':
            e.control.content.controls[2].offset = transform.Offset(0, 0)
            e.control.content.controls[2].opacity = 1.0
            e.control.update()
        else:
            e.control.content.controls[2].offset = transform.Offset(0, 1)
            e.control.content.controls[2].opacity = 0.0
            e.control.update()

    def change_icon(self, e):
        e.control.selected = not e.control.selected
        e.control.icon_color = 'white' if e.control.selected else 'white54'
        e.control.update()

    def icon(self, name, color, selected):
        return IconButton(
            icon=name,
            icon_size=18,
            icon_color=color,
            selected=selected,
            on_click=lambda e: self.change_icon(e),
        )

    def highlight_link(self,e):
        e.control.style.color = ft.colors.BLUE
        e.control.update()

    def unhighlight_link(self,e):
        e.control.style.color = None
        e.control.update()

    def MainContainer(self):
        self.main = Container(
            width=340, height=680, bgcolor='black', 
            border_radius=35, padding=8,
        )

        self.main_col = Column()

        self.green_container = Container(
            width=self.main.width,
            height=self.main.height * 0.45,
            border_radius=30,
            gradient=LinearGradient(
                begin=alignment.top_left,
                end=alignment.bottom_right,
                colors=["#01171c","#7de3fa"],
            ),
        )

        self.inner_green_container = Container(
            width=self.green_container.width,
            height=self.green_container.height,
            content=Row(
                spacing=0,
                controls=[
                    Column(
                        expand=4,
                        controls=[
                            Container(
                                padding=20, 
                                expand=True,
                                content=Row(
                                    controls=[
                                        Column(
                                            horizontal_alignment='center',
                                            controls=[
                                                Text(
                                                    'EXOPLANETES CONFIRMEES',
                                                    color='white',
                                                    size=18,
                                                    weight='bold',
                                                ),
                                                Text(
                                                    str(nb_exoplanets),
                                                    color='white',
                                                    size=18,
                                                    weight='bold',
                                                ),
                                                Text(
                                                    disabled=False,
                                                    color=colors.BLACK,
                                                    text_align=ft.TextAlign.CENTER,
                                                    spans=[
                                                        ft.TextSpan(
                                                            "Go to NASA Exoplanet Archive",
                                                            ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                                                            url="https://exoplanetarchive.ipac.caltech.edu",
                                                        )
                                                    ],
                                                ),
                                                Row(
                                                    [
                                                        ft.Container(
                                                            content=ft.Text("0",color=colors.BLACK,weight='bold'),
                                                            margin=5,
                                                            padding=5,
                                                            alignment=ft.alignment.center,
                                                            bgcolor=ft.colors.AMBER,
                                                            width=20,
                                                            height=30,
                                                            border_radius=10,
                                                            on_click=lambda e: self.colnom_0(e),
                                                        ),
                                                        ft.Container(
                                                            content=ft.Text("1",color=colors.BLACK,weight='bold'),
                                                            margin=5,
                                                            padding=5,
                                                            alignment=ft.alignment.center,
                                                            bgcolor=ft.colors.GREEN_200,
                                                            width=20,
                                                            height=30,
                                                            border_radius=10,
                                                            on_click=lambda e: print("VERT"),
                                                        ),
                                                        ft.Container(
                                                            content=ft.Text("2",color=colors.BLACK,weight='bold'),
                                                            margin=5,
                                                            padding=5,
                                                            alignment=ft.alignment.center,
                                                            bgcolor=ft.colors.CYAN_200,
                                                            width=20,
                                                            height=30,
                                                            border_radius=10,
                                                            on_click=lambda e: print("CYAN"),
                                                        ),
                                                        ft.Container(
                                                            content=ft.Text("3",color=colors.BLACK,weight='bold'),
                                                            margin=5,
                                                            padding=5,
                                                            alignment=ft.alignment.center,
                                                            bgcolor=ft.colors.RED_200,
                                                            width=20,
                                                            height=30,
                                                            border_radius=10,
                                                            on_click=lambda e: print("ROUGE"),
                                                        ),
                                                    ],
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                ),
                                                self.datatable := ft.DataTable(
                                                    width=280,
                                                    bgcolor="yellow",
                                                    heading_row_height=20,
                                                    heading_row_color="#5e0b66",
                                                    data_row_min_height=35,
                                                    data_row_max_height=35,
                                                    data_row_color={"hovered":"0x30FF0000"},
                                                    border_radius=30,
                                                    columns=[
                                                        ft.DataColumn(ft.Text(str(col1),
                                                                              color="yellow",
                                                                              weight="bold")),
                                                        ft.DataColumn(ft.Text(str(col2),
                                                                              color="yellow",
                                                                              weight="bold",
                                                                              )),
                                                        ft.DataColumn(ft.Text(str(col3),
                                                                              color="yellow",
                                                                              weight="bold"
                                                                              )),
                                                                              
                                                    ],
                                                    rows=[
                                                        ft.DataRow(
                                                           cells=[
                                                                ft.DataCell(ft.Text("cel11")),
                                                                ft.DataCell(ft.Text("cel12")),
                                                                ft.DataCell(ft.Text("cel13")), 
                                                           ],   
                                                       ),
                                                        ft.DataRow(
                                                            cells=[
                                                                ft.DataCell(ft.Text("cel21")),
                                                                ft.DataCell(ft.Text("cel22")),
                                                                ft.DataCell(ft.Text("cel23")), 
                                                           ],
                                                       ),
                                                        ft.DataRow(
                                                           cells=[
                                                               ft.DataCell(ft.Text("cel31")),
                                                               ft.DataCell(ft.Text("cel32")),
                                                               ft.DataCell(ft.Text("cel33")), 
                                                           ],
                                                       ),    
                                                   ],
                                                ),
                                            ],
                                        ),
                                    ]
                                ),
                            )
                        ],
                    ),
                    Column(
                        expand=1,
                        controls=[
                            Container(
                                padding=padding.only(right=10),
                                expand=True,
                                content=Row(
                                    alignment='center',
                                    controls=[
                                        Column(
                                            alignment='center',
                                            horizontal_alignment='center',
                                            controls=[
                                                Column(
                                                    alignment='center',
                                                    horizontal_alignment='start',
                                                    controls=[],
                                                )
                                            ],
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )

        self.grid_distances = GridView(
            expand=True,
            max_extent=150,
            runs_count=0,
            spacing=12,
            run_spacing=5,
            horizontal=True,
        )

        self.grid_decouverte = GridView(
            expand=True,
            max_extent=150,
            runs_count=0,
            spacing=12,
            run_spacing=5,
        )

        self.main_content_area = Container(
            width=self.main.width,
            height=self.main.height * 0.50,
            padding=padding.only(top=10, left=10, right=10),
            content=Column(
                spacing=20,
                controls=[
                    Row(
                        alignment='spaceBetween',
                        vertical_alignment='end',
                        controls=[
                            Container(
                                content=Text(
                                    'Nombres planètes par distances',
                                    color=colors.BLACK,
                                    size=16,
                                    weight='bold',
                                ),
                            ),
                        ],
                    ),
                    self.grid_distances,
                    Row(
                        alignment='spaceBetween',
                        vertical_alignment='end',
                        controls=[
                            Container(
                                content=Text(
                                    'Planètes découvertes par année',
                                    color=colors.BLACK,
                                    size=16,
                                    weight='bold',
                                ),
                            ),
                        ],
                    ),
                    self.grid_decouverte,
                ],
            ),
        )

        self.main_col.controls.extend(
            [self.inner_green_container, self.main_content_area]
        )

        self.main.content = self.main_col
        self.controls.append(self.main)

    def __init__(self):
        super().__init__()
        self.datatable = None
        self.MainContainer()

def main(page: Page):
    page.title = "Exoplanet App"
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.bgcolor = '#f8f8f8'
    page.update()

    exoplanet = Exoplanet()
    page.add(exoplanet)

flet.app(target=main)
