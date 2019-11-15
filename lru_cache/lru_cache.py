# ### LRU Cache
# An LRU (Least Recently Used) cache is an in-memory storage structure that adheres to the 
# [Least Recently Used](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)) 
# caching strategy. 

# In essence, you can think of an LRU cache as a data structure that keeps track of the order 
# in which elements (which take the form of key-value pairs) it holds are added and updated. 
# The cache also has a max number of entries it can hold. This is important because once the 
# cache is holding the max number of entries, if a new entry is to be inserted, another 
# pre-existing entry needs to be evicted from the cache. Because the cache is using a 
# least-recently used strategy, the oldest entry (the one that was added/updated the 
# longest time ago) is removed to make space for the new entry. 

# So what operations will we need on our cache? We'll certainly need some sort of `set` 
# operation to add key-value pairs to the cache. Newly-set pairs will get moved up the 
# priority order such that every other pair in the cache is now one spot lower in the 
# priority order that the cache maintains. The lowest-priority pair will get removed from 
# the cache if the cache is already at its maximal capacity. Additionally, in the case 
# that the key already exists in the cache, we simply want to overwrite the old value 
# associated with the key with the newly-specified value. 

# We'll also need a `get` operation that fetches a value given a key. When a key-value 
# pair is fetched from the cache, we'll go through the same priority-increase dance 
# that also happens when a new pair is added to the cache.

# Note that the only way for entries to be removed from the cache is when one needs to
#  be evicted to make room for a new one. Thus, there is no explicit `remove` method. 

# Given the above spec, try to get a working implementation that passes the tests. What 
# data structure(s) might be good candidates with which to build our cache on top of? 
# Hint: Since our cache is going to be storing key-value pairs, we might want to use a
# structure that is adept at handling those. 

# ---

# Once you've gotten the tests passing, it's time to analyze the runtime complexity of 
# your `get` and `set` operations. There's a way to get both operations down to sub-linear 
# time. In fact, we can get them each down to constant time by picking the right data structures to use. 

# Here are you some things to think about with regards to optimizing your implementation: 
# If you opted to use a dictionary to work with key-value pairs, we know that dictionaries 
# give us constant access time, which is great. It's cheap and efficient to fetch pairs. 
# A problem arises though from the fact that dictionaries don't have any way of remembering 
# the order in which key-value pairs are added. But we definitely need something to remember 
# the order in which pairs are added. Can you think of some ways to get around this constraint?

from doubly_linked_list import DoublyLinkedList

class LRUCache:

    def __init__(self, limit=10):
        
        # keeps track of the max number of nodes it can hold
        self.limit = limit

        # the current number of nodes it is holding
        self.size = 0
        
        # a doubly-linked list that holds the key-value entries in the correct order
        self.order = DoublyLinkedList()
        
        # storage dict that provides fast access to every node stored in the cache
        self.storage = dict()
        
        


    def get(self, key):
        
        # Retrieves the value associated with the given key
        if key in self.storage:
            node = self.storage[key]
            # needs to move the key-value pair to the end of the order
            # such that the pair is considered most-recently used.
            self.order.move_to_end(node)
            # Returns the value associated with the key
            return node.value[1]
        else:
            # Return None if the key-value pair doesn't exist in the cache
            return None


    def set(self, key, value):
        
        # if key already exists in the cache
        if key in self.storage:
            # overwrite the old value associated with the key with the newly-specified value
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return

        # If the cache is already at max capacity.
        if self.size == self.limit:
            #oldest entry in the cache needs to be removed
            del self.storage[self.order.head.value[0]]
            self.order.remove_from_head()
            self.size += 1

        # Adds the given key-value pair to the cache.
        # newly-added pair should be considered the most-recently used entry in the cache
        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
        self.size += 1
