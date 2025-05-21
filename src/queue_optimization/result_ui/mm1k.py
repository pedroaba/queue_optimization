from src.queue_optimization.theming.colors import TailwindColors

import matplotlib
matplotlib.use("Agg")
from flet.matplotlib_chart import MatplotlibChart

import matplotlib.pyplot as plt

import flet as ft


class MM1KResultUI:
    def __init__(self, page: ft.Page):
        self.page = page
        self._results_section = self._init_results_section()

    @staticmethod
    def _init_results_section():
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(
                        "Resultados do Modelo M/M/1/K",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=TailwindColors.zinc.tw_zinc_50,
                    ),
                ),
            ],
            visible=False,
        )

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

    @staticmethod
    def _create_probability_chart(probabilities):
        fig, ax = plt.subplots(figsize=(8, 4))
        prob_values = list(probabilities.values())
        prob_keys = list(probabilities.keys())
        indices = [int(key.replace('p', '')) for key in prob_keys]

        bars = ax.bar(indices, prob_values, color='#3b82f6', alpha=0.8)
        ax.set_xlabel('n (número de clientes)', color='white')
        ax.set_ylabel('Probabilidade P(n)', color='white')
        ax.set_title('Distribuição de Probabilidades P(n)', color='white')

        ax.set_facecolor(TailwindColors.zinc.tw_zinc_900)
        fig.patch.set_facecolor(TailwindColors.zinc.tw_zinc_900)

        ax.spines['bottom'].set_color(TailwindColors.zinc.tw_zinc_600)
        ax.spines['top'].set_color(TailwindColors.zinc.tw_zinc_600)
        ax.spines['right'].set_color(TailwindColors.zinc.tw_zinc_600)
        ax.spines['left'].set_color(TailwindColors.zinc.tw_zinc_600)
        ax.tick_params(colors='white')
        ax.grid(True, linestyle='--', alpha=0.3, color=TailwindColors.zinc.tw_zinc_500)

        for bar in bars:
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2.,
                height + 0.01,
                f'{height:.4f}',
                ha='center',
                va='bottom',
                color='white',
                fontsize=8
            )

        plt.tight_layout()

        return MatplotlibChart(fig, expand=True)

    def display_results(self, results):
        self._results_section.controls = [self._results_section.controls[0]]
        probabilities = {k: v for k, v in results.items() if k.startswith('p') and k != 'P0'}

        performance_metrics = ft.Container(
            content=ft.Column([
                ft.Text("Métricas de Desempenho", weight=ft.FontWeight.BOLD, color=TailwindColors.zinc.tw_zinc_200,
                        size=18),
                ft.Container(height=10),
                ft.Row([
                    self._create_metric_card(
                        "Tempo Médio no Sistema (W)",
                        results["Tempo médio gasto no sistema (w)"],
                        "Tempo médio que um cliente passa no sistema",
                        ft.Icons.TIMER
                    ),
                    self._create_metric_card(
                        "Tempo Médio na Fila (Wq)",
                        results["Tempo médio de espera na fila (wq)"],
                        "Tempo médio de espera antes do atendimento",
                        ft.Icons.HOURGLASS_EMPTY
                    ),
                ], spacing=15),
                ft.Container(height=15),
                ft.Row([
                    self._create_metric_card(
                        "Clientes no Sistema (L)",
                        results["Número médio de clientes no sistema (l)"],
                        "Média de clientes presentes no sistema",
                        ft.Icons.PEOPLE
                    ),
                    self._create_metric_card(
                        "Clientes na Fila (Lq)",
                        results["Número médio de clientes na fila (lq)"],
                        "Média de clientes aguardando na fila",
                        ft.Icons.QUEUE
                    ),
                ], spacing=15),
            ]),
            padding=15,
            border=ft.border.all(1, TailwindColors.zinc.tw_zinc_800),
            border_radius=10,
            margin=ft.margin.only(top=10, bottom=20),
        )

        system_params = ft.Container(
            content=ft.Column([
                ft.Text("Parâmetros do Sistema", weight=ft.FontWeight.BOLD, color=TailwindColors.zinc.tw_zinc_200,
                        size=18),
                ft.Container(height=10),
                ft.Row([
                    self._create_metric_card(
                        "Intensidade de Tráfego (ρ)",
                        results["𝜌"],
                        "Razão entre taxa de chegada e taxa de serviço",
                        ft.Icons.SPEED
                    ),
                    self._create_metric_card(
                        "Taxa de Chegada Efetiva (λ')",
                        results["_lambda"],
                        "Taxa de chegada efetiva ao sistema",
                        ft.Icons.INPUT
                    ),
                    self._create_metric_card(
                        "Probabilidade Sistema Vazio (P₀)",
                        results["𝑃0"],
                        "Probabilidade de não haver clientes",
                        ft.Icons.HIGHLIGHT_OFF
                    ),
                ], spacing=15),
            ]),
            padding=15,
            border=ft.border.all(1, TailwindColors.zinc.tw_zinc_800),
            border_radius=10,
            margin=ft.margin.only(bottom=20),
        )

        chart_section = ft.Container(
            content=ft.Column([
                ft.Text("Distribuição de Probabilidades", weight=ft.FontWeight.BOLD,
                        color=TailwindColors.zinc.tw_zinc_200, size=18),
                ft.Container(height=10),
                ft.Container(
                    content=self._create_probability_chart(probabilities),
                    height=300,
                ),
            ]),
            padding=15,
            border=ft.border.all(1, TailwindColors.zinc.tw_zinc_800),
            border_radius=10,
        )

        self._results_section.controls.extend([
            performance_metrics,
            system_params,
            chart_section
        ])

        self._results_section.visible = True
        self.page.update()

    def get_results_section(self):
        return self._results_section

    def hide_results(self):
        self._results_section.visible = False
        self.page.update()