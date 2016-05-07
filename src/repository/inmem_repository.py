'''
Created on Nov 7, 2015

@author: marius
'''
from src.domain.entities import Film, Client, Rent

class RepositoryException(Exception):
    def __init__(self, errors):
        self.__errors = errors
    
    def getErrors(self):
        eroare = self.__errors[0]
        for i in range(1, len(self.__errors)): eroare +="\n"+self.__errors[i] 
        return eroare
    
    def __str__(self):
        return self.getErrors()


class FilmRepository():
    
    def __init__(self):
        self.__filme = []
    
    def createEntryes(self):
        film = Film("1", "Rush Hour", "Film foarte bun", "Comedie")
        self.add(film)
        film = Film("2", "Rush Hour 2", "Film oarte bun", "Comedie")
        self.add(film)
        film = Film("3", "Fast and Furious 1", "Masini scumpe :)", "Actiune")
        self.add(film)
        film = Film("4", "Fast and Furious 2", "Masini scumpe :)", "Actiune")
        self.add(film)
        film = Film("5", "Fast and Furious 7", "O adevarata capodopera", "Actiune")
        self.add(film)
        film = Film("6", "Circle(2015)", "Ceva descriere", "SF")
        self.add(film)

    def add(self, film):
        """
        Adauga un film in repository
        Ridica RepositoryException daca exista un film cu acelasi id
        """
        if film in self.__filme: raise RepositoryException(["Duplicated film id!"])
        self.__filme.append(film)
    
    def update(self, film):
        """
        Modifica un film din repository
        Daca filmul cautat nu exista se ridica RepositoryException
        """
        errors = []
        if not film in self.__filme: errors.append("Nu exista nici un film cu id-ul introdus")
        else:
            pos = self.__filme.index(film)
            self.__filme[pos] = film
        if len(errors) > 0: raise RepositoryException(errors)
    
    def delete(self, film):
        """
        Sterge filmul din repository
        Daca filmul de sters nu exista se ridica RepositoryException
        """
        if film in self.__filme: self.__filme.remove(film)
        else: raise RepositoryException(["Nu exista nici un film cu id-ul introdus!"])
        
    def findById(self, idFilm):
        """
        Primeste un id si returneaza filmul cu id-ul corespunzator
        raise RepositoryException daca filmul cu id-ul introdus nu exista 
        """
        pos = -1
        alls = self.__filme
        for i in range(len(alls)):
            if alls[i].getId() == idFilm:
                pos = i
                break    
        if pos != -1: return self.__filme[pos]
        else: raise RepositoryException(["Nu exista nici un film cu id-ul introdus!"])
               
    def size(self):
        """
        Returneaza numarul de filme din repository
        """
        return len(self.__filme)
    
    def getAllFilms(self):
        """
        Returneaza o lista cu toate filmele din repository
        """
        return self.__filme
    
    def removeAll(self):
        self.__filme = []
        
class ClientRepository():
    
    def __init__(self):
        self.__clienti = []
    
    def add(self, client):
        """
        Adauga un client in dictionarul __clienti
        Ridica RepositoryException daca exista un client cu acelasi id
        """
        errors = []
        if client in self.__clienti: errors.append("Duplicated client id")
        else: self.__clienti.append(client)
        if len(errors) > 0: raise RepositoryException(errors)
    
    def update(self, client):
        """
        Modifica un film din repository
        Daca filmul cautat nu exista se ridica RepositoryException
        """
        errors = []
        if not (client in self.__clienti): errors.append("Nu exista nici un film cu id-ul introdus")
        else:
            pos  = self.__clienti.index(client)
            self.__clienti[pos] = client
        if len(errors) > 0: raise RepositoryException(errors)
    
    def createEntryes(self):
        client = Client("1", "Bill Gates", "1960313012653")   
        self.add(client)
        client = Client("2", "Ceva Nume", "1851021345131")   
        self.add(client)
        client = Client("3", "Nume Test", "1930114152084")   
        self.add(client)
        client = Client("4", "Inca un test", "1930729213031")   
        self.add(client)
        client = Client("5", "Abc", "1931110257176")   
        self.add(client)
        client = Client("6", "Nume", "1911202393786")   
        self.add(client)
        
    def size(self):
        """
        Returneaza numarul de clienti din repository
        """
        return len(self.__clienti)
    
    def getAllClients(self):
        """
        Returneaza o lista cu toti clientii din repository
        """
        return self.__clienti
    
    def delete(self, client):
        """
        Sterge clientul din repository
        Daca clientul de sters nu exista se ridica RepositoryException
        """
        if client in self.__clienti: self.__clienti.remove(client)
        else: raise RepositoryException(["Nu exista nici un client cu id-ul introdus!"])
        
    def findById(self, idClient):
        """
        Primeste un id si returneaza clientul cu id-ul corespunzator
        raise RepositoryException daca clientul cu id-ul introdus nu exista 
        """
        pos = -1
        alls = self.__clienti
        for i in range(len(alls)):
            if alls[i].getId() == idClient:
                pos = i
                break
        if pos != -1: return self.__clienti[pos]
        else: raise RepositoryException(["Nu exista nici un client cu id-ul introdus!"])
        
    def removeAll(self):
        self.__clienti = []

class RentRepository():
    
    def __init__(self):
        self.__items = []
        self.__nr_inchirieri = {}
    
    def createEntryes(self):
        rent = Rent('1', '1')
        self.add(rent)    
        rent = Rent('2', '2')
        self.add(rent) 
        rent = Rent('2', '3')
        self.add(rent) 
        rent = Rent('2', '4')
        self.add(rent) 
        rent = Rent('2', '6')
        self.add(rent) 
        rent = Rent('3', '5')
        self.add(rent) 
   
    def add(self, rent):
        """
        Adauga un imprumut in lista de imprumuturi
        Ridica RepositoryException daca exista imprumutul exista deja in lista
        """
        errors = []
        if rent in self.__items:
            errors.append("Clientul cu id-ul "+str(rent.getClientId())+" are deja imprumutat filmul cu id-ul "+str(rent.getFilmId()))
        else:
            if self.__imprumutat(rent.getFilmId()):
                errors.append("Filmul cu id-ul "+str(rent.getFilmId())+" este deja imprumutat")  
        if len(errors) > 0: raise RepositoryException(errors)
        else:
            self.__items.append(rent)
            self.__countOne(rent.getFilmId())
     
    def __countOne(self, id_film):
        if id_film in self.__nr_inchirieri: self.__nr_inchirieri[id_film] += 1
        else: self.__nr_inchirieri[id_film] = 1
                    
    def __countAll(self):
        all_rents = self.getAllRents()
        for rent in all_rents:
            id_film = rent.getFilmId()
            self.__countOne(id_film)
            
    def getNrInchirieri(self, id_film):
        if id_film in self.__nr_inchirieri: return self.__nr_inchirieri[id_film]
        else: return 0  
            
    def __imprumutat(self, idFilm):
        allRents = self.getAllRents()
        for rent in allRents:
            if idFilm == rent.getFilmId(): return True
        return False
           
    def getAllRents(self):
        """
        Returneaza o lista cu toate imprumuturile din repository
        """
        return self.__items
    
    def removeAll(self):
        self.__items = []
        
    def size(self):
        return len(self.__items)
    
    def delete(self, rent):
        """
        Sterge imprumutul din repository
        Daca imprumutul de sters nu exista se ridica RepositoryException
        """
        if rent in self.__items: self.__items.remove(rent)
        else: raise RepositoryException(["Clientul cu id-ul "+str(rent.getClientId())+" nu a imprumutat filmul cu id-ul "+str(rent.getFilmId())])