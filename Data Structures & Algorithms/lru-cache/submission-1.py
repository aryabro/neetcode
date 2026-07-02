class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val # each node contains
        self.next = self.prev = None # pointers for doubly linked list

class LRUCache:
    """
    Pattern: Hash Map + Doubly Linked List.
    
    Key idea:
    - Hash map gives O(1) access to nodes by key.
    - Doubly linked list tracks usage order.
    - Left side (head) is least recently used.
    - Right side (tail) is most recently used.

    Reason for hashmap:
    If a key exists in the hashmap, its node exists in the linked list,
    so we can remove it, update it, or move it to the MRU position in O(1).

    We use dummy head and tail nodes to avoid edge cases when inserting
    or removing nodes from the beginning/end of the list.

    Time: get and put in O(1)
    Space: O(capacity), because we store at most capacity nodes.
    """
    def __init__(self, capacity: int):
        self.cap = capacity
        # Maps key -> node in the doubly linked list.
        # This lets us find and update any node in O(1).
        self.cache = {}
        
        # Dummy boundary nodes:
        # head <-> ... <-> tail
        # LRU              MRU
        # basically, add new elements to tail
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node):
        
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = node.next, node.prev

    def insert(self, node):
        # Insert node right before tail.
        # Since tail side represents MRU, this marks node as most recently used.
        prev, nxt = self.tail.prev, self.tail
        prev.next, nxt.prev = node, node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:     
        # if key exists in cache, we must return value and update it as MRU
        if key in self.cache:
            node = self.cache[key]
            # Move node to MRU
            self.remove(node)
            self.insert(node)

            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove node from linked list as it's used recently
            self.remove(self.cache[key])
        
        # add/update value and cache
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # check if len(cache) increases cap as we added new key
        if len(self.cache) > self.cap:
            # get node of lru and delete it
            lru = self.head.next
            self.remove(lru)
            # update the cache
            del self.cache[lru.key]

