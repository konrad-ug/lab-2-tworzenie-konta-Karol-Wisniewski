import unittest
import requests

class TestObslugaKont(unittest.TestCase):
    body = {
        "imie": "John",
        "nazwisko": "Maślak",
        "pesel": "01234557895"
    } #Body, które będzie modyfikowane

    body_to_put = {
        "imie": "Janek",
        "pesel": "01234567889"
    } #Dane, które chcemy modyfikować w body
    
    #W testach zakładamy, że pesel został zmieniony i usuwamy konto z nowym peselem!

    url = "http://localhost:5000"

    def test_1_tworzenie_konta_poprawne(self):
        create_resp = requests.post(self.url + "/konta/stworz_konto", json = self.body)
        self.assertEqual(create_resp.status_code, 201)
        
    def test_2_tworzenie_konta_powtorzenie_peselu(self):
        create_resp = requests.post(self.url + "/konta/stworz_konto", json = self.body)
        self.assertEqual(create_resp.status_code, 400)

    def test_3_get_po_peselu(self):
        get_resp = requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(get_resp.status_code, 200)
        resp_body = get_resp.json()
        self.assertEqual(resp_body["imie"], self.body["imie"])
        self.assertEqual(resp_body["nazwisko"], self.body["nazwisko"])
        self.assertEqual(resp_body["saldo"], 0)

    def test_4_zmodyfikowanie_konta_poprawne(self):
        put_resp = requests.put(self.url + f"/konta/konto/{self.body['pesel']}", json = self.body_to_put)
        self.assertEqual(put_resp.status_code, 200)

    def test_5_usuniecie_konta_poprawne(self):
        delete_resp = requests.delete(self.url + f"/konta/konto/{self.body_to_put['pesel']}", json = self.body)
        self.assertEqual(delete_resp.status_code, 204)

