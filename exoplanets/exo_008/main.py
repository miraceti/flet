import flet
from flet import (
    UserControl, Page, Column, Row, icons,
    Container, Text, padding, alignment,
    LinearGradient,IconButton,GridView,
    transform, animation,colors,Stack
    )

import flet as ft
from urllib.request import urlopen
import json

urlexo1 = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+count(pl_name)+as+nbe+from+ps+where+default_flag=1&format=json"
print(urlexo1)
data = json.loads(urlopen(urlexo1).read().decode("utf-8"))
# print(data)
data0=data[0]
# print(data0)
nb_exoplanets= data0['nbe']
print(nb_exoplanets)


class Exoplanet(Stack):

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
        if e.control.selected != True:
            e.control.selected = True
            e.control.icon_color = 'white'
            e.control.update()
        else:
            e.control.selected = False
            e.control.icon_color = 'white54'
            e.control.update()

    def icon(self, name, color, selected):
        return IconButton(
            icon=name,
            icon_size=18,
            icon_color=color,
            selected=selected,
            on_click=lambda e:self.change_icon(e),
        )

    def highlight_link(self,e):
        e.control.style.color = ft.colors.BLUE
        e.control.update()

    def unhighlight_link(self,e):
        e.control.style.color = None
        e.control.update()

    def MainContainer(self):
        self.main =Container(
            width=290, height=600, bgcolor='black', 
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

        self.notification = self.icon(icons.NOTIFICATIONS, 'white54', True)
        self.hide = self.icon(icons.HIDE_SOURCE, 'white54', False)
        self.chat = self.icon(icons.CHAT_ROUNDED, 'white54', False)


        self.icon_column=Column(
            alignment='center',
            spacing=5,
            controls=[
                self.notification,
                self.hide,
                self.chat,
            ],
        )

        self.inner_green_container = Container(
            width=self.green_container.width,
            height=self.green_container.height,
            #bgcolor='blue',
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
                                                    #text_align=ft.TextAlign.CENTER,
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
                                                            # on_enter=self.highlight_link,
                                                            # on_exit=self.unhighlight_link,
                                                            )
                                                    ],
                                                ),
                                                Row(
                                                    [
                                                ft.Container(
                                                    content=ft.Text("Non clickable"),
                                                    margin=10,
                                                    padding=10,
                                                    alignment=ft.alignment.center,
                                                    bgcolor=ft.colors.AMBER,
                                                    width=20,
                                                    height=30,
                                                    border_radius=10,
                                                ),
                                                ft.Container(
                                                    content=ft.Text("Clickable without Ink"),
                                                    margin=10,
                                                    padding=10,
                                                    alignment=ft.alignment.center,
                                                    bgcolor=ft.colors.GREEN_200,
                                                    width=20,
                                                    height=30,
                                                    border_radius=10,
                                                    on_click=lambda e: print("Clickable without Ink clicked!"),
                                                ),
                                                ft.Container(
                                                    content=ft.Text("Clickable with Ink"),
                                                    margin=10,
                                                    padding=10,
                                                    alignment=ft.alignment.center,
                                                    bgcolor=ft.colors.CYAN_200,
                                                    width=20,
                                                    height=30,
                                                    border_radius=10,
                                                    ink=True,
                                                    on_click=lambda e: print("Clickable with Ink clicked!"),
                                                ),
                                                ft.Container(
                                                    content=ft.Text("Clickable transparent with Ink"),
                                                    margin=10,
                                                    padding=10,
                                                    alignment=ft.alignment.center,
                                                    bgcolor=ft.colors.RED_200,
                                                    width=20,
                                                    height=30,
                                                    border_radius=10,
                                                    ink=True,
                                                    on_click=lambda e: print("Clickable transparent with Ink clicked!"),
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                                ),
                                                Text(
                                                    'TOTAL CURRENT BALANCE',
                                                    color='white',
                                                    size=10,
                                                    weight='bold',
                                                ),
                                                Text(
                                                    '11,764.28 €',
                                                    color='white',
                                                    size=22,
                                                    weight='bold',
                                                ),
                                            ]
                                        )
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
                                                    controls=[
                                                        # Container(
                                                        #     width=40,
                                                        #     height=150,
                                                        #     bgcolor='white10',
                                                        #     border_radius=14,
                                                        #     # content=self.icon_column,
                                                        # )
                                                    ]
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

        self.grid_transfers = GridView(
            expand=True,
            max_extent=150,
            runs_count=0,
            spacing=12,
            run_spacing=5,
            horizontal=True,
        )

        self.grid_payments = GridView(
            expand=True,
            max_extent=150,
            runs_count=0,
            spacing=12,
            run_spacing=5,
           
        )

        self.main_content_area = Container(
            width=self.main.width,
            height=self.main.height * 0.50,
            #bgcolor='blue',
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
                                    'Recent Transfert',
                                    size=14,
                                    color='white',
                                    weight='bold',
                                )
                            ),
                            Container(
                                content=Text(
                                    'view all',
                                    size=10,
                                    color='white54',
                                    weight='w400',
                                )
                            ),
                        ]
                    ),
                    Container(
                        height=50,
                        content=self.grid_transfers,
                    ),
                    Row(
                        alignment='spaceBetween',
                        vertical_alignment='end',
                        controls=[
                            Container(
                                content=Text(
                                    'Pending Patments',
                                    size=14,
                                    color='white',
                                    weight='bold',
                                )
                            ),
                            Container(
                                content=Text(
                                    'view all',
                                    size=10,
                                    color='white54',
                                    weight='w400',
                                )
                            ),
                        ],
                    ),
                    self.grid_payments,
                ],
            ),
        )

        info_list = ["PH","SD","WQ","KG","TY","SB","LP","LK"]
        for i in info_list:
            __ = Container(
                width=100,
                height=100,
                bgcolor='white10',
                border_radius=15,
                alignment=alignment.center,
                content = Text( f'{i}',color='white', weight='bold' ),
            )
            self.grid_transfers.controls.append(__)

        payment_list = [
            ["utilities", "$523.23"],
            ["Phone Bill", "$102.32"],
            ["Insurance", "$128.51"],
            ["Gas", "$45.65"],
            ["Groceries", "$289.42"],
            ["Documents", "$77.82"],
        ]
        for i in payment_list:
            __ = Container(
                width=100,
                height=100,
                bgcolor='white10',
                border_radius=15,
                alignment=alignment.center,
                content = Text( f'{i}',color='white', weight='bold' ),
                on_hover=lambda e: self.hover_animation(e),
            )
            self.grid_payments.controls.append(__)

            for x in i:
                __.content = Column(
                    alignment='center',
                    horizontal_alignment='center',
                    controls=[
                        Text(f'{i[0]}', size=11, color='white54'),
                        Text(f'{i[1]}', size=16,color='white', weight='bold'),

                        Text(
                            'Pay Now?',
                            color='white',
                            size=12, 
                            text_align='start',
                            weight='w600',
                            offset= transform.Offset(0, 1),
                            animate_offset = animation.Animation(duration=900, curve='decelerate'),
                            animate_opacity=300,
                            opacity=0,

                        )
                    ]
                )


        self.green_container.content = self.inner_green_container

        self.main_col.controls.append(self.green_container)
        self.main_col.controls.append(self.main_content_area)

        self.main.content = self.main_col

        for icon in self.icon_column.controls[:]:
            if icon.selected== True:
                icon.icon_color = 'white'
        
        return self.main

    def build(self):
        return Column(controls=[self.MainContainer(),])


def start(page: Page):
    page.title='Flet Expense Concept'
    page.horizontal_alignment='center'
    page.vertical_alignment='center'
    #page.theme_mode = flet.ThemeMode.DARK
    
    app = Exoplanet()
    page.add(app)
    page.update()
    
    
if __name__ == '__main__':
    flet.app(target=start)

