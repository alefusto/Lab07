from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""

        if biblioteca == "Nessun filtro":
            biblioteca = None
        if genere == "Nessun filtro":
            genere = None

        return self._libro_dao.get_books_by_library_and_genre(biblioteca, genere)


    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        return self._libro_dao.get_genre()

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        return self._biblioteca_dao.get_library()
