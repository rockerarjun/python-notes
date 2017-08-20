import time
import datetime
today = datetime.datetime.today()
today = datetime.date.today()

#format = "(%b), %d, %Y, %H:%M:%S ,(%a)"#strftime.org
#format = "(%b) %d/%Y, (%A)"#strftime.org
format = "(%B) %d/%Y, (%A)"#strftime.org
print('ISO     :', today)
b =  today+datetime.timedelta(days=23)
future= b.strftime(format)
print("the date after twentythreedays",future)
s = today.strftime(format)
print('strftime:',s)
d = datetime.datetime.strptime(s, format)
print('strptime:', d.strftime(format))

