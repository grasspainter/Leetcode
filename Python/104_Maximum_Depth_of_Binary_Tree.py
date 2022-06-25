'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 參考https://ithelp.ithome.com.tw/articles/10270148
    def maxDepth(self, root):
        curr = root
        if not curr:
            return 0
        else:
            print (curr.val)
            #return self.maxDepth(root.left) + 1 
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == '__main__':
    result = Solution()
    root = TreeNode(val=3, left=TreeNode(val=9, left=None, right=None), right=TreeNode(val=20, left=TreeNode(val=15, left=None, right=None), right=TreeNode(val=7, left=None, right=None)))
    #root = TreeNode(val=1, left=None, right=TreeNode(val=2, left=None, right=None))
    #root = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3, left=TreeNode(val=4, left=TreeNode(val=5, left=None, right=None), right=None), right=None), right=None), right=None)
    #root = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=4, left=None, right=None), right=TreeNode(val=5, left=None, right=None)), right=TreeNode(val=3, left=None, right=None))
    #root  = TreeNode(val=2, left=None, right=TreeNode(val=3, left=None, right=TreeNode(val=4, left=None, right=TreeNode(val=5, left=None, right=TreeNode(val=6, left=None, right=None)))))
    print (result.maxDepth(root))