import unittest

from ..Konto import Konto

from ..Konto import KontoFirmowe

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "87090889276")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, "87090889276", "Pesel nieprawidłowy!")

    def test_tworzenie_konta_firmowego(self):
        pierwsze_konto_firmowe = KontoFirmowe("VueLamp", "0123456789")
        self.assertEqual(pierwsze_konto_firmowe.nazwa_firmy, "VueLamp", "Nazwa firmy nie została zapisana!")
        self.assertEqual(pierwsze_konto_firmowe.NIP, "0123456789", "NIP firmy nie został zapisany")

    def test_poprawny_NIP(self):
        drugie_konto_firmowe = KontoFirmowe("KWeather", "0987654321")
        self.assertEqual(len(drugie_konto_firmowe.NIP), 10)

    def test_niepoprawny_NIP(self):
        trzecie_konto_firmowe = KontoFirmowe("FilMind", "098765432")
        self.assertEqual(trzecie_konto_firmowe.NIP, "Niepoprawny NIP!")

    def test_poprawny__pesel(self):
        drugie_konto = Konto("Mariusz", "Januszewski", "87090889279")
        self.assertEqual(drugie_konto.pesel, "87090889279")

    def test_niepoprawny__pesel(self):
        drugie_konto = Konto("Mariusz", "Januszewski", "8709088927")
        self.assertEqual(drugie_konto.pesel, "Niepoprawny pesel!")

    def test_poprawny_kod_promocyjny(self):
        trzecie_konto = Konto("Monika", "Kociołek", "92090889272", "PROM_-V6")
        self.assertEqual(trzecie_konto.saldo, 50, "Saldo się nie zgadza!")

    def test_niepoprawny_kod_promocyjny(self):
        trzecie_konto = Konto("Monika", "Kociołek", "92090889272", "PROM_-V69")
        self.assertEqual(trzecie_konto.saldo, 0, "Saldo się nie zgadza!")

    def test_poprawny_kod_promocyjny_mlody(self):
        czwarte_konto = Konto("Albert", "Einstein", "92090889272", "PROM_V?9")
        self.assertEqual(czwarte_konto.saldo, 50)

    def test_poprawny_kod_promocyjny_senior(self):
        czwarte_konto = Konto("Paweł", "Einstein", "58090889272", "PROM_V?9")
        self.assertEqual(czwarte_konto.saldo, 0)

    def test_niepoprawny_kod_promocyjny_mlody(self):
        czwarte_konto = Konto("Przemysław", "Tytoń", "04290889272", "PROM_V?9-")
        self.assertEqual(czwarte_konto.saldo, 0)

    def test_niepoprawny_kod_promocyjny_senior(self):
        czwarte_konto = Konto("Jarosław", "Tytoń", "55020889272", "PROM_V?9-")
        self.assertEqual(czwarte_konto.saldo, 0)