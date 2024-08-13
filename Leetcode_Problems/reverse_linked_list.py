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
            while tail.next:
                tail = tail.next
            tail.next = Node(value)
            
    def output_list(self):
        out_original = []
        node = self.head
        while node:
            out_original.append(node.value)        
            node = node.next
        return out_original
    
def reverse_linked_list(out_original):
    
    reversed_ll = LinkedList()
    prev_node = None
    for value in out_original:
        new_node = Node(value)
        
        new_node.next = prev_node
        prev_node = new_node
    
    reversed_ll.head = prev_node
    return reversed_ll      
