'''
Created on Nov 7, 2015
@author: marius
'''
from src.ui.console import Console
from test.startTests import TestApp
from src.repository.inmem_repository import FilmRepository, ClientRepository,\
    RentRepository
from src.repository.file_repository import FilmFileRepository,\
    ClientFileRepository, RentFileRepository
from src.controller.controller import FilmController, ClientController,\
    RentController
from src.domain.validator import FilmValidator, ClientValidator, RentValidator


class Application:
    '''
    Builder for the application
    '''
    @staticmethod
    def run():
        
        TestApp.run()
        '''
        film_repo = FilmRepository()
        film_repo.createEntryes() #Creeaza intrari pentru a face testarea mai usoara
        client_repo = ClientRepository()
        client_repo.createEntryes() #Creeaza intrari pentru a face testarea mai usoara
        rent_repo = RentRepository()
        rent_repo.createEntryes()
        '''
        film_repo = FilmFileRepository("filme.txt")
        #film_repo.createEntryes()
        client_repo = ClientFileRepository("clienti.txt")
        #client_repo.createEntryes()
        rent_repo = RentFileRepository("rents.txt")
        #rent_repo.createEntryes()
        
        film_validator = FilmValidator()
        client_validator = ClientValidator()
        rent_validator = RentValidator()
        
        film_ctr = FilmController(film_repo, film_validator)
        client_ctr = ClientController(client_repo, client_validator)
        rent_ctr = RentController(rent_repo, film_repo, client_repo, rent_validator)
        
        console = Console(film_ctr, client_ctr, rent_ctr)
        console.run()
        
if __name__ == '__main__':
    try:
        Application.run()
    except:
        print("Aplicatia nu este functionala!!!") #it fuckin' works (assert stergere !) + many others
        raise
