    def middleNode(self, head: ListNode) -> ListNode:
        
        if head is None:
            return self.head
        
        self.firstptr = head
        self.secondptr = head
        
        while self.secondptr is not None and self.secondptr.next is not None:
            self.firstptr = self.firstptr.next
            self.secondptr = self.secondptr.next.next
        return self.firstptr