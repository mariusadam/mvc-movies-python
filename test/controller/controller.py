'''
Created on Nov 9, 2015

@author: marius
'''
from src.controller.controller import FilmController, ClientController,\
    RentController
from src.domain.validator import ValidatorException, FilmValidator,\
    ClientValidator, RentValidator
from src.repository.inmem_repository import RepositoryException, FilmRepository,\
    ClientRepository
import unittest
from src.repository.file_repository import FilmFileRepository,\
    ClientFileRepository, RentFileRepository
from src.domain.entities import Film, Client

class TestFilmController(unittest.TestCase):
    
    def setUp(self):
        repo            = FilmRepository()
        validator       = FilmValidator()
        self.__film_ctr = FilmController(repo, validator)
        unittest.TestCase.setUpClass()
        
    def tearDown(self):
        self.__film_ctr.removeAll()
        unittest.TestCase.tearDown(self)
    
    def testCreate(self):
        film            = self.__film_ctr.createFilm("1", "Filmul1", "Descriere", "SF")
        self.__film_ctr.add(film)
        self.assertEqual(len(self.__film_ctr.getAllFilms()), 1, "Ar trebuie sa fie doar un film adaugat")
        with self.assertRaises(ValidatorException):
            film = self.__film_ctr.createFilm("1", "titlu", "", "Comedie")
            del film
        with self.assertRaises(ValidatorException):
            film = self.__film_ctr.createFilm("-1", "Titlu", "Descriere", "Comedie")
        with self.assertRaises(ValidatorException):
            film = self.__film_ctr.createFilm("-1", "Titlu", "Descriere", "")
        with self.assertRaises(ValidatorException):
            film = self.__film_ctr.createFilm("1", "", "Descriere", "Comedie")
        with self.assertRaises(ValidatorException):
            film = self.__film_ctr.createFilm("1", "", "", "Comedie")
        with self.assertRaises(ValidatorException):
            film = self.__film_ctr.createFilm("", "", "", "")
    
    def testAdd(self):
        film            = self.__film_ctr.createFilm("1", "Filmul1", "Descriere", "SF")
        self.__film_ctr.add(film)
        with self.assertRaises(RepositoryException):
            film = self.__film_ctr.createFilm("1", "Filmul1", "Descriere", "SF")
            self.__film_ctr.add(film)
        film = self.__film_ctr.createFilm("2", "Filmul2", "Descriere", "SF")
        self.__film_ctr.add(film)
        with self.assertRaises(RepositoryException):
            film = self.__film_ctr.createFilm("2", "Filmul1", "Descriere", "SF")
            self.__film_ctr.add(film)
            
    def testUpdate(self):
        film            = self.__film_ctr.createFilm("1", "Filmul1", "Descriere", "SF")
        self.__film_ctr.add(film)
        film = self.__film_ctr.createFilm("2", "Filmul2", "Descriere", "SF")
        self.__film_ctr.add(film)
        film_nou = self.__film_ctr.createFilm("2", "Titlu nou", "Descriere noua", "Comedie")
        self.__film_ctr.update(film_nou)
        self.assertEqual(self.__film_ctr.findById("2").getTitlu(), film_nou.getTitlu(), "Titlul ar trebui sa se modifice")
        self.assertEqual(self.__film_ctr.findById("2").getGen(), film_nou.getGen(), "Genul ar trebui sa se modifice")
        film_nou2 = self.__film_ctr.createFilm("3", "Titlu", "Desc", "Gen")
        with self.assertRaises(RepositoryException):
            self.__film_ctr.update(film_nou2)
            
    def testFindById(self):
        film            = self.__film_ctr.createFilm("1", "Filmul1", "Descriere", "SF")
        self.__film_ctr.add(film)
        film = self.__film_ctr.createFilm("2", "Titlu", "Descriere", "Gen")
        self.__film_ctr.add(film)
        self.assertEqual(self.__film_ctr.findById("2"), film, "Ar trebui sa retunreze filmul u id-ul 2")
        film2 = self.__film_ctr.createFilm("3", "Titlu3", "Desc", "Gen")
        self.__film_ctr.add(film2)
        self.assertEqual(self.__film_ctr.findById("3"), film2, "Ar trebui sa returneze filmul cu id-ul 3")
        with self.assertRaises(RepositoryException):
            film = self.__film_ctr.findById("1234")
        with self.assertRaises(RepositoryException):
            film = self.__film_ctr.findById("-1")
            
    def testDelete(self):
        film            = self.__film_ctr.createFilm("1", "Filmul1", "Descriere", "SF")
        self.__film_ctr.add(film)
        film2 = self.__film_ctr.createFilm("2", "Titlu2", "Descriere", "Gen")
        self.__film_ctr.add(film2)
        self.assertEqual(len(self.__film_ctr.getAllFilms()), 2, "Ar trebui sa fie doua filme adaugate")
        film_de_sters = self.__film_ctr.findById("1")
        self.__film_ctr.delete(film_de_sters)
        self.assertEqual(len(self.__film_ctr.getAllFilms()), 1, "Ar trebui sa existe doar un film")
        film_de_sters2 = self.__film_ctr.findById("2")
        self.__film_ctr.delete(film_de_sters2)
        self.assertEqual(self.__film_ctr.getAllFilms(), [], "Nu ar mai trebui sa existe niciun film")
        
    def testSearch(self):
        film            = self.__film_ctr.createFilm("1", "Filmul1", "Descriere", "SF")
        self.__film_ctr.add(film)
        film2 = self.__film_ctr.createFilm("2", "Titlu2", "Descriere", "Gen")
        self.__film_ctr.add(film2)
        self.assertEqual(len(self.__film_ctr.search("")), len(self.__film_ctr.getAllFilms()), "Ar trebui sa returneze toti clientii")
        self.assertEqual(self.__film_ctr.search("3"), [], "Niciun film nu corespunde criteriului de cautare")
        self.assertEqual(self.__film_ctr.search("2"), [film2], "Doar clientul cu id-ul 2 corespunde criteriului")
        
class TestClientController(unittest.TestCase):
    '''
    Clasa de test pentru controller-ul de clienti
    '''
    def setUp(self):
        repo              = ClientRepository()
        validator         = ClientValidator()
        self.__client_ctr = ClientController(repo, validator)
        unittest.TestCase.setUp(self)
    
    def tearDown(self):
        self.__client_ctr.removeAll()
        unittest.TestCase.tearDown(self)
        
    def testCreate(self):
        client = self.__client_ctr.createClient("1", "Ceva nume", "1960313012653")
        self.__client_ctr.add(client)
        self.assertEqual(len(self.__client_ctr.getAllClients()), 1, "Ar trebuie sa fie doar un client in repository")
        with self.assertRaises(ValidatorException):
            client = self.__client_ctr.createClient("32r2r", "Nume nou", "1960313012653")
            del client
        with self.assertRaises(ValidatorException):
            client = self.__client_ctr.createClient("qwe", "Nume nou", "1960313012653")
        with self.assertRaises(ValidatorException):
            client = self.__client_ctr.createClient("2", "Nume nou", "1111111111111")
        with self.assertRaises(ValidatorException):
            client = self.__client_ctr.createClient("-11", "", "1960313012653")
        with self.assertRaises(ValidatorException):
            client = self.__client_ctr.createClient("", "", "")
        with self.assertRaises(ValidatorException):
            client = self.__client_ctr.createClient("", "Nume", "1960313012653")
        with self.assertRaises(ValidatorException):
            client = self.__client_ctr.createClient("1", "Nume", "")
        with self.assertRaises(ValidatorException):
            client = self.__client_ctr.createClient("1", "", "1960313012653")

    def testAdd(self):
        client = self.__client_ctr.createClient("1", "Ceva nume", "1960313012653")
        self.__client_ctr.add(client)
        with self.assertRaises(RepositoryException):
            client2 = self.__client_ctr.createClient("1", "Nume Nou", "1960313012653")
            self.__client_ctr.add(client2)
        client3 = self.__client_ctr.createClient("3", "Clientul3", "1960313012653")
        self.__client_ctr.add(client3)
        with self.assertRaises(RepositoryException):
            client4 = self.__client_ctr.createClient("3", "Nume Nou", "1960313012653")
            self.__client_ctr.add(client4)
        
    def testUpdate(self):
        client = self.__client_ctr.createClient("1", "Ceva nume", "1960313012653")
        self.__client_ctr.add(client)
        client_nou = self.__client_ctr.createClient("1", "Nume actualizat", "1960313012653")
        self.__client_ctr.update(client_nou)
        self.assertEqual(self.__client_ctr.search("actualizat"), [client_nou], "Ar trebui sa returneze clientul actualizat")
        client_nou2 = client_nou = self.__client_ctr.createClient("211", "Nume actualizat", "1960313012653")
        with self.assertRaises(RepositoryException):
            self.__client_ctr.update(client_nou2)
     
    def testFindById(self):
        client = self.__client_ctr.createClient("1", "Ceva nume", "1960313012653")
        self.__client_ctr.add(client)
        client2 = self.__client_ctr.createClient("2", "Andrei", "1960313012653")
        self.__client_ctr.add(client2)
        self.assertEqual(self.__client_ctr.findById("2"), client2, "Ar trebui sa returneze clientul cu id-ul 2")   
        with self.assertRaises(RepositoryException):
            client = self.__client_ctr.findById("1234")
            del client
        with self.assertRaises(RepositoryException):
            client = self.__client_ctr.findById("-1")
        
        
    def testSearch(self):
        client = self.__client_ctr.createClient("1", "Ceva nume", "1960313012653")
        self.__client_ctr.add(client)
        self.assertEqual(len(self.__client_ctr.search("")), 
                         len(self.__client_ctr.getAllClients()), 
                         "Ar trebui sa returneze numarul de clienti inregistrati")
        client2 = self.__client_ctr.createClient("2", "Andrei", "1960313012653")
        self.__client_ctr.add(client2)
        self.assertEqual(len(self.__client_ctr.search("")), 
                         len(self.__client_ctr.getAllClients()), #aici!!!
                         "Ar trebui sa returneze numarul de clienti inregistrati")
        self.assertEqual(len(self.__client_ctr.getAllClients()), 2, "Numarul de clienti inregistrati ar trebui sa fie 2")
    
    def testDelete(self):
        client = self.__client_ctr.createClient("1", "Ceva nume", "1960313012653")
        self.__client_ctr.add(client)
        client2 = self.__client_ctr.createClient("2", "Clientul3", "1960313012653")
        self.__client_ctr.add(client2)
        self.assertEqual(len(self.__client_ctr.getAllClients()), 2, "Ar trebui sa fie 2 clienti inregistrati")
        client_de_sters = self.__client_ctr.findById("1")
        self.__client_ctr.delete(client_de_sters)
        self.assertEqual(self.__client_ctr.getAllClients(), [client2], "Numai al doilea client ar trebui sa mai fie inregistrat")
        client_de_sters = self.__client_ctr.findById("2")
        self.__client_ctr.delete(client_de_sters)
        self.assertEqual(len(self.__client_ctr.getAllClients()), 0, "Nu ar mai trebui sa fie niciun client inregistrat")

class TestRentController(unittest.TestCase):
    
    def setUp(self):
        rent_repo          = RentFileRepository  ("test_rents.txt")
        film_repo          = FilmFileRepository  ("test_filme.txt")
        client_repo        = ClientFileRepository("test_clienti.txt")
        validator          = RentValidator()
        self.__ctr         = RentController(rent_repo, film_repo, client_repo, validator)
        self.__film_repo   = film_repo
        self.__client_repo = client_repo
        self.__ctr.removeAll()
        self.__film_repo.removeAll()
        self.__client_repo.removeAll()
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        self.__ctr.removeAll()
        self.__film_repo.removeAll()
        self.__client_repo.removeAll()
        unittest.TestCase.tearDown(self)
        
    def testCreateRent(self):
        rent = self.__ctr.createRent("1", "1")
        self.__ctr.add(rent)
        with self.assertRaises(RepositoryException):
            self.__ctr.add(rent)
        with self.assertRaises(ValidatorException):
            rent = self.__ctr.createRent("", "1")
        with self.assertRaises(ValidatorException):
            rent = self.__ctr.createRent("-1", "1")
        with self.assertRaises(ValidatorException):
            rent = self.__ctr.createRent("23e23e", "1")
        with self.assertRaises(ValidatorException):
            rent = self.__ctr.createRent("9999999", "2")
        with self.assertRaises(ValidatorException):
            rent = self.__ctr.createRent("2", "")
        with self.assertRaises(ValidatorException):
            rent = self.__ctr.createRent("4", "-5")
            
    def testAdd(self):
        self.assertEqual(self.__ctr.getAllRents(), [])
        rent = self.__ctr.createRent("1", "1")
        self.__ctr.add(rent)
        self.assertEqual(self.__ctr.getAllRents(), [rent])
        with self.assertRaises(RepositoryException):
            self.__ctr.add(rent)
            
    def testGetAllRents(self):
        self.assertTrue(self.__ctr.getAllRents() == [])
        rent1 = self.__ctr.createRent("1", "1")
        self.__ctr.add(rent1)
        rent2 = self.__ctr.createRent("1", "2")
        self.__ctr.add(rent2)
        rent3 = self.__ctr.createRent("1", "3")
        self.__ctr.add(rent3)
        self.assertTrue(self.__ctr.getAllRents() == [rent1, rent2, rent3])
        self.__ctr.removeAll()
        self.assertTrue(self.__ctr.getAllRents() == [])
    
    def testDelete(self):
        rent1 = self.__ctr.createRent("1", "1")
        self.__ctr.add(rent1)
        rent2 = self.__ctr.createRent("1", "2")
        self.__ctr.add(rent2)
        self.__ctr.delete(rent1)
        self.assertTrue(self.__ctr.getAllRents() == [rent2])
        self.__ctr.delete(rent2)
        self.assertTrue(self.__ctr.getAllRents() == [])
        with self.assertRaises(RepositoryException):
            self.__ctr.delete(rent1)
        with self.assertRaises(RepositoryException):
            self.__ctr.delete(rent1)
        
    def testGetClientiOrdByNrFilmeNume(self):
        rez = self.__ctr.getClientiOrdByNrFilmeNume()
        self.assertTrue(rez == [])
        film1 = Film("1", "Aaaa", "Neimportant1", "Gen1")
        self.__film_repo.add(film1)
        film2 = Film("2", "Bbbb", "Neimportant2", "Gen2")
        self.__film_repo.add(film2)
        film3 = Film("3", "Aacc", "Neimportant3", "Gen3")
        self.__film_repo.add(film3)
        film4 = Film("4", "Aacc", "Neimportant4", "Gen4")
        self.__film_repo.add(film4)
        film5 = Film("5", "Bbbb", "Neimportant5", "Gen5")
        self.__film_repo.add(film5)
        client1 = Client("1", "Nume1", "1960312012653")
        self.__client_repo.add(client1)
        client2 = Client("2", "Nume2", "1960312012653")
        self.__client_repo.add(client2)
        client3 = Client("3", "Nume3", "1960312012653")
        self.__client_repo.add(client3)
        rent = self.__ctr.createRent("1", "1")
        self.__ctr.add(rent)
        rent = self.__ctr.createRent("1", "2")
        self.__ctr.add(rent)
        rent = self.__ctr.createRent("2", "3")
        self.__ctr.add(rent)
        rent = self.__ctr.createRent("3", "4")
        self.__ctr.add(rent)
        rent = self.__ctr.createRent("3", "5")
        self.__ctr.add(rent)
        rez = self.__ctr.getClientiOrdByNrFilmeNume()
        self.assertEqual(rez[0].getClient(), client1)
        self.assertEqual(rez[1].getClient(), client3)
        self.assertEqual(rez[2].getClient(), client2)
        
    def testGetClientiOrdByNumeNrFilme(self):
        rez = self.__ctr.getClientiOrdByNumeNrFilme()
        self.assertTrue(rez == [])
        film1 = Film("1", "Aaaa", "Neimportant1", "Gen1")
        self.__film_repo.add(film1)
        film2 = Film("2", "Bbbb", "Neimportant2", "Gen2")
        self.__film_repo.add(film2)
        film3 = Film("3", "Aacc", "Neimportant3", "Gen3")
        self.__film_repo.add(film3)
        film4 = Film("4", "Aacc", "Neimportant4", "Gen4")
        self.__film_repo.add(film4)
        film5 = Film("5", "Bbbb", "Neimportant5", "Gen5")
        self.__film_repo.add(film5)
        client1 = Client("1", "Nume", "1960312012653")
        self.__client_repo.add(client1)
        client2 = Client("2", "Nume2", "1960312012653")
        self.__client_repo.add(client2)
        client3 = Client("3", "Nume", "1960312012653")
        self.__client_repo.add(client3)
        rent = self.__ctr.createRent("1", "1")
        self.__ctr.add(rent)
        rent = self.__ctr.createRent("1", "2")
        self.__ctr.add(rent)
        rent = self.__ctr.createRent("1", "3")
        self.__ctr.add(rent)
        rent = self.__ctr.createRent("3", "4")
        self.__ctr.add(rent)
        rent = self.__ctr.createRent("3", "5")
        self.__ctr.add(rent)
        rez = self.__ctr.getClientiOrdByNumeNrFilme()
        self.assertEqual(rez[0].getClient(), client3)
        self.assertEqual(rez[1].getClient(), client1)

    def testGetFilmeInchiriate(self):
        rez = self.__ctr.getFilmeInchiriateOrdonat()
        self.assertTrue(rez == [])
        film1 = Film("1", "Aaaa", "Neimportant1", "Gen1")
        self.__film_repo.add(film1)
        film2 = Film("2", "Bbbb", "Neimportant2", "Gen2")
        self.__film_repo.add(film2)
        film3 = Film("3", "Aacc", "Neimportant3", "Gen3")
        self.__film_repo.add(film3)
        film4 = Film("4", "Aacc", "Neimportant4", "Gen4")
        self.__film_repo.add(film4)
        film5 = Film("5", "Bbbb", "Neimportant5", "Gen5")
        self.__film_repo.add(film5)
        client1 = Client("1", "Nume", "1960312012653")
        self.__client_repo.add(client1)
        client2 = Client("2", "Nume2", "1960312012653")
        self.__client_repo.add(client2)
        client3 = Client("3", "Nume", "1960312012653")
        self.__client_repo.add(client3)
        rent = self.__ctr.createRent("1", "1")
        self.__ctr.add(rent)
        self.__ctr.delete(rent)
        rent = self.__ctr.createRent("2", "1")
        self.__ctr.add(rent)
        rent = self.__ctr.createRent("1", "3")
        self.__ctr.add(rent)
        self.__ctr.delete(rent)
        rent = self.__ctr.createRent("2", "3")
        self.__ctr.add(rent)
        rent = self.__ctr.createRent("3", "5")
        self.__ctr.add(rent)        
        rez = self.__ctr.getFilmeInchiriateOrdonat()
        self.assertEqual(rez[0].getFilm(), film1)
        self.assertEqual(rez[1].getFilm(), film3)
        self.assertEqual(rez[2].getFilm(), film5)
        
def suite_controller():
    ts = unittest.TestSuite()
    ts.addTests(unittest.TestLoader().loadTestsFromTestCase(TestClientController))
    ts.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFilmController))
    ts.addTests(unittest.TestLoader().loadTestsFromTestCase(TestRentController))
    return ts
