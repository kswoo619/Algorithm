import sys

doc = sys.stdin.readline().rstrip()
find = sys.stdin.readline().rstrip()

ans = 0
for _ in range(0, len(doc) - len(find) + 1):
    if(doc[0:len(find)] == find):
        ans += 1
        doc = doc[len(find):]
    else:
        doc = doc[1:]

print(ans)
