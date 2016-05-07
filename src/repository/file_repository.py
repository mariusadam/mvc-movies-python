'''
Created on Nov 19, 2015

@author: Adam
'''
from src.domain.entities import Film, Client, Rent
from src.repository.inmem_repository import RepositoryException
    
class FilmFileRepository:
    """
    Salveaza/returneaza filme din repository
    """
    def __init__(self, file):
        """
        initializeza repository
        file - string, numele/calea fisierului unde sunt memorate filmele
        post: filmele sunt incarcate din fisier
        """
        self.__file_name = file
        self.__sep = " _ "
        
    def __loadFromFile(self):
        """
        Incarca filmele din fisier
        Returneaza o lista formata din obiecte de tip film
        raise RepositoryException if there is an error when reading from the file
        """
        rez = []
        try:
            f = open(self.__file_name, "r")
            line = f.readline().strip()
            while line!="":
                attrs = line.split(self.__sep)
                film = Film(attrs[0], attrs[1], attrs[2], attrs[3])
                rez.append(film)
                line = f.readline().strip()
            f.close()
        except IOError:
            f = open(self.__file_name, "w")
            #raise RepositoryException(["Error while loading from file "+self.__file_name])
        return rez
    
    def __storeToFile(self, filme):
        """
         Store all the films in the file 
         raise RepositoryException if we can not store to the file
        """
        #open file (rewrite file)
        try:
            f = open(self.__file_name, "w")
            for film in filme:
                film_format = film.getId()+self.__sep+film.getTitlu()+self.__sep+film.getDescriere()+self.__sep+film.getGen() 
                film_format += "\n"
                f.write(film_format)
            f.close()
        except IOError:
            raise RepositoryException(["Error while saving to file " +self.__file_name])
    
    def add(self, film):
        """
        Adauga un film in fisier
        Ridica RepositoryException daca exista un film cu acelasi id
        """
        all_films = self.__loadFromFile()
        if all_films != [] and film in all_films: raise RepositoryException(["Duplicated film id"])
        all_films.append(film)
        self.__storeToFile(all_films)
            
    
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
            
    def update(self, film):
        """
        Modifica un film din repository
        Daca filmul cautat nu exista se ridica RepositoryException
        """
        errors = []
        all_films = self.__loadFromFile()
        if not (film in all_films): errors.append("Nu exista nici un film cu id-ul introdus")
        else:
            pos = all_films.index(film)
            all_films[pos] = film
            self.__storeToFile(all_films)
        if len(errors) > 0: raise RepositoryException(errors)
    
    def delete(self, film):
        """
        Sterge filmul din repository
        Daca filmul de sters nu exista se ridica RepositoryException
        """
        all_films = self.__loadFromFile()
        pos = -1
        for i in range(len(all_films)):
            if film == all_films[i]:
                pos = i
                break
        if pos == -1: raise RepositoryException(["Nu exista nici un film cu id-ul introdus!"])
        else:
            del all_films[pos]
            self.__storeToFile(all_films)
            
    def findById(self, idFilm):
        """
        Primeste un id si returneaza filmul cu id-ul corespunzator
        raise RepositoryException daca filmul cu id-ul introdus nu exista 
        """
        all_films = self.__loadFromFile()
        for film in all_films:
            if film.getId() == idFilm: return film
        raise RepositoryException(["Nu exista nici un film cu id-ul introdus!"])
               
    def size(self):
        """
        Returneaza numarul de filme din repository
        """
        return len(self.__loadFromFile())
    
    def getAllFilms(self):
        """
        Returneaza o lista cu toate filmele din repository
        """
        return self.__loadFromFile()

    def removeAll(self):
        self.__storeToFile([])
        
class ClientFileRepository():
    """
    Salveaza/returneaza clientii din repository
    """
    def __init__(self, file):
        """
        initializeza repository
        file - string, numele/calea fisierului unde sunt memorati clientii
        post: clientii sunt incarcate din fisier
        """
        self.__file_name = file 
        self.__sep = " _ "
        
    def __loadFromFile(self):
        """
        Incarca clientii din fisier
        Returneaza o lista formata din obiecte de tip client
        raise RepositoryException if there is an error when reading from the file
        """
        rez = []
        try:
            f = open(self.__file_name, "r")
            line = f.readline().strip()
            while line!="":
                attrs = line.split(self.__sep)
                client = Client(attrs[0], attrs[1], attrs[2])
                rez.append(client)
                line = f.readline().strip()
            f.close()
        except IOError:
            f = open(self.__file_name, "w")
            #raise RepositoryException(["Error while loading from file "+self.__file_name])
        return rez
    
    def __storeToFile(self, clienti):
        """
         Store all the clients in the file 
         raise RepositoryException if we can not store to the file
        """
        #open file (rewrite file)
        try:
            f = open(self.__file_name, "w")
            for client in clienti:
                client_format = client.getId()+self.__sep+client.getNume()+self.__sep+\
                                client.getCNP()
                client_format += "\n"
                f.write(client_format)
            f.close()
        except IOError:
            raise RepositoryException(["Error while saving to file " +self.__file_name])
    
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
        
    def add(self, client):
        """
        Adauga un client in fisier
        Ridica RepositoryException daca exista un client cu acelasi id
        """
        all_clients = self.__loadFromFile()
        if all_clients != [] and client in all_clients: raise RepositoryException(["Clientul deja exista in evidenta"])
        all_clients.append(client)
        self.__storeToFile(all_clients)
            
        
    def update(self, client):
        """
        Modifica un client din repository
        Daca clientul cautat nu exista se ridica RepositoryException
        """
        errors = []
        all_clients = self.__loadFromFile()
        if not (client in all_clients): errors.append("Nu exista nici un client cu id-ul introdus")
        else:
            pos = all_clients.index(client)
            all_clients[pos] = client
            self.__storeToFile(all_clients)
        if len(errors) > 0: raise RepositoryException(errors)            
            
    def getAllClients(self):
        """
        Returneaza o lista cu toti clientii din repository
        """
        return self.__loadFromFile()
    
    def delete(self, client):
        """
        Sterge clientul din repository
        Daca clientul de sters nu exista se ridica RepositoryException
        """
        all_clients = self.__loadFromFile()
        pos = -1
        for i in range(len(all_clients)):
            if client == all_clients[i]:
                pos = i
                break
        if pos == -1: raise RepositoryException(["Nu exista nici un client cu id-ul introdus!"])
        else:
            del all_clients[pos]
            self.__storeToFile(all_clients)
            
    def findById(self, idClient):
        """
        Primeste un id si returneaza clientul cu id-ul corespunzator
        raise RepositoryException daca filmul cu id-ul introdus nu exista 
        """
        all_clients = self.__loadFromFile()
        for client in all_clients:
            if client.getId() == idClient: return client
        raise RepositoryException(["Nu exista nici un client cu id-ul introdus!"])
     
    def size(self):
        """
        Returneaza numarul de clienti din repository
        """
        return len(self.__loadFromFile())
    
    def getAllFilms(self):
        """
        Returneaza o lista cu toti clientii din repository
        """
        return self.__loadFromFile()

    def removeAll(self):
        self.__storeToFile([])
        
class RentFileRepository():
    """
    Salveaza/returneaza imprumuturile din repository
    """
    def __init__(self, file):
        """
        initializeza repository
        file - string, numele/calea fisierului unde sunt memorate imprumuturile
        post: impurmuturile sunt incarcate din fisier
        """
        self.__file_name = file 
        self.__nr_inchirieri = {}
        self.__sep = " _ "
        self.__countAll()
        
    def __loadFromFile(self):
        """
        Incarca imprumuturile din fisier
        Returneaza o lista formata din obiecte de tip rent
        raise RepositoryException if there is an error when reading from the file
        """
        rez = []
        try:
            f = open(self.__file_name, "r")
            line = f.readline().strip()
            while line!="":
                attrs = line.split(self.__sep)
                rent = Rent(attrs[0], attrs[1])
                rez.append(rent)
                line = f.readline().strip()
            f.close()
        except IOError:
            f = open(self.__file_name, "w")
            #raise RepositoryException(["Error while loading from file "+self.__file_name])
        return rez
    
    def __storeToFile(self, rents):
        """
         Store all the rents in the file 
         raise RepositoryException if we can not store to the file
        """
        #open file (rewrite file)
        try:
            f = open(self.__file_name, "w")
            for rent in rents:
                rent_format = rent.getClientId()+self.__sep+rent.getFilmId()
                rent_format += "\n"
                f.write(rent_format)
            f.close()
        except IOError:
            raise RepositoryException(["Error while saving to file " +self.__file_name])
    
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
     
    def __countOne(self, id_film):
        if id_film in self.__nr_inchirieri: self.__nr_inchirieri[id_film] += 1
        else: self.__nr_inchirieri[id_film] = 1
            
    def add(self, rent):
        """
        Adauga un imprumut in fisier
        Ridica RepositoryException daca exista imprumutul exista deja in lista
        """
        all_rents = self.__loadFromFile()
        if rent in all_rents:
            raise RepositoryException(["Clientul cu id-ul "+str(rent.getClientId())+\
                                       " are deja imprumutat filmul cu id-ul "+\
                                       str(rent.getFilmId())])
        elif self.__imprumutat(rent.getFilmId()):
            raise RepositoryException(["Filmul cu id-ul "+str(rent.getFilmId())+" este deja imprumutat"])
        all_rents.append(rent)
        self.__countOne(rent.getFilmId())
        self.__storeToFile(all_rents)
    
    def delete(self, rent):
        """
        Sterge imprumutul din repository
        Daca imprumutul de sters nu exista se ridica RepositoryException
        """
        all_rents = self.getAllRents()
        if rent in all_rents:
            all_rents.remove(rent)
            self.__storeToFile(all_rents)
        else: raise RepositoryException(["Clientul cu id-ul "+str(rent.getClientId())+" nu a imprumutat filmul cu id-ul "+str(rent.getFilmId())])
            
    def __imprumutat(self, idFilm):
        all_rents = self.getAllRents()
        for rent in all_rents:
            if idFilm == rent.getFilmId(): return True
        return False
    
    def __countAll(self):
        all_rents = self.getAllRents()
        for rent in all_rents:
            id_film = rent.getFilmId()
            self.__countOne(id_film)
            
    def getNrInchirieri(self, id_film):
        if id_film in self.__nr_inchirieri: return self.__nr_inchirieri[id_film]
        else: return 0
               
    def getAllRents(self):
        """
        Returneaza o lista cu toate imprumuturile din repository
        """
        return self.__loadFromFile()
    
    def size(self):
        """
        Returneaza numarul de imprumuturi din repository
        """
        return len(self.__loadFromFile())
    
    def removeAll(self):
        self.__storeToFile([])