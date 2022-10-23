class Konto:
    def __init__(self, imie, nazwisko, pesel, kod = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0 if kod == None else 50 if kod.startswith("PROM_") and len(kod) == 8 else 0
        self.pesel = pesel if len(pesel) == 11 else "Niepoprawny pesel!"
