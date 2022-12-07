#!/usr/bin/env python3

import bt
import sys
import logging

log = logging.getLogger(__name__)


class BST(bt.BT):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(BST(), BST())

    def is_member(self, v):
        '''
        Returns true if the value `v` is a member of the tree.
        '''

        if self.is_empty():
            return False
        if self.value() == v:
            return True
        if self.value() < v:
            return self.rc().is_member(v)
        else:
            return self.lc().is_member(v)
        return False

    def size(self):
        '''
        Returns the number of nodes in the tree.
        '''

        if self.is_empty():
            return 0
        else:
            left = self.lc().height()
            right = self.rc().height()
            return 1 + left + right

        return 0

    def height(self):
        '''
        Returns the height of the tree.
        '''

        if self.is_empty():
            return 0
        else:
            l = self.lc().height()
            r = self.rc().height()
            return 1 + max(l, r)

    def preorder(self):
        '''
        Returns a list of all members in preorder.
        '''
        if self.is_empty():
            return []
        return [self.value()] + self.lc().preorder() + self.rc().preorder()

    def inorder(self):
        '''
        Returns a list of all members in inorder.
        '''

        if self.is_empty():
            return []
        else:
            return self.lc().inorder() + [self.value()] + self.rc().inorder()

    def postorder(self):
        '''
        Returns a list of all members in postorder.
        '''

        if self.is_empty():
            return 0
        else:
            return self.lc().inorder() + self.rc().inorder() + [self.value()]



    def none_fix(self, arr):
        '''
        Inserts None to make it possible to print a full tree to the bottom.
        Like the example in bfs_order_star
        '''
        counter = 0
        for i in range(0, self.height()):
            for j in range(0, 2**i):
                if len(arr) > counter and arr[counter] == None:
                    arr.insert((counter*2)+1, None)
                    arr.insert((counter*2)+2, None)
                counter += 1
        while(len(arr) > (2**self.height()-1)):
            arr.pop()

        return arr
    

    def bfs_order_star(self):
        '''
        Returns a list of all members in breadth-first search* order, which
        means that empty nodes are denoted by "stars" (here the value None).

        For example, consider the following tree `t`:
                    10
              5           15
           *     *     *     20

        The output of t.bfs_order_star() should be:
        [ 10, 5, 15, None, None, None, 20 ]
        '''
        
        if self.is_empty():
            return []
        
        #
        temp_queue = []
        arr = []
        temp_queue.append(self)
        
        
        while(len(temp_queue) > 0):
            arr.append(temp_queue[0].value()) #stores values of nodes in queue
            parent = temp_queue.pop(0)
            
            
            #Stores left node in queue if its not None
            if parent.lc() is not None:
                temp_queue.append(parent.lc())
                
            #Stores right node in queue if its not None
            if parent.rc() is not None:
                temp_queue.append(parent.rc())
        
        

        
        return self.none_fix(arr)

    def add(self, v):
        '''
        Adds the value `v` and returns the new (updated) tree.  If `v` is
        already a member, the same tree is returned without any modification.
        '''
        if self.is_empty():
            self.__init__(value=v)
            return self
        if v < self.value():
            return self.cons(self.lc().add(v), self.rc())
        if v >= self.value():
            return self.cons(self.lc(), self.rc().add(v))
        return self
    
    def minimum(self):
        '''
        Minimum node of tree
        '''
        if self.lc() is None:
            return self
        else:
            return self.lc().minimum()
    
    

    def delete(self, v):
        '''
        Removes the value `v` from the tree and returns the new (updated) tree.
        If `v` is a non-member, the same tree is returned without modification.
        '''
        #if it is a leaf node, in other words if the node has no children
        if not self.is_member(v):
            return self
        if v < self.value():
            self.lc().delete(v)
        elif v > self.value():
            self.rc().delete(v)
            
        #if the node has 1 or more children
        else:
            if self.lc().is_empty():
                self.set_value(self.rc().value())
                return self.rc().set_value(None)
            elif self.rc().is_empty():
                self.set_value(self.lc().value())
                return self.lc().set_value(None)
            
            tmp = self.rc().min_value_node()
            self.set_value(tmp.value())
            self.rc().delete(tmp.value())
                
        return self       
        
        
        
    def min_value_node(self):
        '''
        traverse left in the tree until NULL and returns the
        last node that has a value
        '''
        
        if self.lc().value() is not None:
            return self.lc().min_value_node()
        else:
            return self

    def max_value_node(self):
        '''
        Traverse right in the tree until NULL and returns the
        last node that has a value
        '''
        
        
        if self.rc().value() is not None:
            return self.rc().max_value_node()
        else:
            return self   
                
            
        
      


if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
