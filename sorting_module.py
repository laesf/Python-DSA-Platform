import time
import random
import matplotlib.pyplot as plt

class Sort:

    @staticmethod
    def quick_sort(arr):
        def _quick_sort(arr, start, end):
            if start < end:
                pivot_index = partition(arr, start, end)
                _quick_sort(arr, start, pivot_index - 1)
                _quick_sort(arr, pivot_index + 1, end)

        def partition(arr, start, end):
            pivot = arr[end]
            i = start - 1
            for j in range(start, end):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[end] = arr[end], arr[i + 1]
            return i + 1

        _quick_sort(arr, 0, len(arr) - 1)
        return arr

    @staticmethod
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = Sort.merge_sort(arr[:mid])
        right = Sort.merge_sort(arr[mid:])
        return Sort._merge(left, right)

    @staticmethod
    def _merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    @staticmethod
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    @staticmethod
    def counting_sort(arr):
        if not arr:
            return arr
        max_val = max(arr)
        count = [0] * (max_val + 1)
        for num in arr:
            count[num] += 1
        sorted_arr = []
        for i, c in enumerate(count):
            sorted_arr.extend([i] * c)
        return sorted_arr


def performance_test():
    algorithms = {
        'Quick Sort': Sort.quick_sort,
        'Merge Sort': Sort.merge_sort,
        'Insertion Sort': Sort.insertion_sort,
        'Bubble Sort': Sort.bubble_sort,
        'Counting Sort': Sort.counting_sort,
    }
    sizes = [10, 100, 1000, 10000]
    results = {name: [] for name in algorithms}

    for size in sizes:
        for name, func in algorithms.items():
            times = []
            for _ in range(10):
                data = [random.randint(0, 10000) for _ in range(size)]
                if name == 'Counting Sort':
                    data = [random.randint(0, 1000) for _ in range(size)]
                start = time.time()
                func(data.copy())
                times.append(time.time() - start)
            results[name].append(sum(times) / len(times))

    for name, timings in results.items():
        plt.plot(sizes, timings, label=name)

    plt.xlabel("Input Size")
    plt.ylabel("Average Time (s)")
    plt.title("Sorting Algorithm Performance")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("sorting_performance.png")
    plt.show()
