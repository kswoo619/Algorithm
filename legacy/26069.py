N = int(input())

dance = ['ChongChong']

for _ in range(N):
    a, b = input().split()
    if(a in dance) or (b in dance):
        dance.append(a)
        dance.append(b)

print(len(set(dance)))
