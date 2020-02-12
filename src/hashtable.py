# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0
        # print(self.storage)


    def _hash(self, key):

        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):

        return self._hash(key) % self.capacity


    def insert(self, key, value):

        hashed_index = self._hash_mod(key)
        current = self.storage[hashed_index]
        depth = 0
        def adder(node = self.storage[hashed_index]):
            nonlocal current
            nonlocal depth
            if node == None:
                # print(f'current:  {current}')
                self.storage[hashed_index] = LinkedPair(key, value)
                depth =+ 1
                # print('break')
                # print(self.storage)
                return
            elif node == None and depth > 0:
                # print(f'current:  {current}')
                current.next = LinkedPair(key, value)
                # print('break')
                # print(self.storage)
                return
            else:
                # print('branch')
                # print(f'node_next:  {node.next}')
                current = node
                adder(node.next)
        # print(f'this one here: {self.storage}')
        return adder()



    def remove(self, key):

        hashed_index = self._hash_mod(key)
        current = self.storage[hashed_index]
        depth = 0
        def search(node = self.storage[hashed_index]):
            nonlocal depth
            nonlocal current
            if node == None:
                print('Error, no value found for this key')
                return
            elif node.key == key and node.next != None and depth == 0:
                self.storage[hashed_index] = node.next
                self.count -= 1
                return
            elif node.key == key and node.next != None and depth > 0:
                current.next = node.next
                self.count -= 1
                print(depth)
                return
            elif node.key == key and node.next == None and depth > 0:
                current.next = None
                self.count -= 1
                print(depth)
                return
            elif node.key == key and node.next == None and depth == 0:
                self.storage[hashed_index] = None
                self.count -= 1
                # print(depth)
                return
            elif self.storage[hashed_index].key != key and self.storage[hashed_index].next != None:
                current = node
                depth =+ 1
                search(node.next)
                return
        # print(f'After remove: {self.storage}')
        return search()
 



    def retrieve(self, key):

        hashed_index = self._hash_mod(key)

        def search(node):
            if node == None:
                return None
            elif node.key == key:
                return node.value
            else: 
                search(node.next)
        return search(self.storage[hashed_index])



    def resize(self):
        new_storage = self.storage * 2
        for i in self.storage:
            print(new_storage)
            
        

test = HashTable(20)
test.insert('a', 1)
test.insert('b', 2)
test.insert('c', 3)
test.insert('d', 4)
test.insert('e', 5)
print(f'just printing: {test.retrieve("a")}')
# test.insert('f', 6)
# test.insert('g', 7)
# test.insert('h', 8)
# test.insert('i', 9)
# test.insert('j', 10)
# test.insert('k', 11)
# test.insert('l', 12)
# test.insert('m', 13)
# test.insert('n', 14)
# test.insert('o', 15)
# test.insert('p', 16)
# test.insert('q', 17)
# test.insert('r', 18)
# test.insert('s', 19)
# test.insert('t', 20)
# test.insert('u', 21)
# test.insert('v', 22)
# test.insert('w', 23)
# test.insert('x', 24)
# test.insert('y', 25)
# test.insert('z', 26)
print("****", test.storage)
test.remove('a')
print("****", test.storage)
# test.remove('c')
# test.remove('d')




# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

