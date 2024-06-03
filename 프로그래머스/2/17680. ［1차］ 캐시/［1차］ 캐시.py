from collections import deque
def solution(cacheSize, cities):
    cache = deque()
    time = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for i in cities:
        i = i.lower()
        
        if i in cache:
            time += 1
            cache.remove(i)
            cache.append(i)
        else:
            time += 5
            if len(cache) < cacheSize:
                cache.append(i)
            else:
                cache.popleft()
                cache.append(i)
    return time