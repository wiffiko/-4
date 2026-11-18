import bisect

def find_nearest(arr, x):
    pos = bisect.bisect_left(arr, x)
    if pos == 0:
        return arr[0]
    if pos == len(arr):
        return arr[-1]
    left = arr[pos - 1]
    right = arr[pos]
    if (x - left) <= (right - x):
        return left
    return right

def main():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(q):
        x = int(input())
        print(find_nearest(arr, x))

if __name__ == "__main__":
    main()
