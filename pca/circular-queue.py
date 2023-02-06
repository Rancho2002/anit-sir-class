class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = self.tail = -1

    def enqueue(self, data):
        if ((self.tail + 1) % self.size == self.head):
            print("Queue is Full\n")
 
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.size
            self.queue[self.tail] = data
 
    def dequeue(self):
        if (self.head == -1):
            print("Queue is Empty\n")
 
        elif (self.head == self.tail):
            temp=self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.size
            return temp
 
    def display(self):
        if(self.head == -1):
            print("No element in the Queue")
        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.head, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
