import time
import random
import matplotlib.pyplot as plt
from hashtable_module import HashTableChaining, HashTableOpenDouble, HashTableOpenLinear


def time_operation(operation, *args):
    """Misura il tempo di esecuzione di un'operazione"""
    start = time.perf_counter()
    operation(*args)
    end = time.perf_counter()
    return end - start


def generate_random_values(n):
    """Genera n valori casuali"""
    return [random.randint(0, 100000) for _ in range(n)]


def hashtable_performance_test():
    """Test delle performance per le tre implementazioni di HashTable"""
    sizes = [10, 100, 1000, 10000]
    search_attempts = [10, 100, 1000]
    
    results_successful = {}
    results_unsuccessful = {}
    
    for size in sizes:
        print(f"Testing con {size} elementi...")
        values = generate_random_values(size)
        
        # Inizializza le tabelle hash
        ht_chaining = HashTableChaining(100)  # Grandezza fissa 100
        ht_double = HashTableOpenDouble(size * 2)  # Doppia grandezza
        ht_linear = HashTableOpenLinear(size * 2)  # Doppia grandezza
        
        tables = {
            'Chaining': ht_chaining,
            'Double Hashing': ht_double,
            'Linear Probing': ht_linear
        }
        
        # Inserisci gli stessi elementi in tutte le tabelle
        for table in tables.values():
            for i, val in enumerate(values):
                table.inserisci(val, f"value_{i}")
        
        # Test ricerche con successo
        for search_count in search_attempts:
            if size not in results_successful:
                results_successful[size] = {}
            if search_count not in results_successful[size]:
                results_successful[size][search_count] = {}
                
            search_values = random.choices(values, k=search_count)
            
            for name, table in tables.items():
                def search_operation():
                    for val in search_values:
                        table.ricerca(val)
                
                time_taken = time_operation(search_operation)
                results_successful[size][search_count][name] = time_taken
        
        # Test ricerche senza successo
        for search_count in search_attempts:
            if size not in results_unsuccessful:
                results_unsuccessful[size] = {}
            if search_count not in results_unsuccessful[size]:
                results_unsuccessful[size][search_count] = {}
                
            # Genera valori non presenti nella tabella
            unsuccessful_values = []
            while len(unsuccessful_values) < search_count:
                val = random.randint(100001, 200000)  # Range diverso da quello inserito
                if val not in values:
                    unsuccessful_values.append(val)
            
            for name, table in tables.items():
                def search_operation():
                    for val in unsuccessful_values:
                        table.ricerca(val)
                
                time_taken = time_operation(search_operation)
                results_unsuccessful[size][search_count][name] = time_taken
    
    # Crea i grafici
    create_hashtable_plots(results_successful, results_unsuccessful, sizes, search_attempts)


def create_hashtable_plots(results_successful, results_unsuccessful, sizes, search_attempts):
    """Crea i grafici delle performance"""
    
    # Grafico ricerche con successo
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('HashTable Performance - Ricerche con Successo', fontsize=16)
    
    for idx, search_count in enumerate([10, 100, 1000]):
        if idx >= 3:
            break
        row = idx // 2
        col = idx % 2
        ax = axes[row, col]
        
        for table_name in ['Chaining', 'Double Hashing', 'Linear Probing']:
            times = [results_successful[size][search_count][table_name] for size in sizes]
            ax.plot(sizes, times, marker='o', label=table_name)
        
        ax.set_xlabel('Numero di elementi inseriti')
        ax.set_ylabel('Tempo (secondi)')
        ax.set_title(f'{search_count} ricerche con successo')
        ax.legend()
        ax.grid(True)
        ax.set_xscale('log')
        ax.set_yscale('log')
    
    # Rimuovi il subplot vuoto
    fig.delaxes(axes[1, 1])
    
    plt.tight_layout()
    plt.savefig('hashtable_successful_searches.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Grafico ricerche senza successo
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('HashTable Performance - Ricerche senza Successo', fontsize=16)
    
    for idx, search_count in enumerate([10, 100, 1000]):
        if idx >= 3:
            break
        row = idx // 2
        col = idx % 2
        ax = axes[row, col]
        
        for table_name in ['Chaining', 'Double Hashing', 'Linear Probing']:
            times = [results_unsuccessful[size][search_count][table_name] for size in sizes]
            ax.plot(sizes, times, marker='o', label=table_name)
        
        ax.set_xlabel('Numero di elementi inseriti')
        ax.set_ylabel('Tempo (secondi)')
        ax.set_title(f'{search_count} ricerche senza successo')
        ax.legend()
        ax.grid(True)
        ax.set_xscale('log')
        ax.set_yscale('log')
    
    # Rimuovi il subplot vuoto
    fig.delaxes(axes[1, 1])
    
    plt.tight_layout()
    plt.savefig('hashtable_unsuccessful_searches.png', dpi=300, bbox_inches='tight')
    plt.show()


def hashtable_comparison_test():
    """Test di confronto semplificato per la GUI"""
    sizes = [100, 1000, 5000]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Test inserimento
    insert_times = {'Chaining': [], 'Double Hashing': [], 'Linear Probing': []}
    
    for size in sizes:
        values = generate_random_values(size)
        
        # Chaining
        ht_chain = HashTableChaining(100)
        start = time.perf_counter()
        for i, val in enumerate(values):
            ht_chain.inserisci(val, f"v{i}")
        insert_times['Chaining'].append(time.perf_counter() - start)
        
        # Double Hashing
        ht_double = HashTableOpenDouble(size * 2)
        start = time.perf_counter()
        for i, val in enumerate(values):
            ht_double.inserisci(val, f"v{i}")
        insert_times['Double Hashing'].append(time.perf_counter() - start)
        
        # Linear Probing
        ht_linear = HashTableOpenLinear(size * 2)
        start = time.perf_counter()
        for i, val in enumerate(values):
            ht_linear.inserisci(val, f"v{i}")
        insert_times['Linear Probing'].append(time.perf_counter() - start)
    
    # Plot inserimento
    for name, times in insert_times.items():
        ax1.plot(sizes, times, marker='o', label=name)
    ax1.set_xlabel('Numero di elementi')
    ax1.set_ylabel('Tempo (secondi)')
    ax1.set_title('Performance Inserimento')
    ax1.legend()
    ax1.grid(True)
    
    # Test ricerca
    search_times = {'Chaining': [], 'Double Hashing': [], 'Linear Probing': []}
    
    for size in sizes:
        values = generate_random_values(size)
        
        # Prepara le tabelle
        ht_chain = HashTableChaining(100)
        ht_double = HashTableOpenDouble(size * 2)
        ht_linear = HashTableOpenLinear(size * 2)
        
        for i, val in enumerate(values):
            ht_chain.inserisci(val, f"v{i}")
            ht_double.inserisci(val, f"v{i}")
            ht_linear.inserisci(val, f"v{i}")
        
        search_vals = random.choices(values, k=100)
        
        # Test ricerca Chaining
        start = time.perf_counter()
        for val in search_vals:
            ht_chain.ricerca(val)
        search_times['Chaining'].append(time.perf_counter() - start)
        
        # Test ricerca Double Hashing
        start = time.perf_counter()
        for val in search_vals:
            ht_double.ricerca(val)
        search_times['Double Hashing'].append(time.perf_counter() - start)
        
        # Test ricerca Linear Probing
        start = time.perf_counter()
        for val in search_vals:
            ht_linear.ricerca(val)
        search_times['Linear Probing'].append(time.perf_counter() - start)
    
    # Plot ricerca
    for name, times in search_times.items():
        ax2.plot(sizes, times, marker='o', label=name)
    ax2.set_xlabel('Numero di elementi')
    ax2.set_ylabel('Tempo (secondi)')
    ax2.set_title('Performance Ricerca (100 operazioni)')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig('hashtable_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    print("Avviando test completo delle performance HashTable...")
    hashtable_performance_test()
    
    print("\nAvviando test di confronto semplificato...")
    hashtable_comparison_test()
