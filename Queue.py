from Node import Node

class Queue:

    def __init__(self):
        self.head = Node(None)   # front
        self.tail = None   # Rear

    # add new element to Queue
    def enqueue():
        pass

    # return the value of peek and remove the front element
    def dequeue(self):
        if self.head is None:
            return "empty"
        deqval = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return deqval

    # check if Queue is empty
    def is_empty():
        pass

    # return the peek item
    def get_peek():
        pass

    # print all items
    def print_queue():
        pass
