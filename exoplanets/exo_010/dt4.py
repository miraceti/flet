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
print("keys : ",(list7[0]).keys())
print("values : ",(list7[0]).values())
print("items : ",(list7[0]).items())
dict_7_0 = list7[0]
print("dict_7-0 : ",dict_7_0)

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

#liste des planetes les plus proches : 3
distmax = 100000
p1="vide"
p=0
planete_dist=[]
for planete in list7:
    if planete['sy_dist'] is None:
        pass
    else:
        p+=1
        planete_dist.append((planete['pl_name'], 
                             planete['sy_dist'], 
                             planete['pl_bmasse'], 
                             planete['pl_rade'],
                             planete['pl_dens'],))
        if planete['sy_dist'] < distmax:
            pl = planete['pl_name']#planete la plus proche 
            distmax = planete['sy_dist']

planete_la_plus_proche = pl
print("planete la plus proche : ", pl)

#tri par ordre de distance
proche_list = sorted(planete_dist, key= lambda x: x[1])
print(proche_list[:3])

#entete tableau depart
col1=str("col01")
col2=str("col02")
col3=str("col03")

#entete tableau new
ncol1 = str("ncoll1")
ncol2 = str("ncoll2")
ncol3 = str("ncoll3")

################################################tableau 0
n0col01 = str("pl_name")
n0col02 = str("sy_dist")
n0col03 = str("pl_bmasse")

n0cel01 = proche_list[0][0]
n0cel02 = proche_list[0][1]
n0cel03 = proche_list[0][2]

n0cel11 = proche_list[1][0]
n0cel12 = proche_list[1][1]
n0cel13 = proche_list[1][2]

n0cel21 = proche_list[2][0]
n0cel22 = proche_list[2][1]
n0cel23 = proche_list[2][2]
##########################################################


##################################################tableau 1
n1col01 = str("pl_name")
n1col02 = str("pl_rade")
n1col03 = str("pl_dens")

n1cel01 = proche_list[0][0]
n1cel02 = proche_list[0][3]
n1cel03 = proche_list[0][4]

n1cel11 = proche_list[1][0]
n1cel12 = proche_list[1][3]
n1cel13 = proche_list[1][4]

n1cel21 = proche_list[2][0]
n1cel22 = proche_list[2][3]
n1cel23 = proche_list[2][4]
#########################################################


#################################################tableau 2

#########################################################


################################################tableau 3

########################################################


###############################################tableau 4

########################################################


###############################################tableau 5

#######################################################

#############################################################

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
            width=350, height=700, bgcolor='black', 
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
        def table_0(e):
            print(self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[3].controls[0].content)
            #text {'value': '0', 'weight': 'bold', 'color': 'black', 'n': 'content'}

            #nom des colonne
            print(self.datatable.columns[0].label) 
            print(self.datatable.columns[0].label.value) 
            self.datatable.columns[0].label.value=str(n0col01)
            self.datatable.columns[1].label.value=str(n0col02)
            self.datatable.columns[2].label.value=str(n0col03)
            print(self.datatable.bgcolor)
            self.datatable.bgcolor = ft.colors.AMBER

            #valeur des cellules par ligne
            print(self.datatable.rows[0].cells[1].content.value)
            self.datatable.rows[0].cells[0].content.value = str(n0cel01)
            self.datatable.rows[0].cells[1].content.value = str(n0cel02)
            self.datatable.rows[0].cells[2].content.value = str(n0cel03)

            self.datatable.rows[1].cells[0].content.value = str(n0cel11)
            self.datatable.rows[1].cells[1].content.value = str(n0cel12)
            self.datatable.rows[1].cells[2].content.value = str(n0cel13)

            self.datatable.rows[2].cells[0].content.value = str(n0cel21)
            self.datatable.rows[2].cells[1].content.value = str(n0cel22)
            self.datatable.rows[2].cells[2].content.value = str(n0cel23)
            print(self.datatable.rows[0].cells[1].content.value)

            Exoplanet.update(self)

        def table_1(e):
            #nom des colonnes
            self.datatable.columns[0].label.value=str(ncol2)
            print(self.datatable.bgcolor)
            self.datatable.bgcolor = ft.colors.GREEN_200
            self.datatable.columns[0].label.value=str(n1col01)
            self.datatable.columns[1].label.value=str(n1col02)
            self.datatable.columns[2].label.value=str(n1col03)

            #valeur des cellules par ligne
            self.datatable.rows[0].cells[0].content.value = str(n1cel01)
            self.datatable.rows[0].cells[1].content.value = str(n1cel02)
            self.datatable.rows[0].cells[2].content.value = str(n1cel03)

            self.datatable.rows[1].cells[0].content.value = str(n1cel11)
            self.datatable.rows[1].cells[1].content.value = str(n1cel12)
            self.datatable.rows[1].cells[2].content.value = str(n1cel13)

            self.datatable.rows[2].cells[0].content.value = str(n1cel21)
            self.datatable.rows[2].cells[1].content.value = str(n1cel22)
            self.datatable.rows[2].cells[2].content.value = str(n1cel23)
            print(self.datatable.rows[0].cells[1].content.value)

            Exoplanet.update(self)

        def table_2(e):
            #nom des colonnes
            self.datatable.columns[0].label.value=str(ncol2)
            print(self.datatable.bgcolor)
            self.datatable.bgcolor = ft.colors.CYAN_200

            #valeur des cellules par ligne
            self.datatable.rows[0].cells[1].content.value = "cel112"

            Exoplanet.update(self)

        def table_3(e):
            #nom des colonnes
            self.datatable.columns[0].label.value=str(ncol2)
            print(self.datatable.bgcolor)
            self.datatable.bgcolor = ft.colors.RED_200

            #valeur des cellules par ligne
            self.datatable.rows[0].cells[1].content.value = "cel112"

            Exoplanet.update(self)

        def table_4(e):
            #nom des colonnes
            self.datatable.columns[0].label.value=str(ncol2)
            print(self.datatable.bgcolor)
            self.datatable.bgcolor = ft.colors.PURPLE_200

            #valeur des cellules par ligne
            self.datatable.rows[0].cells[1].content.value = "cel112"

            Exoplanet.update(self)

        def table_5(e):
            #nom des colonnes
            self.datatable.columns[0].label.value=str(ncol2)
            print(self.datatable.bgcolor)
            self.datatable.bgcolor = ft.colors.DEEP_ORANGE

            #valeur des cellules par ligne

            self.datatable.rows[0].cells[1].content.value = "cel112"
            print(self.datatable.rows[0].cells[1].content.value)


            Exoplanet.update(self)

        self.datatable=ft.DataTable(
                    width=340,
                    bgcolor="yellow",
                    column_spacing=1,
                    heading_row_height=20,
                    heading_row_color="#5e0b66",
                    data_row_min_height=25,
                    data_row_max_height=25,
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
                                ft.DataCell(ft.Text("cel11", size=10, weight="bold")),
                                ft.DataCell(ft.Text("cel12", size=10, weight="bold")),
                                ft.DataCell(ft.Text("cel13", size=10, weight="bold")), 
                                # ft.DataCell(ft.Text("cel14")),                                                             
                            ],   
                        ),
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("cel21", size=10, weight="bold")),
                                ft.DataCell(ft.Text("cel22", size=10, weight="bold")),
                                ft.DataCell(ft.Text("cel23", size=10, weight="bold")), 
                                # ft.DataCell(ft.Text("cel24")),                                                             
                            ],
                        ),
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("cel31", size=10, weight="bold")),
                                ft.DataCell(ft.Text("cel32", size=10, weight="bold")),
                                ft.DataCell(ft.Text("cel33", size=10, weight="bold")), 
                            #    ft.DataCell(ft.Text("cel43")),                                                             
                            ],
                        ),    
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
                        expand=8,
                        controls=[
                            Container(
                                padding=20, 
                                expand=True,
                                content=Row(
                                    controls=[
                                        Column(
                                            expand=True,
                                            horizontal_alignment='center',
                                            controls=[
                                                Text(
                                                    'EXOPLANETES CONFIRMEES',
                                                    color=colors.LIGHT_BLUE,
                                                    size=16,
                                                    weight='bold',

                                                ),
                                                Text(
                                                    str(nb_exoplanets),
                                                    color='white',
                                                    size=20,
                                                    weight='bold',
                                                    #text_align=ft.TextAlign.CENTER,
                                                ),
                                                Text(
                                                    disabled=False,
                                                    color=colors.YELLOW,
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
                                                    on_click= table_0,
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
                                                    on_click=table_1,
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
                                                    on_click=table_2,
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
                                                    on_click=table_3,
                                                ),
                                                ft.Container(
                                                    content=ft.Text("4",color=colors.BLACK,weight='bold'),
                                                    margin=5,
                                                    padding=5,
                                                    alignment=ft.alignment.center,
                                                    bgcolor=ft.colors.PURPLE_200,
                                                    width=20,
                                                    height=30,
                                                    border_radius=10,
                                                    # ink=True,
                                                    on_click=table_4,
                                                ),
                                                ft.Container(
                                                    content=ft.Text("5",color=colors.BLACK,weight='bold'),
                                                    margin=5,
                                                    padding=5,
                                                    alignment=ft.alignment.center,
                                                    bgcolor=ft.colors.DEEP_ORANGE,
                                                    width=20,
                                                    height=30,
                                                    border_radius=10,
                                                    # ink=True,
                                                    on_click=table_5,
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                                ),
                                                Text(
                                                    "planetes les plus proches",
                                                    color='white',
                                                    size=15,
                                                    weight='bold',
                                                    #text_align=ft.TextAlign.CENTER,
                                                ),
                                                self.datatable,
                                            ],
                                        ),
                                    ]
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
                                    'Nombres planètes par distances (parsec)',
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
                                    'Nombres planetes par années',
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


