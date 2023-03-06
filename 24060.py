n, c = map(int, input().split())

data = list(map(int, input().split()))

def merge_sort(arr):
    if(len(arr) <= 1):
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    print('merge')
    print(*left, ',', *right)
    a, b = 0, 0
    tmp = []

    # 두 리스트에서 더 작은 값 선택 (merge)
    while(a < len(left) and b < len(right)):
        if(left[a] <= right[a]):
            tmp.append(left[a])
            a += 1
        else:
            tmp.append(right[b])
            b += 1
        
    # 리스트 남은 값 처리
    while(a < len(left)):
        tmp.append(left[a])
        a += 1
    while(b < len(right)):
        tmp.append(right[b])
        b += 1

    return tmp

print(merge_sort(data))