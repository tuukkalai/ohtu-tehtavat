from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Summa:
    def __init__(self, sovellus, syote) -> None:
        self._sovellus = sovellus
        self._syote = syote
        self.__viimeisin_arvo = 0

    def suorita(self):
        arvo = 0
        try:
            arvo = int(self._syote())
            self.__viimeisin_arvo = arvo
            self._sovellus.plus(arvo)
        except Exception:
            pass

    def kumoa(self):
        try:
            self._sovellus.plus(-self.__viimeisin_arvo)
            self.__viimeisin_arvo = 0
        except Exception:
            pass

class Erotus:
    def __init__(self, sovellus, syote) -> None:
        self._sovellus = sovellus
        self._syote = syote
        self.__viimeisin_arvo = 0

    def suorita(self):
        arvo = 0
        try:
            arvo = int(self._syote())
            self.__viimeisin_arvo = arvo
            self._sovellus.miinus(arvo)
        except Exception:
            pass

    def kumoa(self):
        try:
            self._sovellus.miinus(-self.__viimeisin_arvo)
            self.__viimeisin_arvo = 0
        except Exception:
            pass

class Nollaus:
    def __init__(self, sovellus) -> None:
        self._sovellus = sovellus
        self.__viimeisin_arvo = 0

    def suorita(self):
        try:
            self.__viimeisin_arvo = self._sovellus.tulos
            self._sovellus.nollaa()
        except Exception:
            pass

    def kumoa(self):
        try:
            self._sovellus.plus(self.__viimeisin_arvo)
            self.__viimeisin_arvo = 0
        except Exception:
            pass

class Kumoa:
    def __init__(self, sovellus) -> None:
        self._sovellus = sovellus
        self.__edellinen_komento = None

    def edellinen_komento(self, komento):
        self.__edellinen_komento = komento

    def suorita(self):
        if self.__edellinen_komento and self.__edellinen_komento != self:
            self.__edellinen_komento.kumoa()


class Kayttoliittyma:
    def __init__(self, sovellus, root):
        self._sovellus = sovellus
        self._root = root
        self._komennot = {
            Komento.SUMMA: Summa(self._sovellus, self._lue_syote),
            Komento.EROTUS: Erotus(self._sovellus, self._lue_syote),
            Komento.NOLLAUS: Nollaus(self._sovellus),
            Komento.KUMOA: Kumoa(self._sovellus)
        }

    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovellus.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        return self._syote_kentta.get()

    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        komento_olio.suorita()
        self._komennot[Komento.KUMOA].edellinen_komento(komento_olio)
        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovellus.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovellus.tulos)
