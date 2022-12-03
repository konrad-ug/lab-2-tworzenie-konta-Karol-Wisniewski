from .Konto import Konto

class RejestrKont:

    kontaOsobiste = []

    @classmethod
    def dodajKontoOsobiste(cls, kontoOsobiste):
        cls.kontaOsobiste.append(kontoOsobiste)
        

    @classmethod
    def znajdzKontoPoPeselu(cls, pesel):
        for konto in cls.kontaOsobiste:
            if(konto.pesel == pesel):
                return konto
            return None

    @classmethod
    def usunKontoOsobiste(cls, kontoOsobiste):
        cls.kontaOsobiste.remove(kontoOsobiste)
    
    @classmethod
    def iloscKontOsobistych(cls):
        return len(cls.kontaOsobiste)

    @classmethod
    def modyfikujKontoOsobiste(cls, kontoOsobiste, dane):
        kontoOsobiste.imie = dane["imie"] if "imie" in dane else kontoOsobiste.imie
        kontoOsobiste.nazwisko = dane["nazwisko"] if "nazwisko" in dane else kontoOsobiste.nazwisko
        kontoOsobiste.pesel = dane["pesel"] if "pesel" in dane else kontoOsobiste.pesel
        kontoOsobiste.saldo = dane["saldo"] if "saldo" in dane else kontoOsobiste.saldo
        