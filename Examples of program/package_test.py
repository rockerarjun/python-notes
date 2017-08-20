import python_package as pp
# from python_package import test
# from python_package import test_again
import python_package.test as t
import python_package.test_again as ta
import python_package.package_python.test_test as tt
from python_package.test import hi,hello
#from python_package.test import hello#hello is declear

print("Dir: ",dir(pp))
print("Doc: ",pp.__doc__)
print("File: ",pp.__file__)
print("Name: ",pp.__name__)
print("Path: ",pp.__path__)
#print("Builtins: ",pp.__builtins__)



#calling
t.hello()
ta.hello()
t.hi()
ta.hi()


#calling again
hi()
hello()


#calling again
print("TestTest: ",tt.__file__)
#tt.hello()
#tt.hello()
tt.hi()
print("the document:",tt.__doc__)
quit()