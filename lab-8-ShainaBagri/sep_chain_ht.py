
class MyHashTable:

    def __init__(self, table_size=11):
        self.table_size = table_size
        self.hash_table = [[] for _ in range(table_size)] # List of lists implementation
        self.num_items = 0
        self.num_collisions = 0

    def insert(self, key, value):
        "Takes a key, and an item.  Keys are valid Python non-negative integers. \
        The function will insert the key-item pair into the hash table based on the \
        hash value of the key mod the table size (hash_value = key % table_size)"
        tup = (key, value)
        if self.load_factor()>1.5:
            self.resize()
        inserted = False
        x = self.hash_table[key % self.table_size]
        for i in range(len(x)):
            if (x[i])[0]==key:
                x[i] = tup
                inserted = True
        if not inserted:
            if x != []:
                self.num_collisions += 1
            x.append(tup)
            self.num_items += 1

    def resize(self):
        self.table_size = self.table_size*2+1
        newhash = [[] for _ in range(self.table_size)]
        for i in self.hash_table:
            for j in i:
                tup = (j[0], j[1])
                newhash[j[0] % self.table_size].append(tup)
        self.hash_table = newhash

    def get_item(self, key):
        "Takes a key and returns the item from the hash table associated with the key. \
        If no key-item pair is associated with the key, the function raises a LookupError exception."
        for i in self.hash_table[key % self.table_size]:
            if i[0]==key:
                return i[1]
        raise LookupError

    def remove(self, key):
        "Takes a key, removes the key-item pair from the hash table and returns the key-item pair. \
        If no key-item pair is associated with the key, the function raises a LookupError exception. \
        (The key-item pair should be returned as a tuple)"
        x = self.hash_table[key % self.table_size]
        for i in range(len(x)):
            if key==(x[i])[0]:
                ans = x[i]
                self.hash_table = self.hash_table[:i] + self.hash_table[i+1:]
                self.num_items -= 1
                return ans
        raise LookupError


    def load_factor(self):
        "Returns the current load factor of the hash table"
        return self.num_items/self.table_size

    def size(self):
        "Returns the number of key-item pairs currently stored in the hash table"
        return self.num_items

    def collisions(self):
        "Returns the number of collisions that have occurred during insertions into the hash table"
        return self.num_collisions
