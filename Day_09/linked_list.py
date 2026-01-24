class node:
    def __init__(self,val):
        self.val = val
        self.next = None


node1  = node(5)
node2  = node(4)
node3  = node(7)
node4  = node(87)


print(node1.val)

node1.next = node2
node2.next = node3
node3.next = node4

print(node1.next.next.val)