from abc import ABC, abstractmethod

import matplotlib
matplotlib.use("Agg")

import flet as ft

from src.queue_optimization.theming.colors import TailwindColors


class ResultUI(ABC):
    def __init__(self, page: ft.Page):
        self.page = page
        self._results_section = self._init_results_section()

    @abstractmethod
    def _init_results_section(self):
        raise NotImplementedError()

    @staticmethod
    def _format_number(value, precision=4):
        if isinstance(value, float):
            return f"{value:.{precision}f}"
        return str(value)

    def _create_metric_card(self, title, value, description=None, icon=None):
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Icon(icon or ft.Icons.INSERT_CHART,
                            color=TailwindColors.blue.tw_blue_400) if icon else ft.Container(),
                    ft.Text(
                        title,
                        color=TailwindColors.zinc.tw_zinc_400,
                        size=14,
                        overflow=ft.TextOverflow.CLIP,
                        max_lines=2,
                        weight=ft.FontWeight.BOLD,
                        expand=True,
                        text_align=ft.TextAlign.LEFT,
                    ),
                ], alignment=ft.MainAxisAlignment.START),
                ft.Container(height=8),
                ft.Text(
                    self._format_number(value),
                    color=TailwindColors.zinc.tw_zinc_50,
                    size=24,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Container(height=4),
                ft.Text(description or "", color=TailwindColors.zinc.tw_zinc_500, size=12,
                        italic=True) if description else ft.Container(),
            ], spacing=0),
            bgcolor=TailwindColors.zinc.tw_zinc_900,
            border_radius=8,
            padding=15,
            expand=True,
        )

    @abstractmethod
    def _create_chart(self, data):
        raise NotImplementedError()

    @abstractmethod
    def display_results(self, results):
        raise NotImplementedError()

    def get_results_section(self):
        return self._results_section

    def hide_results(self):
        self._results_section.visible = False
        self.page.update()
