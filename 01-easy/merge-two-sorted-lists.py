
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def MergeTwoSortedLists(self, list1: ListNode, list2: ListNode):
        dummy_node = ListNode()
        tail = dummy_node
        while list1 and list2: # while not empty
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # remaining of the longer list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2


        return dummy_node.next



#test case:
sol = Solution()
def print_list(node: ListNode):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Test case
sol = Solution()
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
merged_list = sol.MergeTwoSortedLists(list1, list2)
print_list(merged_list)
