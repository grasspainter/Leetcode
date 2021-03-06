'''
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''

class Solution:
    #2022-04-07
    def addBinary(self, a, b):
        a = int(a,2)
        b = int(b,2)
        c = a + b
        return bin(c)[2:]

if __name__ == '__main__':
    result = Solution()
    #a = "11"
    #b = "1"
    a = "1010"
    b = "1011"
    print (result.addBinary(a,b))