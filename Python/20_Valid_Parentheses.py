'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''


class Solution:
    def isValid(self, s: str) -> bool:

        #S = {0:['{','}'],1:['(',')'],2:['[',']']}
        #S = ['{','}','(',')','[',']']
        #S = ['{','(','[','}',')',']']
        S = {')':'(',']':'[','}':'{'}
        a = [None]

        if len(list(s))%2 != 0:
            return False
        else: 
            for i in s:
                if i in S:
                    if S[i] != a.pop():
                        return False
                else:
                    a.append(i)
        return len(a) == 1

Result = Solution()
print (Result.isValid("(}{)"))
print (Result.isValid("()[]{}"))
print (Result.isValid("{[]}"))