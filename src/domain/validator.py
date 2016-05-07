'''
Created on Nov 7, 2015

@author: marius
'''
class ValidatorException(Exception):
    
    def __init__(self, errors):
        """
        Primeste o lista nevida de erori
        """
        self.__errors = errors
    
    def getErrors(self):
        """
        Configureaza modul in care este afisata lista de erori
        """
        eroare = self.__errors[0]
        for i in range(1, len(self.__errors)):
            eroare +="\n"+self.__errors[i] 
        return eroare
    
class FilmValidator():
    
    def validate(self, film):
        """
        Arunca ValidatorException daca campurile filmului sunt invalide 
        """
        errors = []
        if (film.getId() == ""): errors.append("Id nu poate fi gol!")
        try:
            idFilm = int(film.getId())
            if idFilm <= 0 or idFilm > 9999: errors.append("Id-ul trebuie sa fie un numar intreg strict pozitiv mai mic decat 10000!")
        except ValueError: errors.append("Id-ul trebuie sa fie un numar intreg strict pozitiv mai mic decat 10000!!")
        if (film.getTitlu() == ""): errors.append("Titlul nu poate fi gol!")
        if (len(film.getTitlu()) > 20): errors.append("Titlul nu poate sa contina mai mult de 20 de caractere!")
        if (film.getDescriere() == ""): errors.append("Descrierea nu poate sa lipseasa!")
        if (len(film.getDescriere()) > 20):errors.append("Descrierea nu poate sa contina mai mult de 20 de caractere!")
        if (film.getGen() == ""): errors.append("Genul nu poate sa lipseasca!")  
        if (len(film.getGen()) > 15):errors.append("Genul nu poate sa fie mai lung de 15 caractere!")
        if len(errors) > 0: raise ValidatorException(errors)
        
class ClientValidator():
    
    def validate(self, client):
        """
        Arunca ValidatorException daca atributele clientului sunt invalide 
        """
        errors = []
        if (client.getId() == ""): errors.append("Id nu poate fi gol!")
        try:
            idClient = int(client.getId())
            if (idClient <= 0 or idClient > 9999): 
                errors.append("Id-ul trebuie sa fie un numar intreg strict pozitiv mai mic decat 10000!")
        except ValueError: 
            errors.append("Id-ul trebuie sa fie un numar intreg strict pozitiv mai mic decat 10000!")
        if (client.getNume() == ""): errors.append("Numele nu poate sa lipseasca")
        if (len(client.getNume()) > 20): errors.append("Numele nu poate sa contina mai mult de 20 de caractere!")
        if (client.getCNP() == ""): errors.append("CNP-ul nu poate sa lipseasca")
        try:
            cnp = int(client.getCNP())
            if not self.__respectaRegula(cnp) or len(client.getCNP()) < 13: 
                errors.append("Introduceti un CNP valid!")
        except ValueError:
            errors.append("CNP-ul trebuie sa contina numai cifre!")
        if len(errors) > 0: raise ValidatorException(errors)
    
    def __respectaRegula(self, cnp):
        """
        Primeste un intreg (cnp-ul unei persoane)
        Returneaza true daca cifra de control coincide cu ultima cifra,
        false in caz contrar
        """
        uc_cnp = cnp % 10
        return self.__cifraCtrCnp(cnp) == uc_cnp
        
    def __cifraCtrCnp(self, cnp):
        """
        Primeste un intreg (cnp-ul unei persoane)
        Returneaza cifra de control corespunzatoare
        """
        cnp = cnp // 10
        nr = 279146358279
        suma = 0
        while cnp > 0:
            suma += (nr % 10) * (cnp % 10)
            cnp =  cnp // 10
            nr = nr // 10
        rest = suma % 11
        if rest == 10: rest = 1
        return rest
    
class RentValidator():
    
    def validate(self, rent):
        """
        Arunca ValidatorException daca atributele imprumutului sunt invalide 
        """
        errors = []
        if rent.getFilmId() == "": errors.append("Id-ul filmului nu poate sa lipseasca")
        try:
            idFilm = int(rent.getFilmId())
            if idFilm <= 0 or idFilm > 9999:
                errors.append("Id-ul fimului trebuie sa fie un numar intreg strict pozitiv mai mic decat 10000")
        except ValueError:
            errors.append("Id-ul fimului trebuie sa fie un numar intreg strict pozitiv mai mic decat 10000")
        if rent.getClientId() == "":errors.append("Id-ul clientului nu poate sa lipseasca")
        try:
            idClient = int(rent.getClientId())
            if idClient <= 0 or idClient > 9999:
                errors.append("Id-ul clientului trebuie sa fie un numar intreg strict pozitiv mai mic decat 10000")
        except ValueError:
            errors.append("Id-ul clientului trebuie sa fie un numar intreg strict pozitiv mai mic decat 10000")
        if len(errors) > 0: raise ValidatorException(errors)