sugar = int(input())

bag = 0

while(sugar > 0):
    if(sugar % 5 == 0):
        bag += sugar // 5
        sugar %= 5
        break
    else:
        bag += 1
        sugar -= 3
    
print(bag if sugar == 0 else -1)
