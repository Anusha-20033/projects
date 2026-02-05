'''nested functions
================='''

def outerfun():
    x=10
    def innerfun():
        nonlocal x
        x=40
        y=20
        print(x)#40
        print(y)#20
    return innerfun()
fun=outerfun()
fun()#nonetype it is not callable




