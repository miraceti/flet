import flet
from flet import (
    UserControl, Page, Column, Row, icons,
    Container, Text, padding, alignment,
    LinearGradient,IconButton,GridView,
    transform, animation,colors,Stack,
        )
import flet as ft
from urllib.request import urlopen
import json

import datetime
import matplotlib
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart

#######################
urlexo1 = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+count(pl_name)+as+nbe+from+ps+where+default_flag=1&format=json"
print(urlexo1)
data = json.loads(urlopen(urlexo1).read().decode("utf-8"))
# print(data)
data0=data[0]
# print(data0)
nb_exoplanets= data0['nbe']
print(nb_exoplanets)
######################
now = datetime.date.today()
y0 = now.year
print(y0)

############################################################
#data de champs multiples
urlexo7 = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+\
pl_name,hostname,pl_letter,pl_bmasse,pl_bmassj,pl_rade,pl_radj,pl_orbper,pl_dens,pl_trandur,pl_ratror,\
sy_snum,sy_pnum,sy_mnum,st_mass,st_lum,st_age,st_dens,sy_dist,disc_year,disc_telescope,discoverymethod\
+from+ps+where+default_flag=1&format=json"

list7 = json.loads(urlopen(urlexo7).read().decode("utf-8"))
print((list7[0]).keys())
print((list7[0]).values())
print((list7[0]).items())
dict_7_0 = list7[0]
print(dict_7_0)

#############################################################
#nombre de planetes par années
#nombre de planete par année
y0=y1=y2=y3=y4=y5=y6=y7=y8=y9=y10=0
now = datetime.date.today()
y0 = now.year
for planete in list7:
    #print(planete['pl_name'])
    if planete['disc_year'] is None: 
        pass
    else:
        if planete['disc_year'] == y0 :
            #print(planete['pl_name'])
            y1+=1
        elif planete['disc_year'] == y0  -1 :
            #print(planete['pl_name'])
            y2+=1
        elif planete['disc_year'] == y0 - 2 :
            #print(planete['pl_name'])
            y3+=1
        elif planete['disc_year'] == y0 - 3 :
            #print(planete['pl_name'])
            y4+=1
        elif planete['disc_year'] == y0 - 4 :
            #print(planete['pl_name'])
            y5+=1
        elif planete['disc_year'] == y0 - 5 :
            #print(planete['pl_name'])
            y6+=1
        elif planete['disc_year'] == y0 - 6 :
            #print(planete['pl_name'])
            y7+=1
        elif planete['disc_year'] == y0 - 7 :
            #print(planete['pl_name'])
            y8+=1
        elif planete['disc_year'] == y0 - 8 :
            #print(planete['pl_name'])
            y9+=1
        else:
            y10+=1

print("nombre de planetes par année de découverte")            
print(str(y0 ),' : ',y1)
print(str(y0 - 1 ),' : ',y2)
print(str(y0 - 2 ),' : ',y3)
print(str(y0 - 3),' : ',y4)
print(str(y0 - 4),' : ',y5)
print(str(y0 - 5),' : ',y6)
print(str(y0 - 6),' : ',y7)
print(str(y0 - 7),' : ',y8)
print(str(y0 - 8),' : ',y9)
print(str(y0 - 9),' : ',y10)

#############################################################
#############################################################
#nombre de planetes par distances
d10=d20=d30=d40=d50=d60=d70=d80=d90=d100=0
for planete in list7:
    #print(planete['pl_name'])
    if planete['sy_dist'] is None: 
        pass
    else:
        if planete['sy_dist'] < 10.00:
            #print(planete['pl_name'])
            d10+=1
        elif planete['sy_dist'] >= 10.00 and planete['sy_dist'] < 20.00:
            #print(planete['pl_name'])
            d20+=1
        elif (planete['sy_dist'] >= 20.00) and (planete['sy_dist']) < 30.00:
            #print(planete['pl_name'])
            d30+=1
        elif (planete['sy_dist'] >= 30.00) and (planete['sy_dist']) < 40.00:
            #print(planete['pl_name'])
            d40+=1
        elif (planete['sy_dist'] >= 40.00) and (planete['sy_dist']) < 50.00:
            #print(planete['pl_name'])
            d50+=1
        elif (planete['sy_dist'] >= 50.00) and (planete['sy_dist']) < 60.00:
            #print(planete['pl_name'])
            d60+=1
        elif (planete['sy_dist'] >= 60.00) and (planete['sy_dist']) < 70.00:
            #print(planete['pl_name'])
            d70+=1
        elif (planete['sy_dist'] >= 70.00) and (planete['sy_dist']) < 80.00:
            #print(planete['pl_name'])
            d80+=1
        elif (planete['sy_dist'] >= 80.00) and (planete['sy_dist']) < 90.00:
            #print(planete['pl_name'])
            d90+=1
        else:
            d100+=1

print("Nombre de planètes par bloc de distances 10 parsec")            
print(d10)
print(d20)
print(d30)
print(d40)
print(d50)
print(d60)
print(d70)
print(d80)
print(d90)
print(d100)

col1=str("col1")
col2=str("col2")
col3=str("col3")

#############################################################

class Exoplanet(Stack):
    
    def colnom_0(self,e):
            self.datatable.columns[0].label="col01"
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

        # self.notification = self.icon(icons.NOTIFICATIONS, 'white54', True)
        # self.hide = self.icon(icons.HIDE_SOURCE, 'white54', False)
        # self.chat = self.icon(icons.CHAT_ROUNDED, 'white54', False)


        # self.icon_column=Column(
        #     alignment='center',
        #     spacing=5,
        #     controls=[
        #         self.notification,
        #         self.hide,
        #         self.chat,
        #     ],
        # )

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
                                                    # ink=True,
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
                                                    # ink=True,
                                                    on_click=lambda e: print("ROUGE"),
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                                ),
                                                datatable := ft.DataTable(
                                                    width=280,
                                                    bgcolor="yellow",
                                                    heading_row_height=20,
                                                    heading_row_color="#5e0b66",
                                                    data_row_min_height=35,
                                                    data_row_max_height=35,
                                                    data_row_color =({"hovered":"0x30FF0000"}),
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
                                                                # ft.DataCell(ft.Text("cel14")),                                                             
                                                           ],   
                                                       ),
                                                        ft.DataRow(
                                                            cells=[
                                                                ft.DataCell(ft.Text("cel21")),
                                                                ft.DataCell(ft.Text("cel22")),
                                                                ft.DataCell(ft.Text("cel23")), 
                                                                # ft.DataCell(ft.Text("cel24")),                                                             
                                                           ],
                                                       ),
                                                        ft.DataRow(
                                                           cells=[
                                                               ft.DataCell(ft.Text("cel31")),
                                                               ft.DataCell(ft.Text("cel32")),
                                                               ft.DataCell(ft.Text("cel33")), 
                                                            #    ft.DataCell(ft.Text("cel43")),                                                             
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
                                    'Nombres planètes par distances',
                                    size=14,
                                    color='white',
                                    weight='bold',
                                )
                            ),
                        ]
                    ),
                    Container(
                        height=50,
                        content=self.grid_distances,
                    ),
                    Row(
                        alignment='spaceBetween',
                        vertical_alignment='end',
                        controls=[
                            Container(
                                content=Text(
                                    'Nombres planetes découvertes par années',
                                    size=14,
                                    color='white',
                                    weight='bold',
                                )
                            ),
                        ],
                    ),
                    self.grid_decouverte,
                ],
            ),
        )

        distance_list = [["10", str(d10)],
                     ["20", str(d20)],
                     ["30", str(d30)],
                     ["40", str(d40)],
                     ["50", str(d50)],
                     ["60", str(d60)],
                     ["70", str(d70)],
                     ["80", str(d80)],
                     ["90", str(d90)],
                     ["100", str(d100)],
                     ]
        for i in distance_list:
            __ = Container(
                width=100,
                height=100,
                bgcolor='white10',
                border_radius=15,
                alignment=alignment.center,
                content = Text( f'{i}',color='white', weight='bold' ),
            )
            self.grid_distances.controls.append(__)

            for x in i:
                __.content = Column(
                    alignment='center',
                    horizontal_alignment='center',
                    controls=[
                        Text(f'{i[0]}', size=11, color='yellow54'),
                        Text(f'{i[1]}', size=16,color='white', weight='bold'),
                    ]
                )

        decouverte_list = [
            [str(y0), str(y1)],
            [str(y0 - 1), str(y2)],
            [str(y0 - 2), str(y3)],
            [str(y0 - 3), str(y4)],
            [str(y0 - 4), str(y5)],
            [str(y0 - 5), str(y6)],
            [str(y0 - 6), str(y7)],
            [str(y0 - 7), str(y8)],
            [str(y0 - 8), str(y9)],
            [str(y0 - 9), str(y10)],       
        ]
        for i in decouverte_list:
            __ = Container(
                width=100,
                height=100,
                bgcolor='white10',
                border_radius=15,
                alignment=alignment.center,
                content = Text( f'{i}',color='white', weight='bold' ),
                # on_hover=lambda e: self.hover_animation(e),
            )
            self.grid_decouverte.controls.append(__)

            for x in i:
                __.content = Column(
                    alignment='center',
                    horizontal_alignment='center',
                    controls=[
                        Text(f'{i[0]}', size=11, color='yellow54'),
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

            
        # for icon in self.icon_column.controls[:]:
        #     if icon.selected== True:
        #         icon.icon_color = 'white'
        
        return self.main
    

    # def build(self):
    #     return Column(controls=[self.MainContainer(),])


def start(page: Page):
    page.title='Flet Exoplanets Concept'
    page.horizontal_alignment='center'
    page.vertical_alignment='center'
    #page.theme_mode = flet.ThemeMode.DARK
    
    app = Exoplanet()
    page.add(app)
    page.update()
    
    
if __name__ == '__main__':
    flet.app(target=start)


