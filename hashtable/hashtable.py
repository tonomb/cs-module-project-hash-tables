class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'HashTableEntry({self.key, self.value, self.next})'


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 2


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):   # The capacity is the number of buckets in the hash table
        if capacity < MIN_CAPACITY:
            self.capacity =  MIN_CAPACITY
        else:
            self.capacity = capacity  
        
        self.table = [None] * capacity 
        self.count = 0 


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):   # The load factor is a measure of how full the hash table is allowed to get before its capacity is automatically increased.
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        load_factor = self.count / self.capacity
        return load_factor


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        FNV_prime = 1099511628211 # 64-bit
        offset_basis = 14695981039346656037 # 64 bit offset_basis

        hash = offset_basis
        for b in key:
            hash *= FNV_prime
            hash ^= ord(b)
        
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        return key


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # new entry
        entry = HashTableEntry(key, value)
        
        # get the index of the key 
        index = self.hash_index(key)
        # if index is empty add the entry 
        if self.table[index] is None:
            self.table[index] = entry
            self.table[index].head = entry
            self.count += 1
            return

        # search for value 
        cur = self.table[index].head

        while cur is not None:
           # if key already exists 
            if cur.key == entry.key:
                #overwrite value
                cur.value = entry.value
                return
            # else insert new entry at head
            else:
                entry.next = self.table[index].head
                self.table[index] = entry
                self.table[index].head = entry  

            cur = cur.next              

        # print(self.table)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        entry = self.table[index]
        if entry.key == key:
            self.table[index] = None
            self.count -= 1
        else:
            return f'key not found'


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # get the index for the key
        index = self.hash_index(key)
        # pointer to head at current index
        cur = self.table[index].head
        # print('head' , cur)
        while cur is not None:
            # print(cur.key, key)
            if cur.key == key:
                # print('same')
                return cur.value

            cur = cur.next

        return None


    def resize(self, new_capacity):   # When the number of entries in the hash table exceeds the product of the load factor and the current capacity, the hash table is rehashed (that is, internal data structures are rebuilt) so that the hash table has approximately twice the number of buckets.
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(2)

    # print(ht.get_num_slots())
    # print(ht.get_load_factor())
    # print(ht.hash_index('Antonio'))
    # print(ht.table)

    # ht.put("key-0", "val-0")
    ht.put('one', 1)
    # print(ht.get("one"))
    ht.put('two', 2)
    # print(ht.get("two"))
    ht.put('two', 2.2)
    # print(ht.get("two"))
    # print(ht.get("one"))
    
    # ht.put("line_1", "'Twas brillig, and the slithy toves")
    # ht.put("line_2", "Did gyre and gimble in the wabe:")
    # ht.put("line_3", "All mimsy were the borogoves,")
    # ht.put("line_4", "And the mome raths outgrabe.")
    # ht.put("line_5", '"Beware the Jabberwock, my son!')
    # ht.put("line_6", "The jaws that bite, the claws that catch!")
    # ht.put("line_7", "Beware the Jubjub bird, and shun")
    # ht.put("line_8", 'The frumious Bandersnatch!"')
    # ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")

    # print(ht.table)
    # ht.put("key-0", "new-val-0")
    # print(ht.get("key-0"))


    # print(ht.get('line_12'))

    # # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")
