class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

tree_1 = [3,9,20,None,None,15,7]
tree_2 = [1,2,3]

def create_tree(trees):
    for idx,tree in enumerate(trees):
        if idx == 0:
            root = TreeNode(tree)
            temp = root
            continue
        if (idx % 2 == 1):
            temp.left = TreeNode(tree)
        if (idx % 2 == 0):
            temp.right = TreeNode(tree)
            temp = temp.left
    return(root)

def preorder(root):
    queue = []
    if root is not None:
        print(root.val,end=" | ")
        queue.append(root.val)
        preorder(root.left)
        if root.right == None:
            queue.append(None)
        preorder(root.right)

a = create_tree(tree_1)
preorder(a)