# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #using recursion
        def trBST(root,ans):
            if not root:
                return None
            else:
                trBST(root.left,ans)
                ans.append(root.val)
                trBST(root.right,ans)
            return ans
        
        elems = trBST(root,[])
        head0 = TreeNode(elems[0])
        head = head0
        for i in elems[1:]:
            head.right = TreeNode(i)
            head = head.right
        return head0
