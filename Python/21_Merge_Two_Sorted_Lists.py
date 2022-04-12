'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

# Definition for singly-linked list.


class ListNode:
     def __init__(self, val=None, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1:ListNode, list2:ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1 != None:
            curr.next = list1
        if list2 != None:
            curr.next = list2
        return dummy.next

def print_list(l):
    v = l
    while v:
        print(v.val)
        v = v.next    

#l1 = ListNode(1)
#l1.next = ListNode(2)
#l1.next.next = ListNode(4)
#
#l2 = ListNode(1)
#l2.next = ListNode(3)
#l2.next.next = ListNode(4)
#
#Result = Solution().mergeTwoLists(l1,l2)
#print_list(Result)

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, data):
        #建立 class Node 的instance(實體)
        new_node = ListNode(data)
        
        # 如果head == None 代表為第一個Node
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next    

        return

    def output_list(self):

        current_node = self.head
        results = []
        
        while current_node!=None:  
            results.append(current_node.val)
            current_node = current_node.next

        print(results)
        return


list = SingleLinkedList()
list.output_list()
list.append(1)
list.append(2)
list.output_list()
#l1 = list
l2 = list
l2.output_list()
#print (l1,l2)



'''
class Solution:
    def mergeTwoLists(self, list1, list2 ):
        a = list1
        b = list2
        c = a+b
        return c
Result = Solution()
print (Result.mergeTwoLists([1,2,4],[1,3,4]))
'''