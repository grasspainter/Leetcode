'''
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
 

Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.
from calendar import c


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    #2022-06-22
    def isSameTree(self, p, q):
        stack1 = []
        stack2 = []
        curr1 = p
        curr2 = q
        #print (curr1.val,curr2)

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
                    curr2 = curr2.left
                else:
                    return 0
            curr1 = stack1.pop()
            curr2 = stack2.pop()
            if (curr1.val == curr2.val):
                curr1 = curr1.right
                curr2 = curr2.right
            else:
                return 0
        return 1

if __name__ == '__main__':
    result = Solution()
    p = TreeNode(val=1, left=TreeNode(val=2, left=None, right=None), right=TreeNode(val=3, left=None, right=None))
    #p = TreeNode(val=1, left=None, right=TreeNode(val=3, left=None, right=None))
    #q = TreeNode(val=1, left=TreeNode(val='', left=None, right=None), right=TreeNode(val=3, left=None, right=None))
    q = TreeNode(val=1, left=None, right=TreeNode(val=3, left=None, right=None))
    print (bool(result.isSameTree(p,q)))

'''
TreeNode{val: 1, left: TreeNode{val: 2, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}
TreeNode{val: 1, left: None, right: TreeNode{val: 3, left: None, right: None}}
'''
