import flet as ft

style_frame: dict = {
    "expand": True,
    "bgcolor": "#1f2128",
    "border_radius": 10,
    "padding": 20,
}


class GraphOne(ft.Container):
    def __init__(self):
        super().__init__(**style_frame)
        data_1 = [
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(0, 3),
                    ft.LineChartDataPoint(2, 2),
                    ft.LineChartDataPoint(4, 5),
                    ft.LineChartDataPoint(6, 3.1),
                    ft.LineChartDataPoint(8, 4),
                    ft.LineChartDataPoint(10, 3),
                    ft.LineChartDataPoint(11, 4),
                ],
                stroke_width=5,
                color=ft.colors.CYAN,
                curved=True,
                stroke_cap_round= True,
                gradient= ft.LinearGradient([ft.colors.CYAN, ft.colors.WHITE]),
                
            )
        ]

        self.content = ft.LineChart(
            data_series=data_1,
            border=ft.border.all(3, ft.colors.with_opacity(0.2, ft.colors.BLACK)),
            horizontal_grid_lines=ft.ChartGridLines(interval=1, color=ft.colors.BLACK),
            vertical_grid_lines=ft.ChartGridLines(interval=1, color=ft.colors.BLACK),
            left_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=1,
                        label=ft.Text("10k", size=14,
                                      color=ft.colors.with_opacity(0.8, ft.colors.WHITE),),
                    ),
                    ft.ChartAxisLabel(
                        value=3,
                        label=ft.Text("30k", size=14,
                                      color=ft.colors.with_opacity(0.8, ft.colors.WHITE),),
                    ),
                    ft.ChartAxisLabel(
                        value=5,
                        label=ft.Text("50k", size=14,
                                      color=ft.colors.with_opacity(0.8, ft.colors.WHITE),),
                    )
                ],
                labels_size=40,
                
            ),
            bottom_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=2,
                        label=ft.Container(
                            ft.Text(
                                "2",
                                size=16,
                                color=ft.colors.with_opacity(0.8, ft.colors.WHITE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=6,
                        label=ft.Container(
                            ft.Text(
                                "6",
                                size=16,
                                color=ft.colors.with_opacity(0.8, ft.colors.WHITE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=10,
                        label=ft.Container(
                            ft.Text(
                                "10",
                                size=16,
                                color=ft.colors.with_opacity(0.8, ft.colors.WHITE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                ],
                labels_size=32,
                
            ),
            tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLACK),
            min_y=0,
            max_y=6,
            min_x=0,
            max_x=11,
            expand=True,

        )
class GraphTwo(ft.Container):
    def __init__(self):
        super().__init__(**style_frame)
        self.content = ft.BarChart(
            bar_groups=[
                ft.BarChartGroup(
                    x=0,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=40,
                            width=30,
                            gradient=ft.LinearGradient([ft.colors.CYAN,ft.colors.CYAN_100], rotation=90),
                            tooltip="€40.00",
                            border_radius=15,
                        ),
                    ],
                ),
                ft.BarChartGroup(
                    x=1,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=48,
                            width=30,
                            gradient=ft.LinearGradient([ft.colors.CYAN,ft.colors.CYAN_100]),
                            tooltip="€48.00",
                            border_radius=15,
                        ),
                    ],
                ),
                ft.BarChartGroup(
                    x=2,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=36,
                            width=30,
                            gradient=ft.LinearGradient([ft.colors.CYAN,ft.colors.CYAN_100]),
                            tooltip="€36.00",
                            border_radius=15,
                        ),
                    ],
                ),
                ft.BarChartGroup(
                    x=3,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=68,
                            width=30,
                            gradient=ft.LinearGradient([ft.colors.CYAN,ft.colors.CYAN_100]),
                            tooltip="€68.00",
                            border_radius=15,
                        ),
                    ],
                ),
                ft.BarChartGroup(
                    x=4,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=80,
                            width=30,
                            gradient=ft.LinearGradient([ft.colors.CYAN,ft.colors.CYAN_100]),
                            tooltip="€80.00",
                            border_radius=15,
                        ),
                    ],
                ),
           
            ],
            border=ft.border.all(1, ft.colors.BLACK),
            left_axis=ft.ChartAxis(
                labels_size=40, 
                title=ft.Text("Production"),title_size=40
            ),
            bottom_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=0, label=ft.Container(ft.Text("Janvier"),padding=10)
                    ),
                    ft.ChartAxisLabel(
                        value=1, label=ft.Container(ft.Text("Fevrier"),padding=10)
                    ),
                    ft.ChartAxisLabel(
                        value=2, label=ft.Container(ft.Text("Mars"),padding=10)
                    ),
                    ft.ChartAxisLabel(
                        value=3, label=ft.Container(ft.Text("Avril"),padding=10)
                    ),
                    ft.ChartAxisLabel(
                        value=4, label=ft.Container(ft.Text("Mai"),padding=10)
                    ),
                ],
                labels_size=40,
            ),
            horizontal_grid_lines=ft.ChartGridLines(
                color=ft.colors.BLACK, width=1, dash_pattern=[3, 3]
            ),
            tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.BLACK),
            max_y=100,
            interactive=True,
            expand=True,

        )
class GraphThree(ft.Container):
    def __init__(self):
        super().__init__(**style_frame)
        self.normal_radius = 80
        self.hover_radius = 90
        self.normal_title_style = ft.TextStyle(
            size=16, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD
        )
        self.hover_title_style=ft.TextStyle(
            size=16,
            color=ft.colors.WHITE,
            weight=ft.FontWeight.BOLD,
            shadow=ft.BoxShadow(blur_radius=2, color=ft.colors.BLACK),
        )
        self.normal_badge_size=40

        self.content = ft.PieChart(
            sections=[
                ft.PieChartSection(
                    40,
                    title="40%",
                    title_style=self.normal_title_style,
                    color=ft.colors.BLUE,
                    radius=self.normal_radius,
                    badge=self.badge(ft.icons.FACEBOOK, self.normal_badge_size),
                    badge_position=1,
                ),
                ft.PieChartSection(
                    30,
                    title="30%",
                    title_style=self.normal_title_style,
                    color=ft.colors.ORANGE,
                    radius=self.normal_radius,
                    badge=self.badge(ft.icons.WINDOW, self.normal_badge_size),
                    badge_position=1,
                ),
                ft.PieChartSection(
                    15,
                    title="15%",
                    title_style=self.normal_title_style,
                    color=ft.colors.PURPLE,
                    radius=self.normal_radius,
                    badge=self.badge(ft.icons.APPLE, self.normal_badge_size),
                    badge_position=1,
                ),
                ft.PieChartSection(
                    25,
                    title="25%",
                    title_style=self.normal_title_style,
                    color=ft.colors.GREEN,
                    radius=self.normal_radius,
                    badge=self.badge(ft.icons.TIKTOK, self.normal_badge_size),
                    badge_position=1,
                ),
                
            ],
            sections_space=0,
            center_space_radius=0,
            on_chart_event=self.on_chart_event,
            expand=True
        )

    def badge(self,icon, size):
        return ft.Container(
            ft.Icon(icon, color=ft.colors.BLACK),
            width=size,
            height=size,
            border=ft.border.all(1, ft.colors.BLACK),
            border_radius=size / 2,
            bgcolor=ft.colors.WHITE,
        )
    
    def on_chart_event(self, e: ft.PieChartEvent):
        for idx, section in enumerate(self.content.sections):
            if idx == e.section_index:
                section.radius = self.hover_radius
                section.title_style= self.hover_title_style
            else:
                section.radius = self.normal_radius
                section.title_style= self.normal_title_style
        self.content.update()
class GraphFour(ft.Container):
    def __init__(self):
        super().__init__(**style_frame)
        self.normal_border=ft.BorderSide(2, ft.colors.with_opacity(0.5,ft.colors.WHITE))
        self.hovered_border=ft.BorderSide(4, ft.colors.WHITE)
        self.radius=80
        self.normal_title_style=ft.TextStyle(
            size=16, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD )
        self.content=ft.PieChart(
            sections=[
                ft.PieChartSection(
                    30,
                    title="30%",
                    title_position=0.7,
                    title_style=self.normal_title_style,
                    color=ft.colors.ORANGE,
                    radius=self.radius,
                    border_side=self.normal_border
                ),
                ft.PieChartSection(
                    20,
                    title="20%",
                    title_position=0.7,
                    title_style=self.normal_title_style,
                    color=ft.colors.RED,
                    radius=self.radius,
                    border_side=self.normal_border,
                ),
                ft.PieChartSection(
                    15,
                    title="15%",
                    title_position=0.7,
                    title_style=self.normal_title_style,
                    color=ft.colors.GREEN,
                    radius=self.radius,
                    border_side=self.normal_border
                ),
                ft.PieChartSection(
                    35,
                    title="35%",
                    title_position=0.7,
                    title_style=self.normal_title_style,
                    color=ft.colors.PINK,
                    radius=self.radius,
                    border_side=self.normal_border
                ),
                
            ],
            sections_space=10,
            center_space_radius=0,
            on_chart_event=self.on_chart_event,
            expand=True,
        )

    def on_chart_event(self, e: ft.PieChartEvent):
        for idx, section in enumerate(self.content.sections):
            section.border_side = (
                self.hovered_border if idx == e.section_index else self.normal_border
            )
        self.content.update()
class GraphFive(ft.Container):
    def __init__(self):
        super().__init__(**style_frame)
        self.normal_border=ft.BorderSide(2, ft.colors.with_opacity(0.5,ft.colors.WHITE))
        self.hovered_border=ft.BorderSide(4, ft.colors.WHITE)
        self.normal_title_style=ft.TextStyle(
            size=16, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD )
        self.normal_radius = 50
        self.content=ft.PieChart(
            sections=[
                ft.PieChartSection(
                    35,
                    title="35%",
                    title_style=self.normal_title_style,
                    color=ft.colors.YELLOW,
                    radius=self.normal_radius,
                    border_side=self.normal_border
                ),
                ft.PieChartSection(
                    15,
                    title="15%",
                    title_style=self.normal_title_style,
                    color=ft.colors.CYAN,
                    radius=self.normal_radius,
                    border_side=self.normal_border,
                ),
                ft.PieChartSection(
                    10,
                    title="10%",
                    title_style=self.normal_title_style,
                    color=ft.colors.PURPLE,
                    radius=self.normal_radius,
                    border_side=self.normal_border
                ),
                ft.PieChartSection(
                    40,
                    title="40%",
                    title_style=self.normal_title_style,
                    color=ft.colors.CYAN_ACCENT,
                    radius=self.normal_radius,
                    border_side=self.normal_border
                ),
                
            ],
            sections_space=2,
            center_space_radius=40,
            on_chart_event=self.on_chart_event,
            expand=True,
        )

    def on_chart_event(self, e: ft.PieChartEvent):
        for idx, section in enumerate(self.content.sections):
            section.border_side= (
                self.hovered_border if idx == e.section_index else self.normal_border
            )
        self.content.update()

graph_one: ft.Container = GraphOne()
graph_two: ft.Container = GraphTwo()
graph_Three: ft.Container = GraphThree()
graph_four: ft.Container = GraphFour()
graph_five: ft.Container = GraphFive()

def main(page: ft.Page):
    #page.add(ft.SafeArea(ft.Text("Hello, Flet Dashboard!")))
    page.bgcolor = 'black'
    page.padding = 10
    page.add(
        ft.Row(
            expand= True,
            controls=[
            ft.Column(
                expand= True,
                controls=[graph_one,graph_two],

            ),
            ft.Column(
                expand= True,
                controls=[graph_Three, graph_four, graph_five]
            )    
            ]
        )
    )

    



ft.app(target=main)
