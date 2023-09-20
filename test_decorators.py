from sole_decorators import get_log


@get_log
def myprinting(text):
    print (text)
    


myprinting('clen')