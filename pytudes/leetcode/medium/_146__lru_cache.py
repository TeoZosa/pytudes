"""https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints of a
Least Recently Used (LRU) cache.

Constraints:
    - 1 ≤ capacity ≤ 3000
    - 0 ≤ key ≤ 3000
    - 0 ≤ value ≤ 104
    - At most 3 * 10**4 calls will be made to get and put.

Examples:
    >>> lRUCache = LRUCache(capacity=2)
    >>> lRUCache.put(key=1, value=0) # cache is {1=0}
    >>> lRUCache.get(key=1)
    0
    >>> lRUCache.put(key=1, value=1) # LRU key was 1, overwrites value at key 1, cache is {1=1}
    >>> lRUCache.put(key=2, value=2) # cache is {1=1, 2=2}
    >>> lRUCache.get(key=1)
    1
    >>> lRUCache.put(key=3, value=3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    >>> lRUCache.get(key=2)
    -1
    >>> lRUCache.put(key=4, value=4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    >>> lRUCache.get(key=1)
    -1
    >>> lRUCache.get(key=3)
    3
    >>> lRUCache.get(key=4)
    4

"""


class DoublyLinkedListNode:
    """Doubly-linked list node

    Attributes:
        key: unique key associated with a DoublyLinkedListNode instance
        val: value associated the key
        prev: [optional] predecessor node
        next: [optional] successor node
    """

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    """Emulates an LRU cache,

    Internally, LRUCache uses a hashmap and doubly-linked list for efficient
    cache insertions, deletions, and updates.

    Complexity:
        n = capacity of cache
        Time:
            get: O(1)
            put: O(1)
        Space: O(n) (2n: n for the hash table, n (+2: dummy head and tail) for the linked list)

    Attributes:
        capacity:
            an integer indicating how many entries the cache can store
            before an entry must be evicted
        cache:
            a dictionary mapping keys to cache Nodes
        head:
            a dummy DoublyLinkedListNode used as a handle to the first (MRU) cache entry
        tail:
            a dummy DoublyLinkedListNode used as a handle to the last (LRU) cache entry

    """

    def __init__(self, capacity: int):
        """Inits LRUCache with designated capacity"""
        self.capacity = capacity
        self.cache: dict[int, DoublyLinkedListNode] = {}
        self.head = DoublyLinkedListNode("HEAD", None)
        self.tail = DoublyLinkedListNode("TAIL", None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """Returns the value of the cache entry corresponding to the given key

        Args:
            key: key of the cache entry to retrieve

        """
        if key not in self.cache:
            return -1

        cache_entry = self.cache[key]
        _remove_from_lru_list(cache_entry)
        self._make_mru(cache_entry)
        return cache_entry.val

    def _make_mru(self, cache_entry: DoublyLinkedListNode) -> None:
        """Moves given cache entry to the MRU position in the LRU list

        Implicitly right-shifting all other cache entries in the LRU list

        Args:
            cache_entry: entry which we are movign to the MRU position

        """
        cache_entry.prev, cache_entry.next = self.head, self.head.next

        old_lru_entry = self.head.next
        old_lru_entry.prev = self.head.next = cache_entry

    def put(self, key: int, value: int) -> None:
        """Inserts (key, value) item into cache

        Evicting the LRU entry if the cache's capacity will be exceeded.

        Args:
            key: key of item to insert
            value: value of item to insert

        """
        if key in self.cache:  # Updating existing entry
            cache_entry = self.cache[key]
            cache_entry.val = value
            _remove_from_lru_list(cache_entry)
        else:  # Adding new entry
            if len(self.cache) == self.capacity:  # Evict entry if at capacity
                lru_cache_entry = self.tail.prev
                del self.cache[lru_cache_entry.key]
                _remove_from_lru_list(lru_cache_entry)

            cache_entry = DoublyLinkedListNode(key, value)
            self.cache[key] = cache_entry

        self._make_mru(cache_entry)


def _remove_from_lru_list(cache_entry: DoublyLinkedListNode) -> None:
    """Removes a given node from its doubly-linked list

    Precondition: cache_entry's `prev` and `next` attributes are DoublyLinkedListNode instances

    Module-level function following guidance from https://google.github.io/styleguide/pyguide.html#217-function-and-method-decorators
    Namely:
        "Never use staticmethod unless forced to in order to integrate
        with an API defined in an existing library.
        Write a module level function instead."

    Args:
        cache_entry: cache entry which we must excise from the LRU list

    """
    predecessor_entry, successor_entry = cache_entry.prev, cache_entry.next
    predecessor_entry.next, successor_entry.prev = successor_entry, predecessor_entry
