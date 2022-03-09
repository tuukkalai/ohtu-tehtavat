from kps import KPS
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KPS):
    def __init__(self) -> None:
        super().__init__()
        self.tekoaly = TekoalyParannettu(10)

    def _tokan_siirto(self) -> str:
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        self.tekoaly.aseta_siirto(siirto)
        return siirto
