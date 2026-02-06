class Stack:
    def __init__(self):
        self.capacity = 64
        self.items = []    
        
    def limit_check(self):
        if len(self.items) == self.capacity:
            return True
        return False
    
    
    def push(self, item):
        if self.limit_check():
            print("[STACK OVERFLOW ERROR]. Limit Reached. Cannot push item")
            return
        self.items.append(item)
        print(f"PUSH SUCCESS. {item}. Item pushed to stack")
                
        
    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False
    
    
    def pop_stack(self):
        if self.is_empty():
            print("[STACK UNDERFLOW ERROR]: Stack is empty. Cannot pop.")
            return None
        return self.items.pop()

        
    
    def peek(self):
        if self.is_empty():
            print("[EMPTY STACK]. Stack is empty. Cannot peek")
            return None
        return self.items[-1]
    
    def search(self, item):
        print("[SEARCH WARNING] Before proceeding, understand that this is a time expensive operation")
        if self.is_empty():
            return "Unable to perform operation, Stack is empty"
        for _ in range(len(self.items)):
            if item == self.items[-1]:
                break
            self.items.pop()
        return self.peek()
    

my_stack = Stack()

for i in range(64):
    my_stack.push(i)

print(my_stack.search(466))

        
            