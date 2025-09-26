from Stack import Stack
from Node import Node

class Stack:
    
    def __init__(self):
        self.top = None

    # push new element to Stack
    def push_element(value):
        pass

    # pop top element and return value
    def pop_element():
        pass

    # check if Stack is empty
    def is_empty():
        pass

    # return the top item
    def get_top(self):
        if self.top == None:
            return None
        return self.top.data

    # print all items
    def print_stack(self):
        if self.top == None:
            print("Stack is empty")
        while self.top != None:
            print(self.top.data)
            self.top = self.top.next
        