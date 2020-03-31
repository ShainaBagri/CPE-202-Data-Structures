class HashTable:

    def __init__(self, table_size=191):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value):
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        When used with the concordance, value is a Python List of line numbers.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""
        x = 0
        hash = self.horner_hash(key)
        pos = hash
        inserted = False
        while not inserted and self.hash_table[pos] is not None:
            if (self.hash_table[pos])[0] == key:
                self.hash_table[pos] = (key, value)
                inserted = True
            x += 1
            pos = hash + (x * x)
            pos = pos % self.table_size
        if not inserted:
            self.hash_table[pos] = (key, value)
            self.num_items += 1
        if self.get_load_factor() > 0.5:
            self.resize()

    def resize(self):
        tmp = []
        self.table_size = self.table_size*2+1
        for i in self.hash_table:
            if i is not None:
                tmp.append((i[0], i[1]))
        self.hash_table = [None]*self.table_size
        for i in tmp:
            self.insert(i[0], i[1])
            self.num_items -= 1

    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        n = min(len(key), 8)
        hash = 0
        i = 0
        while i<n:
            hash += (ord(key[i])*(31**(n-1-i)))
            i += 1
        return hash % self.table_size

    def retrieval(self, key):
        #returns tuple (index, value) of key
        x = 0
        hash = self.horner_hash(key)
        pos = hash
        while self.hash_table[pos] is not None:
            if (self.hash_table[pos])[0] == key:
                tup = (pos, (self.hash_table[pos])[1])
                return tup
            x += 1
            pos = hash + (x * x)
            pos = pos % self.table_size
        return None

    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise."""
        return self.retrieval(key) is not None

    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None."""
        tup = self.retrieval(key)
        if tup is not None:
            return tup[0]
        return None

    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        lis = []
        for i in self.hash_table:
            if i is not None:
                lis.append(i[0])
        return lis

    def get_value(self, key):
        """ Returns the value (list of line numbers) associated with the key. 
        If key is not in hash table, returns None."""
        tup = self.retrieval(key)
        if tup is not None:
            return tup[1]
        return None

    def get_num_items(self):
        """ Returns the number of entries (words) in the table."""
        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items/self.table_size