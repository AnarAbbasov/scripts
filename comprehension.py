import decorators
#r=[x for x in range (6)]
@decorators.mydecorator(3)
def myfunc(text1,text2):
    print('ggg')
    return
#print (r)
#myfunc('ff','gg')

if __name__=='__main__':
    myfunc('hgt','hyt')