from flask import Flask, request, jsonify
from .RejestrKont import RejestrKont
from .Konto import Konto
from datetime import date

app = Flask(__name__)

today = date.today()

@app.route('/konta/stworz_konto', methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    if RejestrKont.znajdzKontoPoPeselu(dane['pesel']) != None:
        return jsonify("Konto z podanym peselem już istnieje"), 400
    konto = Konto(dane['imie'], dane['nazwisko'], dane['pesel'])
    RejestrKont.dodajKontoOsobiste(konto)
    return jsonify("Konto zostało utworzone"), 201

@app.route('/konta/ile_kont', methods=['GET'])
def ile_kont():
    return jsonify(ilosc= RejestrKont.iloscKontOsobistych()), 200

@app.route('/konta/konto/<pesel>', methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    rezultat = RejestrKont.znajdzKontoPoPeselu(pesel)
    if rezultat is not None:
        return jsonify(
            imie=rezultat.imie,
            nazwisko=rezultat.nazwisko,
            pesel=rezultat.pesel,
            saldo=rezultat.saldo
        ), 200
    else:
        return jsonify("Nie znaleziono konta"), 404

@app.route('/konta/konto/<pesel>', methods=['DELETE'])
def usun_konto(pesel):
    konto = RejestrKont.znajdzKontoPoPeselu(pesel)
    dane = request.get_json()
    RejestrKont.usunKontoOsobiste(konto)
    return jsonify(f"Konto zostało usunięte. \n Dane usuniętego konta: \n {dane}"), 204

@app.route('/konta/konto/<pesel>', methods=['PUT'])
def modyfikuj_konto(pesel):
    konto = RejestrKont.znajdzKontoPoPeselu(pesel)
    dane = request.get_json()
    dane_konta_przed_modyfikacja = {"imie": konto.imie, "nazwisko": konto.nazwisko, "pesel": konto.pesel, "saldo": konto.saldo}
    RejestrKont.modyfikujKontoOsobiste(konto, dane)
    return jsonify(
        f"Konto zostało zmodyfikowane. Domyślne dane: {dane_konta_przed_modyfikacja} Zmienione dane: {dane}"
    ), 200
    