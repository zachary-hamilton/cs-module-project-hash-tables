class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.hash_table = [None] * capacity
        self.number_entries = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.hash_table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.number_entries / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        
        
        """
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211

        fnv_hash = FNV_offset_basis

        for each in key:
            fnv_hash *= FNV_prime 
            fnv_hash ^= ord(each)
        return fnv_hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        new_entry = HashTableEntry(key, value)
        hash_index = self.hash_index(key)
        
        new_entry.next = self.hash_table[hash_index]
        self.hash_table[hash_index] = new_entry
        self.number_entries += 1

        # resizing if necessary
        load_factor = self.get_load_factor()
        if load_factor > 0.7:
            new_capacity = self.capacity * 2
            self.resize(new_capacity)
        if load_factor < 0.2:
            new_capacity = max(8, self.capacity // 2)
            self.resize(new_capacity)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        hash_index = self.hash_index(key)
        self.hash_table[hash_index]
        # warning for if key is not found
        if self.hash_table[hash_index] == None:
            print('key not found')
            #return
        current = self.hash_table[hash_index]
        previous = None
        while current !=  None:
            if current.key == key:
                if previous == None:
                    self.hash_table[hash_index] = current.next
                else:
                    previous.next = current.next
                self.number_entries -= 1
                #return
            previous = current
            current = current.next
        print('key not found')
        #return

        # resizing if necessary
        load_factor = self.get_load_factor()
        if load_factor > 0.7:
            new_capacity = self.capacity * 2
            self.resize(new_capacity)
        if load_factor < 0.2:
            new_capacity = max(8, self.capacity // 2)
            self.resize(new_capacity)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        
        hash_index = self.hash_index(key)
        
        if self.hash_table[hash_index] == None:
            return self.hash_table[hash_index]
        else:
            current = self.hash_table[hash_index]
            while current != None:
                if current.key == key:
                    return current.value
                current = current.next
            return current




            return self.hash_table[hash_index].value
        
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # saving old hash table to rehash it later
        old_hash = self.hash_table

        # changing the capacity of the hash table
        self.capacity = new_capacity
                
        # rehashing
        self.hash_table = [None] * self.capacity
        for each in old_hash:
            current = each
            while current != None:
                new_entry = HashTableEntry(each.key, each.value)
                hash_index = self.hash_index(each.key)       
                new_entry.next = self.hash_table[hash_index]
                self.hash_table[hash_index] = new_entry              
                current = current.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
    woo = HashTable(8)

    woo.put("key-0", "val-0")
    woo.put("key-1", "val-1")
    woo.put("key-2", "val-2")
    woo.put("key-3", "val-3")
    woo.put("key-4", "val-4")
    woo.put("key-5", "val-5")
    woo.put("key-6", "val-6")
    woo.put("key-7", "val-7")
    woo.put("key-8", "val-8")
    woo.put("key-9", "val-9")
    woo.resize(1024)
    print(f'number slots: {woo.get_num_slots()}')