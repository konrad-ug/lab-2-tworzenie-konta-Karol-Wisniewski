class Konto:
    def __init__(self, imie, nazwisko, pesel, kod = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 50 if kod != None and kod.startswith("PROM_") and len(kod) == 8 and oblicz_rok_urodzenia_z_peselu(pesel) >= 1960 else 0
        self.pesel = pesel if len(pesel) == 11 else "Niepoprawny pesel!"

    def zaksieguj_przelew_wychodzacy(self, kwota):
        self.saldo = self.saldo - kwota if kwota <= self.saldo and kwota > 0 else self.saldo

    def zaksieguj_przelew_wychodzacy_ekspresowy(self, kwota):
        self.saldo = self.saldo - kwota - 1 if kwota <= self.saldo and kwota > 0 else self.saldo

    def zaksieguj_przelew_przychodzacy(self, kwota):
        self.saldo = self.saldo + kwota if kwota > 0 else self.saldo


class KontoFirmowe(Konto):
    def __init__(self, nazwa_firmy, NIP):
        self.nazwa_firmy = nazwa_firmy
        self.NIP = NIP if len(NIP) == 10 else "Niepoprawny NIP!"
        self.saldo = 0

    def zaksieguj_przelew_wychodzacy_ekspresowy(self, kwota):
        self.saldo = self.saldo - kwota - 5 if kwota <= self.saldo and kwota > 0 else self.saldo



def oblicz_rok_urodzenia_z_peselu(pesel: str) -> int:
    rok = int(pesel[0:2])
    miesiac = int(pesel[2:4])

    if miesiac > 80:
        rok += 1800
    elif miesiac > 60:
        rok += 2200
    elif miesiac > 40:
        rok += 2100
    elif miesiac > 20:
        rok += 2000
    else:
        rok += 1900
    return rok