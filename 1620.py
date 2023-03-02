M, N = map(int, input().split())
mon_name = []

for i in range(M + N):
    mon_name.append(input())

mon_dict = dict(zip(mon_name[:M], range(1, M + 1)))

for Q in mon_name[M:]:
    if(Q.isalpha()):
        print(mon_dict[Q])
    else:
        print(mon_name[int(Q) - 1])