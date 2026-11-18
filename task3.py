def bubble_sort_early_stop(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    passes = 0
    for i in range(n - 1):
        passes += 1
        swapped = False
        for j in range(n - 1 - i):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return arr, comparisons, swaps, passes

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    sorted_arr, comparisons, swaps, passes = bubble_sort_early_stop(arr)
    print(*sorted_arr)
    print(f"Сравнений: {comparisons}")
    print(f"Обменов: {swaps}")
    print(f"Проходов: {passes}")

if __name__ == "__main__":
    main()
