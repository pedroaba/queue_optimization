from src.queue_optimization.models.mm1k import MM1KModel
import flet as ft

from src.queue_optimization.forms._form import Form


class MM1KFormUI(Form):
    def __init__(self, page: ft.Page, on_submit_callback):
        super(MM1KFormUI, self).__init__(page, on_submit_callback)

    def _set_props(self):
        self._field_labels = {
            'y': 'Taxa de chegada (λ)',
            'u': 'Taxa de atendimento (μ)',
            'K': 'Capacidade máxima do sistema (K)',
            'n': 'Número de probabilidades (n)'
        }

        self._model = MM1KModel()
