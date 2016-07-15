def find_last(search_string, target_string):
    lpos=-1
    while True:
        pos = search_string.find(target_string,lpos+1)
        if pos == -1:
            return lpos
        lpos=pos

print find_last('aba', 'a')
