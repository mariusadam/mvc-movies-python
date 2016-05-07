'''
Created on Nov 7, 2015

@author: marius
'''
from src.repository.inmem_repository import FilmRepository, RepositoryException,\
    ClientRepository, RentRepository
from src.domain.entities import Film, Client, Rent
import unittest

class TestFilmRepository(unittest.TestCase):

    def setUp(self):
        self.__repo = FilmRepository()
        self.__repo.removeAll()
        unittest.TestCase.setUp(self)

    def tearDown(self):
        self.__repo.removeAll()
        unittest.TestCase.tearDown(self)

    def testAdd(self):
        film =Film("1", "Titlu 1", "Descriere 1", "Gen 1")
        self.__repo.add(film)
        with self.assertRaises(RepositoryException):
            self.__repo.add(film)  #filmul exista deja in fisier si nu va fi adaugat
        film2 = Film("2", "Titlu 2", "Descriere 2", "Gen 2")
        self.__repo.add(film2)
        film3 = Film("3", "Titlu 3", "Descriere 3", "Gen 3")
        self.__repo.add(film3)
        film4 = Film("4", "Titlu 4", "Descriere 4", "Gen 4")
        self.__repo.add(film4)
        self.assertEqual(self.__repo.size(), 4, "Ar trebui sa fie 4 filme in fisier")
        
    def testGetAll(self):
        self.assertEqual(self.__repo.getAllFilms(), [], "Nu exista niciun client")
        film2 = Film("2", "Titlu 2", "Descriere 2", "Gen 2")
        self.__repo.add(film2)
        film3 = Film("3", "Titlu 3", "Descriere 3", "Gen 3")
        self.__repo.add(film3)
        self.assertEqual(self.__repo.getAllFilms(), [film2, film3], "Ar trebui sa returneze 2 clienti")
        self.__repo.removeAll()
        self.assertEqual(self.__repo.getAllFilms(), [], "Nu exista niciun client")
        
    def testRemoveAll(self):
        film2 = Film("2", "Titlu 2", "Descriere 2", "Gen 2")
        self.__repo.add(film2)
        film3 = Film("3", "Titlu 3", "Descriere 3", "Gen 3")
        self.__repo.add(film3)
        self.assertEqual(self.__repo.size(), 2, "2 filme existente")
        self.__repo.removeAll()
        self.assertEqual(self.__repo.size(), 0, "Nu exista niciun film")
        
    def testDelete(self):
        film2 = Film("2", "Titlu 2", "Descriere 2", "Gen 2")
        self.__repo.add(film2)
        film3 = Film("3", "Titlu 3", "Descriere 3", "Gen 3")
        self.__repo.add(film3)
        self.assertEqual(self.__repo.getAllFilms(), [film2, film3])
        self.__repo.delete(film3)
        self.assertEqual(self.__repo.getAllFilms(), [film2], "Filmul cu id-ul 3 ar trebui sa fie sters")
        self.__repo.delete(film2)
        self.assertEqual(self.__repo.getAllFilms(), [])
        with self.assertRaises(RepositoryException):
            self.__repo.delete(film2) #incerc sa sterg un film care nu exista
            
    def testFindById(self):
        film =Film("1", "Titlu 1", "Descriere 1", "Gen 1")
        self.__repo.add(film)
        film2 = Film("2", "Titlu 2", "Descriere 2", "Gen 2")
        self.__repo.add(film2)
        self.assertEqual(self.__repo.findById("1"), film, "Ar trebui sa returneze filmul cu id-ul 1")
        self.assertEqual(self.__repo.findById("2"), film2, "Ar trebui sa returneze filmul cu id-ul 2")
        with self.assertRaises(RepositoryException):
            fl = self.__repo.findById("123")
            del fl
        with self.assertRaises(RepositoryException):
            fl = self.__repo.findById("-1")
        with self.assertRaises(RepositoryException):
            fl = self.__repo.findById("")
        with self.assertRaises(RepositoryException):
            fl = self.__repo.findById("122343")
        with self.assertRaises(RepositoryException):
            fl = self.__repo.findById("12dsf4fff3")
        
    def testUpdate(self):
        film =Film("1", "Titlu 1", "Descriere 1", "Gen 1")
        self.__repo.add(film)
        film2 = Film("2", "Titlu 2", "Descriere 2", "Gen 2")
        self.__repo.add(film2)
        film_nou = Film("1", "Titlu nou", "Alta descriere", "Comedie")
        self.assertEqual(self.__repo.getAllFilms(), [film, film2], "Lista de filme initiala")
        self.__repo.update(film_nou)
        self.assertEqual(self.__repo.getAllFilms(), [film_nou, film2], "Filmul ar trebui sa se actualizeze")
        self.assertEqual(self.__repo.findById("1"), film_nou, "Filmul ar trebui sa se actualizeze")
        with self.assertRaises(RepositoryException):
            film_nou = Film("1333", "Titlu nou", "Alta descriere", "Comedie") 
            self.__repo.update(film_nou) 
        with self.assertRaises(RepositoryException):
            film_nou = Film("", "Titlu nou", "Alta descriere", "Comedie") 
            self.__repo.update(film_nou)
        with self.assertRaises(RepositoryException):
            film_nou = Film("-1", "Titlu nou", "Alta descriere", "Comedie") 
            self.__repo.update(film_nou)
        with self.assertRaises(RepositoryException):
            film_nou = Film("2342142341", "Titlu nou", "Alta descriere", "Comedie") 
            self.__repo.update(film_nou)
        with self.assertRaises(RepositoryException):
            film_nou = Film("asdsadsad", "Titlu nou", "Alta descriere", "Comedie") 
            self.__repo.update(film_nou)

class TestClientRepository(unittest.TestCase):

    def setUp(self):
        self.__repo = ClientRepository()
        self.__repo.removeAll()
        unittest.TestCase.setUp(self)

    def tearDown(self):
        self.__repo.removeAll()
        unittest.TestCase.tearDown(self)

    def testAdd(self):
        self.assertEqual(self.__repo.size(), 0, "Nu exista niciun client")
        client = Client("1", "Nume 1", "1960313012653")
        self.__repo.add(client)
        self.assertEqual(self.__repo.size(), 1, "Exista un client in repository")
        with self.assertRaises(RepositoryException):
            self.__repo.add(client) #incerc sa introduc un client cu un id existent
            
    def testGetAll(self):
        client2 = Client("2", "Nume 2", "1911202393786")
        self.__repo.add(client2)
        client3 = Client("3", "Nume 3", "1930729213031")
        self.__repo.add(client3)
        client4 = Client("4", "Nume 4", "1851021345131")
        self.__repo.add(client4)
        self.assertEqual(self.__repo.size(), 3)
        self.assertEqual(self.__repo.getAllClients(), [client2, client3, client4])
        self.__repo.removeAll()
        self.assertEqual(self.__repo.getAllClients(), [])
        
    def testRemoveAll(self):
        client2 = Client("2", "Nume 2", "1911202393786")
        self.__repo.add(client2)
        client3 = Client("3", "Nume 3", "1930729213031")
        self.__repo.add(client3)
        self.assertEqual(self.__repo.size(), 2)
        self.__repo.removeAll()
        self.assertEqual(self.__repo.size(), 0)
        self.assertEqual(self.__repo.getAllClients(), [])
        
    def testDelete(self):
        client2 = Client("2", "Nume 2", "1911202393786")
        self.__repo.add(client2)
        client3 = Client("3", "Nume 3", "1930729213031")
        self.__repo.add(client3)
        self.assertEqual(self.__repo.getAllClients(), [client2, client3])
        self.__repo.delete(client2)
        self.assertEqual(self.__repo.getAllClients(), [client3], "Clientul cu id-ul 2 ar trebui sa fie sters")
        self.__repo.delete(client3)
        self.assertEqual(self.__repo.getAllClients(), [])
        with self.assertRaises(RepositoryException):
            self.__repo.delete(client2)
        
    def testFindById(self):
        client2 = Client("2", "Nume 2", "1911202393786")
        self.__repo.add(client2)
        client3 = Client("3", "Nume 3", "1930729213031")
        self.__repo.add(client3)
        self.assertEqual(self.__repo.findById("2"), client2)
        self.assertEqual(self.__repo.findById("3"), client3)
        with self.assertRaises(RepositoryException):
            cl = self.__repo.findById("1234")
            del cl
        with self.assertRaises(RepositoryException):
            cl = self.__repo.findById("-1")
        with self.assertRaises(RepositoryException):
            cl = self.__repo.findById("")
        with self.assertRaises(RepositoryException):
            cl = self.__repo.findById("123224")
        with self.assertRaises(RepositoryException):
            cl = self.__repo.findById("123f34")
            
    def testUpdate(self):
        client2 = Client("2", "Nume 2", "1911202393786")
        self.__repo.add(client2)
        client3 = Client("3", "Nume 3", "1930729213031")
        self.__repo.add(client3)
        self.assertEqual(self.__repo.getAllClients(), [client2, client3])
        client_nou = Client("2", "Nume Nou", "1911202393786")
        self.__repo.update(client_nou)
        self.assertEqual(self.__repo.getAllClients(), [client_nou, client3])
        self.assertEqual(self.__repo.findById("2"), client_nou)
        with self.assertRaises(RepositoryException):
            client_nou = Client("21333", "Nume", "1911202393786")
            self.__repo.update(client_nou)
        with self.assertRaises(RepositoryException):
            client_nou = Client("213r23r", "Nume", "1911202393786")
            self.__repo.update(client_nou)
        with self.assertRaises(RepositoryException):
            client_nou = Client("0", "Nume", "1911202393786")
            self.__repo.update(client_nou)
        with self.assertRaises(RepositoryException):
            client_nou = Client("-1", "Nume", "1911202393786")
            self.__repo.update(client_nou)
        with self.assertRaises(RepositoryException):
            client_nou = Client("", "Nume", "1911202393786")
            self.__repo.update(client_nou)

class TestRentRepository(unittest.TestCase):
    
    def setUp(self):
        self.__repo = RentRepository()
        self.__repo.removeAll()
        unittest.TestCase.setUp(self)   
        
    def tearDown(self):
        self.__repo.removeAll()
        unittest.TestCase.tearDown(self)
               
    def testAdd(self):
        self.assertEqual(self.__repo.size(), 0)
        rent1 = Rent("1", "1")
        self.__repo.add(rent1)
        self.assertEqual(self.__repo.size(), 1)
        rent2 = Rent("2", "3")
        self.__repo.add(rent2)
        rent3 = Rent("3", "2")
        self.__repo.add(rent3)
        self.assertEqual(self.__repo.size(), 3)
        self.assertEqual(self.__repo.getAllRents(), [rent1, rent2, rent3])
        with self.assertRaises(RepositoryException):
            self.__repo.add(rent3)
    
    def testDelete(self):
        rent1 = Rent("1", "1")
        self.__repo.add(rent1)
        self.assertEqual(self.__repo.size(), 1)
        rent2 = Rent("2", "3")
        self.__repo.add(rent2)
        self.assertEqual(self.__repo.size(), 2)
        self.__repo.delete(rent1)
        self.assertEqual(self.__repo.getAllRents(), [rent2])
        self.__repo.delete(rent2)
        self.assertEqual(self.__repo.getAllRents(), [])
        with self.assertRaises(RepositoryException):
            self.__repo.delete(rent2)
        
    def testRemoveAll(self):
        rent1 = Rent("1", "1")
        self.__repo.add(rent1)
        self.assertEqual(self.__repo.size(), 1)
        rent2 = Rent("2", "3")
        self.__repo.add(rent2)
        rent3 = Rent("3", "2")
        self.__repo.add(rent3)
        self.assertEqual(self.__repo.size(), 3)
        self.__repo.removeAll()
        self.assertEqual(self.__repo.size(), 0)
        
    def testGetNrInchirieri(self):
        rent = Rent("1", "3")
        self.__repo.add(rent)
        self.__repo.delete(rent)
        rent = Rent("2", "3")
        self.__repo.add(rent)
        self.__repo.delete(rent)
        rent = Rent("3", "3")
        self.__repo.add(rent)
        self.__repo.delete(rent)
        rent = Rent("2", "2")
        self.__repo.add(rent)
        self.__repo.delete(rent)
        rent = Rent("1", "2")
        self.__repo.add(rent)
        self.__repo.delete(rent)
        rent = Rent("3", "1")
        self.__repo.add(rent)
        self.__repo.delete(rent)
        rent = Rent("2", "1")
        self.__repo.add(rent)
        self.__repo.delete(rent)
        rent = Rent("1", "1")
        self.__repo.add(rent)
        self.__repo.delete(rent)
        rent = Rent("4", "1")
        self.__repo.add(rent)
        self.assertEqual(self.__repo.size(), 1)
        self.assertEqual(self.__repo.getNrInchirieri("1"), 4)
        self.assertEqual(self.__repo.getNrInchirieri("2"), 2)
        self.assertEqual(self.__repo.getNrInchirieri("3"), 3)
        self.assertEqual(self.__repo.getNrInchirieri("12"), 0)
        self.assertEqual(self.__repo.getNrInchirieri("1123"), 0)
        self.assertEqual(self.__repo.getNrInchirieri("1321312"), 0)
        self.assertEqual(self.__repo.getNrInchirieri("13e2e21312"), 0)
        self.assertEqual(self.__repo.getNrInchirieri("effwefwfwe"), 0)
        self.assertEqual(self.__repo.getNrInchirieri("-12"), 0)
        self.assertEqual(self.__repo.getNrInchirieri(""), 0)        
        
def suite_inmem_repository():
    ts = unittest.TestSuite()
    ts.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFilmRepository))
    ts.addTests(unittest.TestLoader().loadTestsFromTestCase(TestClientRepository))
    ts.addTests(unittest.TestLoader().loadTestsFromTestCase(TestRentRepository))
    return ts