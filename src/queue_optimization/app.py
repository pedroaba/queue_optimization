import re

import flet as ft
from flet.core.text_style import TextStyle

from models.mm1k import MM1KModel
from src.queue_optimization.forms.mm1k import MM1KFormUI
from src.queue_optimization.result_ui.mm1k import MM1KResultUI
from theming.colors import TailwindColors

import matplotlib
matplotlib.use("Agg")
from flet.matplotlib_chart import MatplotlibChart

import matplotlib.pyplot as plt


class Application:
    def __init__(self):
        self.page: ft.Page
        self.title: ft.Text
        self.form_ui = None
        self.result_ui = None

    def __call__(self, page: ft.Page):
        self.page = page
        self._setup_window()
        self._set_title("Modelo de Filas")

        self.form_ui = MM1KFormUI(page, self._on_form_submit)

        self._mount_ui()

    def _setup_window(self):
        self.page.title = "Modelo de Filas"
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.bgcolor = TailwindColors.zinc.tw_zinc_950
        self.page.window_min_width = 400

    def _set_title(self, title: str):
        self.title = ft.Text(
            title,
            size=30,
            weight=ft.FontWeight.BOLD,
            color=TailwindColors.zinc.tw_zinc_50,
        )

    def _on_form_submit(self, result):
        try:
            self.page.splash = ft.ProgressBar(color=TailwindColors.blue.tw_blue_400)
            self.page.update()

            if not self.result_ui:
                self.result_ui = MM1KResultUI(self.page)
                self.page.add(
                    ft.Column(
                        [ft.Container(
                            content=self.result_ui.get_results_section(),
                            padding=ft.padding.only(36, 0, 36, 20)
                        )]
                    )
                )

            self.result_ui.display_results(result)

            self.page.splash = None
            self.page.update()

        except Exception as e:
            self.page.splash = None
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Erro ao calcular: {str(e)}"),
                bgcolor=TailwindColors.red.tw_red_600,
                action="OK"
            )
            self.page.snack_bar.open = True
            self.page.update()

    def _mount_ui(self):
        content = ft.Column(
            controls=[
                self.title,
                self.form_ui.get_form_ui(),
                ft.Divider(color=TailwindColors.zinc.tw_zinc_800, height=1),
            ],
        )

        main_container = ft.Container(
            content=content,
            alignment=ft.alignment.top_center,
            padding=ft.padding.symmetric(horizontal=36, vertical=20),
            expand=True,
        )

        self.page.add(
            ft.Row(
                [main_container],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
            )
        )


if __name__ == "__main__":
    import flet

    app = Application()
    flet.app(target=app)
