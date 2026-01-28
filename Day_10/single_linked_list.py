from selenium.webdriver.support.expected_conditions import none_of
from sqlalchemy import false


class Node:
    def __init__(self,val):
        self.val=  val
        self.next = None


class singlylinklist:
    def __init__(self):
        self.head = None


    def append(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def traversal(self):
        if self.head is None:
            print("list is empty")

        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end = " ")
                curr = curr.next
            print()


    def insert(self,position,val):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            currunt = self.head
            pre = None
            count = 0

            while currunt is not None and count < position:
                pre = currunt
                currunt = currunt.next
                count+=1
            pre.next = new_node
            new_node.next = currunt
    def delete(self,val):
        temp = self.head
        if temp.next is not None:
            if temp.val == val:
                self.head = temp.next
                return
            else:
                found = False
                prev = None
                while temp is not None:
                    if temp.val == val:
                        found = True
                        break
                    prev = temp
                    temp = temp.next


                if found:
                    prev.next = temp.next
                    return
                else:
                    print("node not found")










all = singlylinklist()
all.append(45)
all.append(89)
all.append(87)
all.append(87)
all.append(99)

all.traversal()