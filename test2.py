# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        mem = {}
        def traverse(root,target):
            if root:    
                if (root.val not in mem):
                    #print(root.val,mem)
                    mem[target-root.val] = root.val
                else:
                    return True
                return traverse(root.left,target) or traverse(root.right,target)
        return  traverse(root,k)
    