class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
            
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node 
            self.tail = new_node
            
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next 
                
        return False
    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

test1 = LinkedList()
test1.insert_at_beginning("Ram")
test1.insert_at_end("Shyam")
print(test1.search("Hari"))
test1.print_list()
