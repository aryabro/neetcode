class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        # cache is a dict that points to location in doubly linked list
        self.cache = {}
        
        # head <----> tail
        # LRU          MRU
        # basically, add new elements to tail
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = node.next, node.prev

    def insert(self, node):
        # insertion is only done through tail(i.e. dummy_node) here as we insert MRU
        prev, nxt = self.tail.prev, self.tail
        prev.next, nxt.prev = node, node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:     
        if key in self.cache:
            # update the cache with new MRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            # go through the key in cache to the node and return its value
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove node from
            self.remove(self.cache[key])
        
        # add Node to cache accessed through key if it doesn't exist
        # if it exists, the Node at key is updated
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # check if len(cache) increases cap as we added new key
        if len(self.cache) > self.cap:
            # get node of lru and delete it
            lru = self.head.next
            self.remove(lru)
            # update the cache
            del self.cache[lru.key]

