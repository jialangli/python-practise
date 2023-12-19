# 李佳朗
# 开发时间：2023
import heapq
class ListNode:
    """链表节点类"""
    def __init__(self, val: int):
        self.val: int = val               # 节点值
        self.next: ListNode | None = None # 指向下一节点的引用

n0=ListNode(1)
n1=ListNode(3)
n2=ListNode(2)
n3=ListNode(5)
n4=ListNode(4)
n0.next=n1
n1.next=n2
n2.next=n3
n3.next=n4
def insert(n0:ListNode,P:ListNode):
    n1=n0.next
    P.next=n1
    n0.next=P
def remove(n0:ListNode):
    if not n0.next:
        return
    P=n0.next
    n1=P.next
    n0.next=n1
def access(head:ListNode,index:int)->ListNode|None:
    for _ in range(index):
        if not head:
            return None
        head=head.next
    return head
def find(head:ListNode,target:int)->int:
    index=0
    while head:
        if head.val==target:
            return index
        head=head.next
        index+=1
    return -1
#双向链表
class ListNode:
    def __init__(self,val:int):
        self.val:int=val
        self.next:ListNode|None=None
        self.prev:ListNode|None=None