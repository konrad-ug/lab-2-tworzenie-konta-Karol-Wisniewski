import unittest

from ..Konto import Konto

from ..RejestrKont import RejestrKont

class TestAddPersonalAccountToList(unittest.TestCase):

    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "87090883276"
    imie2 = "Jacek"
    nazwisko2 = "Budyń"
    pesel2 = "09876543229"
    saldo2 = 200

    @classmethod
    def setUpClass(cls):
        cls.konto_osobiste = Konto(cls.imie, cls.nazwisko, cls.pesel)
        cls.dane = {"imie": cls.imie2, "nazwisko": cls.nazwisko2, "pesel": cls.pesel2, "saldo": cls.saldo2}
        cls.dane2 = {"imie": cls.imie2, "saldo": cls.saldo2}

    def test_1_dodaj_konto_osobiste(self):
        RejestrKont.dodajKontoOsobiste(self.konto_osobiste)
        self.assertEqual(RejestrKont.kontaOsobiste, [self.konto_osobiste])

    def test_2_znajdz_konto_osobiste_po_peselu_znaleziono(self):
        self.assertEqual(RejestrKont.znajdzKontoPoPeselu("87090883276"), self.konto_osobiste)

    def test_3_znajdz_konto_osobiste_po_peselu_nie_znaleziono(self):
        self.assertEqual(RejestrKont.znajdzKontoPoPeselu("87090883279"), None)

    def test_4_ilosc_kont_osobistych(self):
        RejestrKont.iloscKontOsobistych
        self.assertEqual(RejestrKont.iloscKontOsobistych(), 1)
        
    def test_5_modyfikuj_konto_osobiste_wszystkie_dane(self):
        RejestrKont.modyfikujKontoOsobiste(self.konto_osobiste, self.dane)
        self.assertEqual(RejestrKont.kontaOsobiste[0].imie, self.dane["imie"])
        self.assertEqual(RejestrKont.kontaOsobiste[0].nazwisko, self.dane["nazwisko"])
        self.assertEqual(RejestrKont.kontaOsobiste[0].pesel, self.dane["pesel"])
        self.assertEqual(RejestrKont.kontaOsobiste[0].saldo, self.dane["saldo"])
    
    def test_6_modyfikuj_konto_osobiste_niektore_dane(self):
        RejestrKont.modyfikujKontoOsobiste(self.konto_osobiste, self.dane2)
        self.assertEqual(RejestrKont.kontaOsobiste[0].imie, self.dane["imie"])
        self.assertEqual(RejestrKont.kontaOsobiste[0].nazwisko, self.konto_osobiste.nazwisko)
        self.assertEqual(RejestrKont.kontaOsobiste[0].pesel, self.konto_osobiste.pesel)
        self.assertEqual(RejestrKont.kontaOsobiste[0].saldo, self.dane["saldo"])
        
    def test_7_usun_konto_osobiste(self):
        RejestrKont.usunKontoOsobiste(RejestrKont.kontaOsobiste[0])
        self.assertEqual(RejestrKont.kontaOsobiste, [])

    @classmethod
    def tearDownClass(cls):
        RejestrKont.kontaOsobiste = []