"""
String variable and some basic operations
"""

words = "I Love Python"  #type 1
words_again ='I Love Python' #type 2
name = 'student' 

#Multi-Line String #type 3
words_multi_line= '''Python is a scientific
programming language and is very famous
among the Researchers globally'''

print("Length words : ",len(words_multi_line))#Total Length of Characters
print("Count Spaces : ",words_multi_line.count(' '))#spaces

print("\nConcat Strings: "+words+" , "+name)
print("Multiple using * ",name*4)

print("\nMax char : ",max(words_multi_line))#max alphabetical char in string
print("\nMin char : ",min(words_multi_line))#min alphabetical char in string


#Case Related
print("\nTitle : ",words_multi_line.title()) #all begining chars to Uppercase.
print("\nSwapCase : ",words_multi_line.swapcase()) #invert cases of all chars
print("\nUpperCase words : ",words_multi_line.upper())
print("\nLowerCase words : ",words_multi_line.lower())
print("Split Multi line : ",words_multi_line.split())#List



#SplitLines, used to split '\n': newline char
print("\nSplit Lines : ", words_multi_line.splitlines())

print("\nJoin : ", '<>'.join(words))
print("Split words : ",words.split())#List
print("Join Lists : ", '__'.join(words.split()))


#String Replace
print("\nReplace 'Python' from '",words,"' :", words.replace('Python','Python Programming'))


#use of Special Operators, helpful in Decision making 
if "P" in words:
    print("'P' exist in Words")

if "p" in words:
    print("'p' exist in Words")
else:
    print("'p' doesnot exist in Words")

#replace('existing char','new char'):
#Strips: lstrip(), rstrip(), strip() removing spaces in Strings.
#Other Decision Making functions: isalnum(), isalpha(),isdigit(),islower(),isnumeric(),isspace(),istitle(),isupper()
