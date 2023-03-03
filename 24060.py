n, c = map(int, input().split())

data = list(map(int, input().split()))

def merge_sort(left, right):
    if(left < right):
        mid = (left + right) // 2
        merge_sort(left, mid)
        merge_sort(mid + 1, right)
        merge(left, mid, right)

def merge(left, mid, right):
    a = left
    b = mid + 1
    c = right
    tmp = []

    while(a <= mid and b <= right):
        global data
        if(data[a] <= data[c]):
            tmp.append(data[a])
            a += 1
        else:
            tmp.append(data[c])
            b += 1
        print(*tmp)

    if(a > mid):
        tmp += data[c:]
    else:
        tmp += data[a:]
    
    data = tmp

# merge_sort(0, n)
# print(*data)
