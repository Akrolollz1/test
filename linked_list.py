class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
    
    
    def add_to_end(head: ListNode, val: Any) -> None:
        new_node = ListNode(val)
    def add_to_front(head: ListNode, val: Any) -> ListNode:
        node = ListNode(val)
        node.next = head
        return node


    def display(head: ListNode) -> None:
        ptr = head
        while ptr is not None:
            print(ptr.val, end=" -> ")
            ptr = ptr.next
        print("None")

head = ListNode(10)

head.add_to_end(head, "hello")
head.add_to_front(head, 2)
print(head)
