n, c = map(int, input().split())
data = list(map(int, input().split()))
save = []

def merge_sort(arr):
    if(len(arr) == 1):
        return arr
    
    mid = (len(arr) + 1) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    a, b = 0, 0
    tmp = []
    global save

    while(a < len(left) and b < len(right)):
        if(left[a] <= right[b]):
            save.append(left[a])
            tmp.append(left[a])
            a += 1
        else:
            save.append(right[b])
            tmp.append(right[b])
            b += 1
        
    while(a < len(left)):
        save.append(left[a])
        tmp.append(left[a])
        a += 1
    while(b < len(right)):
        save.append(right[b])
        tmp.append(right[b])
        b += 1

    return tmp

merge_sort(data)
print(save[c - 1] if c - 1 < len(save) else -1)