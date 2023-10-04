class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Handle edge cases
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move prev to the (left-1)th node
        for _ in range(left - 1):
            prev = prev.next
        
        # Initialize pointers for reversal
        current = prev.next
        next_node = None
        reversed_head = None
        
        # Reverse the portion between left and right
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = reversed_head
            reversed_head = current
            current = next_node
        
        # Connect the reversed portion back to the original list
        prev.next.next = current
        prev.next = reversed_head
        
        # If left is equal to 1, update the head of the list
        if left == 1:
            head = reversed_head
        
        return head
