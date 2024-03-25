import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    res = []
    my_dict = dict(zip([terms[i][0] for i in range(len(terms))], [int(terms[i].split()[-1]) for i in range(len(terms))]))
    month = relativedelta(months=1)
    today = datetime.datetime.strptime(today, '%Y.%m.%d')
    
    for i, j in enumerate(privacies):
        after = datetime.datetime.strptime(j[:-1], '%Y.%m.%d ') + month * my_dict[j[-1]] - datetime.timedelta(days=1)
        if after.day >= 28:
            after = after.replace(day=28)
        
        if after < today:
            res.append(i + 1)
        
    return res