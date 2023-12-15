class Node:
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev
    
    def __str__(self) -> str:
        return str(self.data)


class Queue:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def enqueue(self, value):
        add_node = Node(value, self.head.next, self.head)
        self.head.next.prev = add_node
        self.head.next = add_node
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            return
        remove_node = self.tail.prev
        self.tail.prev = remove_node.prev
        remove_node.prev.next = remove_node.next
        return_value = remove_node.data
        remove_node.next = None
        remove_node.prev = None
        self.length -= 1
        return return_value
    
    def peek(self):
        if self.is_empty():
            return    
        remove_node = self.tail.prev

    def get_length(self):
        current_node = self.head.next
        length = 0
        while current_node != current_node.next:
            length += 1
            current_node = current_node.next

        return length
    
    def is_empty(self):
        if self.head.next == self.tail:
            return True
        else:
            return False
    
    def clear(self):
        for i in range(self.length):
            self.dequeue()
        self.length = 0

    def __str__(self) -> str:
        current_node = self.head.next
        res = "["
        while current_node != self.tail:
            res += str(current_node.data) + " "
            current_node = current_node.next
        return res + "]"

queue = Queue()

queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(2)

print(queue)

queue.dequeue()

print(queue)

