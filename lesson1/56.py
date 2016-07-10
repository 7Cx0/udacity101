s='s'
t='t'
i=5

print s.find(t,i)
print '----'
print s[i:].find(t)
#print s.find(t)[:i] #error outs
print s[i:].find(t)+i
print s[i:].find(t[i:])
