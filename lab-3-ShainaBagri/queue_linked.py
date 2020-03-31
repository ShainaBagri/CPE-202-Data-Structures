# Linked list version of ADT Queue

# Node class for use with Queue implemented with linked list
class Node:
    def __init__(self, data, next=None):
        self.data = data    # data held by Node
        self.next = next    # reference to next Node

    def __eq__(self, other):
        return ((type(other) == Node)
          and self.data == other.data
          and self.next == other.next
        )

    def __repr__(self):
        return ("Node({!r}, {!r})".format(self.data, self.next))

class Queue:
    """Implements an efficient Queue ADT using a linked list of Nodes"""

    def __init__(self, capacity, front=None):
        """Creates a queue with a capacity and initializes with front Node"""
        self.capacity = capacity    # capacity of queue
        self.front = front          # front Node of Queue (next item out)
        self.rear = None            # rear Node of Queue (last item in)
        self.num_items = 0          # number of items in queue
        node = front
        while node is not None:     # set number of items based on input
            self.num_items += 1
            self.rear = node        # set rear Node
            node = node.next
            if self.num_items > capacity:
                raise IndexError

    def __eq__(self, other):
        return ((type(other) == Queue)
          and self.capacity == other.capacity
          and self.front == other.front
        )

    def __repr__(self):
        return ("Queue({!r}, {!r})".format(self.capacity, self.front))

# ----------------------------- #

    def is_empty(self):
        """Returns true if the queue is empty and false otherwise"""
        return self.num_items==0

    def is_full(self):
        """Returns true if the queue is full and false otherwise"""
        return self.num_items==self.capacity

    def enqueue(self, item):
        """enqueues item"""
        if self.is_full():
            raise IndexError
        elif self.is_empty():
            newnode = Node(item)
            self.front = newnode
            self.rear = self.front
            self.num_items += 1
        else:
            newnode = Node(item)
            self.rear.next = newnode
            self.rear = newnode
            self.num_items += 1

    def dequeue(self):
        """dequeues item"""
        if self.is_empty():
            raise IndexError
        else:
            temp = self.front.data
            self.front = self.front.next
            self.num_items -= 1
            return temp

    def size(self):
        """Returns the number of items in the queue"""
        return self.num_items
