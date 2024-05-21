class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def InsertAtBegin(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node 
    
    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
            
list = LinkedList()
list.InsertAtBegin("Ram")
list.InsertAtBegin("Shyam")
list.InsertAtBegin("Rahul")
list.print()
