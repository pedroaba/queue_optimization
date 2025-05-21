from utils.oklch_to_hex import OklchUtils


class _ColorMeta(type):
    def __getattribute__(cls, name: str):
        is_color_prop = type.__getattribute__(cls, "_is_color_property")
        if is_color_prop(name):
            raw = type.__getattribute__(cls, name)
            return OklchUtils.oklch_str_to_hex(raw)
        return type.__getattribute__(cls, name)


class Color(metaclass=_ColorMeta):
    def __getattribute__(self, item: str):
        is_color_prop = object.__getattribute__(self, "_is_color_property")
        if is_color_prop(item):
            raw = object.__getattribute__(self, item)
            return OklchUtils.oklch_str_to_hex(raw)
        return super().__getattribute__(item)

    @classmethod
    def get(cls, color_number: str | int) -> str:
        color = getattr(cls, f"tw_{cls.__name__.lower()}_{color_number}")

        return str(color)

    @staticmethod
    def _is_color_property(attr: str) -> bool:
        starts_with_tw = attr.startswith("tw_")
        last_part = attr.split("_")[-1]
        return starts_with_tw and last_part.isdigit()


class Yellow(Color):
    tw_yellow_50: str = "oklch(98.7% 0.026 102.212)"
    tw_yellow_100: str = "oklch(97.3% 0.071 103.193)"
    tw_yellow_200: str = "oklch(94.5% 0.129 101.54)"
    tw_yellow_300: str = "oklch(90.5% 0.182 98.111)"
    tw_yellow_400: str = "oklch(85.2% 0.199 91.936)"
    tw_yellow_500: str = "oklch(79.5% 0.184 86.047)"
    tw_yellow_600: str = "oklch(68.1% 0.162 75.834)"
    tw_yellow_700: str = "oklch(55.4% 0.135 66.442)"
    tw_yellow_800: str = "oklch(47.6% 0.114 61.907)"
    tw_yellow_900: str = "oklch(42.1% 0.095 57.708)"
    tw_yellow_950: str = "oklch(28.6% 0.066 53.813)"


class Amber(Color):
    tw_amber_50: str = "oklch(98.7% 0.022 95.277)"
    tw_amber_100: str = "oklch(96.2% 0.059 95.617)"
    tw_amber_200: str = "oklch(92.4% 0.12 95.746)"
    tw_amber_300: str = "oklch(87.9% 0.169 91.605)"
    tw_amber_400: str = "oklch(82.8% 0.189 84.429)"
    tw_amber_500: str = "oklch(76.9% 0.188 70.08)"
    tw_amber_600: str = "oklch(66.6% 0.179 58.318)"
    tw_amber_700: str = "oklch(55.5% 0.163 48.998)"
    tw_amber_800: str = "oklch(47.3% 0.137 46.201)"
    tw_amber_900: str = "oklch(41.4% 0.112 45.904)"
    tw_amber_950: str = "oklch(27.9% 0.077 45.635)"


class Orange(Color):
    tw_orange_50: str = "oklch(98% 0.016 73.684)"
    tw_orange_100: str = "oklch(95.4% 0.038 75.164)"
    tw_orange_200: str = "oklch(90.1% 0.076 70.697)"
    tw_orange_300: str = "oklch(83.7% 0.128 66.29)"
    tw_orange_400: str = "oklch(75% 0.183 55.934)"
    tw_orange_500: str = "oklch(70.5% 0.213 47.604)"
    tw_orange_600: str = "oklch(64.6% 0.222 41.116)"
    tw_orange_700: str = "oklch(55.3% 0.195 38.402)"
    tw_orange_800: str = "oklch(47% 0.157 37.304)"
    tw_orange_900: str = "oklch(40.8% 0.123 38.172)"
    tw_orange_950: str = "oklch(26.6% 0.079 36.259)"


class Red(Color):
    tw_red_50: str = "oklch(97.1% 0.013 17.38)"
    tw_red_100: str = "oklch(93.6% 0.032 17.717)"
    tw_red_200: str = "oklch(88.5% 0.062 18.334)"
    tw_red_300: str = "oklch(80.8% 0.114 19.571)"
    tw_red_400: str = "oklch(70.4% 0.191 22.216)"
    tw_red_500: str = "oklch(63.7% 0.237 25.331)"
    tw_red_600: str = "oklch(57.7% 0.245 27.325)"
    tw_red_700: str = "oklch(50.5% 0.213 27.518)"
    tw_red_800: str = "oklch(44.4% 0.177 26.899)"
    tw_red_900: str = "oklch(39.6% 0.141 25.723)"
    tw_red_950: str = "oklch(25.8% 0.092 26.042)"


class Lime(Color):
    tw_lime_50: str = "oklch(98.6% 0.031 120.757)"
    tw_lime_100: str = "oklch(96.7% 0.067 122.328)"
    tw_lime_200: str = "oklch(93.8% 0.127 124.321)"
    tw_lime_300: str = "oklch(89.7% 0.196 126.665)"
    tw_lime_400: str = "oklch(84.1% 0.238 128.85)"
    tw_lime_500: str = "oklch(76.8% 0.233 130.85)"
    tw_lime_600: str = "oklch(64.8% 0.2 131.684)"
    tw_lime_700: str = "oklch(53.2% 0.157 131.589)"
    tw_lime_800: str = "oklch(45.3% 0.124 130.933)"
    tw_lime_900: str = "oklch(40.5% 0.101 131.063)"
    tw_lime_950: str = "oklch(27.4% 0.072 132.109)"


class Green(Color):
    tw_green_50: str = "oklch(98.2% 0.018 155.826)"
    tw_green_100: str = "oklch(96.2% 0.044 156.743)"
    tw_green_200: str = "oklch(92.5% 0.084 155.995)"
    tw_green_300: str = "oklch(87.1% 0.15 154.449)"
    tw_green_400: str = "oklch(79.2% 0.209 151.711)"
    tw_green_500: str = "oklch(72.3% 0.219 149.579)"
    tw_green_600: str = "oklch(62.7% 0.194 149.214)"
    tw_green_700: str = "oklch(52.7% 0.154 150.069)"
    tw_green_800: str = "oklch(44.8% 0.119 151.328)"
    tw_green_900: str = "oklch(39.3% 0.095 152.535)"
    tw_green_950: str = "oklch(26.6% 0.065 152.934)"


class Emerald(Color):
    tw_emerald_50: str = "oklch(97.9% 0.021 166.113)"
    tw_emerald_100: str = "oklch(95% 0.052 163.051)"
    tw_emerald_200: str = "oklch(90.5% 0.093 164.15)"
    tw_emerald_300: str = "oklch(84.5% 0.143 164.978)"
    tw_emerald_400: str = "oklch(76.5% 0.177 163.223)"
    tw_emerald_500: str = "oklch(69.6% 0.17 162.48)"
    tw_emerald_600: str = "oklch(59.6% 0.145 163.225)"
    tw_emerald_700: str = "oklch(50.8% 0.118 165.612)"
    tw_emerald_800: str = "oklch(43.2% 0.095 166.913)"
    tw_emerald_900: str = "oklch(37.8% 0.077 168.94)"
    tw_emerald_950: str = "oklch(26.2% 0.051 172.552)"


class Teal(Color):
    tw_teal_50: str = "oklch(98.4% 0.014 180.72)"
    tw_teal_100: str = "oklch(95.3% 0.051 180.801)"
    tw_teal_200: str = "oklch(91% 0.096 180.426)"
    tw_teal_300: str = "oklch(85.5% 0.138 181.071)"
    tw_teal_400: str = "oklch(77.7% 0.152 181.912)"
    tw_teal_500: str = "oklch(70.4% 0.14 182.503)"
    tw_teal_600: str = "oklch(60% 0.118 184.704)"
    tw_teal_700: str = "oklch(51.1% 0.096 186.391)"
    tw_teal_800: str = "oklch(43.7% 0.078 188.216)"
    tw_teal_900: str = "oklch(38.6% 0.063 188.416)"
    tw_teal_950: str = "oklch(27.7% 0.046 192.524)"


class Cyan(Color):
    tw_cyan_50: str = "oklch(98.4% 0.019 200.873)"
    tw_cyan_100: str = "oklch(95.6% 0.045 203.388)"
    tw_cyan_200: str = "oklch(91.7% 0.08 205.041)"
    tw_cyan_300: str = "oklch(86.5% 0.127 207.078)"
    tw_cyan_400: str = "oklch(78.9% 0.154 211.53)"
    tw_cyan_500: str = "oklch(71.5% 0.143 215.221)"
    tw_cyan_600: str = "oklch(60.9% 0.126 221.723)"
    tw_cyan_700: str = "oklch(52% 0.105 223.128)"
    tw_cyan_800: str = "oklch(45% 0.085 224.283)"
    tw_cyan_900: str = "oklch(39.8% 0.07 227.392)"
    tw_cyan_950: str = "oklch(30.2% 0.056 229.695)"


class Sky(Color):
    tw_sky_50: str = "oklch(97.7% 0.013 236.62)"
    tw_sky_100: str = "oklch(95.1% 0.026 236.824)"
    tw_sky_200: str = "oklch(90.1% 0.058 230.902)"
    tw_sky_300: str = "oklch(82.8% 0.111 230.318)"
    tw_sky_400: str = "oklch(74.6% 0.16 232.661)"
    tw_sky_500: str = "oklch(68.5% 0.169 237.323)"
    tw_sky_600: str = "oklch(58.8% 0.158 241.966)"
    tw_sky_700: str = "oklch(50% 0.134 242.749)"
    tw_sky_800: str = "oklch(44.3% 0.11 240.79)"
    tw_sky_900: str = "oklch(39.1% 0.09 240.876)"
    tw_sky_950: str = "oklch(29.3% 0.066 243.157)"


class Blue(Color):
    tw_blue_50: str = "oklch(97% 0.014 254.604)"
    tw_blue_100: str = "oklch(93.2% 0.032 255.585)"
    tw_blue_200: str = "oklch(88.2% 0.059 254.128)"
    tw_blue_300: str = "oklch(80.9% 0.105 251.813)"
    tw_blue_400: str = "oklch(70.7% 0.165 254.624)"
    tw_blue_500: str = "oklch(62.3% 0.214 259.815)"
    tw_blue_600: str = "oklch(54.6% 0.245 262.881)"
    tw_blue_700: str = "oklch(48.8% 0.243 264.376)"
    tw_blue_800: str = "oklch(42.4% 0.199 265.638)"
    tw_blue_900: str = "oklch(37.9% 0.146 265.522)"
    tw_blue_950: str = "oklch(28.2% 0.091 267.935)"


class Indigo(Color):
    tw_indigo_50: str = "oklch(96.2% 0.018 272.314)"
    tw_indigo_100: str = "oklch(93% 0.034 272.788)"
    tw_indigo_200: str = "oklch(87% 0.065 274.039)"
    tw_indigo_300: str = "oklch(78.5% 0.115 274.713)"
    tw_indigo_400: str = "oklch(67.3% 0.182 276.935)"
    tw_indigo_500: str = "oklch(58.5% 0.233 277.117)"
    tw_indigo_600: str = "oklch(51.1% 0.262 276.966)"
    tw_indigo_700: str = "oklch(45.7% 0.24 277.023)"
    tw_indigo_800: str = "oklch(39.8% 0.195 277.366)"
    tw_indigo_900: str = "oklch(35.9% 0.144 278.697)"
    tw_indigo_950: str = "oklch(25.7% 0.09 281.288)"


class Violet(Color):
    tw_violet_50: str = "oklch(96.9% 0.016 293.756)"
    tw_violet_100: str = "oklch(94.3% 0.029 294.588)"
    tw_violet_200: str = "oklch(89.4% 0.057 293.283)"
    tw_violet_300: str = "oklch(81.1% 0.111 293.571)"
    tw_violet_400: str = "oklch(70.2% 0.183 293.541)"
    tw_violet_500: str = "oklch(60.6% 0.25 292.717)"
    tw_violet_600: str = "oklch(54.1% 0.281 293.009)"
    tw_violet_700: str = "oklch(49.1% 0.27 292.581)"
    tw_violet_800: str = "oklch(43.2% 0.232 292.759)"
    tw_violet_900: str = "oklch(38% 0.189 293.745)"
    tw_violet_950: str = "oklch(28.3% 0.141 291.089)"


class Purple(Color):
    tw_purple_50: str = "oklch(97.7% 0.014 308.299)"
    tw_purple_100: str = "oklch(94.6% 0.033 307.174)"
    tw_purple_200: str = "oklch(90.2% 0.063 306.703)"
    tw_purple_300: str = "oklch(82.7% 0.119 306.383)"
    tw_purple_400: str = "oklch(71.4% 0.203 305.504)"
    tw_purple_500: str = "oklch(62.7% 0.265 303.9)"
    tw_purple_600: str = "oklch(55.8% 0.288 302.321)"
    tw_purple_700: str = "oklch(49.6% 0.265 301.924)"
    tw_purple_800: str = "oklch(43.8% 0.218 303.724)"
    tw_purple_900: str = "oklch(38.1% 0.176 304.987)"
    tw_purple_950: str = "oklch(29.1% 0.149 302.717)"


class Fuchsia(Color):
    tw_fuchsia_50: str = "oklch(97.7% 0.017 320.058)"
    tw_fuchsia_100: str = "oklch(95.2% 0.037 318.852)"
    tw_fuchsia_200: str = "oklch(90.3% 0.076 319.62)"
    tw_fuchsia_300: str = "oklch(83.3% 0.145 321.434)"
    tw_fuchsia_400: str = "oklch(74% 0.238 322.16)"
    tw_fuchsia_500: str = "oklch(66.7% 0.295 322.15)"
    tw_fuchsia_600: str = "oklch(59.1% 0.293 322.896)"
    tw_fuchsia_700: str = "oklch(51.8% 0.253 323.949)"
    tw_fuchsia_800: str = "oklch(45.2% 0.211 324.591)"
    tw_fuchsia_900: str = "oklch(40.1% 0.17 325.612)"
    tw_fuchsia_950: str = "oklch(29.3% 0.136 325.661)"


class Pink(Color):
    tw_pink_50: str = "oklch(97.1% 0.014 343.198)"
    tw_pink_100: str = "oklch(94.8% 0.028 342.258)"
    tw_pink_200: str = "oklch(89.9% 0.061 343.231)"
    tw_pink_300: str = "oklch(82.3% 0.12 346.018)"
    tw_pink_400: str = "oklch(71.8% 0.202 349.761)"
    tw_pink_500: str = "oklch(65.6% 0.241 354.308)"
    tw_pink_600: str = "oklch(59.2% 0.249 0.584)"
    tw_pink_700: str = "oklch(52.5% 0.223 3.958)"
    tw_pink_800: str = "oklch(45.9% 0.187 3.815)"
    tw_pink_900: str = "oklch(40.8% 0.153 2.432)"
    tw_pink_950: str = "oklch(28.4% 0.109 3.907)"


class Rose(Color):
    tw_rose_50: str = "oklch(96.9% 0.015 12.422)"
    tw_rose_100: str = "oklch(94.1% 0.03 12.58)"
    tw_rose_200: str = "oklch(89.2% 0.058 10.001)"
    tw_rose_300: str = "oklch(81% 0.117 11.638)"
    tw_rose_400: str = "oklch(71.2% 0.194 13.428)"
    tw_rose_500: str = "oklch(64.5% 0.246 16.439)"
    tw_rose_600: str = "oklch(58.6% 0.253 17.585)"
    tw_rose_700: str = "oklch(51.4% 0.222 16.935)"
    tw_rose_800: str = "oklch(45.5% 0.188 13.697)"
    tw_rose_900: str = "oklch(41% 0.159 10.272)"
    tw_rose_950: str = "oklch(27.1% 0.105 12.094)"


class Slate(Color):
    tw_slate_50: str = "oklch(98.4% 0.003 247.858)"
    tw_slate_100: str = "oklch(96.8% 0.007 247.896)"
    tw_slate_200: str = "oklch(92.9% 0.013 255.508)"
    tw_slate_300: str = "oklch(86.9% 0.022 252.894)"
    tw_slate_400: str = "oklch(70.4% 0.04 256.788)"
    tw_slate_500: str = "oklch(55.4% 0.046 257.417)"
    tw_slate_600: str = "oklch(44.6% 0.043 257.281)"
    tw_slate_700: str = "oklch(37.2% 0.044 257.287)"
    tw_slate_800: str = "oklch(27.9% 0.041 260.031)"
    tw_slate_900: str = "oklch(20.8% 0.042 265.755)"
    tw_slate_950: str = "oklch(12.9% 0.042 264.695)"


class Gray(Color):
    tw_gray_50: str = "oklch(98.5% 0.002 247.839)"
    tw_gray_100: str = "oklch(96.7% 0.003 264.542)"
    tw_gray_200: str = "oklch(92.8% 0.006 264.531)"
    tw_gray_300: str = "oklch(87.2% 0.01 258.338)"
    tw_gray_400: str = "oklch(70.7% 0.022 261.325)"
    tw_gray_500: str = "oklch(55.1% 0.027 264.364)"
    tw_gray_600: str = "oklch(44.6% 0.03 256.802)"
    tw_gray_700: str = "oklch(37.3% 0.034 259.733)"
    tw_gray_800: str = "oklch(27.8% 0.033 256.848)"
    tw_gray_900: str = "oklch(21% 0.034 264.665)"
    tw_gray_950: str = "oklch(13% 0.028 261.692)"


class Zinc(Color):
    tw_zinc_50: str = "oklch(98.5% 0 0)"
    tw_zinc_100: str = "oklch(96.7% 0.001 286.375)"
    tw_zinc_200: str = "oklch(92% 0.004 286.32)"
    tw_zinc_300: str = "oklch(87.1% 0.006 286.286)"
    tw_zinc_400: str = "oklch(70.5% 0.015 286.067)"
    tw_zinc_500: str = "oklch(55.2% 0.016 285.938)"
    tw_zinc_600: str = "oklch(44.2% 0.017 285.786)"
    tw_zinc_700: str = "oklch(37% 0.013 285.805)"
    tw_zinc_800: str = "oklch(27.4% 0.006 286.033)"
    tw_zinc_900: str = "oklch(21% 0.006 285.885)"
    tw_zinc_950: str = "oklch(14.1% 0.005 285.823)"


class Neutral(Color):
    tw_neutral_50: str = "oklch(98.5% 0 0)"
    tw_neutral_100: str = "oklch(97% 0 0)"
    tw_neutral_200: str = "oklch(92.2% 0 0)"
    tw_neutral_300: str = "oklch(87% 0 0)"
    tw_neutral_400: str = "oklch(70.8% 0 0)"
    tw_neutral_500: str = "oklch(55.6% 0 0)"
    tw_neutral_600: str = "oklch(43.9% 0 0)"
    tw_neutral_700: str = "oklch(37.1% 0 0)"
    tw_neutral_800: str = "oklch(26.9% 0 0)"
    tw_neutral_900: str = "oklch(20.5% 0 0)"
    tw_neutral_950: str = "oklch(14.5% 0 0)"


class Stone(Color):
    tw_stone_50: str = "oklch(98.5% 0.001 106.423)"
    tw_stone_100: str = "oklch(97% 0.001 106.424)"
    tw_stone_200: str = "oklch(92.3% 0.003 48.717)"
    tw_stone_300: str = "oklch(86.9% 0.005 56.366)"
    tw_stone_400: str = "oklch(70.9% 0.01 56.259)"
    tw_stone_500: str = "oklch(55.3% 0.013 58.071)"
    tw_stone_600: str = "oklch(44.4% 0.011 73.639)"
    tw_stone_700: str = "oklch(37.4% 0.01 67.558)"
    tw_stone_800: str = "oklch(26.8% 0.007 34.298)"
    tw_stone_900: str = "oklch(21.6% 0.006 56.043)"
    tw_stone_950: str = "oklch(14.7% 0.004 49.25)"
