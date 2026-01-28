from numpy.ma.core import append
from selenium.webdriver.support.expected_conditions import none_of


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class singlylinkedlist:

    def __init__(self):
        self.head = None



    def append(self,val):
        new_node =  Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next =  new_node


    def traversal(self):
        if self.head is None:
            print("list is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val,end=" ")
                curr  = curr.next
            print()


ss = singlylinkedlist()
# ss.traversal()
ss.append(54)
ss.append(58)
ss.append(96)

ss.traversal()

