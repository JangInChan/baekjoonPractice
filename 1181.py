import sys

N = int(input())
ar_Word = []
for _ in range(N):
    ar_Word.append(sys.stdin.readline().strip())

Word_Set = list(set(ar_Word))
Word_Set.sort()
Word_Set.sort(key=lambda x: len(x))
for w in Word_Set:
    print(w)