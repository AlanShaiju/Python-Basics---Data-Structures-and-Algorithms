class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    def print(self):
        if self.head is None:
            print('Linked List is Empty')
            return
        itr=self.head
        llstr=''
        while itr:
            if itr.next== None:
                llstr+=str(itr.data)
            else:
                llstr+=str(itr.data)+'-->'
            itr=itr.next
        print(llstr)
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)  
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)
    def get_length(self):
        count=0
        iter=self.head
        while iter:
            count+=1
            iter=iter.next
        return count
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            print('Invalid Index')
            return
        if index == 0:
            self.head=self.head.next
            return
        count=0
        iter=self.head
        while iter:
            if count== index-1:
                iter.next=iter.next.next
                break
            iter=iter.next
            count+=1
    def insert_at(self,index,data):
        if index<0 or index>=self.get_length():
            print('Invalid Index')
            return
        if index==0:
            self.insert_at_begining(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
            
                  
if __name__== '__main__':
    ll=LinkedList()
    l=ll.get_length()
    print('Length of linked List:',l)
    ll.remove_at(1)
    ll.remove_at(-1)
    ll.insert_at_end(10)
    ll.insert_at_begining(5)
    ll.insert_at_begining(3)
    ll.insert_at_begining(2)
    ll.print()
    l=ll.get_length()
    print('Length of linked List:',l)
    ll.insert_at(2,88)
    ll.print()
    l=ll.get_length()
    print('Length of linked List:',l)
    ll.insert_at_begining(6)
    ll.insert_at_begining(0)
    ll.insert_at_end(9)
    ll.print()
    l=ll.get_length()
    print('Length of linked List:',l)
    ll.insert_values(['mango','apple','orange','grapes','cherry'])
    ll.print()
    l=ll.get_length()
    print('Length of linked List:',l)
    ll.remove_at(2)
    ll.print()
    ll.remove_at(20)       
    
    
    
    
    
# mylist=[123,345,567,789]
# mylist.insert(1,258)
# print(mylist)
#arrays store values in contigous memory locations
#linked list stores values in different memory locations using links
#linked lists have two componenets value and link the link part is used to point to 
#the next value while the value part has the value of element
#O(1) to insert and delete element at begining
#O(n) to insert/delete element at middle or end
#for linked list:
#no previously allocated space is necessary
#insertion is easier
#implementation: 