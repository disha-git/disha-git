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
    
