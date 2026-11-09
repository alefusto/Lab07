from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca
import mysql.connector
from mysql.connector import errorcode

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_library(self):
        cnx = DBConnect.get_connection()
        result = []

        if cnx is not None:
            query = """ SELECT *
                        FROM biblioteca """

            cursor = cnx.cursor()
            cursor.execute(query)

            for row in cursor:
                biblioteca = Biblioteca(*row)
                result.append(biblioteca)

            cursor.close()
        cnx.close()
        return result
