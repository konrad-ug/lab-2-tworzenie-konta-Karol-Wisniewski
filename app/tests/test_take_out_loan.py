import unittest

from ..Konto import Konto

from ..Konto import KontoFirmowe

class TestTakeOutLoan(unittest.TestCase):
    
    def test_zaciagnij_kredyt_konto_osobiste_spelnione_warunki(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "87090883276")
        pierwsze_konto.historia = [-100, 100, 100, 100, 600]
        czy_przyznany = pierwsze_konto.zaciagnij_kredyt(500)
        self.assertTrue(czy_przyznany)
        self.assertEqual(pierwsze_konto.saldo, 500)

    def test_zaciagnij_kredyt_konto_osobiste_nieprawidlowa_historia(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "87090883276")
        pierwsze_konto.historia = [-100, 100, -100, 100, 600]
        czy_przyznany = pierwsze_konto.zaciagnij_kredyt(500)
        self.assertFalse(czy_przyznany)
        self.assertEqual(pierwsze_konto.saldo, 0)
    
    def test_zaciagnij_kredyt_konto_osobiste_pusta_historia(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "87090883276")
        pierwsze_konto.historia = []
        czy_przyznany = pierwsze_konto.zaciagnij_kredyt(500)
        self.assertFalse(czy_przyznany)
        self.assertEqual(pierwsze_konto.saldo, 0)

    def test_zaciagnij_kredyt_konto_osobiste_niewystarczajace_przychody(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "87090883276")
        pierwsze_konto.historia = [-200, 100, 100, 100, 100]
        czy_przyznany = pierwsze_konto.zaciagnij_kredyt(500)
        self.assertFalse(czy_przyznany)
        self.assertEqual(pierwsze_konto.saldo, 0)