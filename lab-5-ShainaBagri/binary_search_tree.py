from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other):
        return ((type(other) == TreeNode)
                and self.key == other.key
                and self.data == other.data
                and self.left == other.left
                and self.right == other.right
                )

    def __repr__(self):
        return ("TreeNode({!r}, {!r}, {!r}, {!r})".format(self.key, self.data, self.left, self.right))

class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

    def is_empty(self): # returns True if tree is empty, else False
        return self.root is None

    def search(self, key): # returns True if key is in a node of the tree, else False
        if self.is_empty():
            return False
        return self.search_h(key, self.root)

    #helper function for search recursion function
    def search_h(self, key, node):
        if key==node.key:
            return True
        if key<node.key and node.left is not None:
            return self.search_h(key, node.left)
        if key>node.key and node.right is not None:
            return self.search_h(key, node.right)
        return False

    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # Example creation of node: temp = TreeNode(key, data)
        newnode = TreeNode(key, data)
        insert = False
        node = self.root
        if node is None:
            self.root = newnode
            insert = True
        while(not insert):
            if key==node.key:
                node.data = data
                insert = True
            elif key<node.key:
                if node.left is None:
                    node.left = newnode
                    insert = True
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = newnode
                    insert = True
                else:
                    node = node.right

    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        return self.find_min_h(self.root)

    # helper function for find_min recursion function
    def find_min_h(self, node):
        if node.left is None:
            return (node.key, node.data)
        return self.find_min_h(node.left)

    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        return self.find_max_h(self.root)

    # helper function for find_max recursion function
    def find_max_h(self, node):
        if node.right is None:
            return (node.key, node.data)
        return self.find_max_h(node.right)

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.is_empty():
            return None
        return self.tree_height_h(self.root)

    # helper function for tree_height recursion function
    def tree_height_h(self, node):
        if node is None:
            return -1
        left = self.tree_height_h(node.left)
        right = self.tree_height_h(node.right)
        return 1 + max(left, right)

    def inorder_list(self, node=None, ans=[]): # return Python list of BST keys representing in-order traversal of BST
        if self.is_empty():
            return []
        left = False
        visit = False
        right = False
        if node is None:
            node = self.root
            ans = []
        if node.left is not None and not left:
            self.inorder_list(node.left, ans)
            left = True
        if not visit:
            ans.append(node.key)
            visit = True
        if node.right is not None and not right:
            self.inorder_list(node.right, ans)
            right = True
        return ans

    def preorder_list(self, node=None, ans=[]):  # return Python list of BST keys representing pre-order traversal of BST
        if self.is_empty():
            return []
        left = False
        visit = False
        right = False
        if node is None:
            node = self.root
            ans = []
        if not visit:
            ans.append(node.key)
            visit = True
        if node.left is not None and not left:
            self.preorder_list(node.left, ans)
            left = True
        if node.right is not None and not right:
            self.preorder_list(node.right, ans)
            right = True
        return ans
        
    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000)  # Don't change this!
        ans = []
        if self.is_empty():
            return []
        q.enqueue(self.root)
        while not q.is_empty():
            node = q.dequeue()
            ans.append(node.key)
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
        return ans