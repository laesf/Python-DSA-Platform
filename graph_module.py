import random
from collections import deque, defaultdict
import heapq

class Grafo:
    def __init__(self, orientato=False, pesato=False):
        self.adiacenze = defaultdict(list)
        self.orientato = orientato
        self.pesato = pesato

    def aggiungi_arco(self, u, v, peso=1):
        if self.pesato:
            self.adiacenze[u].append((v, peso))
            if not self.orientato:
                self.adiacenze[v].append((u, peso))
        else:
            self.adiacenze[u].append(v)
            if not self.orientato:
                self.adiacenze[v].append(u)

    def genera_random(self, n_nodi, n_archi):
        for _ in range(n_archi):
            u, v = random.randint(0, n_nodi-1), random.randint(0, n_nodi-1)
            while v == u or (v in self.adiacenze[u]):
                u, v = random.randint(0, n_nodi-1), random.randint(0, n_nodi-1)
            peso = random.randint(1, 10) if self.pesato else None
            self.aggiungi_arco(u, v, peso)

    def carica_da_file(self, path):
        with open(path, 'r') as f:
            matrice = [list(map(int, r.strip().split())) for r in f.readlines()]
        for i in range(len(matrice)):
            for j in range(len(matrice[i])):
                if matrice[i][j] != 0:
                    self.aggiungi_arco(i, j, matrice[i][j] if self.pesato else 1)

    def bfs(self, partenza):
        visitati = set()
        coda = deque([partenza])
        ordine = []
        while coda:
            nodo = coda.popleft()
            if nodo not in visitati:
                visitati.add(nodo)
                ordine.append(nodo)
                vicini = [v for v in self.adiacenze[nodo]]
                if self.pesato:
                    vicini = [v[0] for v in self.adiacenze[nodo]]
                coda.extend(vicini)
        return ordine

    def dfs(self, partenza):
        visitati = set()
        ordine = []
        def _dfs(nodo):
            visitati.add(nodo)
            ordine.append(nodo)
            vicini = [v for v in self.adiacenze[nodo]]
            if self.pesato:
                vicini = [v[0] for v in self.adiacenze[nodo]]
            for v in vicini:
                if v not in visitati:
                    _dfs(v)
        _dfs(partenza)
        return ordine

    def componenti_connesse(self):
        visitati = set()
        componenti = []
        for nodo in self.adiacenze:
            if nodo not in visitati:
                comp = self.dfs(nodo)
                visitati.update(comp)
                componenti.append(comp)
        return componenti

    def ordinamento_topologico(self):
        indegree = defaultdict(int)
        for u in self.adiacenze:
            for v in self.adiacenze[u]:
                if self.pesato:
                    v = v[0]
                indegree[v] += 1
                if u not in indegree:
                    indegree[u] = 0
        coda = deque([n for n in indegree if indegree[n] == 0])
        ordine = []
        while coda:
            u = coda.popleft()
            ordine.append(u)
            for v in self.adiacenze[u]:
                if self.pesato:
                    v = v[0]
                indegree[v] -= 1
                if indegree[v] == 0:
                    coda.append(v)
        return ordine if len(ordine) == len(indegree) else None

    def kruskal(self):
        parent = {}

        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u

        def union(u, v):
            parent[find(u)] = find(v)

        edges = []
        for u in self.adiacenze:
            for v in self.adiacenze[u]:
                if self.pesato:
                    v, peso = v
                else:
                    peso = 1
                if self.orientato or (u < v):
                    edges.append((peso, u, v))

        for u in self.adiacenze:
            parent[u] = u

        mst = []
        for peso, u, v in sorted(edges):
            if find(u) != find(v):
                union(u, v)
                mst.append((u, v, peso))
        return mst

    def dijkstra(self, sorgente):
        dist = {nodo: float('inf') for nodo in self.adiacenze}
        dist[sorgente] = 0
        heap = [(0, sorgente)]

        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v in self.adiacenze[u]:
                if self.pesato:
                    v, peso = v
                else:
                    peso = 1
                if dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
                    heapq.heappush(heap, (dist[v], v))
        return dist
