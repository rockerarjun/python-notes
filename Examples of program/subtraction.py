"""
map(), filter(), reduce() and lambda
"""
from functools import reduce
a = [4,5,8,9,7]
b = [14,15,13,16,19] 
c =[-4,-5,-3,2,-6]
print(list(map(lambda x,y:y-x, a,b)))##subtraction
print(list(map(lambda x,y,z:y-x+z, a,b,c)))##
