# 李佳朗
# 开发时间：2023
from collections import deque
que:deque[int]=deque()
que.append(1)
que.append(2)
que.append(3)
front:int=que[0];#访问队首元素
pop:int=que.popleft()
size:int=len(que)
#判断队列是否为空
is_empty:bool=len(que)==0

def __init__(self):
    self._front:ListNode|None=None
    #指向链表的第一个节点）的引用，默认为空。
    self._front:ListNode|None=None
    #表示队列的尾节点（指向链表的最后一个节点）的引用，默认为空。
    self.size:int=0#表示队列的大小（元素个数），初始值为0。
def size(self)->int:#返回队列的大小（元素个数）。
    return self._size
def is_empty(self)->bool:#判断队列是否为空，如果队列的头节点为空则返回 True，否则返回 False。
    return not self._front
def push(self,num:int):
    node=ListNode(num)
    if self._front is None:
        self._front=node
        self._rear=node
    else:
        self._rear.next=node
        self._rear=node
    self._size+=1
def pop(self)->int:
    num=self.peek()
    #方法获取队列头部元素值，并将其赋值给 num。然后将队列的头节点指向头节点的下一个节点，
    # 相当于将队列头节点弹出。最后，减少队列的大小 _size，并返回 num。
    self._front=self._front.next
    self._size-=1
    return num
def peak(self)->int:
    if self.is_empty():
        raise IndexError("队列为空")
    return self._front.val
def to_list(self)->list[int]:
    queue=[]
    temp=self._front
    while temp:
        queue.append(temp.val)
        temp=temp.next
    return queue

class  ArrayQueue:
    def __init__(self,size:int):
        self._nums:list[int]=[0]*size#用于储存队列元素的数组
        self._front:int=0 #队首指针，指向队首元素
        self._size:int=0  #队列长度
    def capacity(self)->int:
        return len(self._nums)
    def size(self)->int:#获取队列的长度
        return self._size
    def is_empty(self)->bool:#判断队列是否为空
        return self._size==0
    def push(self,num:int):
        if self._size==self.capacity():
            raise IndexError("队列已满")
        #计算尾指针，指向队尾索引+1from
        #通过取余操作，实现rear越过数组尾部后回到头部
        rear:int = (self._front+self._size)%self.capacity()
        #将num添加至队尾
        self._nums[rear]=num
        self._size+=1
    def pop(self)->int:
        num:int=self.peek()

from collections import deque
deque:deque[int]=deque()
deque.append(2)
deque.qppend(3)
deque.appendleft(4)
deque.appednleft(5)
front:int=deque[0]#队首元素
rear:int=deque[-1]#队尾元素
#元素出队
pop_front:int=deque.popleft()#队首元素出队
pop_rear:int=deque.pop()
#获取双向队列的长度
size:int=len(deque)
#判断双向队列是否为空
is_empty:bool=len(deque)==0

class ListNode:
    def __init__(self,val:int):
        self.val:int=val
        self.next:ListNode|None=None#后继节点引用
        self.prev:ListNode|None=None#前驱节点引用
class LinkedListDeque:#基于双向链表实现的双向队列
    def __init__(self):
        self._front:ListNode|None=None
        self._rear:ListNode|None=None
        self._size:int=0 #双向队列的长度
    def size(self)->bool:
        return self.size()==0
    def push(self,num:int,is_front:bool):
        node=ListNode(num)