n, k = map(int, input().split())

data = list(map(int, input().split()))

def merge_sort(left, right):
    if(left < right):
        mid = (left + right) // 2
        merge_sort(left, mid)
        merge_sort(mid + 1, right)
        print(*data)
        merge(left, mid, right)

def merge(left, mid, right):
    j = mid + 1
    i = left
    k = right
    tmp = []

    while(i <= mid and j <= right):
        global data
        if(data[i] <= data[j]):
            tmp.append(data[i])
            i += 1
        else:
            tmp.append(data[j])
            j += 1

    if(i > mid):
        tmp += data[j:]
    else:
        tmp += data[i:]
    
    data = tmp

merge_sort(0, n)
print(*data)

# 28~ 슬라이싱에서 data list보다 크게 리스트 만들어졌음
