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
    def iloscKontOsobistych(cls):
        return len(cls.kontaOsobiste)