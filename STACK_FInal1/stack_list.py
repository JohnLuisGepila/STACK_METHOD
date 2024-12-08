class Node:
    def __init__(self, data):
        # Initializes a node with the given data and sets the next node to None
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        # Initializes an empty stack with the top set to None
        self.top = None

    def push(self, item):
        # Creates a new node with the given item and adds it to the top of the stack
        new_node = Node(item)
        new_node.next = self.top  # The new node's next points to the current top
        self.top = new_node  # The new node becomes the new top of the stack

    def pop(self):
        # Removes and returns the top item of the stack, if not empty
        if not self.is_empty():
            popped_item = self.top.data
            self.top = self.top.next  # Move the top to the next node
            return popped_item
        else:
            return "Stack is empty"

    def peek(self):
        # Returns the top item of the stack without removing it, if not empty
        if not self.is_empty():
            return self.top.data
        else:
            return "Stack is empty"

    def is_empty(self):
        # Checks if the stack is empty
        return self.top is None

    def print_stack(self):
        # Returns the current state of the stack as a list for easy display
        current = self.top
        stack_elements = []
        while current is not None:
            stack_elements.append(current.data)
            current = current.next
        return stack_elements