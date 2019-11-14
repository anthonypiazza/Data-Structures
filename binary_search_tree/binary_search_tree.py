# ### Binary Search Trees
# * Should have the methods `insert`, `contains`, `get_max`.
#   * `insert` adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
#   * `contains` searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
#   * `get_max` returns the maximum value in the binary search tree.
#   * `for_each` performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value. 
#      There is a myriad of ways to perform tree traversal; in this case any of them should work. 

# ![Image of Binary Search Tree](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/300px-Binary_search_tree.svg.png)


import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # adds the input value to the binary search tree, 
    # adhering to the rules of the ordering of elements 
    # in a binary search tree   
    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else: 
                self.left.insert(value)

        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else: 
                self.right.insert(value)
        


        # if not self.left and not self.right:
        #     if value < self.value:
        #         self.left = BinarySearchTree(value)
        #     else: 
        #         self.right = BinarySearchTree(value)
        #     return              

        # elif value < self.value:
        #     while value < self.value:
        #         if self.left == None:
        #             self.left = BinarySearchTree(value)
        #         elif value >= self.value:
        #             self = self.right
        #         else:
        #             self = self.left

        #     if value < self.value:
        #         self.left = BinarySearchTree(value)
        #     else: 
        #         self.right = BinarySearchTree(value)
                
        # elif value > self.value:
        #     while value > self.value:
        #         if self.right == None:
        #             self.right = BinarySearchTree(value)
        #         elif value <= self.value:
        #             self = self.left
        #         else:
        #             self = self.right
        #     if value > self.value:
        #         self.right = BinarySearchTree(value)
        #     else: 
        #         self.left = BinarySearchTree(value)
        
        

    # searches the binary search tree for the input value, 
    # returning a boolean indicating whether the value 
    # exists in the tree or not.
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        # RECURSIVE SOLUTION 
        if self.value == target:
            return True
        
        if target < self.value:
            if not self.left:
                return False
            else: 
                return self.left.contains(target)
        
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)



        # ITERATIVE SOLUTION
        # contains = False
        # if target < self.value:
        #     while target < self.value:
        #         if self.left == None:
        #             return contains
        #         elif target > self.value:
        #             self = self.right
        #         elif target < self.value:
        #             self = self.left
        #         elif target == self.value:
        #             contains = True

        # elif target > self.value:
        #     while target > self.value:
        #         if self.right == None:
        #             return contains
        #         elif target < self.value:
        #             self = self.left
        #         elif target > self.value:
        #             self = self.right
        #         elif target == self.value:
        #             contains = True
        #     if target == self.value:
        #         contains = True
                
        # else:
        #     contains = True
        # return contains

    # Return the maximum value found in the tree
    def get_max(self):
        #RECURSIVE SOLUTION 1
        if not self.right:
            return self.value
        return self.right.get_max()

        # RECURSIVE SOLUTION 2
        # return self.right.get_max() if self.right else self.value

        # ITERATIVE SOLUTION 1
        # max = self.value
        # while self.right:
        #     if self.value < self.right.value:
        #         max = self.right.value
        #     self = self.right
        
        # return max
        

    # performs a traversal of _every_ node in the tree, 
    # executing the passed-in callback function on each 
    # tree node value. 
    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        
        if self.left:      
            self.left.in_order_print(self)
        print(self.value)
            # print(self.value)
        if self.right:
            self.right.in_order_print(self)
            # print(self.value)
        return
                

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
       
        queue.enqueue(node)
        while queue.storage.length > 0:
            node = queue.dequeue()
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)
            print(node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        while self.left or self.right:
            print(f"Self Value: {self.value}") 
            if self.left:
                self = self.left
            elif self.right:
                self = self.right


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
