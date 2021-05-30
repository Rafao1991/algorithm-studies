# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    if not l1 or not l2:
        return ListNode(None)
    
    str_num1 = linked_list_to_string(l1)
    str_num2 = linked_list_to_string(l2)
            
    return string_to_linked_list(list(str(int(str_num1[::-1]) + int(str_num2[::-1]))[::-1]))

def linked_list_to_string(ll):
    return_str = ''
    
    if not ll:
        return return_str
    
    q = [ll]
    while q:
        node = q.pop(0)
        return_str += str(node.val)
        if node.next:
            q.append(node.next)
    
    return return_str

def string_to_linked_list(str_list):
    root = ListNode(None)
    head = root
    while str_list:
        head.val = str_list.pop(0)
        if str_list:
            head.next = ListNode(None)
            head = head.next
    
    return root
    
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
# 7 0 8