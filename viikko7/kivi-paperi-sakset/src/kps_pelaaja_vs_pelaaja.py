from kps import KPS


class KPSPelaajaVsPelaaja(KPS):
    def _tokan_siirto(self) -> str:
        return input("Toisen pelaajan siirto: ")
