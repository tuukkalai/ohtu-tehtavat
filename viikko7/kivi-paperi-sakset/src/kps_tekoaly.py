from kps import KPS
from tekoaly import Tekoaly


class KPSTekoaly(KPS):
    def __init__(self) -> None:
        super().__init__()
        self.tekoaly = Tekoaly()

    def _tokan_siirto(self) -> str:
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto
