class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node 
            return
            
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next 
            
        current_node.next = new_node
        
    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node=current_node.next
        
        
list = LinkedList()
list.insertAtEnd("a")
list.insertAtEnd("b")
list.print()