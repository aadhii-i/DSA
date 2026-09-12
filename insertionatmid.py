class node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = node(5)
b = node(10)
c = node(15)
a.next=b
b.next=c
head=a
temp=head
while temp is not None:
    print(temp.data)
    temp=temp.next

temp=head
while temp.data!=10:
    temp=temp.next
d=node(12)
d.next=temp.next
temp.next=d
temp=head
print ("after insertion at intervel")
while temp is not None:
    print(temp.data)
    temp=temp.next


