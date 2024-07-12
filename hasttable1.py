# This is to implement hash table in python

# we use dictionaries to implement hastables in python
#we retrive data with O(1) in hashtable/dictionary
#insertion and deletion is also O(1)
#we implement a dictionary using : myhastable={}
#function ord() is used tgo get the ASCII value for a specific character
# the function __setitem__() is used to add elements to the dictionary
# the function __getitem__() is used to retrieve data from the dictionary
class HashTable:
    def __init__(self):
        self.MAX=100
        self.arr=[None for i in range(self.MAX)]
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.MAX
    def __setitem__(self,key,value):
        h=self.get_hash(key)
        self.arr[h]=value
    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.arr[h]
    def __delitem__(self,key):
        h=self.get_hash(key)
        self.arr[h]=None
        
t=HashTable()
t['march 9']=130
t.__setitem__('march 1',240)
print(t.arr)
print(t.__getitem__('march 9'))