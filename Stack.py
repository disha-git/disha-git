class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, max_size):
        self.top = None
        self.max_size = max_size
        self.size = 0

    def push(self, data):
        if self.is_full():
            print("Stack is full. Cannot push.")
            return
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    
    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_data

 
    def peek(self):
        if self.is_empty():
            print("Stack is empty. Cannot peek.")
            return None
        return self.top.data


    def is_full(self):
        return self.size == self.max_size

    
    def is_empty(self):
        return self.size == 0

    
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


stack = Stack(max_size=4)
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)  
stack.display()  

print("popped element:",stack.pop())
print("popped elemnt :" ,stack.pop()) 
  
stack.display()

print("top elemnt:",stack.peek())







### OR ######
def push():
    n = int(input("enter a stack of the element: "))
    if len(stack) == 0:
        stack.append(n)
    else:
        stack.insert(0,n)
    print(n , "is add into the srack")

def pop():
    if len(stack) == 0:
        print("stack is empty")
    else:
        print("is deleted from the stack" , stack[0])
        del stack[0]

def display():
    if len(stack) == 0:
        print("stack is empty")
    else:
        print("ELEMENT OF THE STACK ARE")
        for ele in stack:
            print(ele)
        print("stack os the top element" , stack[0])


stack = list()
while(1):
    print("enter any key givien below\nA-push\nB-pop\nC-Display\nEnter any key for exit")
    str=input()
    if str =='A':
        print("PuSH opertion")
        push()
    elif str == 'B':
        print("POP operation")
        pop()
    elif str == 'C': 
        print("Display OPERATION")
        display()
    else:
        print("exit")
        break
    
