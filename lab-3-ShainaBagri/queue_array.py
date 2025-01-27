# Queue ADT - circular array implementation

class Queue:
    """Implements an efficient first-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity, init_items=None):
        """Creates a queue with a capacity and initializes with init_items"""
        self.capacity= capacity         # capacity of queue
        self.items = [None]*capacity    # array for queue
        self.num_items = 0              # number of items in queue
        self.front = 0                  # front index of queue (items removed from front)
        self.rear = 0                   # rear index of queue (items enter at rear)
        if init_items is not None:      # if init_items is not None, initialize queue
            if len(init_items) > capacity:
                raise IndexError
            else:
                self.num_items = len(init_items)
                self.items[:self.num_items] = init_items
                self.rear = self.num_items % self.capacity # % capacity addresses length=capacity

    def __eq__(self, other):
        return ((type(other) == Queue)
            and self.capacity == other.capacity
            and self.get_items() == other.get_items()
            )

    def __repr__(self):
        return ("Queue({!r}, {!r})".format(self.capacity, self.get_items()))

    # get_items returns array (Python list) of items in queue
    # first item in the list will be front of queue, last item is rear of queue
    def get_items(self):
        if self.num_items == 0:
            return []
        if self.front < self.rear:
            return self.items[self.front:self.rear]
        else:
            return self.items[self.front:] + self.items[:self.rear]

# ----------------------------- #

    def is_empty(self):
        """Returns true if the queue is empty and false otherwise"""
        return self.rear==self.front and self.num_items==0

    def is_full(self):
        """Returns true if the queue is full and false otherwise"""
        return self.rear==self.front and self.num_items==self.capacity

    def enqueue(self, item):
        """enqueues item"""
        if self.is_full():
            raise IndexError
        else:
            self.items[self.rear] = item
            self.rear += 1
            if self.rear >= self.capacity:
                self.rear = self.rear - self.capacity
            self.num_items += 1

    def dequeue(self):
        """dequeues item"""
        if self.is_empty():
            raise IndexError
        else:
            temp = self.items[self.front]
            self.front += 1
            if self.front >= self.capacity:
                self.front = self.front - self.capacity
            self.num_items -= 1
            return temp

    def size(self):
       """Returns the number of items in the queue"""
       return self.num_items
