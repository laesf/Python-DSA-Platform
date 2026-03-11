import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import matplotlib.pyplot as plt

from sorting_module import Sort, performance_test
from linked_list_module import ListaCollegata
from abr_module import ABR
from hashtable_module import HashTableChaining, HashTableOpenDouble, HashTableOpenLinear
from hashtable_perf import hashtable_performance_test
from graph_module import Grafo
from performance_module import performance_test_structures

class PiattaformaIA(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gui Algoritmi")
        self.geometry("1000x700")

        self.tab_control = ttk.Notebook(self)
        self.sorting_tab = ttk.Frame(self.tab_control)
        self.lista_tab = ttk.Frame(self.tab_control)
        self.abr_tab = ttk.Frame(self.tab_control)
        self.hash_tab = ttk.Frame(self.tab_control)
        self.graph_tab = ttk.Frame(self.tab_control)
        self.perf_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.sorting_tab, text='Ordinamento')
        self.tab_control.add(self.lista_tab, text='Liste Concatenate')
        self.tab_control.add(self.abr_tab, text='ABR')
        self.tab_control.add(self.hash_tab, text='Hash Table')
        self.tab_control.add(self.graph_tab, text='Grafi')
        self.tab_control.add(self.perf_tab, text='Performance Strutture')
        self.tab_control.pack(expand=1, fill='both')

        self.init_sorting_tab()
        self.init_lista_tab()
        self.init_abr_tab()
        self.init_hash_tab()
        self.init_graph_tab()
        self.init_perf_tab()

    def init_sorting_tab(self):
        frame = self.sorting_tab

        self.input_entry = tk.Entry(frame, width=80)
        self.input_entry.pack(pady=10)

        self.sorting_result = tk.Label(frame, text="Risultato:")
        self.sorting_result.pack()

        algo_var = tk.StringVar()
        algo_menu = ttk.Combobox(frame, textvariable=algo_var)
        algo_menu['values'] = ['Quick Sort', 'Merge Sort', 'Insertion Sort', 'Bubble Sort', 'Counting Sort']
        algo_menu.current(0)
        algo_menu.pack()

        def sort_input():
            try:
                values = list(map(int, self.input_entry.get().split(',')))
                algo = algo_var.get()
                sort_func = getattr(Sort, algo.lower().replace(" ", "_"))
                result = sort_func(values)
                self.sorting_result.config(text=f"Risultato: {result}")
            except Exception as e:
                messagebox.showerror("Errore", str(e))

        tk.Button(frame, text="Ordina", command=sort_input).pack(pady=5)
        tk.Button(frame, text="Test Prestazioni", command=performance_test).pack(pady=5)
    
    def init_lista_tab(self):
        frame = self.lista_tab
        self.lista = ListaCollegata()

        self.lista_output = tk.Label(frame, text="Lista corrente:")
        self.lista_output.pack(pady=5)

        insert_entry = tk.Entry(frame, width=40)
        insert_entry.pack()

        def inserisci():
            try:
                valore = int(insert_entry.get())
                self.lista.inserisci_in_testa(valore)
                self.lista_output.config(text=f"Lista corrente: {self.lista}")
            except:
                messagebox.showerror("Errore", "Inserisci un numero valido")

        def carica_file():
            filepath = filedialog.askopenfilename()
            try:
                with open(filepath, 'r') as f:
                    numeri = [int(x) for x in f.read().split(',')]
                    for n in numeri:
                        self.lista.inserisci_in_testa(n)
                self.lista_output.config(text=f"Lista corrente: {self.lista}")
            except:
                messagebox.showerror("Errore", "Formato file non valido. Usa numeri separati da virgola.")

        def operazione(nome):
            if nome in ['minimum', 'maximum']:
                nodo = getattr(self.lista, nome)()
            else:
                valore = int(insert_entry.get())
                nodo = getattr(self.lista, nome)(valore)
            text = nodo.valore if nodo else 'Nessun risultato'
            messagebox.showinfo("Risultato", f"{nome.capitalize()}: {text}")

        tk.Button(frame, text="Inserisci in testa", command=inserisci).pack()
        tk.Button(frame, text="Carica da file", command=carica_file).pack(pady=2)

        for op in ['search', 'minimum', 'maximum', 'trova_successore', 'trova_predecessore']:
            tk.Button(frame, text=op.replace('_', ' ').capitalize(), command=lambda op=op: operazione(op)).pack(pady=2)   
            
    def init_abr_tab(self):
        frame = self.abr_tab
        self.abr = ABR()

        self.abr_output = tk.Label(frame, text="Albero (in ordine):")
        self.abr_output.pack(pady=5)

        insert_entry = tk.Entry(frame, width=40)
        insert_entry.pack()

        def aggiorna():
            in_ord = self.abr.in_ordine()
            self.abr_output.config(text=f"In ordine: {in_ord}")

        def inserisci():
            try:
                valore = int(insert_entry.get())
                self.abr.inserisci(valore)
                aggiorna()
            except:
                messagebox.showerror("Errore", "Inserisci un numero valido")

        def carica_file():
            filepath = filedialog.askopenfilename()
            try:
                with open(filepath, 'r') as f:
                    numeri = [int(x) for x in f.read().split(',')]
                    for n in numeri:
                        self.abr.inserisci(n)
                aggiorna()
            except:
                messagebox.showerror("Errore", "Formato file non valido. Usa numeri separati da virgola.")

        def elimina():
            try:
                valore = int(insert_entry.get())
                self.abr.delete(valore)
                aggiorna()
            except:
                messagebox.showerror("Errore", "Inserisci un numero valido")

        def operazione(nome):
            if nome in ['minimum', 'maximum']:
                nodo = getattr(self.abr, nome)()
            else:
                valore = int(insert_entry.get())
                nodo = getattr(self.abr, nome)(valore)
            text = nodo.valore if nodo else 'Nessun risultato'
            messagebox.showinfo("Risultato", f"{nome.capitalize()}: {text}")

        tk.Button(frame, text="Inserisci", command=inserisci).pack(pady=2)
        tk.Button(frame, text="Carica da file", command=carica_file).pack(pady=2)
        tk.Button(frame, text="Elimina", command=elimina).pack(pady=2)

        for op in ['search', 'minimum', 'maximum', 'trova_successore', 'trova_predecessore']:
            tk.Button(frame, text=op.replace('_', ' ').capitalize(), command=lambda op=op: operazione(op)).pack(pady=2)

    def init_hash_tab(self):
        frame = self.hash_tab
        self.hash_type_var = tk.StringVar(value='Chaining')
        self.hash_table = None

        tk.Label(frame, text="Tipo di Hash Table:").pack(pady=5)
        hash_types = ['Chaining', 'Double Hashing', 'Linear Probing']
        hash_menu = ttk.Combobox(frame, textvariable=self.hash_type_var, values=hash_types, state='readonly')
        hash_menu.pack(pady=5)

        tk.Label(frame, text="Chiave (intero):").pack()
        key_entry = tk.Entry(frame, width=30)
        key_entry.pack()
        tk.Label(frame, text="Valore (stringa):").pack()
        value_entry = tk.Entry(frame, width=30)
        value_entry.pack()

        output_label = tk.Label(frame, text="Output:")
        output_label.pack(pady=5)

        def crea_tabella():
            tipo = self.hash_type_var.get()
            if tipo == 'Chaining':
                self.hash_table = HashTableChaining(100)
            elif tipo == 'Double Hashing':
                self.hash_table = HashTableOpenDouble(200)
            else:
                self.hash_table = HashTableOpenLinear(200)
            output_label.config(text=f"Tabella {tipo} creata.")

        def inserisci():
            if self.hash_table is None:
                crea_tabella()
            try:
                key = int(key_entry.get())
                value = value_entry.get()
                self.hash_table.inserisci(key, value)
                output_label.config(text="Inserito!")
            except Exception as e:
                messagebox.showerror("Errore", str(e))

        def ricerca():
            if self.hash_table is None:
                crea_tabella()
            try:
                key = int(key_entry.get())
                result = self.hash_table.ricerca(key)
                output_label.config(text=f"Risultato: {result}")
            except Exception as e:
                messagebox.showerror("Errore", str(e))

        def cancella():
            if self.hash_table is None:
                crea_tabella()
            try:
                if hasattr(self.hash_table, 'cancella'):
                    key = int(key_entry.get())
                    self.hash_table.cancella(key)
                    output_label.config(text="Cancellato!")
                else:
                    output_label.config(text="Cancellazione non supportata per questa tabella.")
            except Exception as e:
                messagebox.showerror("Errore", str(e))

        def test_performance():
            hashtable_performance_test()

        tk.Button(frame, text="Crea Tabella", command=crea_tabella).pack(pady=2)
        tk.Button(frame, text="Inserisci", command=inserisci).pack(pady=2)
        tk.Button(frame, text="Ricerca", command=ricerca).pack(pady=2)
        tk.Button(frame, text="Cancella", command=cancella).pack(pady=2)
        tk.Button(frame, text="Test Performance", command=test_performance).pack(pady=5)

    def init_graph_tab(self):
        frame = self.graph_tab
        self.grafo = None
        self.graph_orientato = tk.BooleanVar(value=False)
        self.graph_pesato = tk.BooleanVar(value=False)
        self.graph_nodi_entry = tk.Entry(frame, width=10)
        self.graph_archi_entry = tk.Entry(frame, width=10)
        self.graph_output = tk.Text(frame, height=15, width=80)
        self.graph_output.pack(pady=5)

        options_frame = tk.Frame(frame)
        options_frame.pack(pady=5)
        tk.Checkbutton(options_frame, text="Orientato", variable=self.graph_orientato).pack(side=tk.LEFT)
        tk.Checkbutton(options_frame, text="Pesato", variable=self.graph_pesato).pack(side=tk.LEFT)
        tk.Label(options_frame, text="Nodi:").pack(side=tk.LEFT)
        self.graph_nodi_entry.pack(in_=options_frame, side=tk.LEFT)
        tk.Label(options_frame, text="Archi:").pack(side=tk.LEFT)
        self.graph_archi_entry.pack(in_=options_frame, side=tk.LEFT)

        def crea_random():
            try:
                n_nodi = int(self.graph_nodi_entry.get())
                n_archi = int(self.graph_archi_entry.get())
                self.grafo = Grafo(orientato=self.graph_orientato.get(), pesato=self.graph_pesato.get())
                self.grafo.genera_random(n_nodi, n_archi)
                self.graph_output.delete(1.0, tk.END)
                self.graph_output.insert(tk.END, f"Grafo random creato con {n_nodi} nodi e {n_archi} archi.\n")
            except Exception as e:
                self.graph_output.insert(tk.END, f"Errore: {e}\n")

        def carica_file():
            filepath = filedialog.askopenfilename()
            try:
                self.grafo = Grafo(orientato=self.graph_orientato.get(), pesato=self.graph_pesato.get())
                self.grafo.carica_da_file(filepath)
                self.graph_output.delete(1.0, tk.END)
                self.graph_output.insert(tk.END, f"Grafo caricato da file: {filepath}\n")
            except Exception as e:
                self.graph_output.insert(tk.END, f"Errore: {e}\n")

        def bfs():
            if not self.grafo:
                self.graph_output.insert(tk.END, "Crea o carica prima un grafo!\n")
                return
            try:
                partenza = int(self.graph_nodi_entry.get()) if self.graph_nodi_entry.get() else 0
                ordine = self.grafo.bfs(partenza)
                self.graph_output.insert(tk.END, f"BFS da {partenza}: {ordine}\n")
            except Exception as e:
                self.graph_output.insert(tk.END, f"Errore: {e}\n")

        def dfs():
            if not self.grafo:
                self.graph_output.insert(tk.END, "Crea o carica prima un grafo!\n")
                return
            try:
                partenza = int(self.graph_nodi_entry.get()) if self.graph_nodi_entry.get() else 0
                ordine = self.grafo.dfs(partenza)
                self.graph_output.insert(tk.END, f"DFS da {partenza}: {ordine}\n")
            except Exception as e:
                self.graph_output.insert(tk.END, f"Errore: {e}\n")

        def componenti():
            if not self.grafo:
                self.graph_output.insert(tk.END, "Crea o carica prima un grafo!\n")
                return
            try:
                comps = self.grafo.componenti_connesse()
                self.graph_output.insert(tk.END, f"Componenti connesse: {comps}\n")
            except Exception as e:
                self.graph_output.insert(tk.END, f"Errore: {e}\n")

        def topologico():
            if not self.grafo:
                self.graph_output.insert(tk.END, "Crea o carica prima un grafo!\n")
                return
            try:
                ordine = self.grafo.ordinamento_topologico()
                self.graph_output.insert(tk.END, f"Ordinamento topologico: {ordine}\n")
            except Exception as e:
                self.graph_output.insert(tk.END, f"Errore: {e}\n")

        def kruskal():
            if not self.grafo:
                self.graph_output.insert(tk.END, "Crea o carica prima un grafo!\n")
                return
            try:
                mst = self.grafo.kruskal()
                self.graph_output.insert(tk.END, f"Kruskal (MST): {mst}\n")
            except Exception as e:
                self.graph_output.insert(tk.END, f"Errore: {e}\n")

        def dijkstra():
            if not self.grafo:
                self.graph_output.insert(tk.END, "Crea o carica prima un grafo!\n")
                return
            try:
                sorgente = int(self.graph_nodi_entry.get()) if self.graph_nodi_entry.get() else 0
                dist = self.grafo.dijkstra(sorgente)
                self.graph_output.insert(tk.END, f"Dijkstra da {sorgente}: {dist}\n")
            except Exception as e:
                self.graph_output.insert(tk.END, f"Errore: {e}\n")

        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Crea Random", command=crea_random).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text="Carica da file", command=carica_file).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text="BFS", command=bfs).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text="DFS", command=dfs).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text="Componenti Connesse", command=componenti).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text="Topologico", command=topologico).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text="Kruskal", command=kruskal).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text="Dijkstra", command=dijkstra).pack(side=tk.LEFT, padx=2)

    def init_perf_tab(self):
        frame = self.perf_tab
        tk.Label(frame, text="Confronto Performance tra Array, Lista Concatenata, ABR, RBT").pack(pady=10)
        tk.Button(frame, text="Esegui Test Performance", command=performance_test_structures).pack(pady=10)
        tk.Label(frame, text="Il grafico verrà mostrato a fine test.").pack(pady=5)


if __name__ == '__main__':
    app = PiattaformaIA()
    app.mainloop()
