'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Linkedlist():
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
            #self.tail.next = new_node
        #print (self.head.val,self.tail.val)
        return
    def output_list(self):

        current_node = self.head
        results = []
        
        while current_node!=None:  
            results.append(current_node.val)
            current_node = current_node.next

        #print(results)
        return results
    def index(self,data):
        temp = self.head
        count = 0
        data = ListNode(data)
        #print (temp,data.val)
        while temp:
            #print (temp.val,data.val)
            if temp.val == data.val:
                    return count
            temp = temp.next
            count += 1
    
class Solution(ListNode):
    #2022-04-12
    def deleteDuplicates(self,head):
        #List = Linkedlist()
        #for i in List:
        #    if list.index(i) == None:
        #        list.append(i)
        #    #print (list.index(i))
        #return list.output_list()
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head
            

if __name__ == '__main__':
    #head = [1,2,3]
    head = ListNode(val= 1, next= ListNode(val= 2, next= ListNode(val= 3, next= ListNode(val= 3, next= None))))
    result = Solution()
    print (result.deleteDuplicates(head))
    #Solution(head).output