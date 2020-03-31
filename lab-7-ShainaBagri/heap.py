
class MaxHeap:

    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.capacity = capacity
        self.heap = [None]
        self.num_items = 0

    def enqueue(self, item):
        """inserts "item" into the heap, returns true if successful, false if there is no room in the heap"""
        if self.is_full():
            return False
        self.num_items += 1
        self.heap.append(item)
        self.perc_up(self.num_items)
        return True

    def peek(self):
        """returns max without changing the heap, returns None if the heap is empty"""
        if self.is_empty():
            return None
        return self.heap[1]

    def dequeue(self):
        """returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty"""
        if self.is_empty():
            return None
        item = self.heap[1]
        self.heap[1] = self.heap[self.num_items]
        self.heap = self.heap[:self.num_items]
        self.num_items -= 1
        i = self.num_items // 2
        while i > 0:
            self.perc_down(i)
            i -= 1
        return item

    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)"""
        return self.heap[1:]

    def build_heap(self, alist):
        """Discards the items in the current heap and builds a heap from 
        the items in alist using the bottom up method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate the items in alist"""
        if self.capacity < len(alist):
            self.capacity = len(alist)
        self.heap = [None] + alist
        self.num_items = len(alist)
        i = self.num_items//2
        while i > 0:
            self.perc_down(i)
            i -= 1

    def is_empty(self):
        """returns True if the heap is empty, false otherwise"""
        return self.num_items == 0

    def is_full(self):
        """returns True if the heap is full, false otherwise"""
        return self.num_items == self.capacity
        
    def get_capacity(self):
        """this is the maximum number of a entries the heap can hold, which is one less
        than the number of entries that the Python List array allocated to hold the heap can hold"""
        return self.capacity
    
    def get_size(self):
        """the actual number of elements in the heap, not the capacity"""
        return self.num_items
        
    def perc_down(self, i):
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        if i==0:
            raise IndexError
        while i*2 <= self.num_items:
            c = i*2
            if i*2 != self.num_items and self.heap[i*2] < self.heap[i*2+1]:
                c += 1
            if self.heap[i] < self.heap[c]:
                self.heap[i], self.heap[c] = self.heap[c], self.heap[i]
            i = c

        
    def perc_up(self, i):
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while i//2>0:
            if self.heap[i] > self.heap[i//2]:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2

    def heap_sort_ascending(self, alist):
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, and mutate alist to put the items in ascending order"""
        self.build_heap(alist)
        i = len(alist)-1
        while i>=0:
            alist[i] = self.dequeue()
            i -= 1


