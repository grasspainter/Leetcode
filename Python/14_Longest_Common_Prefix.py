'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

'''



class Solution:

    def longestCommonPrefix(self, STR):

        #print (Dic)

        #LEN = map(lambda x: len(x),STR)
        #LENmin = min(list(LEN))#;print(LENmin)
        LENmin = min(list(map(lambda x: len(x),STR)))#;print(LENmin)

        LL = []
        for j in range(0,LENmin):
            if "" in STR:
                Check3 = [""]
                break
            else:
                Check3 = map(lambda x: list(x)[j],STR)
                CK3 = list(Check3)
                if len(set(CK3)) != 1:
                    break
                else:
                    LL.append(CK3[0])
                    #print ('CHECK3',list(CK3))

            #print ("CK3",set(CK3))

        LL2 = "".join(LL)

        return LL2

Result = Solution()
#print (Result.longestCommonPrefix(["flower","flow","flight"]))
#print (Result.longestCommonPrefix(["aa","aa"]))
#print (Result.longestCommonPrefix(["aa","ab"]))
#print (Result.longestCommonPrefix(["c","acc","ccc"]))
print (Result.longestCommonPrefix(["abca","aba","aaab"]))
#print (Result.longestCommonPrefix([""]))
print (Result.longestCommonPrefix(["",""]))