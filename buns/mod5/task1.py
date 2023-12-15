class Stack:
    class Node:
        def __init__(self,value,next_node = None) -> None:
            self.value = value
            self.next_node = next_node

    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def push(self,el) -> None:
        self.head = Stack.Node(el, self.head)
        self.length += 1
    
    def pop(self):
        if not self.head:
            return None
        el = self.head.value
        self.head = self.head.next_node
        self.length -= 1
        return el

    def get_length(self):
        return self.length
    
    
s = Stack()
s.push(1)
s.push(2)
print(s.get_length())
print(s.pop())
print(s)
