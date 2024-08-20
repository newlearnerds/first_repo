class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class StackLinkedList:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self,value):
        if self.head is None:
            self.head = Node(value)
        
        else:
            current_node = Node(value)
            current_node.next = self.head
            self.head = current_node        
        
        self.num_elements += 1

    def size(self):
        return self.num_elements

    def is_empty(self):
         return self.head is None    
    
    def pop(self):
        if self.head is None:
            return None
        else:
            to_pop = self.head
            self.head = self.head.next
            self.num_elements -= 1
        return to_pop.value
    
    def output_stack(self):
        out = []
        if self.head is None:
            return None
            
        current_node = self.head
        
        while current_node:
            out.append(current_node.value)
            current_node = current_node.next
        return out
    
stack = StackLinkedList()
stack.push(6)
stack.push(3)
stack.push('hi')
print(stack.output_stack())

print(stack.size())
print(stack.pop())
print(stack.size())
print(stack.output_stack())


print(stack.pop())
print(stack.size())