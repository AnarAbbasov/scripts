from datetime import datetime
def mydecorator(numberoftimes):
    def inner(func):
        for i in range(numberoftimes):
          func('tdr','tfr')
        return func
    
    return inner
        
def get_log(function):
    def inner(*args, **kwargs):
        print ( str(datetime.now()))
        
        return function(*args, **kwargs)
    return inner

def execute_rep(number_of_times):
    def wrapper(func):
        print (number_of_times)
        def inner(*args,**kwargs):
            
            return func(*args,**kwargs)
        return inner
    return wrapper
        
       
@mydecorator(numberoftimes=3)
def my_function(text,text2):
    print (text,text2)
    