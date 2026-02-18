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





head = node1



print(node1.val)
print(node2.val)
print(node3.val)
print(node4.val)
print(node5.val)
print(node6.val)

