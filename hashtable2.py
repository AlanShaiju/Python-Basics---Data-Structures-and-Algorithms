# implement chaining in hahtables
# we initialize an individual array as each element in the array
# The enumerate() function in Python is used to iterate over a sequence 
# (like a list, tuple, or string) while keeping track of both the 
# index and the corresponding value. It returns an enumerate object, 
# which can be converted to a list of tuples, 
# where each tuple contains the index and the value.

class HashTable:
    def __init__(self):
        self.MAX=10
        self.arr=[[] for i in range(self.MAX)]
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.MAX
    def __setitem__(self,key,value):
        h=self.get_hash(key)
        found=False
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx]=(key,value)
                found=True
                break
        # if key not present in hashtable then do the following:
        if not found:
            self.arr[h].append((key,value))   
    def __getitem__(self,key):
        h=self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]
    def __delitem__(self,key):
        h=self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][idx]
                
        
t=HashTable()
t['march 6']=123
t['march 17']=345
t['march 19']=567
print(t.arr)
print(t['march 17'])
del t['march 17']
print(t.arr)