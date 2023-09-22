from sole_decorators import get_log
import my_class

@get_log
def myprinting(text):
    print (text)
    
anar_class= my_class.MyClass()

anar_class.show_list()
myprinting('clen')