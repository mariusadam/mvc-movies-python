'''
Created on Nov 7, 2015

@author: marius
'''
class Film():
    
    def __init__(self, idFilm, titlu, descriere, gen):
        """
        Creeaza un film nou primind un id, titlul, descrierea si genul
        """
        self.__id = idFilm
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen
        
    def getId(self):
        return self.__id
    
    def getDescriere(self):
        return self.__descriere
    
    def getTitlu(self):
        return self.__titlu
    
    def getGen(self):
        return self.__gen
    
    def __eq__(self, film):
        if film == None:
            return False
        return self.__id == film.getId()
    
    def __str__(self):
        return str(self.__id+" "+self.__titlu+" "+self.__descriere+" "+self.__gen)
    
class Client():
    
    def __init__(self, idClient, nume, CNP):
        """
        Creeaza un client nou primind id-ul, numele si CNP-ul
        """
        self.__id = idClient
        self.__nume = nume
        self.__CNP = CNP
        
    def getId(self):
        return self.__id
    
    def getNume(self):
        return self.__nume
    
    def getCNP(self):
        return self.__CNP   
     
    def __eq__(self, client):
        """
        Testeaza daca doi clienti sunt egali (au acelasi id sau acelasi CNP)
        """
        if client == None: return False
        return self.__id == client.getId()
    
class Rent:
    """
    Reprezinta un imprumut
    """
    def __init__(self, client_id, film_id):
        """
        Primeste id-ul unui client si id-ul unui film inchiriat
        """
        self.__client_id = client_id
        self.__film_id = film_id
        
    def getClientId(self):
        return self.__client_id
    
    def getFilmId(self):
        return self.__film_id
    
    def __str__(self):
        return str(self.__client_id+" "+self.__film_id)
    
    def __eq__(self, ot):
        if ot == None: return False
        return self.__client_id == ot.getClientId() and self.__film_id == ot.getFilmId()

class FilmRent():
    '''
    data transfer object
    '''
    def __init__(self, film, nr_inchirieri):
        self.__film = film 
        self.__nr_inchirieri =  nr_inchirieri
        
    def getFilm(self):
        return self.__film
    
    def getNrInchirieri(self):
        return self.__nr_inchirieri
    
class ClientRent():
    '''
    Data transfer object
    '''
    def __init__(self, client, nr_filme):
        self.__client = client
        self.__nr_filme = nr_filme
    
    def getClient(self):
        return self.__client
    
    def getNrFilme(self):
        return self.__nr_filme
    
    def __eq__(self, cr):
        if cr == None: return False
        return self.getClient() == cr.getClient() and self.getNrFilme() == cr.getNrFilme()
    