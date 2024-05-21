class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 
        
# Update node of a linked list
# at given position
def updateNode(self, val, index):
	current_node = self.head
	position = 0
	if position == index:
		current_node.data = val
	else:
		while(current_node != None and position != index):
			position = position+1
			current_node = current_node.next

		if current_node != None:
			current_node.data = val
		else:
			print("Index not present")
