import re

def solution(new_id):
    # 1
    new_id = new_id.lower()
    # 2
    new_id = re.sub('[^a-z0-9-_\.]*', '', new_id)
    # 3
    new_id = re.sub('\.\.+', '.', new_id)
    # 4
    new_id = re.sub('^\.', '', new_id)
    new_id = re.sub('\.$', '', new_id)
    # 5
    if not new_id:
        new_id += 'a'
    # 6
    new_id = new_id[:15]
    new_id = re.sub('\.$', '', new_id)
    # 7
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))
    
    return new_id
