import bisect

class SortedArray:
    def __init__(self, initial=None):
        self._data = sorted(set(initial)) if initial else []

    def add(self, x):
        pos = bisect.bisect_left(self._data, x)
        if pos < len(self._data) and self._data[pos] == x:
            return
        self._data.insert(pos, x)

    def contains(self, x):
        pos = bisect.bisect_left(self._data, x)
        return pos < len(self._data) and self._data[pos] == x

    def remove(self, x):
        pos = bisect.bisect_left(self._data, x)
        if pos < len(self._data) and self._data[pos] == x:
            self._data.pop(pos)

    def count_range(self, l, r):
        left_pos = bisect.bisect_left(self._data, l)
        right_pos = bisect.bisect_right(self._data, r)
        return right_pos - left_pos

    def print_all(self):
        print(*self._data)

def main():
    n, q = map(int, input().split())
    initial = list(map(int, input().split())) if n > 0 else []
    sa = SortedArray(initial)
    for _ in range(q):
        command = input().strip().split()
        op = command[0]
        if op == "ADD":
            sa.add(int(command[1]))
        elif op == "CONTAINS":
            print("YES" if sa.contains(int(command[1])) else "NO")
        elif op == "REMOVE":
            sa.remove(int(command[1]))
        elif op == "COUNT_RANGE":
            print(sa.count_range(int(command[1]), int(command[2])))
        elif op == "PRINT":
            sa.print_all()

if __name__ == "__main__":
    main()
