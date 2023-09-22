from sole_decorators import get_log, repeat_n
import my_class

@get_log
def myprinting(text):
    print (text)
    
anar_class= my_class.MyClass()

anar_class.show_list()
anar_class.show_my_dict()

anar_class.show_set()
myprinting('clen')