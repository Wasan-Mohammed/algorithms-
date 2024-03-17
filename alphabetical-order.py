#BST=binary search tree
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

def inorder_traversal(root):
    result =[]
    if root:
        result += inorder_traversal(root.left)
        result.append(root.key)
        result += inorder_traversal(root.right)
    return result

words=["oenology","phrenology","campaology","ornithology","ichthyology","limnology","alchemy","astrology"]
#create a BST and insert the words
root = None
for word in words:
    root = insert(root, word)

sorted_words = inorder_traversal(root)
#Display the sorted words
print("Sorted Words: ",sorted_words)
