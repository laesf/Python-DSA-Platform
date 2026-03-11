RED = True
BLACK = False

class NodoRBT:
    def __init__(self, valore, colore=RED):
        self.valore = valore
        self.colore = colore
        self.sinistro = None
        self.destro = None
        self.padre = None

class RBT:
    def __init__(self):
        self.NIL = NodoRBT(None, BLACK)
        self.radice = self.NIL

    def inserisci(self, valore):
        nuovo = NodoRBT(valore)
        nuovo.sinistro = nuovo.destro = self.NIL
        y = None
        x = self.radice

        while x != self.NIL:
            y = x
            if nuovo.valore < x.valore:
                x = x.sinistro
            else:
                x = x.destro

        nuovo.padre = y
        if y is None:
            self.radice = nuovo
        elif nuovo.valore < y.valore:
            y.sinistro = nuovo
        else:
            y.destro = nuovo

        nuovo.colore = RED
        self.fix_inserimento(nuovo)

    def fix_inserimento(self, k):
        while k != self.radice and k.padre.colore == RED:
            if k.padre == k.padre.padre.sinistro:
                y = k.padre.padre.destro
                if y and y.colore == RED:
                    k.padre.colore = BLACK
                    y.colore = BLACK
                    k.padre.padre.colore = RED
                    k = k.padre.padre
                else:
                    if k == k.padre.destro:
                        k = k.padre
                        self.rotazione_sinistra(k)
                    k.padre.colore = BLACK
                    k.padre.padre.colore = RED
                    self.rotazione_destra(k.padre.padre)
            else:
                y = k.padre.padre.sinistro
                if y and y.colore == RED:
                    k.padre.colore = BLACK
                    y.colore = BLACK
                    k.padre.padre.colore = RED
                    k = k.padre.padre
                else:
                    if k == k.padre.sinistro:
                        k = k.padre
                        self.rotazione_destra(k)
                    k.padre.colore = BLACK
                    k.padre.padre.colore = RED
                    self.rotazione_sinistra(k.padre.padre)
        self.radice.colore = BLACK

    def rotazione_sinistra(self, x):
        y = x.destro
        x.destro = y.sinistro
        if y.sinistro != self.NIL:
            y.sinistro.padre = x
        y.padre = x.padre
        if x.padre is None:
            self.radice = y
        elif x == x.padre.sinistro:
            x.padre.sinistro = y
        else:
            x.padre.destro = y
        y.sinistro = x
        x.padre = y

    def rotazione_destra(self, x):
        y = x.sinistro
        x.sinistro = y.destro
        if y.destro != self.NIL:
            y.destro.padre = x
        y.padre = x.padre
        if x.padre is None:
            self.radice = y
        elif x == x.padre.destro:
            x.padre.destro = y
        else:
            x.padre.sinistro = y
        y.destro = x
        x.padre = y

    def in_ordine(self):
        def _in_ordine(n):
            if n == self.NIL or n is None:
                return []
            return _in_ordine(n.sinistro) + [n.valore] + _in_ordine(n.destro)
        return _in_ordine(self.radice)
