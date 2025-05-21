import math


class OklchUtils:
    @staticmethod
    def oklch_str_to_hex(oklch_str: str):
        l, c, h = OklchUtils._parse_oklch(oklch_str)
        return OklchUtils.oklch_to_hex(l, c, h)

    @staticmethod
    def oklch_to_hex(l: float, c: float, h: float):
        h_rad = math.radians(h)
        a = c * math.cos(h_rad)
        b = c * math.sin(h_rad)

        l_ = l + 0.3963377774 * a + 0.2158037573 * b
        m_ = l - 0.1055613458 * a - 0.0638541728 * b
        s_ = l - 0.0894841775 * a - 1.2914855480 * b

        l_ = l_ ** 3
        m_ = m_ ** 3
        s_ = s_ ** 3

        r = +4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_
        g = -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_
        b = -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_

        r = max(0, min(1, r))
        g = max(0, min(1, g))
        b = max(0, min(1, b))

        r = OklchUtils._srgb_transfer(r)
        g = OklchUtils._srgb_transfer(g)
        b = OklchUtils._srgb_transfer(b)

        hex_color = "#{:02x}{:02x}{:02x}".format(
            round(r * 255),
            round(g * 255),
            round(b * 255)
        )

        return hex_color

    @staticmethod
    def _srgb_transfer(x: int | float) -> float:
        if x <= 0.0031308:
            return 12.92 * x
        else:
            return 1.055 * (x ** (1 / 2.4)) - 0.055

    @staticmethod
    def _parse_oklch(oklch_str: str):
        values = oklch_str.replace("oklch(", "").replace(")", "")
        parts = values.split()

        l = float(parts[0].replace("%", "")) / 100
        c = float(parts[1])
        h = float(parts[2])

        return l, c, h
