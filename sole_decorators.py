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


def repeat_n(number):
    def wrapper(func):
        
        
        
        
           
            
        def inner(*args,**kwargs):
            for i in range(number):
                
                func(*args,**kwargs)
                
            return func(*args,**kwargs)
        return inner
    return wrapper
    