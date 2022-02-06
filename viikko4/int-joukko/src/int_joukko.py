class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")
        self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, alkio):
        for i in range(0, self.alkioiden_lkm):
            if alkio == self.ljono[i]:
                return True
        return False

    def lisaa(self, alkio):
        if not self.kuuluu(alkio):
            if self.alkioiden_lkm > 0 and self.alkioiden_lkm % self.kapasiteetti == 0:
                taulukko_old = self.ljono
                self.kopioi_taulukko(self.ljono, taulukko_old)
                self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.ljono)
                self.kapasiteetti += self.kasvatuskoko

            self.ljono[self.alkioiden_lkm] = alkio
            self.alkioiden_lkm += 1

            return True
        return False

    def poista(self, alkio):
        if not self.kuuluu(alkio):
            return False

        kohta = -1
        for i in range(0, self.alkioiden_lkm - 1):
            if self.ljono[i] != alkio and kohta < 0:
                continue

            kohta = i
            self.ljono[i] = self.ljono[i+1]

        self.ljono[self.alkioiden_lkm - 1] = 0
        self.alkioiden_lkm = self.alkioiden_lkm - 1

        return True

    def kopioi_taulukko(self, kohde, kopioitava):
        for i in range(0, len(kohde)):
            kopioitava[i] = kohde[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(alpha, beta):
        joukko = IntJoukko()
        a_taulu = alpha.to_int_list()
        b_taulu = beta.to_int_list()

        for i in range(0, len(a_taulu)):
            joukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            joukko.lisaa(b_taulu[i])

        return joukko

    @staticmethod
    def leikkaus(alpha, beta):
        joukko = IntJoukko()
        a_taulu = alpha.to_int_list()
        b_taulu = beta.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    joukko.lisaa(b_taulu[j])

        return joukko

    @staticmethod
    def erotus(alpha, beta):
        joukko = IntJoukko()
        a_taulu = alpha.to_int_list()
        b_taulu = beta.to_int_list()

        for i in range(0, len(a_taulu)):
            joukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            joukko.poista(b_taulu[i])

        return joukko

    def __str__(self):
        if self.alkioiden_lkm > 0:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos

        return "{}"
