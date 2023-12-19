# 李佳朗
# 开发时间：2023
nums1:list[int]=[]
nums:list[int]=[1,3,2,5,4]
#访问元素
num:int=nums[1]
nums[1]=0
nums.clear()
nums.append(1)
nums.append(3)
nums.append(2)
nums.append(5)
nums.append(4)
nums.insert(3,6)
#在索引3处插入数字6
#删除元素
nums.pop(3)
#遍历列表
count=0
for i in range(len(nums)):
    count+=nums[i]
#直接遍历列表元素
for num in nums:
    count+=num

#5.拼接列表
nums1:list[int]=[6,8,7,10,9]
nums+=nums1

#简单的列表实现
class Mylist:
    def __init__(self):
        self._capacity:int=10
        self._arr:list[int]=[0]*self._capacity
        self._size:int = 0
        self._extend_ratio:int=2
    def size(self)->int:
        return self._size
    def capacity(self)->int:
        return self._capacity
    def get(self,index:int)->int:
        if index<0 or index>=self._size:
            raise IndexError("索引越界")
        return self._arr[index]
    def set(self,num:int,index:int):
        if index<0 or index>=self._size:
            raise IndexError("索引越界")
        if self._size==self.capacity():
            self.extend_capacity