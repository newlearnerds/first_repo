from typing import List

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList():
    def __init__(self, init_list : List=None):
        self.head = None
        if init_list:
            for value in init_list:
                 self.append(value)
            
    def append(self,value):
        if self.head is None:
             self.head = Node(value)
             
        else:
            tail = self.head
            if tail.next:
                tail = tail.next
            tail.next = Node(value)
            
    def output_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)        
            node = node.next
        return out
        
        
def reverse_linked_list(original_ll):
    reversed_ll = LinkedList()
    prev_node = None
    for value in original_ll:
        new_node = Node(value)
        
        new_node.next = prev_node
        prev_node = new_node
    
    reversed_ll.head = prev_node
    return reversed_ll    

ll = LinkedList()
ll.append(2)
ll.append(4)
ll.append(6)
ll.append(8)
print('original linked list :',ll.output_list())
a = reverse_linked_list(ll.output_list())
print('reversed linked list :',a.output_list())   