from Queue import Queue


class Queue:

    def __init__(self):
        self.head = None  # front
        self.tail = None  # Rear

    # add new element to Queue
    def enqueue():
        pass

    # return the value of peek and remove the front element
    def dequeue():
        pass

    # check if Queue is empty
    def is_empty(self):
        return self.head == None

    # return the peek item
    def get_peek(self):
        if self.head:
            return self.head.data
        else:
            return None

    # print all items
    def print_queue(self):
        current = self.head
        values = []
        while current:
            values.append(current.data)
            current = current.next
        print(values)
