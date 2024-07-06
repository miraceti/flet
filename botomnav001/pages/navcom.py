from flet import *

def bar_item(page):
    def change_page(e, page):
        print(page.route)
        # print(page.control.selected_index)

        if e.control.selected_index == 0:
            page.go("/")
            page.update()

        if e.control.selected_index == 1:
            page.go("/about")
            page.update()
        page.update()


    navitem = NavigationBar(
        on_change=lambda e:change_page(e,page),
        destinations=[
            NavigationDestination(icon=icons.HOME, label="Home"),
            NavigationDestination(icon=icons.EXPLORE, label="About"),
        ]
        )
    return navitem