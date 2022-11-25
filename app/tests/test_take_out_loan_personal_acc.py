import unittest

from parameterized import parameterized

from ..Konto import Konto

class TestTakeOutLoanPersonalAcc(unittest.TestCase):

    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "87090883276"

    def setUp(self):
        self.konto_osobiste = Konto(self.imie, self.nazwisko, self.pesel)

    @parameterized.expand([
        ([-100, 100, 100, 100, 600], 500, True, 500),
        ([-100, 100, -100, 100, 600], 500, False, 0),
        ([], 500, False, 0),
        ([1000], 500, False, 0),
        ([-200, 100, 100, 100, 100], 500, False, 0)
    ])
    
    def test_zaciagnij_kredyt_konto_osobiste(self, historia, kwota, oczekiwany_wynik, oczekiwane_saldo):
        self.konto_osobiste.historia = historia
        czy_przyznany = self.konto_osobiste.zaciagnij_kredyt(kwota)
        self.assertEqual(czy_przyznany, oczekiwany_wynik)
        self.assertEqual(self.konto_osobiste.saldo, oczekiwane_saldo)