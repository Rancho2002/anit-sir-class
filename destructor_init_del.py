

#destructor

class A(object): 

    def __init__(self): 

        self.str1 = 'PrepInsta'

        print('Object Created' , self.str1) 

    def __del__(self):

        print('Destructor is called Manually')



ob = A() 

del ob 

#ob1=A()

#destructor will be called automattically for ob1

