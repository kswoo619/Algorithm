import sys

N = int(input())
mat = [sys.stdin.readline().strip() for _ in range(N)]

mxi = mxj = -1 #max
mni = mnj = N #min

for i in range(N):
    for j in range(N):
        if(mat[i][j] == 'G'):
            if(mxi < i):
                mxi = i
            if(mxj < j):
                mxj = j
            if(mni > i):
                mni = i
            if(mnj > j):
                mnj = j
res = ''
if(mxi != mni):
    if(mxi < N - mni - 1):
        res += '^' * mxi
    else:
        res += 'v' * (N - mni - 1)
    
if(mxj != mnj):
    if(mxj < N - mnj - i):
        res += '>' * mxj
    else:
        res += '<' * (N - mnj - 1)

print("%d %s" % (len(res), res))
