import unittest

from ..Konto import Konto

from ..Konto import KontoFirmowe

class TestMakeTransfers(unittest.TestCase):

    def test_przelew_wychodzacy_wystarczajace_srodki(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "87090883276")
        pierwsze_konto.saldo = 1000
        pierwsze_konto.zaksieguj_przelew_wychodzacy(500)
        self.assertEqual(pierwsze_konto.saldo, 1000 - 500)

    def test_przelew_wychodzacy_niewystarczajace_srodki(self):
        drugie_konto = Konto("Marek", "Januszewski", "87010883276")
        drugie_konto.saldo = 100
        drugie_konto.zaksieguj_przelew_wychodzacy(500)
        self.assertEqual(drugie_konto.saldo, 100)

    def test_przelew_przychodzacy(self):
        trzecie_konto = Konto("Jacek", "Januszewski", "87010883272")
        trzecie_konto.saldo = 100
        trzecie_konto.zaksieguj_przelew_przychodzacy(500)
        self.assertEqual(trzecie_konto.saldo, 600)

    def test_przelew_wychodzacy_ekspresowy_osobiste_wystarczajace_srodki(self):
        czwarte_konto = Konto("Jan", "Januszewski", "87091883276")
        czwarte_konto.saldo = 50
        czwarte_konto.zaksieguj_przelew_wychodzacy_ekspresowy(50)
        self.assertEqual(czwarte_konto.saldo, -1)
    
    def test_przelew_wychodzacy_ekspresowy_osobiste_niewystarczajace_srodki(self):
        czwarte_konto = Konto("Jan", "Januszewski", "87091883276")
        czwarte_konto.saldo = 40
        czwarte_konto.zaksieguj_przelew_wychodzacy_ekspresowy(50)
        self.assertEqual(czwarte_konto.saldo, 40)

    def test_przelew_wychodzacy_ekspresowy_firmowe_wystarczajace_srodki(self):
        piąte_konto = KontoFirmowe("Polsat", "0123456788")
        piąte_konto.saldo = 500
        piąte_konto.zaksieguj_przelew_wychodzacy_ekspresowy(500)
        self.assertEqual(piąte_konto.saldo, -5)

    def test_przelew_wychodzacy_ekspresowy_firmowe_niewystarczajace_srodki(self):
        piąte_konto = KontoFirmowe("Polsat", "0123456788")
        piąte_konto.saldo = 50
        piąte_konto.zaksieguj_przelew_wychodzacy_ekspresowy(500)
        self.assertEqual(piąte_konto.saldo, 50)

    def test_historia_konta_osobistego_po_przelewie_wychodzacym_zwyklym(self):
        drugie_konto = Konto("Marek", "Januszewski", "87010883276")
        drugie_konto.saldo = 1000
        drugie_konto.zaksieguj_przelew_wychodzacy(500)
        drugie_konto.zaksieguj_przelew_wychodzacy(400)
        self.assertEqual(drugie_konto.historia, [-500, -400])

    def test_historia_konta_osobistego_po_przelewie_wychodzacym_ekspresowym(self):
        drugie_konto = Konto("Marek", "Januszewski", "87010883276")
        drugie_konto.saldo = 1000
        drugie_konto.zaksieguj_przelew_wychodzacy_ekspresowy(500)
        drugie_konto.zaksieguj_przelew_wychodzacy_ekspresowy(400)
        self.assertEqual(drugie_konto.historia, [-500, -1, -400, -1])

    def test_historia_konta_osobistego_po_przelewie_przychodzacym(self):
        drugie_konto = Konto("Marek", "Januszewski", "87010883276")
        drugie_konto.zaksieguj_przelew_przychodzacy(500)
        self.assertEqual(drugie_konto.historia, [500])

    def test_historia_konta_firmowego_po_przelewie_wychodzacym_zwklym(self):
        piąte_konto = KontoFirmowe("Polsat", "0123456788")
        piąte_konto.saldo = 5000
        piąte_konto.zaksieguj_przelew_wychodzacy(500)
        piąte_konto.zaksieguj_przelew_wychodzacy(300)
        piąte_konto.zaksieguj_przelew_wychodzacy(700)
        self.assertEqual(piąte_konto.historia, [-500, -300, -700])

    def test_historia_konta_firmowego_po_przelewie_wychodzacym_ekspresowym(self):
        piąte_konto = KontoFirmowe("Polsat", "0123456788")
        piąte_konto.saldo = 5000
        piąte_konto.zaksieguj_przelew_wychodzacy_ekspresowy(500)
        piąte_konto.zaksieguj_przelew_wychodzacy_ekspresowy(300)
        piąte_konto.zaksieguj_przelew_wychodzacy_ekspresowy(700)
        self.assertEqual(piąte_konto.historia, [-500, -5, -300, -5, -700, -5])

    def test_historia_konta_firmowego_po_przelewie_przychodzacym(self):
        piąte_konto = KontoFirmowe("Polsat", "0123456788")
        piąte_konto.zaksieguj_przelew_przychodzacy(500)
        self.assertEqual(piąte_konto.historia, [500])
