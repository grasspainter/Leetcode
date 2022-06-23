'''
https://leetcode.com/problems/symmetric-tree/

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?
'''

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #2022-06-23
    def isSymmetric(self, root):
        if root == None:
            return 0
        else:
            stack1 = []
            stack2 = []
            curr1 = root.left
            curr2 = root.right
            while curr1 or curr2 or stack1 or stack2:
                while curr1 or curr2:
                    if curr1 and not curr2:
                        return 0
                    elif not curr1 and curr2:
                        return 0
                    if (curr1.val == curr2.val):
                        stack1.append(curr1)
                        stack2.append(curr2)
                        curr1 = curr1.left
                        curr2 = curr2.right
                    else:
                        return 0
                curr1 = stack1.pop()
                curr2 = stack2.pop()
                if (curr1.val == curr2.val):
                    curr1 = curr1.right
                    curr2 = curr2.left
                else:
                    return 0
            return 1

if __name__ == '__main__':
    result = Solution()
    root = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3, left=None, right=None), right=TreeNode(val=4, left=None, right=None)), right=TreeNode(val=2, left=TreeNode(val=4, left=None, right=None), right=TreeNode(val=3, left=None, right=None)))
    print (bool(result.isSymmetric(root)))