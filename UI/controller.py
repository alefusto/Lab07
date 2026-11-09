import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown(self): # Da richiamare nella view dopo aver creato le dropdown
        lista_biblioteche = self._model.get_biblioteche()
        self._view.dd_biblioteca.options.append(ft.dropdown.Option("Nessun filtro")) # .Option è una classe, infatti inizia per maiuscola
        # dropdown viene scritto tutto minuscolo perché è il percorso per aprire Option, non sto creando la DD
        for b in lista_biblioteche:
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(key = str(b.id), text = b.nome))

        lista_generi = self._model.get_generi()
        self._view.dd_genere.options.append(ft.dropdown.Option("Nessun filtro"))
        for g in lista_generi:
            self._view.dd_genere.options.append(ft.dropdown.Option(key = g, text = g)) # Il genere ha già tutto ciò che serve per essere chiave e testo

    # CALLBACKS DROPDOWN, ovvero reazione alla scelta fatta nella dd
    def leggi_biblioteca(self, e):
        self.biblioteca_selezionata = e.control.value # .control.value estrae la scelta fatta nella dd
        return self.biblioteca_selezionata

    def leggi_genere(self, e):
        self.genere_selezionato = e.control.value
        return self.genere_selezionato

    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self, e):
        biblioteca = self.biblioteca_selezionata
        genere = self.genere_selezionato

        libri = self._model.get_libri_filtrati(biblioteca, genere)

        self._view.lista_libri.controls.clear()  # Pulisco la ListView per poterla aggiornare

        if libri is not None:  # Itero sulla lista e aggiungo gli strumenti alla ListView
            for l in libri:
                self._view.lista_libri.controls.append(ft.Text(str(l)))

        self._view.update()
