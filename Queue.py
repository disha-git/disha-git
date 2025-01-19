class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    
    def is_empty(self):
        return self.front is None

    
    def display(self):
        current = self.front
        while current:
            print(current.data, end="--->")
            current = current.next
        print("none")


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()  

print("remove element: ", q.dequeue())
print("remove element: ", q.dequeue())

    

q.display() 











































######## OR #########
def enqueue():
    n = int(input("Enter a element : "))
    queue.append(n)
    print()

def dequeue():
    if len(queue) == 0:
        print("QUEUE IS EMPTY")
        print("-------------------------")
    else:
        print(queue[0] , "is element deleted from the Queue")
        del queue[0]
        print()

def display():
    if len(queue) == 0:
        print("QUEUE IS EMPTY")
    else:
        print("ELEMENT OF THE QUEUE ARE : ")
        for ele in queue:
            print(ele, end=" ")
        print("\nFront ele of the queue : " , queue[0])
        print("RARE ele of the queue: ", queue[-1])
        print()

queue = list()
while(1):
    print("Enter any key\n1-insert\n2-delete\n3-Display\n4-Exit")
    option=int(input())
    if option == 1:
        print("insert the element")
        enqueue()
    elif option == 2:
        print("Delete the element")
        dequeue()
    elif option == 3:
        print("DISPLAY")
        display()
    else:
        print("EXIT")
        break
