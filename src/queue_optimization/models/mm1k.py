import numpy as np

type MM1KReturns = dict[str, float]


class MM1KModel:
    def __init__(self):
        pass

    @staticmethod
    def _calculate_probability_n(n: int, k: float, p: float) -> float:
        return np.multiply(
            np.divide(
                np.subtract(1, p),
                np.subtract(
                    1,
                    np.power(
                        p,
                        np.add(1, k)
                    )
                ),
            ),
            np.power(p, n)
        )

    def queue_mm1k(self, y: float, u: float, k: int, s: float, n: int) -> MM1KReturns:
        p = np.divide(y, u)
        p0 = self._calculate_probability_n(0, k, p)
        pn = {
            f"p{i + 1}": self._calculate_probability_n(i + 1, k, p)
            for i in range(n)
        }

        pk = self._calculate_probability_n(k, k, p)

        l = np.subtract(
            np.divide(p, np.subtract(1, p)),
            np.divide(
                np.multiply(np.add(k, 1), np.power(p, np.add(1, k))),
                np.subtract(1, np.power(p, np.add(1, k))),
            )
        )

        lq = np.subtract(l, np.subtract(1, p0))
        _y = np.multiply(y, np.subtract(1, pk))
        wq = np.divide(lq, _y)
        w = np.divide(l, _y)

        return {
            "Número médio de clientes na fila (lq)": lq,
            "Tempo médio de espera na fila (wq)": wq,
            "Número médio de clientes no sistema (l)": l,
            "Tempo médio gasto no sistema (w)": w,
            "𝑃0": p0,
            "𝜌": p,
            "_lambda": _y,
            **pn,
        }
