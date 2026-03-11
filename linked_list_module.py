class Nodo:
    def __init__(self, valore, prossimo=None):
        self.valore = valore
        self.prossimo = prossimo

    def __str__(self):
        return str(self.valore)


class ListaCollegata:
    def __init__(self):
        self.testa = None

    def __str__(self):
        elementi = []
        nodo_corrente = self.testa
        while nodo_corrente:
            elementi.append(str(nodo_corrente.valore))
            nodo_corrente = nodo_corrente.prossimo
        return " -> ".join(elementi)

    def inserisci_in_testa(self, valore):
        nuovo_nodo = Nodo(valore)
        nuovo_nodo.prossimo = self.testa
        self.testa = nuovo_nodo

    def search(self, valore):
        nodo_corrente = self.testa
        while nodo_corrente:
            if nodo_corrente.valore == valore:
                return nodo_corrente
            nodo_corrente = nodo_corrente.prossimo
        return None

    def minimum(self):
        if not self.testa:
            return None
        min_val = self.testa
        nodo_corrente = self.testa.prossimo
        while nodo_corrente:
            if nodo_corrente.valore < min_val.valore:
                min_val = nodo_corrente
            nodo_corrente = nodo_corrente.prossimo
        return min_val

    def maximum(self):
        if not self.testa:
            return None
        max_val = self.testa
        nodo_corrente = self.testa.prossimo
        while nodo_corrente:
            if nodo_corrente.valore > max_val.valore:
                max_val = nodo_corrente
            nodo_corrente = nodo_corrente.prossimo
        return max_val

    def trova_successore(self, valore):
        nodo_corrente = self.testa
        successore = None
        while nodo_corrente:
            if nodo_corrente.valore > valore:
                if not successore or nodo_corrente.valore < successore.valore:
                    successore = nodo_corrente
            nodo_corrente = nodo_corrente.prossimo
        return successore

    def trova_predecessore(self, valore):
        nodo_corrente = self.testa
        predecessore = None
        while nodo_corrente:
            if nodo_corrente.valore < valore:
                if not predecessore or nodo_corrente.valore > predecessore.valore:
                    predecessore = nodo_corrente
            nodo_corrente = nodo_corrente.prossimo
        return predecessore
