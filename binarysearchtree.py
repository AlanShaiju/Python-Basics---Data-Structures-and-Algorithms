class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):
        if data==self.data:
            return
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTreeNode(data)
    def inorder_traversal(self):
        elements=[]
        #visiting left tree
        if self.left:
            elements+=self.left.inorder_traversal()
        #visit base node
        elements.append(self.data)
        #visit right subtree
        if self.right:
            elements+=self.right.inorder_traversal()
        return elements
    def preorder_traversal(self):
        elements=[]
        #visit base node
        elements.append(self.data)
        #visiting left tree
        if self.left:
            elements+=self.left.inorder_traversal()
        #visit right subtree
        if self.right:
            elements+=self.right.inorder_traversal()
        return elements
    def postorder_traversal(self):
        elements=[]
        #visiting left tree
        if self.left:
            elements+=self.left.inorder_traversal()
        #visit right subtree
        if self.right:
            elements+=self.right.inorder_traversal()
        #visit base node
        elements.append(self.data)
        return elements
    def search(self,value):
        if self.data==value:
            return True
        if self.data>value:
            if self.left:
                return self.left.search(value)
            else:
                return False 
        if self.data<value:
            if self.right:
                return self.right.search(value)
            else:
                return False
    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()
    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()
    def find_sum(self):
        total=0
        if self.left:
            total+=self.left.find_sum()
        if self.right:
            total+=self.right.find_sum()
        total+=self.data
        return total
# implement find_min,find_max,calculate_sum


    

def buildtree(elements):
    root=BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
       
if __name__=='__main__':
    numbers=[23,45,67,2,3,5,98,65,76,43]
    numbers_tree=buildtree(numbers)
    print(numbers_tree.inorder_traversal())
    print(numbers_tree.preorder_traversal())
    print(numbers_tree.postorder_traversal())
    print(numbers_tree.search(5))
    print(numbers_tree.search(99))
    print(numbers_tree.find_max())
    print(numbers_tree.find_min())
    print(numbers_tree.find_sum())