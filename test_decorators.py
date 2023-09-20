import sole_decorators

@sole_decorators.execute_rep(2)
@sole_decorators.repeat_n(2)
def myprinting(text):
    print (text)
    


myprinting('clen')