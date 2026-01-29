from numpy.f2py.rules import check_rules


class node:
    def __init__(self,val):
        self.val = val
        self.next = None


node1  = node(5)
node2  = node(4)
node3  = node(7)
node4  = node(87)
node5 = node(54)
node6 = node(98)




node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6




print(node1.val)
print(node2.val)
print(node3.val)
print(node4.val)
print(node5.val)
print(node6.val)
head = node1

# currunt = head
#
# while currunt.next is not None:
#     currunt = currunt.next
# head = currunt
#
#
# print("new head",head.val)

prev = None
temp = head

while temp is not None:
    front = temp.next
    temp.next = prev
    prev = temp
    temp = front
head = prev

print("ye leeeeee",head.val)
print(head.next.val)

