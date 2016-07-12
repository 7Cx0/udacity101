def big(a,b):
    if a>b:
        return a
    else:
        return b
def biggest(a,b,c):
   return big(a,big(b,c)) 

print biggest(6,2,3)
