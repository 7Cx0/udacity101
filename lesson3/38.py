def measure_udacity(l):
    count = 0
    for i in l:
        if i[0] == 'U':
            count+=1
    return count


print measure_udacity(['Dave','Sebastian','Katy'])
print measure_udacity(['Umika','Umberto'])
