'''
Created on Nov 8, 2015

@author: marius
'''
from src.domain.entities import Film, Client, Rent
from src.domain.validator import FilmValidator, ValidatorException,\
    ClientValidator, RentValidator
import unittest

class TestFilmValidator(unittest.TestCase):

    def setUp(self):
        self.__validator = FilmValidator()
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testValidateFilm(self):
        film = Film("1", "Abcd", "Descriere", "Comedie")
        self.__validator.validate(film)
        with self.assertRaises(ValidatorException):
            film = Film("", "Abcd", "Descriere", "Comedie")
            self.__validator.validate(film)
        with self.assertRaises(ValidatorException):
            film = Film("", "", "Descriere", "Comedie")
            self.__validator.validate(film)
        with self.assertRaises(ValidatorException):
            film = Film("", "Abcd", "", "Comedie")
            self.__validator.validate(film)
        with self.assertRaises(ValidatorException):
            film = Film("", "Abcd", "Descriere", "")
            self.__validator.validate(film)
        with self.assertRaises(ValidatorException):
            film = Film("10000", "Abcd", "Descriere", "Gen")
            self.__validator.validate(film)
        with self.assertRaises(ValidatorException):
            film = Film("-11", "Abcd", "Descriere", "Comedie")
            self.__validator.validate(film)
        with self.assertRaises(ValidatorException):
            film = Film("", "", "Descriere", "Cosdddddddddddddddddddddddddddddddddddddddddddddddddddddmedie")
            self.__validator.validate(film)
 
class TestClientValidator(unittest.TestCase):

    def setUp(self):
        self.__validator = ClientValidator()
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testValidateClient(self):
        client = Client("1", "Bill Gates", "1960313012653")         
        self.__validator.validate(client)
        with self.assertRaises(ValidatorException):
            client = Client("-1", "Bill Gates", "1960313012652")
            self.__validator.validate(client)
        with self.assertRaises(ValidatorException):
            client = Client("", "Bill Gates", "1960313012652")
            self.__validator.validate(client)
        with self.assertRaises(ValidatorException):
            client = Client("1", "Bill Gates", "")
            self.__validator.validate(client)
        with self.assertRaises(ValidatorException):
            client = Client("122222", "Bill Gates", "1960313012652")
            self.__validator.validate(client)
        with self.assertRaises(ValidatorException):
            client = Client("1", "Bill Gates", "1111111111111") #ultima cifra ar trebui sa fie 2 !! deci se arunca exceptie
            self.__validator.validate(client)
        with self.assertRaises(ValidatorException):
            client = Client("", "", "")
            self.__validator.validate(client)
        with self.assertRaises(ValidatorException):
            client = Client("1", "Bill Gates", "1963123123123120313012652")
            self.__validator.validate(client)
    
class TestRentValidator(unittest.TestCase):
    
    def setUp(self):
        self.__validator = RentValidator()
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testValidateRent(self):
        rent = Rent("1", "1")
        self.__validator.validate(rent)
        with self.assertRaises(ValidatorException):
            rent = Rent("1", "")
            self.__validator.validate(rent)
        with self.assertRaises(ValidatorException):
            rent = Rent("-1", "")
            self.__validator.validate(rent)
        with self.assertRaises(ValidatorException):
            rent = Rent("12222", "")
            self.__validator.validate(rent)
        with self.assertRaises(ValidatorException):
            rent = Rent("1", "dffew")
            self.__validator.validate(rent)
        with self.assertRaises(ValidatorException):
            rent = Rent("wef1", "fwfewe")
            self.__validator.validate(rent)
        with self.assertRaises(ValidatorException):
            rent = Rent("", "")
            self.__validator.validate(rent)
        with self.assertRaises(ValidatorException):
            rent = Rent("999999999", "9999999")
            self.__validator.validate(rent)
        with self.assertRaises(ValidatorException):
            rent = Rent("-1", "-1")
            self.__validator.validate(rent)
        
def suite_validator():
    ts = unittest.TestSuite()
    ts.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFilmValidator))
    ts.addTests(unittest.TestLoader().loadTestsFromTestCase(TestClientValidator))
    ts.addTests(unittest.TestLoader().loadTestsFromTestCase(TestRentValidator))
    return ts