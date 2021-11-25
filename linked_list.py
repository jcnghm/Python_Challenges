# A Complete Implementation of a linkedlist

# 2 components to this solution -- A Node Class and the LinkedList class

class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        
    def pushOn(self,new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node
    def insertAfter(self,prev_node,new_value):
        # Check if the previous node even exists
        if prev_node is None:
            print("The given previous node must not be empty!")
            return
        # IF the Node is not empty then create a new node
        new_node = Node(new_value)
        
        # Update the previous node's next pointer to point to the new value
        new_node.next = prev_node.next
        
        # Update the previous node to point to the new node's value
        prev_node.next = new_node
    
    # This method will append a new node to the END of the linkedlist
    def append(self,new_value):
        # Create New Node with a new value
        new_node = Node(new_value)
        
        #Check if the LinkedList is empty
        #And if it is, make THIS new node the head node(beginning of the list)
        if self.head is None:
            self.head = new_node
            
        #BUT if the list is NOT empty - traverse to the end
        # and add the NEW value to the end of the list
        
        last = self.head
        
        #While last.next is not None -> continue to loop until we find a None value
        while(last.next):
            last = last.next
        # Change current last node value to point to the NEW value
        last.next = new_node
        
    def traverse(self):
        temp = self.head
        # while temp is NOT None -> keep looping through the links until you reach a None Value
        while(temp):
            print(temp.value)
            temp = temp.next
            
weekdays_links = LinkedList()

# Insert a new day into the list
weekdays_links.pushOn('Mon')
weekdays_links.append('Tues')
weekdays_links.append('Thurs')
weekdays_links.insertAfter(weekdays_links.head.next,"Wed")
weekdays_links.traverse()