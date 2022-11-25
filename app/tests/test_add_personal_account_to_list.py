import unittest

from ..Konto import Konto

from ..RejestrKont import RejestrKont

class TestAddPersonalAccountToList(unittest.TestCase):

    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "87090883276"

    @classmethod
    def setUpClass(cls):
        cls.konto_osobiste = Konto(cls.imie, cls.nazwisko, cls.pesel)

    def test_dodaj_konto_osobiste(self):
        RejestrKont.dodajKontoOsobiste(self.konto_osobiste)
        self.assertEqual(RejestrKont.kontaOsobiste, [self.konto_osobiste])

    def test_znajdz_konto_osobiste_po_peselu_znaleziono(self):
        self.assertEqual(RejestrKont.znajdzKontoPoPeselu("87090883276"), self.konto_osobiste)

    def test_znajdz_konto_osobiste_po_peselu_nie_znaleziono(self):
        self.assertEqual(RejestrKont.znajdzKontoPoPeselu("87090883279"), None)

    def test_ilosc_kont_osobistych(self):
        RejestrKont.iloscKontOsobistych
        self.assertEqual(RejestrKont.iloscKontOsobistych(), 1)

    @classmethod
    def tearDownClass(cls):
        RejestrKont.kontaOsobiste = []