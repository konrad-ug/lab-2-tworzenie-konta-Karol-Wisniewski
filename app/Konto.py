class Konto:
    def __init__(self, imie, nazwisko, pesel, kod = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 50 if kod != None and kod.startswith("PROM_") and len(kod) == 8 and oblicz_rok_urodzenia_z_peselu(pesel) >= 1960 else 0
        self.pesel = pesel if len(pesel) == 11 else "Niepoprawny pesel!"
        self.historia = []

    def zaksieguj_przelew_wychodzacy(self, kwota):
        self.saldo = self.saldo - kwota if kwota <= self.saldo and kwota > 0 else self.saldo
        self.historia.append(-kwota)

    def zaksieguj_przelew_wychodzacy_ekspresowy(self, kwota):
        self.saldo = self.saldo - kwota - 1 if kwota <= self.saldo and kwota > 0 else self.saldo
        self.historia.append(-kwota)
        self.historia.append(-1)

    def zaksieguj_przelew_przychodzacy(self, kwota):
        self.saldo = self.saldo + kwota if kwota > 0 else self.saldo
        self.historia.append(kwota)

    def zaciagnij_kredyt(self, kwota):
        ostatnie_3_transakcje_czy_dodatnie = all(i > 0 for i in self.historia[-3:])
        suma_ostatnich_5_transakcji = sum(self.historia[-5:])
        if ((suma_ostatnich_5_transakcji > kwota) and (ostatnie_3_transakcje_czy_dodatnie) and (len(self.historia) >= 3)):
            self.saldo = self.saldo + kwota
            return True
        else:
            return False


class KontoFirmowe(Konto):
    def __init__(self, nazwa_firmy, NIP):
        self.nazwa_firmy = nazwa_firmy
        self.NIP = NIP if len(NIP) == 10 else "Niepoprawny NIP!"
        self.saldo = 0
        self.historia = []

    def zaksieguj_przelew_wychodzacy_ekspresowy(self, kwota):
        self.saldo = self.saldo - kwota - 5 if kwota <= self.saldo and kwota > 0 else self.saldo
        self.historia.append(-kwota)
        self.historia.append(-5)

    def zaciagnij_kredyt(self, kwota):
        if ((self.saldo >= kwota * 2) and (1775 in self.historia)):
            self.saldo = self.saldo + kwota
            return True
        else:
            return False



def oblicz_rok_urodzenia_z_peselu(pesel: str) -> int:
    rok = int(pesel[0:2])
    miesiac = int(pesel[2:4])

    if miesiac > 20:
        rok += 2000
    else:
        rok += 1900
    return rok