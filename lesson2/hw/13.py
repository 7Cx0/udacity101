def multiplication_table(num):
    i=1
    while i <= num:
        j=1
        while j <= num:
            k = i*j
            print str(i) + ' * ' +  str(j) + ' = ' + str(k)
            j+=1
        i+=1

multiplication_table(5)
