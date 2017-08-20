import re
s = ['airplane', 'base', 'ALLIGATOR', 'Broad','LION','like' ]
print("Filter 'A' : ",list(filter((lambda x: re.match(r'A', x)),s)))
print("Filter 'L' : ",list(filter((lambda x: re.match(r'L', x)),s)))
print("Filter 'a' : ",list(filter((lambda x: re.match(r'a', x)),s)))
print("Filter 'l' : ",list(filter((lambda x: re.match(r'a', x)),s)))