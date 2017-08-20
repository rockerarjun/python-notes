"""
map(), filter(), reduce() and lambda
"""
from functools import reduce
a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
print(list(map(lambda x,y:x+y, a,b))) 
print(list(map(lambda x,y,z:x+y+z, a,b,c))) 
print(reduce(lambda x, y: x+y, range(1,10)))
print(reduce(lambda a,b: a if (a > b) else b, [47,11,42,102,13]))


print("\n Example 2")


def add(x):
    return int(x[0])+int(x[1]) #int() optional here all vars are int



print([(x,x*2) for x in range(1,11)])




print("\n using map() and add()")
print(list(map(add,[(x,x*2) for x in range(1,11)])))
quit()
