'''
Created on Nov 7, 2015

@author: marius
'''
from src.domain.entities import Film, Client, Rent
import unittest
        
class TestFilm(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testFilm(self):
        film = Film("1", "Rush Hour", "Descriere", "Comedie")
        self.assertEqual(film.getId(), "1")
        self.assertEqual(film.getTitlu(), "Rush Hour")
        self.assertEqual(film.getDescriere(), "Descriere")
        self.assertEqual(film.getGen(), "Comedie")
        
    def testEqual(self):
        film1 = Film("1", "Rush Hour", "Descriere", "Comedie")
        film2 = Film("1", "Titlu", "Desc", "Actiune")
        film3 = Film("2", "asdadssa", "sadasdasd", "asdasd")
        self.assertTrue(film1 == film2, "Doua filme sunt egale daca au acelasi id")
        self.assertFalse(film1 == film3, "Filme au id-ul diferit")
        self.assertFalse(film2 == film3, "Filme au id-ul diferit")

class TestClient(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testClient(self):
        client = Client("1", "Bill Gates", "1960313012653")
        self.assertEqual(client.getId(), "1")
        self.assertEqual(client.getNume(), "Bill Gates")
        self.assertEqual(client.getCNP(), "1960313012653")
        
    def testEqual(self):
        client1 = Client("1", "Bill Gates", "1960313012653")
        client2 = Client("1", "Bill Gates", "1960313012653")
        client3 = Client("2", "Bill Gates", "1960313012653")
        self.assertTrue(client1 == client2, "Au acelasi id")
        self.assertFalse(client1 == client3, "Au id-ul diferit")
        self.assertFalse(client2 == client3, "Au id-ul diferit")
        
class TestRent(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testRent(self):
        rent = Rent("1", "2")
        self.assertEqual(rent.getClientId(), "1")
        self.assertEqual(rent.getFilmId(), "2")
        
    def testEqual(self):
        rent1 = Rent("1", "2")
        rent2 = Rent("1", "2")
        rent3 = Rent("1", "3")
        self.assertTrue(rent1 == rent2)
        self.assertFalse(rent1 == rent3)
        self.assertFalse(rent2 == rent3)
        
def suite_entities():
    ts = unittest.TestSuite()
    ts.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFilm))
    ts.addTests(unittest.TestLoader().loadTestsFromTestCase(TestClient))
    ts.addTests(unittest.TestLoader().loadTestsFromTestCase(TestRent))
    return ts