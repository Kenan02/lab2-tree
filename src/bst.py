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



    def noneroot(self, index, size):
        exclusion = []
        left_child = right_child = index

        while left_child <= size:
            exclusion.append(left_child)
            left_child = (2 * left_child) + 1

        while right_child <= size:
            exclusion.append(right_child)
            right_child = (2 * right_child) + 2

        return exclusion


    def bfs_lista(self):
        queue = []
        temp = []

        queue.append(self)

        while(len(queue) > 0):
            temp.append(queue[0])
            node = queue.pop(0)

            if not node.lc().is_empty():
                queue.append(node.lc())

            if not node.rc().is_empty():
                queue.append(node.rc())

        return temp

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
        else:
            total = ((2**self.height()) - 1)


            tree = self.bfs_lista()
            bfsqueue = [None] * total
            exclusion = []

            for i in range(total):
                if i not in exclusion:
                    if len(tree) > 0:
                        node = tree.pop(0)
                        bfsqueue = node.value()

                        if node.lc().is_empty():
                            i_left = (2 * i) + 1
                            exclusion += self.noneroot(i_left, total)

                        if node.rc().is_empty():
                            i_right = (2 * i) + 2
                            exclusion += self.noneroot(i_right, total)

        return bfsqueue

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
        if v > self.value():
            return self.cons(self.lc(), self.rc().add(v))
        return self

    def delete(self, v):
        '''
        Removes the value `v` from the tree and returns the new (updated) tree.
        If `v` is a non-member, the same tree is returned without modification.
        '''
        log.info("TODO@src/bst.py: implement delete()")
        return self


if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
