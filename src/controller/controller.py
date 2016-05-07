'''
Created on Nov 7, 2015

@author: marius
'''
from src.domain.entities import Film, Client, Rent, FilmRent, ClientRent
#from src.repository.inmem_repository import RepositoryException
from src.utils.sorting_algorithms import quick_sort, gnome_sort

class FilmController():
    
    def __init__(self, repository, validator):
        self.__repo = repository
        self.__validator = validator
        
    def createFilm(self, idFilm, titlu, descriere, gen):
        """
        idFilm, titlu, descriere, gen -stringuri ce reprezinta atributele unui film
        Post: creeaza un nou obiect film daca atributele sunt valide
        raise ValidationException - if film fields are invalid
        """ 
        #creeaza un film
        film = Film(idFilm, titlu, descriere, gen)
        #valideaza filmul folosind un validator
        self.__validator.validate(film)
        return film
    
    def add(self, film):
        """
        Primeste un film si il adauga folosing repository
        raise RepositoryExeption - if film already exist
        """
        #memoreaza filmul folosind repository
        self.__repo.add(film)
    
    def update(self, film):
        """
        Primeste un film si modifica filmul cu id-ul corespunzator din repository
        raise RepositoryException - daca filmul nu exista
        """
        self.__repo.update(film) 
        
    def getAllFilms(self):
        return self.__repo.getAllFilms()
    
    def findById(self, idFilm):
        return self.__repo.findById(idFilm)
    
    def delete(self, film):
        self.__repo.delete(film)
     
    def search(self, crt):
        """
        Date: ctr - string
        Post: Returneaza  lista cu filmele care contin in titlu ca substring pe crt
        """
        allFilms = self.getAllFilms()
        if crt == "": return allFilms
        else:
            rez = []
            for film in allFilms:
                if crt in film.getTitlu(): rez.append(film)
            return rez
        
    def removeAll(self):
        self.__repo.removeAll()
        
class ClientController():
    
    def __init__(self, repository, validator):
        self.__repo = repository
        self.__validator = validator
        
    def createClient(self, idClient, nume, CNP):
        """
        idClient, nume, CNP -stringuri ce reprezinta atributele unui client 
        Post: creeaza un nou obiect client daca atributele sunt valide
        raise ValidationException - if clients fields are invalid
        """ 
        #creeaza un client
        client = Client(idClient, nume, CNP)
        #valideaza clientul folosind un validator
        self.__validator.validate(client)
        return client
    
    def add(self, client):
        """
        Primeste un client si il adauga folosing repository
        raise RepositoryExeption - if client already exist
        """
        #memoreaza client folosind repository
        self.__repo.add(client)
    
    def update(self, client):
        """
        Primeste un client si modifica clientul cu id-ul corespunzator din repository
        raise RepositoryException - daca clientul nu exista
        """
        self.__repo.update(client)
    
    def findById(self, idClient):
        return self.__repo.findById(idClient)
    
    def delete(self, client):
        self.__repo.delete(client)   
            
    def getAllClients(self):
        return self.__repo.getAllClients()
    
    def search(self, crt):
        """
        Date: ctr - string
        Post: Returneaza  lista cu filmele care contin in titlu ca substring pe crt
        """
        allClients = self.getAllClients()
        if crt == "": return allClients
        else:
            return [client for client in allClients if crt in client.getNume()]
        
    def removeAll(self):
        self.__repo.removeAll()

class RentController():
    
    def __init__(self, rent_repo, film_repo, client_repo, validator):
        self.__rent_repo = rent_repo
        self.__film_repo = film_repo
        self.__client_repo = client_repo
        self.__validator = validator 
        
    def createRent(self, idClient, idFilm):
        """
        idClient - id-ul clientului ce efectueaza imprumutul
        idFilm   - id-ul filmului de imprumutat
        Post: creeaza un nou obiect rent daca atributele sunt valide
        raise ValidationException - if rents fields are invalid
        """ 
        #creeaza un imprumut
        rent = Rent(idClient, idFilm)
        #valideaza imprumutul folosind un validator
        self.__validator.validate(rent)
        return rent
    
    def add(self, rent):
        """
        Primeste un imprumut si il adauga folosind repository
        raise RepositoryExeption - if rent already exist
        """
        #memoreaza imprumutul folosind repository
        self.__rent_repo.add(rent)
    
    def delete(self, rent):
        self.__rent_repo.delete(rent)   
            
    def getAllRents(self):
        return self.__rent_repo.getAllRents()  
    
    def getClientiOrdByNrFilmeNume(self):
        '''
        Returneaza o lista sortata dupa numarul de filme, numele clientilor
        Fiecare element al listei returnate este un obiect ce contine un client
        si numarul de filme inchiriate de acesta
        '''
        lista_clienti_cu_filme = self.__getClientiCuFilme()
        #sorted_list = self.__sortByNrFilmeName(lista_clienti_cu_filme)
        sorted_list = quick_sort(lista_clienti_cu_filme, key=lambda x: (-x.getNrFilme(), x.getClient().getNume()))
        return sorted_list
    
    def getClientiOrdByNumeNrFilme(self):
        '''
        Returneaza o lista sortata in care fiecare element este un obiect ce 
        contine un client si nr de filme inchiriate
        lista va fi sortata ascendent dupa numele clientului, iar in caz
        ca doi clienti au acelasi nume, asc dupa nr de filme inchiriate
        '''
        lista_clienti_cu_filme = self.__getClientiCuFilme()   
        #sorted_list = self.__sortClientiByNumeNrFilme(lista_clienti_cu_filme)
        sorted_list = gnome_sort(lista_clienti_cu_filme, key=lambda x: (x.getClient().getNume(), x.getNrFilme()))
        return sorted_list
    
    def getFilmeInchiriate(self):
        '''
        Returneaza o lista cu filme inchiriate 
        Fiecare element din lista este un obiect ce contine 
        un film si nr de inchirieri
        '''
        all_films = self.__film_repo.getAllFilms()
        return [FilmRent(film, self.__rent_repo.getNrInchirieri(film.getId())) for film in all_films if self.__rent_repo.getNrInchirieri(film.getId()) > 0]
    
    def getFilmeInchiriateOrdonat(self):
        '''
        Returneaza o lista cu filme inchiriate ordonata descendent dupa nr. de inchirierim
        ascendent dupa titlu
        Fiecare element din lista este un obiect ce contine un film si nr de inchirieri
        '''
        filme_inchiriate = self.getFilmeInchiriate()
        #return self.__sortFilmeInchiriate(filme_inchiriate)
        return gnome_sort(filme_inchiriate, key=lambda x:(-x.getNrInchirieri(), x.getFilm().getTitlu()))
    
    def removeAll(self):
        self.__rent_repo.removeAll()
    
    def __getClientiCuFilme(self):
        '''
        Returneaza o lista in care fiecare element este un obiect ce 
        contine un client si nr de filme inchiriate
        '''
        all_rents = self.getAllRents()
        all_clients = self.__client_repo.getAllClients()
        lista_clienti_cu_filme = []
        for client in all_clients:
            id_client = client.getId()
            nr_inchirieri = 0
            for rent in all_rents:
                if id_client == rent.getClientId():
                    nr_inchirieri += 1
            if nr_inchirieri > 0:
                lista_clienti_cu_filme.append(ClientRent(client, nr_inchirieri))
        return lista_clienti_cu_filme