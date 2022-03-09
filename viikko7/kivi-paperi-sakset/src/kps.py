from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from tuomari import Tuomari


class KPS:
	def __init__(self) -> None:
		self.tuomari = Tuomari()

	def pelaa(self):
		ekan_siirto = self._ekan_siirto()
		tokan_siirto = self._tokan_siirto()

		while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
			self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
			print(self.tuomari)

			ekan_siirto = self._ekan_siirto()
			tokan_siirto = self._tokan_siirto()

		print("Kiitos!")
		print(self.tuomari)
		
	def _onko_ok_siirto(self, siirto: str) -> bool:
		return siirto in ['k', 'p', 's']
		
	def _ekan_siirto(self) -> str:
		return input("Ensimmäisen pelaajan siirto: ")

	@staticmethod
	def pelaa_p_v_p(self):
		peli = KPSPelaajaVsPelaaja()
		return peli.pelaa()

	@staticmethod
	def pelaa_tekoaly(self):
		peli = KPSTekoaly()
		return peli.pelaa()

	@staticmethod
	def pelaa_parempi_tekoaly(self):
		peli = KPSParempiTekoaly(10)
		return peli.paleaa()
