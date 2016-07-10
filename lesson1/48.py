s = 'anystring'

print s[:] # allways
print s+s[0:-1+1] #trick, last one is a empty string so it works out
print s[0:] #always
print s[:-1] #no
print s[:3]+s[3:] #doesn't matter what string size cause it can be any size. Unlike s[3] which can error out if the string is 2 characters
