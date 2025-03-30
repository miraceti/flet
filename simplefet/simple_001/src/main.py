import flet as ft
from flet import (
    UserControl, Page, Column, Row, icons,
    Container, Text, padding, alignment,
    LinearGradient,IconButton,GridView,
    transform, animation,colors,Stack,
    PieChart,PieChartSection,
        )


class Exoplanet(Stack):
    def build(self):
        return Column(
            controls=[
                self.MainContainer(),
            ]
        )
    
    def MainContainer(self):
        self.main =Container(
            width=350, 
            height=700, 
            bgcolor='black', 
            border_radius=35,
            padding=4,
        )

        self.main_col = Column()

        self.green_container = Container(
            width = self.main.width,
            height = self.main.height * 0.45,
            border_radius=30,
            gradient= LinearGradient(
                begin=alignment.top_left,
                end=alignment.bottom_right,
                colors=["#0f766e","#064e3b"]
            )
        )

        self.main_col.controls.append(self.green_container)

        self.main.content = self.main_col     

        return self.main 

def start(page: Page):
    page.title = "Flet Simple"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    app = Exoplanet()
    page.add(app)
    page.update()

if __name__ == '__main__':
    ft.app(target=start)

