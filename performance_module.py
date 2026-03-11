import time
import random
import matplotlib.pyplot as plt

from linked_list_module import ListaCollegata
from abr_module import ABR
from rbt_module import RBT


def time_operation(operation, *args):
    start = time.perf_counter()
    for _ in range(10):
        operation(*args)
    end = time.perf_counter()
    return (end - start) / 10


def generate_random_values(n):
    return [random.randint(0, 10000) for _ in range(n)]


def performance_test_structures():
    sizes = [10, 100, 1000, 10000]
    results = {
        'Array': [],
        'ListaConcatenata': [],
        'ABR': [],
        'RBT': []
    }

    for n in sizes:
        values = generate_random_values(n)

        def array_search():
            arr = values[:]
            for v in values:
                _ = v in arr
        results['Array'].append(time_operation(array_search))

        def lista_search():
            lista = ListaCollegata()
            for v in values:
                lista.inserisci_in_testa(v)
            for v in values:
                lista.search(v)
        results['ListaConcatenata'].append(time_operation(lista_search))

        def abr_search():
            abr = ABR()
            for v in values:
                abr.inserisci(v)
            for v in values:
                abr.search(v)
        results['ABR'].append(time_operation(abr_search))

        def rbt_search():
            rbt = RBT()
            for v in values:
                rbt.inserisci(v)
            rbt.in_ordine()
        results['RBT'].append(time_operation(rbt_search))

    for name, times in results.items():
        plt.plot(sizes, times, label=name)

    plt.xlabel("Numero di elementi")
    plt.ylabel("Tempo medio (s)")
    plt.title("Confronto strutture dati - Ricerca")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("performance_structures.png")
    plt.show()
