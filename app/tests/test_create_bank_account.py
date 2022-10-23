import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "87090889276")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, "87090889276", "Pesel nieprawidłowy!")

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

    #tutaj proszę dodawać nowe testy