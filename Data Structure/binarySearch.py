#defining a node structure
class Node:
    def __init__ (self,key):
        self.left = None
        self.right = None
        self.val = key


#inserting values to the node
def insert(root,node):
    if root is None:
        root = node
        #if node does not have any values then assign new at very first position
    else:
        #comparing the root value to insert the new node in left/right
        if root.val < node.val:
            #if the right node is empty else recursively call the insert function
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            #if the left node is empty else recursively call the insert function
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
        #these are we doing to add new element at the leaf/last position

    
#inorder tree traversal
#  LEFT  VAL  RIGHT   (LVR)
#inorder traversal always gives you assinding order
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

#Main 
r=int(input("Enter the root element :- "))
n = Node(r)
r=int(input("how many nodes do you want to add :- "))
for i in range(r):
    l=int(input("Enter Non-repetative Number:- "))
    insert(n,Node(l))

inorder(n)

