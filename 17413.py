word = list(input())

reverse = True
res = []
tmp = []

for i in word:
    tmp += i
    if(reverse == True):
        if(i == '<'):
            tmp.pop()
            while(tmp):
                res += tmp.pop()
            tmp += i
            reverse = False
            res += tmp
            tmp = []
        elif(i == ' '):
            tmp.pop()
            while(tmp):
                res += tmp.pop()
            res += ' '
        
    else: #<
        if(i == '>'):
            reverse = True
            tmp.pop()
            res += tmp
            tmp = []
            res += '>'
        
            
res += tmp[::-1]

print(*res, sep = '')
