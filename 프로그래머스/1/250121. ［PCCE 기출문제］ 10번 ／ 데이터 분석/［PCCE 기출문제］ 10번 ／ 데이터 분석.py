def solution(data, ext, val_ext, sort_by):
    get = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    
    data = [data[i] for i in range(len(data)) if data[i][get[ext]] <= val_ext]
    data.sort(key=lambda x: x[get[sort_by]])
    
    return data