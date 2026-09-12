class node:
    def __init__(self, data):
        self.data =data
        self.next=None

a=node(5)  
b=node(10)   
c=node(15)   
d=node(20)

a.next=b
b.next=c
c.next=d

head=a
temp=head
while temp is not None:
    print(temp.data)
    temp=temp.next

temp=head
while temp.next.data !=15:
    temp=temp.next
temp.next=temp.next.next

temp=head
print("after deletion of 15")

while temp is not None:
    print(temp.data)
    temp =temp.next
