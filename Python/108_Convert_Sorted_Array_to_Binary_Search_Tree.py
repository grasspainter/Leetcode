'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
'''



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 2022-06-28 參考https://desolve.medium.com/%E5%BE%9Eleetcode%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-35-bst-3-b1f225f39aa3
    def sortedArrayToBST(self, nums):
        n = len(nums)
        if n == 0:
            return None
        else:
            return self.getNode(nums,0,len(nums)-1)

    def getNode(self,nums,l,r):
        if l > r:
            return None
        mid = (l+r) // 2
        root = TreeNode(nums[mid])
        root.left = self.getNode(nums,l,mid-1)
        root.right = self.getNode(nums,mid+1,r)
        return root

if __name__ == '__main__':
    result = Solution()
    nums = [-10,-3,0,5,9]
    print (result.sortedArrayToBST(nums))