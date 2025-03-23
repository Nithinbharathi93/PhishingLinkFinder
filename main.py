import flet as ft
from flet import Text, ElevatedButton, TextField, Row, Column, Page, ControlEvent
from googlesearch import search
import socket

def main(page: Page):
    page.title = "Malicious Link Finder"
    page.horizontal_alignment = "center"
    page.vertical_alignment = ft.alignment.top_center
    page.theme_mode = 'light'

    def get_first_website(company_name):
        query = f"{company_name} official website"
        websites = []
        try:
            for url in search(query, num_results=5):
                websites.append(url)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        return websites

    def executer(company_name, sus):
        legit_ips = []
        try:
            sus_ip = socket.gethostbyname(sus.split("//")[1].split("/")[0])
        except Exception:
            op_flag.value = "Looks Suspicious"
            op_flag.color = page.bgcolor = "red"
            load.visible = False
            page.update()
            return

        websites = get_first_website(company_name)
        if websites:
            try:
                for website in websites:
                    domain = (website.split("//")[1]).split("/")[0]
                    legit_ips.append(socket.gethostbyname(domain))
                
                if sus_ip in legit_ips:
                    op_flag.value = "It's Legit"
                    op_flag.color = page.bgcolor = ft.Colors.LIGHT_GREEN_600
                    load.visible = False
                    page.update()
                else:
                    op_flag.value = "Looks Suspicious"
                    op_flag.color = page.bgcolor = "red"
                    load.visible = False
                    page.update()
            except Exception as e:
                op_flag.value = f"Error resolving IPs: {e}"
                op_flag.color = page.bgcolor = "orange"
                load.visible = False
                page.update()
        else:
            op_flag.value = f"No websites found for {company_name}"
            op_flag.color = page.bgcolor = "orange"
            load.visible = False
        
        page.update()
        
    def thm_change(e: ControlEvent)->None:
        page.theme_mode = {'light':'dark', 'dark':'light'}[page.theme_mode]
        cont.shadow.color = {
                'light':ft.Colors.WHITE,
                'dark':"#2b2b2b"
            }[page.theme_mode]
        page.update()

    def clk(e: ControlEvent) -> None:
        company_name = comp.value.strip()
        sus_link = lnk.value.strip()

        if not company_name or not sus_link:
            op_flag.value = "Please provide both the organization and the suspicious link."
            op_flag.color = page.bgcolor = "red"
        else:
            op_flag.value = "Searching..."
            op_flag.color = page.bgcolor = "blue"
            load.visible = True
            page.update()
            executer(company_name, sus_link)
    d_theme = {
        'light':ft.Colors.WHITE,
        'dark':ft.Colors.BLACK87
    }[page.theme_mode]
    # UI Components
    title = Text(value="Malicious Link Finder", size=30, weight="bold")
    thm = ft.Switch(value=False, on_change=thm_change, scale=.8)
    comp = TextField(label="Source Organization", width=400)
    lnk = TextField(label="Suspicious Link", width=400)
    load = ft.ProgressBar(width=400, color="blue", visible=False)
    btn = ElevatedButton(text="Search", on_click=clk)
    op_flag = Text(value="Awaiting input...", color="blue", scale=1.5, weight='bold')

    # Page Layout
    page.add(
        Row(
            controls=[
                Column(
                    controls=[
                        (cont:=ft.Container(
                            content=ft.Column(  # Wrap multiple controls in a Column
                            controls=[
                                ft.Container(
                                    content=ft.Row(
                                        controls=[title, thm]),
                                    alignment=ft.alignment.center,
                                    width=400),
                                comp, lnk, btn, op_flag, load],
                            alignment="center",
                            horizontal_alignment="center",
                            height=page.height
                        ),
                            border_radius=10,
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=15,
                                color=d_theme,
                                offset=ft.Offset(0,-10),
                                blur_style=ft.ShadowBlurStyle.NORMAL,
                                ),
                            alignment=ft.alignment.center,
                            )),
                    ],
                    alignment="center",
                    horizontal_alignment="center",
                    expand=True,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
