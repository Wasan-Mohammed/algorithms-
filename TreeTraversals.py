
class Node:
    def __init__(self, key):
        self.left=None
        self.right=None
        self.val=key
#function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end="  "),
        inorder(root.right)
#function to do preorder
def preorder(root):
    if root:
        print(root.val, end=" "),
        preorder(root.left)
        preorder(root.right)
#function to do postorder
def postorder(root):
    if root:
        preorder(root.left)
        preorder(root.right)
        print(root.val, end=" "),
#Driver code
if __name__ == "__main__":
    root = Node("A")
    root.left = Node("B")
    root.left.left = Node("D")
    root.left.left.left = Node("G")
    root.left.right = Node("E")
    root.left.right.left = Node("H")
    root.left.right.right = Node("L")
    root.right = Node("C")
    root.right.right = Node("F")
    root.right.right.left = Node("I")
    root.right.right.right = Node("P")

    print("Inorder : ")
    inorder(root)
    print("\n Preorder : ")
    preorder(root)
    print("\nPostorder : ")
    postorder(root)
