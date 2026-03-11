class NodoABR:
    def __init__(self, valore):
        self.valore = valore
        self.sinistro = None
        self.destro = None


class ABR:
    def __init__(self):
        self.radice = None

    def inserisci(self, valore):
        def _inserisci(nodo, valore):
            if nodo is None:
                return NodoABR(valore)
            elif valore < nodo.valore:
                nodo.sinistro = _inserisci(nodo.sinistro, valore)
            else:
                nodo.destro = _inserisci(nodo.destro, valore)
            return nodo
        self.radice = _inserisci(self.radice, valore)

    def search(self, valore):
        def _search(nodo, valore):
            if nodo is None or nodo.valore == valore:
                return nodo
            if valore < nodo.valore:
                return _search(nodo.sinistro, valore)
            return _search(nodo.destro, valore)
        return _search(self.radice, valore)

    def minimum(self, nodo=None):
        if nodo is None:
            nodo = self.radice
        while nodo and nodo.sinistro:
            nodo = nodo.sinistro
        return nodo

    def maximum(self, nodo=None):
        if nodo is None:
            nodo = self.radice
        while nodo and nodo.destro:
            nodo = nodo.destro
        return nodo

    def trova_predecessore(self, valore):
        nodo = self.radice
        predecessore = None
        while nodo:
            if valore > nodo.valore:
                predecessore = nodo
                nodo = nodo.destro
            else:
                nodo = nodo.sinistro
        return predecessore

    def trova_successore(self, valore):
        nodo = self.radice
        successore = None
        while nodo:
            if valore < nodo.valore:
                successore = nodo
                nodo = nodo.sinistro
            else:
                nodo = nodo.destro
        return successore

    def delete(self, valore):
        def _delete(nodo, valore):
            if nodo is None:
                return nodo
            if valore < nodo.valore:
                nodo.sinistro = _delete(nodo.sinistro, valore)
            elif valore > nodo.valore:
                nodo.destro = _delete(nodo.destro, valore)
            else:
                if nodo.sinistro is None:
                    return nodo.destro
                elif nodo.destro is None:
                    return nodo.sinistro
                temp = self.minimum(nodo.destro)
                nodo.valore = temp.valore
                nodo.destro = _delete(nodo.destro, temp.valore)
            return nodo
        self.radice = _delete(self.radice, valore)

    def in_ordine(self, nodo=None):
        if nodo is None:
            nodo = self.radice
        result = []
        def _in_ordine(n):
            if n:
                _in_ordine(n.sinistro)
                result.append(n.valore)
                _in_ordine(n.destro)
        _in_ordine(nodo)
        return result
