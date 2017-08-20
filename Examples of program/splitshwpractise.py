import re
dog  = "A fast  running dog  doesn't stop running at the time  of seeing monkey and fog in the fild dog ,fog and monkey fight to eachother"
dogmatch = re.split(r"[acbfoed]og",dog)
print("Regular Split : ",dogmatch)
dogmatch = re.findall("\s([acbfoed]og)\s",dog)
print("dogmatch:",dogmatch)


dogmatch = re.split(r"\w+",dog)   #split the word
print("Regular split \w+ :", dogmatch)


sentences = "I am the student of computer engineering, i like programming very much which is python and very intresting; " 
print("\nsentence:", sentences)

meta = re.findall(r'[A-Za-z]{2}',sentences) #2 characterdisplay
print("\n1[A-Za-z]{2}:",meta)

meta = re.findall(r'([^A-Za-z]+)',sentences) #2 characterdisplay
print("\n11([^A-Za-z]+):",meta)



meta = re.findall(r'\b[A-Za-z]{2}\s',sentences) # with space after two characters
print("\n2[A-Za-z]{2}\s :",meta)



meta = re.findall(r'[A-Za-z]{3}', sentences) #3 characterdisplay
print("\n3[A-Za-z]{3} :",meta)


meta = re.findall(r'\b[A-Za-z]{3}\s',sentences) #with sapace after three characters
print("\n4[A-Za-z]{3}\s :",meta)


meta = re.findall(r'[A-Za-z]{4}', sentences) #4 charactersdisplay
print("\n5[A-Za-z]{4} :",meta)


meta = re.findall(r'\b[A-Za-z]{4}\s', sentences)# with space after four characters 
print("\n5[A-Za-z]{4}\s :", meta)


meta = re.findall(r'[A-Za-z]{2}\s(\w+)',sentences) #\w+[a-zA-Z_0-9]
print("\n6[A-Za-z]{2}\s(\w+) :",meta)
print("Length :",len(meta))


meta = re.findall(r'\b[A-Za-z]{2}\s(\w+)',sentences) #w\+[a-zA-Z_0-9]
print("\n7\b[A-Za-z]{2}\s(\w+) :",meta)
print("Length :",len(meta))


meta = re.findall(r'\b[A-Za-z]{2}\s(\w*)',sentences) #\w*[a-zA-Z_0-9]
print("\n7\b[A-Za-z]{2}\s(\w*) :",meta)


meta = re.findall(r'in\s?(\w+)',sentences) #word boundary
print("\n8. Word Boundary: ",meta)

meta = re.findall(r'\bin\s(\w+)',sentences)
print("\n9. Word Boundary:\\b",meta)


meta = re.findall(r'e{2}n\s*(\w+)',sentences) # two 
print("\n10. e{2}n\s*(\w+) : ",meta)







 


