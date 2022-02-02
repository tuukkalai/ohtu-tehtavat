import unittest
from unittest.mock import Mock, ANY
from kassapaate import Kassapaate, HINTA
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_kortilta_velotetaan_hinta_jos_rahaa_on(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 10
        
        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_called_with(HINTA)

    def test_kortilta_ei_veloteta_jos_raha_ei_riita(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 4
        
        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_not_called()

    # Kassapäätteen metodin lataa kutsu lisää maksukortille ladattavan rahamäärän käyttäen kortin metodia lataa jos ladattava summa on positiivinen
    def test_lisaa_kortille_rahaa_ladattaessa(self):
        maksukortti_mock = Mock()
        self.kassa.lataa(maksukortti_mock, 5)

        maksukortti_mock.lataa.assert_called_with(5)

    # Kassapäätteen metodin lataa kutsu ei tee maksukortille mitään jos ladattava summa on negatiivinen
    def test_lisaa_kortille_ei_lisaa_negatiivista_summaa(self):
        maksukortti_mock = Mock()
        self.kassa.lataa(maksukortti_mock, -5)

        maksukortti_mock.lataa.assert_not_called()
