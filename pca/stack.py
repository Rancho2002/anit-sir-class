class stack:
    def __init__(self):
        self.dict = []
        
    def push(self,data):
        self.dict.append(data)
    
    def pop(self):
        if len(self.dict)!=0:
            i = self.dict.pop()
            return i
        else:
            print("stack underflow")
    def traverse(self):
        for i in self.dict:
            print(i,end=" ")

s = stack()
s.push(12)
s.push(13)
s.push(5)
s.push(24)
s.push(62)
s.push(12)
s.traverse()
r = s.pop()
print("\n")
print(r)
s.traverse()
