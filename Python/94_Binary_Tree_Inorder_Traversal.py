'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #2022-04-22 參考https://ithelp.ithome.com.tw/articles/10213280
    def inorderTraversal(self, root):
        #root = TreeNode(root)
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
if __name__ == '__main__':
    result = Solution()
    root = TreeNode(val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=3, left=None, right=None), right=None))
    print (result.inorderTraversal(root))