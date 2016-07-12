def biggest(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    return b

print biggest(6,2,3)
