from database.DB_connect import DBConnect
from model.libro_DTO import Libro
import mysql.connector
from mysql.connector import errorcode # Entrambi esclusivamente per la gestione degli errori, che altrimenti risalirebbero fino al controller

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass


    def get_books_by_library_and_genre(self, id_biblioteca, genere):
        cnx = DBConnect.get_connection()
        result = []

        if cnx is not None:
            query = """ SELECT * 
                         FROM libro
                         WHERE genere = COALESCE(%s, genere)
                         AND id_biblioteca = COALESCE(%s, id_biblioteca) """

            cursor = cnx.cursor()
            cursor.execute(query, (genere, id_biblioteca))

            for row in cursor:
                libro = Libro(*row)
                result.append(libro)

            cursor.close()
        cnx.close()

        return result

    def get_genre(self):
        cnx = DBConnect.get_connection()
        result = []

        if cnx is not None:
            query = """ SELECT DISTINCT genere
                        FROM libro """

            cursor = cnx.cursor()
            cursor.execute(query)

            for row in cursor:
                genere = row[0] # row[0] necessario perché di base viene restituita una tupla, e se non accedo al primo elemento non è "pulito"
                result.append(genere)

            cursor.close()
        cnx.close()
        return result
