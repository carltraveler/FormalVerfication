OntCversion = '2.0.0'
a = 20
b = 30

def Main():
    VaasAssert(a == 20)
    VaasAssert(b == 30)

    modify_global()
    print(a)
    print(b)
    VaasAssert(a == 20)
    #VaasAssert(b == 20)

def modify_global():
    global a, b
    a = 7
    b = 8

def VaasAssert(expr):
    if not expr:
        raise Exception("AssertError")
