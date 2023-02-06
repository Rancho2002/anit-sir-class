class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)
    def __repr__(self):
        return str(self.items)
    def __len__(self):
        return len(self.items)
    def __getitem__(self, index):
        return self.items[index]

q = Queue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
print(q.isEmpty())
q.enqueue(8.4)
# print(q.dequeue())
# print(q.dequeue())
print(q.size())
print(q)
print(q[0])
print(q[1])


    
    

