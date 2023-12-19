# 李佳朗
# 开发时间：2023
#栈
stack:list[int]=[]
stack.append(1)
stack.append(2)
stack.append(3)
#元素入栈
#访问栈顶元素
peek:int=stack[-1]
#元素出栈
pop:int=stack.pop()
size:int=len(stack)
is_empty:bool=len(stack)==0

class LinkedListStack:
    def __init__(self):
       self._peek:ListNode|None=None
       self._size:int = 0
    def is_empty(self)->bool:
        return not self._peek
    def push(self,val:int):
        node=ListNode(val)
        node.next=self._peek
        self._size+=1
    def pop(self)->int:
        num=self.peek()
        self._peek=self._peek.next
        return num

class ArrayStack:
    def __init__(self):
        self.stack:list[int]=[]
    def size(self)->int:
        return len(self._stack)#获取栈的长度

    def is_empty(self)->bool:
        return len(self._stack)
    def pop(self)->int:
        if self.is_empty():
            raise IndexError("栈为空")
        return self._stack.pop()
    def peek(self)->int:
        if self.is_empty():
            raise IndexError("栈为空")
        return self._stack[-1]
    def to_list(self)->list[int]:
        return self._stack