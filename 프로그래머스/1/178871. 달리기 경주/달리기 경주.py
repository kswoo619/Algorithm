def solution(players, callings):
    rank = dict(zip(players, [i for i in range(len(players))]))
    inverse = dict(zip([i for i in range(len(players))], players))
    
    for i in callings:
        idx = rank[i]
        passed = inverse[idx-1]
        idx2 = rank[passed]
        
        rank[i] = idx2
        rank[passed] = idx
        
        rank[passed], rank[i] = idx, idx2
        inverse[idx], inverse[idx2] = inverse[idx2], inverse[idx]
    
    return sorted(rank, key=lambda x:rank[x])