import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    res = 0
    
    while scoville[0] < K and len(scoville) >= 2:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        
        new = a + 2 * b
        heapq.heappush(scoville, new)
        
        res += 1

    if scoville[0] >= K:
        return res
    else:
        return - 1
    