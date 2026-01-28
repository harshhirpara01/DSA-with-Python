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
# temp = head
# count = 0
# while temp is not None:
#     temp = temp.next
#     count +=1
#
#
# lcount = 0
# temp = head
# while True:
#
#     temp = temp.next
#     lcount +=1
#     if lcount == count//2:
#         print("le madar chod ",temp.val)
#         break
#
slow = head
fast = head

while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

print(slow.val)