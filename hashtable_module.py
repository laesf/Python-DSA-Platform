class HashTableChaining:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def inserisci(self, key, value):
        index = self.hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])

    def ricerca(self, key):
        index = self.hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

    def cancella(self, key):
        index = self.hash(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return


class HashTableOpenDouble:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def h1(self, key):
        return hash(key) % self.size

    def h2(self, key):
        return 1 + (hash(key) % (self.size - 1))

    def inserisci(self, key, value):
        for i in range(self.size):
            idx = (self.h1(key) + i * self.h2(key)) % self.size
            if self.table[idx] is None or self.table[idx][0] == key:
                self.table[idx] = (key, value)
                return

    def ricerca(self, key):
        for i in range(self.size):
            idx = (self.h1(key) + i * self.h2(key)) % self.size
            if self.table[idx] is None:
                return None
            if self.table[idx][0] == key:
                return self.table[idx][1]
        return None


class HashTableOpenLinear:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return hash(key) % self.size

    def inserisci(self, key, value):
        idx = self.hash(key)
        while self.table[idx] is not None and self.table[idx][0] != key:
            idx = (idx + 1) % self.size
        self.table[idx] = (key, value)

    def ricerca(self, key):
        idx = self.hash(key)
        for _ in range(self.size):
            if self.table[idx] is None:
                return None
            if self.table[idx][0] == key:
                return self.table[idx][1]
            idx = (idx + 1) % self.size
        return None
