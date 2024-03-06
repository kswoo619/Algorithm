from collections import Counter
import sys

N = sys.stdin.readline()

book = []
for _ in range(int(N)):
    book.append(sys.stdin.readline().rstrip())

book.sort()
cnt = Counter(book)

print(cnt.most_common()[0][0])
