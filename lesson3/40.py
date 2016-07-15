def find_element(l,value):
    count = 0
    for i in l:
        if i == value:
            return count
        count+=1
    return -1

print find_element([1,2,4],3)
