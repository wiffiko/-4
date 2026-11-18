import bisect

def main():
    n = int(input())
    journal = []
    for _ in range(n):
        parts = input().strip().split()
        time_val = int(parts[0])
        event_id = parts[1]
        pos = bisect.bisect_right(journal, (time_val, ""))
        journal.insert(pos, (time_val, event_id))
        formatted = ", ".join(f"{t}{eid}" for t, eid in journal)
        print(formatted)

if __name__ == "__main__":
    main()
