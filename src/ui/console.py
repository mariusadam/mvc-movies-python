'''
Created on Nov 7, 2015

@author: marius
'''
from src.domain.validator import ValidatorException
from src.repository.inmem_repository import RepositoryException
import os


class Screen(object):
    @staticmethod
    def wait():
        stop = input("\nApasati Enter pentru a continua...")
        del stop

class Console:

    '''
    Reprezinta meniul principal in interactiunea cu utilizatorul
    Primeste controller-ele filmului si clientului
    '''

    def __init__(self, film_ctr, client_ctr, rent_ctr):
        '''
        Constructor for the console
        '''
        self.__film_ctr = film_ctr
        self.__client_ctr = client_ctr
        self.__rent_ctr = rent_ctr
        self.__initCommands()       
    
    def __initCommands(self):
        """
        Initializeaza un dictionar cu anumite comenzi corespunzatoare meniului principal
        """
        self.__cmd = {}
        self.__cmd['1'] = AdaugareUI(self.__film_ctr, self.__client_ctr)
        self.__cmd['2'] = ModificareUI(self.__film_ctr, self.__client_ctr)
        self.__cmd['3'] = StergereUI(self.__film_ctr, self.__client_ctr)
        self.__cmd['4'] = CautareUI(self.__film_ctr, self.__client_ctr)
        self.__cmd['5'] = InchiriereUI(self.__film_ctr, self.__client_ctr, self.__rent_ctr)
        self.__cmd['6'] = RapoarteUI(self.__rent_ctr)
        self.__cmd['7'] = AfisareUI(self.__film_ctr, self.__client_ctr)
            
    def __readCommand(self):
        """
        Afiseaza meniul principal si citeste o comanda
        Returneaza o comanda citita de la tastatura
        """
        print("\nMeniul principal:")
        print("                 0 < - > Iesire")
        print("                 1 < - > Adaugare")
        print("                 2 < - > Modificare")
        print("                 3 < - > Stergere")
        print("                 4 < - > Cautare")
        print("                 5 < - > Inchiriere/returnare")
        print("                 6 < - > Rapoarte")
        print("                 7 < - > Afisare")
        return input("Introduceti optiunea ")      
                
    def run(self):
        """
        Porneste interactiunea cu utlizatorul in cadrul meniului principal
        """
        while True:
            os.system("cls")
            c = self.__readCommand()
            if c == '0':
                os.system("cls")
                print('Iesire...')
                Screen.wait()
                break
            try:
                submenu = self.__cmd[c]
                submenu.run()
            except KeyError :
                os.system("cls")
                print('Optiune incorecta.Incercati din nou!')
                Screen.wait()
            except ValueError as ve:
                os.system("cls")
                print('Exceptie in aplicatie: ' + ve)
                Screen.wait   
            except :
                os.system("cls")
                print('Ceva nu a mers bine.Va rog incercati din nou...') 
                raise       

class AdaugareUI():
    '''
    Realizeaza interactiunea cu utilizatorul in cadrul submeniului adaugare
    Primeste controller-ele filmului si clientului
    '''
    def __init__(self, film_ctr, client_ctr):
        self.__film_ctr = film_ctr
        self.__client_ctr = client_ctr
        self.__initCommands()
        
    def __initCommands(self):
        """
        Initializeaza un dictionar cu anumite comenzi corespunzatoare submeniului adaugare
        """
        self.__cmd = {}
        self.__cmd['1'] = self.__addFilm
        self.__cmd['2'] = self.__addClient
        
    def __addFilm(self):
        """
        Adauga un film citit din consola
        """
        idFilm = input("Introduceti id-ul: ")
        titlu = input("Introduceti titlul: ")
        descriere = input ("Introduceti descrierea: ")
        gen = input("Introduceti genul: ") 
        print("\n")
        try:
            film = self.__film_ctr.createFilm(idFilm, titlu, descriere, gen)
            self.__film_ctr.add(film)
            print("Filmul", film.getTitlu(),"a fost salvat.")
        except RepositoryException as re:
            print(re)
        except ValidatorException as ve:
            print(ve.getErrors())
            
    def __addClient(self):
        """
        Adauga un client citit din consola
        """
        idClient = input("Introduceti id-ul: ")
        nume = input("Introduceti numele: ")
        CNP = input("Introduceti CNP-ul: ")
        print("\n")
        try:
            client = self.__client_ctr.createClient(idClient, nume, CNP)
            self.__client_ctr.add(client)
            print("Clientul", client.getNume(),"a fost salvat.")
        except RepositoryException as re:
            print(re.getErrors())
        except ValidatorException as ve:
            print(ve.getErrors())
            
    def __readCommand(self):
        """
        Afiseaza submeniul adaugare si citeste o comanda
        Returneaza o comanda citita de la tastatura
        """
        print("\nAdaugare:")
        print("                 0 < - > Inapoi")
        print("                 1 < - > Adauga un film")
        print("                 2 < - > Adauga un client")
        return input('Introduceti optiunea ')
    
    def run(self):
        """
        Realizeaza interactiunea cu utlizatorul in submeniul adaugare
        """
        
        while True:
            os.system("cls")
            c = self.__readCommand()
            if c == '0':
                break
            try:
                os.system("cls")
                option = self.__cmd[c]
                option()
                Screen.wait()
            except KeyError :
                os.system("cls")
                print('Optiune incorecta.Incercati din nou!')
                Screen.wait()
            except ValueError as ve:
                os.system("cls")
                print('Exceptie in aplicatie: ' + ve) 
                Screen.wait()  
                
class ModificareUI():
    '''
    Este folosite la interactiunea cu utilizatorul in cadrul submeniului adaugare
    Primeste controller-ele filmului si clientului 
    ''' 
    def __init__(self, film_ctr, client_ctr):
        self.__film_ctr = film_ctr
        self.__client_ctr = client_ctr
        self.__initCommands()
        
    def __initCommands(self):
        """
        Initializeaza un dictionar cu anumite comenzi corespunzatoare submeniului modificare
        """
        self.__cmd = {}
        self.__cmd['1'] = self.__updateFilm
        self.__cmd['2'] = self.__updateClient
        
    def __updateFilm(self):
        """
        Citeste un id 
        Modifica un film cu id-ul citit din consola
        daca id-ul introdus nu este valid se ridica ValidatorException iar
        daca id-ul introdus nu corespunde nici unui film se ridica RepositoryException
        """
        idFilm = input("Introduceti id-ul filmului de modificat: ")
        titlu = input("Introduceti titlul: ")
        descriere = input ("Introduceti descrierea: ")
        gen = input("Introduceti genul: ") 
        print("\n")
        try:
            film = self.__film_ctr.createFilm(idFilm, titlu, descriere, gen)
            self.__film_ctr.update(film)
            print("Filmul cu id-ul", film.getId(), "a fost modificat.")
        except RepositoryException as re:
            print(re.getErrors())
        except ValidatorException as ve:
            print(ve.getErrors())
            
    def __updateClient(self):
        """
        Citeste un id 
        Modifica un client cu id-ul citit din consola
        daca id-ul introdus nu este valid se ridica ValidatorException iar
        daca id-ul introdus nu corespunde nici unui client se ridica RepositoryException
        """
        idClient = input("Introduceti id-ul clientului de modificat: ")
        nume = input("Introduceti numele: ")
        CNP = input("Introduceti CNP-ul: ")
        print("\n")
        try:
            client = self.__client_ctr.createClient(idClient, nume, CNP)
            self.__client_ctr.update(client)
            print("Clientul cu id-ul", client.getId(), "a fost modificat.")
        except RepositoryException as re:
            print(re.getErrors())
        except ValidatorException as ve:
            print(ve.getErrors())
            
    def __readCommand(self):
        """
        Afiseaza submeniul adaugare si citeste o comanda
        Returneaza o comanda citita de la tastatura
        """
        print("\nModificare:")
        print("                 0 < - > Inapoi")
        print("                 1 < - > Modifica un film")
        print("                 2 < - > Modifica un client")
        return input('Introduceti optiunea ')
    
    def run(self):
        """
        Realizeaza interactiunea cu utlizatorul in submeniul modificare
        """
        while True:
            os.system("cls")
            c = self.__readCommand()
            if c == '0':
                break
            try:
                os.system("cls")
                option = self.__cmd[c]
                option()
                Screen.wait()
            except KeyError :
                os.system("cls")
                print('Optiune incorecta.Incercati din nou!')
                Screen.wait()
            except ValueError as ve:
                os.system("cls")
                print('Exceptie in aplicatie: ' + ve) 
                Screen.wait() 
                
class AfisareUI():
    '''
    Este folosite la interactiunea cu utilizatorul in cadrul submeniului afisare
    Primeste controller-ele filmului si clientului 
    '''
    def __init__(self, film_ctr, client_ctr):
        self.__film_ctr = film_ctr
        self.__client_ctr = client_ctr
        self.__initCommands()
        
    def __initCommands(self):
        """
        Initializeaza un dictionar cu anumite comenzi corespunzatoare submeniului afisare
        """
        self.__cmd = {}
        self.__cmd['1'] = self.__afisareFilme
        self.__cmd['2'] = self.__afisareClienti
    
    def __afisareFilmeRecursiv(self, filme):
        if filme != []:
            print(filme[0].getId().ljust(4)+"|"+ 
                  filme[0].getTitlu().ljust(20)+"|"+
                  filme[0].getGen())
            self.__afisareFilmeRecursiv(filme[1:])
            
            
    def __afisareFilme(self):
        '''
        Afiseaza filmele existente in repository
        Daca nu exista nici un film, atunci se afiseaza mesaj
        '''
        filme = self.__film_ctr.getAllFilms()
        if len(filme) == 0:
            print("\nNu exista niciun film!")
        else:
            print("\nLista de filme este: ")
            print("#######################################")
            print("Id".ljust(4)+"|"+"Titlu".ljust(20)+"|"+"Gen")
            self.__afisareFilmeRecursiv(filme)
            print("#######################################")
     
    def __afisareClientiRecursiv(self, clienti):
        if clienti != []:
            print(clienti[0].getId().ljust(4)+"|"+ 
                  clienti[0].getNume().ljust(20)+"|"+
                  clienti[0].getCNP())
            self.__afisareClientiRecursiv(clienti[1:])
            
    def __afisareClienti(self):
        '''
        Afiseaza clientii existenti in repository
        Daca nu exista nici un film, atunci se afiseaza mesaj
        '''
        clienti = self.__client_ctr.getAllClients()
        if len(clienti) == 0:
            print("\nNu exista niciun client!")
        else:
            print("\nLista de clienti este: ")
            print("#######################################".ljust(37))
            print("Id".ljust(4)+"|"+"Nume".ljust(20)+"|"+"Cnp".ljust(13))
            self.__afisareClientiRecursiv(clienti)
            print("#######################################")
            
    def __readCommand(self):
        """
        Afiseaza submeniul afisare si citeste o comanda
        Returneaza o comanda citita de la tastatura
        """
        print("\nAfisare:")
        print("                 0 < - > Inapoi")
        print("                 1 < - > Afiseaza lista de filme")
        print("                 2 < - > Afiseaza lista de clienti")
        return input('Introduceti optiunea ')
    
    def run(self):
        """
        Realizeaza interactiunea cu utlizatorul in submeniul afisare
        """
        while True:
            os.system("cls")
            c = self.__readCommand()
            if c == '0':
                break
            try:
                os.system("cls")
                option = self.__cmd[c]
                option()
                Screen.wait()
            except KeyError :
                os.system("cls")
                print('Optiune incorecta.Incercati din nou!')
                Screen.wait()
            except ValueError as ve:
                os.system("cls")
                print('Exceptie in aplicatie: ' + ve) 
                Screen.wait() 

class StergereUI():
    '''
    Este folosite la interactiunea cu utilizatorul in cadrul submeniului stergere
    Primeste controller-ele filmului si clientului 
    '''
    def __init__(self, film_ctr, client_ctr):
        self.__film_ctr = film_ctr
        self.__client_ctr = client_ctr
        self.__initCommands()
        
    def __initCommands(self):
        """
        Initializeaza un dictionar cu anumite comenzi corespunzatoare submeniului stergere
        """
        self.__cmd = {}
        self.__cmd['1'] = self.__delFilm
        self.__cmd['2'] = self.__delClient
    
    def __delFilm(self):
        """
        Sterge un film care are id-ul citit din consola
        Se afiseaza mesaje de eroare daca datele introduse sunt invalide
        """
        idFilm = input("Introduceti id-ul filmului de sters: ")
        print("\n") 
        try:
            film = self.__film_ctr.findById(idFilm)
            self.__film_ctr.delete(film)
            print("Filmul cu id-ul", film.getId(), "a fost sters.")
        except RepositoryException as re:
            print(re.getErrors())
        except ValidatorException as ve:
            print(ve.getErrors())
            
    def __delClient(self):
        """
        Sterge un client care are id-ul citit din consola
        Se afiseaza mesaje de eroare daca datele introduse sunt invalide
        """
        idClient = input("Introduceti id-ul clientului de sters: ")
        print("\n") 
        try:
            client = self.__client_ctr.findById(idClient)
            self.__client_ctr.delete(client)
            print("Clientul cu id-ul", client.getId(), "a fost sters.")
        except RepositoryException as re:
            print(re.getErrors())
        except ValidatorException as ve:
            print(ve.getErrors())
                         
    def __readCommand(self):
        """
        Afiseaza submeniul stergere si citeste o comanda
        Returneaza o comanda citita de la tastatura
        """
        print("\nStergere:")
        print("                 0 < - > Inapoi")
        print("                 1 < - > Sterge un film")
        print("                 2 < - > Sterge un client")
        return input('Introduceti optiunea ')
    
    def run(self):
        """
        Realizeaza interactiunea cu utlizatorul in submeniul stergere
        """
        while True:
            os.system("cls")
            c = self.__readCommand()
            if c == '0':
                break
            try:
                os.system("cls")
                option = self.__cmd[c]
                option()
                Screen.wait()
            except KeyError :
                os.system("cls")
                print('Optiune incorecta.Incercati din nou!')
                Screen.wait()
            except ValueError as ve:
                os.system("cls")
                print('Exceptie in aplicatie: ' + ve) 
                Screen.wait() 

class CautareUI():
    '''
    Este folosite la interactiunea cu utilizatorul in cadrul submeniului stergere
    Primeste controller-ele filmului si clientului 
    '''
    def __init__(self, film_ctr, client_ctr):
        self.__film_ctr = film_ctr
        self.__client_ctr = client_ctr
        self.__initCommands()
        
    def __initCommands(self):
        """
        Initializeaza un dictionar cu anumite comenzi corespunzatoare submeniului stergere
        """
        self.__cmd = {}
        self.__cmd['1'] = self.__searchFilm
        self.__cmd['2'] = self.__searchClient
    
    def __searchFilm(self):
        '''
        Cauta filmele care contin in titlu un string citit de la tastatura
        '''
        cr = input("Titlul contine: ")
        filme = self.__film_ctr.search(cr)    
        if len(filme) == 0:
            print("Nu a fost gasita nici o potrivire.")
        else:
            print("\nRezultatele cautarii:",len(filme),"filme")
            print("#######################################")
            print("Id".ljust(4)+"|"+"Titlu".ljust(20)+"|"+"Gen")
            for film in filme:
                print(film.getId().ljust(4)+"|"+ 
                      film.getTitlu().ljust(20)+"|"+
                      film.getGen())
            print("#######################################")
            
    def __searchClient(self):
        '''
        Cauta clinetii care contin au in nume un string citit de la tastatura
        '''
        cr = input("Numele contine: ")
        clienti = self.__client_ctr.search(cr)    
        if len(clienti) == 0:
            print("Nu a fost gasita nici o potrivire.")
        else:
            print("\nRezultatele cautarii:",len(clienti),"clienti")
            print("#######################################".ljust(37))
            print("Id".ljust(4)+"|"+"Nume".ljust(20)+"|"+"Cnp".ljust(13))
            #print("_____________________________________".ljust(36))
            for client in clienti:
                print(client.getId().ljust(4)+"|"+ 
                      client.getNume().ljust(20)+"|"+
                      client.getCNP())
                #print("_____________________________________".ljust(36))
            print("#######################################")
            
    def __readCommand(self):
        """
        Afiseaza submeniul cautare si citeste o comanda
        Returneaza o comanda citita de la tastatura
        """
        print("\nCautare:")
        print("                 0 < - > Inapoi")
        print("                 1 < - > Cautare filme")
        print("                 2 < - > Cautare clienti")
        return input('Introduceti optiunea ')    
    
    def run(self):
        """
        Realizeaza interactiunea cu utlizatorul in submeniul cautare
        """
        while True:
            os.system("cls")
            c = self.__readCommand()
            if c == '0':
                break
            try:
                os.system("cls")
                option = self.__cmd[c]
                option()
                Screen.wait()
            except KeyError :
                os.system("cls")
                print('Optiune incorecta.Incercati din nou!')
                Screen.wait()
            except ValueError as ve:
                os.system("cls")
                print('Exceptie in aplicatie: ' + ve) 
                Screen.wait() 

class InchiriereUI():
    
    '''
    Este folosite la interactiunea cu utilizatorul in cadrul submeniului inchiriere
    Primeste controller-ele filmului si clientului 
    '''
    def __init__(self, film_ctr, client_ctr, rent_ctr):
        self.__film_ctr = film_ctr
        self.__client_ctr = client_ctr
        self.__rent_ctr = rent_ctr
        self.__initCommands()    
    
    def __initCommands(self):
        """
        Initializeaza un dictionar cu anumite comenzi corespunzatoare submeniului inchiriere
        """
        self.__cmd = {}
        self.__cmd['1'] = self.__inchiriere
        self.__cmd['2'] = self.__returnare
        self.__cmd['3'] = self.__afisare
    
    def __afisare(self):
        allRents = self.__rent_ctr.getAllRents()
        for rent in allRents:
            print(rent)
        
    def __returnare(self):
        """
        Citeste id-ul clientului care inchriaza si id-ul filmului de returnat
        """
        idClient = input("Introduceti id-ul clientului: ")
        idFilm = input("Introduceti id-ul filmului: ")
        try:
            rent = self.__rent_ctr.createRent(idClient, idFilm)
            film = self.__film_ctr.findById(idFilm)
            client = self.__client_ctr.findById(idClient)
            self.__rent_ctr.delete(rent)
            print("Clientul",client.getNume(),"a returnat filmul",film.getTitlu())
        except ValidatorException as ve:
            print(ve.getErrors())
        except RepositoryException as re:
            print(re.getErrors())
            
    def __inchiriere(self):
        """
        Citeste id-ul clientului care inchriaza si id-ul filmului de inchiriat
        """
        idClient = input("Introduceti id-ul clientului: ")
        idFilm = input("Introduceti id-ul filmului: ")
        try:
            rent = self.__rent_ctr.createRent(idClient, idFilm)
            film = self.__film_ctr.findById(idFilm)
            client = self.__client_ctr.findById(idClient)
            self.__rent_ctr.add(rent)
            print("Clientul",client.getNume(),"a imprumutat filmul",film.getTitlu())
        except ValidatorException as ve:
            print(ve.getErrors())
        except RepositoryException as re:
            print(re.getErrors())
            
    def __readCommand(self):
        """
        Afiseaza submeniul inchiriere si citeste o comanda
        Returneaza o comanda citita de la tastatura
        """
        print("\nInchiriere/returnare:")
        print("                 0 < - > Inapoi")
        print("                 1 < - > Inchiriere")
        print("                 2 < - > Returnare")
        return input('Introduceti optiunea ')    
    
    def run(self):
        """
        Realizeaza interactiunea cu utlizatorul in submeniul inchiriere
        """
        while True:
            os.system("cls")
            c = self.__readCommand()
            if c == '0':
                break
            try:
                os.system("cls")
                option = self.__cmd[c]
                option()
                Screen.wait()
            except KeyError :
                os.system("cls")
                print('Optiune incorecta.Incercati din nou!')
                Screen.wait()
            except ValueError as ve:
                os.system("cls")
                print('Exceptie in aplicatie: ' + ve) 
                Screen.wait()

class RapoarteUI():
    
    def __init__(self, rent_ctr):
        self.__rent_ctr = rent_ctr
        self.__initCommands()
    
    def __initCommands(self):
        """
        Initializeaza un dictionar cu anumite comenzi corespunzatoare submeniului rapoarte
        """
        self.__cmd = {}
        self.__cmd['1'] = self.__afisareClientiCuFilme
        self.__cmd['2'] = self.__afisareCeleMaiInchiriateFilme
        self.__cmd['3'] = self.__afisare30PerCent
    
    def __afisareCeleMaiInchiriateFilme(self):  
        '''
        Afiseaza cele mai inchiriate filme
        '''
        filme_inchiriate = self.__rent_ctr.getFilmeInchiriateOrdonat()
        if  filme_inchiriate == []:
            print("\nNu exista niciun film de afisat!")
        else:
            print("\nLista cu cele mai inchiriate filme este: ")
            print("#############################################".ljust(37))
            print("Id Film".ljust(9)+"|"+"Titlu".ljust(20)+"|"+"Nr. Inchirieri".ljust(9))
            for film_rent in filme_inchiriate:
                film = film_rent.getFilm()
                nr_inchirieri = film_rent.getNrInchirieri()
                print(film.getId().ljust(9)+"|"+ 
                      film.getTitlu().ljust(20)+"|"+
                      str(nr_inchirieri))
            print("#############################################")
    
    def __afisare30PerCent(self):
        '''
        Afiseaza primii 30% clienti cu filme inchiriate
        '''
        lista_clienti_cu_filme = self.__rent_ctr.getClientiOrdByNrFilmeNume()   
        first_30_percent = len(lista_clienti_cu_filme) * 0.3
        if  first_30_percent == 0:
            print("\nNu exista niciun client de afisat!")
        else:
            if  first_30_percent > 0 and first_30_percent < 1:
                first_30_percent = 1
            first_30_percent = int(first_30_percent)
            print("\nLista cu primii 30% clienti cu filme inchiriate este: ")
            print("########################################".ljust(37))
            print("Id Client".ljust(9)+"|"+"Nume".ljust(20)+"|"+"Nr. Filme".ljust(9))
            cnt = 0
            for client_rent in lista_clienti_cu_filme:
                client = client_rent.getClient()
                nr_filme = client_rent.getNrFilme()
                print(client.getId().ljust(9)+"|"+ 
                      client.getNume().ljust(20)+"|"+
                      str(nr_filme))
                cnt += 1
                if cnt == first_30_percent:
                    break
            print("########################################")
                      
    def __afisareClientiCuFilme(self):
        '''
        Afiseaza clientii care au filme imprumutate, ordonat dupa 
        nume, numarul de filme inchiriate
        '''
        lista_clienti_cu_filme = self.__rent_ctr.getClientiOrdByNumeNrFilme()
        if len(lista_clienti_cu_filme) == 0:
            print("\nNu exista niciun client de afisat!")
        else:
            print("\nLista de clienti cu filme inchiriate este: ")
            print("########################################".ljust(37))
            print("Id Client".ljust(9)+"|"+"Nume".ljust(20)+"|"+"Nr. Filme".ljust(9))
            #print("_____________________________________".ljust(36))
            for client_rent in lista_clienti_cu_filme:
                client = client_rent.getClient()
                nr_filme = client_rent.getNrFilme()
                print(client.getId().ljust(9)+"|"+ 
                      client.getNume().ljust(20)+"|"+
                      str(nr_filme))
                #print("_____________________________________".ljust(36))
            print("########################################")
            
    def __readCommand(self):
        """
        Afiseaza submeniul afisare si citeste o comanda
        Returneaza o comanda citita de la tastatura
        """
        print("\nRapoarte:")
        print("                 0 < - > Inapoi")
        print("                 1 < - > Afiseaza clientii cu filme imprumutate, "+ \
                                "ordonat dupa nume, numarul de film inchiriate")
        print("                 2 < - > Afiseaza cele mai inchiriate filme")
        print("                 3 < - > Afiseaza primii 30% clienti cu cele mai multe filme")
        return input('Introduceti optiunea ')
    
    def run(self):
        """
        Realizeaza interactiunea cu utlizatorul in submeniul afisare
        """
        while True:
            os.system("cls")
            c = self.__readCommand()
            if c == '0':
                break
            try:
                os.system("cls")
                option = self.__cmd[c]
                option()
                Screen.wait()
            except KeyError :
                os.system("cls")
                print('Optiune incorecta.Incercati din nou!')
                Screen.wait()
            except ValueError as ve:
                os.system("cls")
                print('Exceptie in aplicatie: ' + ve) 
                Screen.wait() 