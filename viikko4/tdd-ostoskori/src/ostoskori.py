from functools import reduce
from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._ostokset = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        return reduce(lambda lukumaara, ostos: lukumaara + ostos.lukumaara(), self.ostokset(), 0)

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        return reduce(lambda summa, tuote: summa + tuote.hinta(), self.ostokset(), 0)

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        lisatty = False
        for ostos in self.ostokset():
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                lisatty = True

        if not lisatty:
            self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for ostos in self.ostokset():
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
            if ostos.lukumaara() < 1:
                self._ostokset.remove(ostos)

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self._ostokset = []

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return self._ostokset
