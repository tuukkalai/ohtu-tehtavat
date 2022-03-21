from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

def peli(peli: str):
	if peli not in ["a","b","c"]:
		return False

	if peli == "a":
		valittu_peli = KPSPelaajaVsPelaaja()
	elif peli == "b":
		valittu_peli = KPSTekoaly()
	else:
		valittu_peli = KPSParempiTekoaly()

	return valittu_peli.pelaa()
