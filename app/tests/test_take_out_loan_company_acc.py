import unittest

from parameterized import parameterized

from ..Konto import KontoFirmowe

class TestTakeOutLoanCompany(unittest.TestCase):

    nazwa_firmy = "Polsat"
    NIP = "0123456788"

    def setUp(self):
        self.konto_firmowe = KontoFirmowe(self.nazwa_firmy, self.NIP)

    @parameterized.expand([
        ([-100, 100, 100, 100, 600], 800, 200, False, 800),
        ([-100, 100, -100, 1225, 1775], 3000, 1500, True, 4500),
        ([], 500, 100, False, 500),
        ([], 0, 2000, False, 0),
        ([-225, -1775, 100, 100, 3000], 1200, 500, False, 1200)
    ])
    
    def test_zaciagnij_kredyt_konto_firmowe(self, historia, saldo, kwota, oczekiwany_wynik, oczekiwane_saldo):
        self.konto_firmowe.historia = historia
        self.konto_firmowe.saldo = saldo
        czy_przyznany = self.konto_firmowe.zaciagnij_kredyt(kwota)
        self.assertEqual(czy_przyznany, oczekiwany_wynik)
        self.assertEqual(self.konto_firmowe.saldo, oczekiwane_saldo)