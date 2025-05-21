import re

from src.queue_optimization.models.mm1k import MM1KModel
from src.queue_optimization.theming.colors import TailwindColors
import flet as ft


class MM1KFormUI:
    def __init__(self, page: ft.Page, on_submit_callback):
        self.page = page
        self._fields = {}
        self._on_submit_callback = on_submit_callback
        self._field_labels = {
            'y': 'Taxa de chegada (λ)',
            'u': 'Taxa de atendimento (μ)',
            'K': 'Capacidade máxima do sistema (K)',
            'n': 'Número de probabilidades (n)'
        }
        self._set_fields()
        self._set_submit_button()

        self._model = MM1KModel()

    def _set_fields(self):
        for label_key in self._field_labels.keys():
            self._fields.update({
                label_key: self._get_text_field(self._field_labels[label_key])
            })

    @staticmethod
    def _get_text_field(label: str) -> ft.TextField:
        field = ft.TextField(
            label=label,
            border_color=TailwindColors.zinc.tw_zinc_800,
            color=TailwindColors.zinc.tw_zinc_50,
            expand=True,
            label_style=ft.TextStyle(
                size=14,
                color=TailwindColors.zinc.tw_zinc_600
            )
        )

        def on_change(_e: ft.ControlEvent):
            formatted_value = field.value.replace(",", ".")
            formatted_value = re.sub(r"[^\d.]", "", formatted_value)

            first_dot_index = formatted_value.find(".")
            if first_dot_index > 0:
                word_after_dot = formatted_value[first_dot_index:].replace(".", '')
                formatted_value = formatted_value[:first_dot_index + 1] + word_after_dot

            field.value = formatted_value
            field.update()

        def on_focus(_e: ft.ControlEvent):
            field.label_style = ft.TextStyle(
                size=14,
                color=TailwindColors.blue.tw_blue_400
            )
            field.focus()

        def on_blur(_e: ft.ControlEvent):
            field.label_style = ft.TextStyle(
                size=14,
                color=TailwindColors.zinc.tw_zinc_600
            )
            field.update()

        field.on_focus = on_focus
        field.on_blur = on_blur
        field.on_change = on_change

        return field

    def _set_submit_button(self):
        self._submit_button = ft.Button(
            text="Calcular",
            bgcolor=TailwindColors.zinc.tw_zinc_100,
            color=TailwindColors.zinc.tw_zinc_950,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=4),
                text_style=ft.TextStyle(
                    size=14
                ),
            ),
            width=100
        )

        self._submit_button.on_click = lambda _: self._on_submit()

    def _on_submit(self):
        try:
            y = float(self._fields["y"].value or "0")
            u = float(self._fields["u"].value or "0")
            k = int(self._fields["K"].value or "0")
            n = int(self._fields["n"].value or "0")

            if y <= 0 or u <= 0 or k <= 0 or n <= 0:
                raise ValueError("Todos os valores devem ser maiores que zero")


            model_result = self._model.queue_mm1k(y, u, k, 1, n)
            self._on_submit_callback(model_result)

        except ValueError as e:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Erro de validação: {str(e)}"),
                bgcolor=TailwindColors.red.tw_red_600,
                action="OK"
            )
            self.page.snack_bar.open = True
            self.page.update()
        except Exception as e:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Erro ao processar: {str(e)}"),
                bgcolor=TailwindColors.red.tw_red_600,
                action="OK"
            )
            self.page.snack_bar.open = True
            self.page.update()

    def _group_fields_by_rows(self, size: int):
        fields = list(self._fields.values())
        return [fields[i:i + size] for i in range(0, len(self._fields), size)]

    def get_form_ui(self, title_text="Insira os parâmetros do sistema"):
        field_rows = self._group_fields_by_rows(2)
        inputs_layout = ft.Column(
            controls=[
                ft.Row(
                    controls=row,
                    spacing=10,
                    expand=True,
                )
                for row in field_rows
            ],
            spacing=10
        )

        return ft.Container(
            content=ft.Column([
                ft.Text(title_text, color=TailwindColors.zinc.tw_zinc_400),
                inputs_layout,
                ft.Row(
                    controls=[self._submit_button],
                    expand=True,
                    alignment=ft.MainAxisAlignment.END,
                ),
            ]),
            padding=15,
            expand=True,
            border=ft.border.all(1, TailwindColors.zinc.tw_zinc_800),
            border_radius=10,
        )