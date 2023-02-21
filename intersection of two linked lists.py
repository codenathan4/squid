class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seta = set()
        node = headA
        while node:
            seta.add(node)
            node = node.next
        nodeB= headB
        while nodeB:
            if nodeB in seta:
                break
            nodeB=nodeB.next
        print(seta)    
        return nodeB
