print map(lambda x: x+1,[1,2,3])
  
print reduce(lambda x,y: x+y,[1,2,3])
  
def p():
    print "gg"
  
p()
  
def pp(a):
    return map(a,[1,2,3,4,5])
  
print pp(lambda x: x+1)
