class Node:
    """Node for use with doubly-linked list"""
    def __init__(self, item, next=None, prev=None):
        self.item = item  # item held by Node
        self.next = next  # reference to next Node
        self.prev = prev  # reference to previous Node

class OrderedList:
    """A doubly-linked ordered list of integers, 
    from lowest (head of list, sentinel.next) to highest (tail of list, sentinel.prev)"""
    def __init__(self, sentinel=None):
        """Use only a sentinel Node. No other instance variables"""
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def is_empty(self):
        return self.sentinel.next==self.sentinel

    def add(self, item):
        """Adds an item to OrderedList, in the proper location based on ordering of items
        from lowest (at head of list) to highest (at tail of list)
        If item is already in list, do not add again (no duplicate items)"""
        newnode = Node(item)
        cur = self.sentinel
        while cur.next != self.sentinel and cur.next.item < item:
            cur = cur.next
        if cur.next.item != item:
            newnode.next = cur.next
            newnode.prev = cur
            cur.next.prev = newnode
            cur.next = newnode

    def remove(self, item):
        """Removes an item from OrderedList. If item is removed (was in the list) returns True
        If item was not removed (was not in the list) returns False"""
        cur = self.sentinel
        while cur.next != self.sentinel and cur.next.item <= item:
            cur = cur.next
        if cur.item == item:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            return True
        return False

    def index(self, item):
        """Returns index of an item in OrderedList (assuming head of list is index 0).
        If item is not in list, return None"""
        ind = -1
        cur = self.sentinel
        while cur.next != self.sentinel and cur.next.item <= item:
            cur = cur.next
            ind += 1
        if cur.item == item:
            return ind
        return None

    def pop(self, index):
        """Removes and returns item at index (assuming head of list is index 0).
        If index is negative or >= size of list, raises IndexError"""
        if index < 0 or index >= self.size():
            raise IndexError
        ind = -1
        cur = self.sentinel
        while ind<index:
            cur = cur.next
            ind += 1
        item = cur.item
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        return item

    def search(self, item):
        """Searches OrderedList for item, returns True if item is in list, False otherwise"""
        return self.h_search(self.sentinel.next, item)

    def h_search(self, node, item):
        #helper function for search
        if node is self.sentinel:
            return False
        if node.item == item:
            return True
        return self.h_search(node.next, item)

    def python_list(self, node=None):
        """Return a Python list representation of OrderedList, from head to tail
        For example, list with integers 1, 2, and 3 would return [1, 2, 3]"""
        if node is None:
            node = self.sentinel.next
        if node is self.sentinel:
            return []
        return [node.item] + self.python_list(node.next)

    def python_list_reversed(self):
        """Return a Python list representation of OrderedList, from tail to head, using recursion
        For example, list with integers 1, 2, and 3 would return [3, 2, 1]"""
        return self.h_python_list_reversed(self.sentinel.next)

    def h_python_list_reversed(self, node):
        #helper function for python_list_reversed
        if node is self.sentinel:
            return []
        return self.h_python_list_reversed(node.next) + [node.item]

    def size(self):
        """Returns number of items in the OrderedList"""
        return self.h_size(self.sentinel.next, 0)

    def h_size(self, node, cnt):
        #helper function for size
        if node is self.sentinel:
            return cnt
        return self.h_size(node.next, cnt+1)
