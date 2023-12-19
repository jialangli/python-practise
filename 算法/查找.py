# 李佳朗
# 开发时间：2023
def dfs(nums:list[int],target:int,i:int,j:int)->int:
    #二分查找：问题f（i,j）
    #若区间为空，代表无目标元素，则返回-1
    if i>j:
        return -1
    m=(i+j)//2
    if nums[m]<target:
        return dfs(nums,target,m+1,j)
    elif nums[m]>target:
        #递归子问题f(m+1,j)
        return des(nums,target,i,m-1)
    else:
        #找到目标元素，返回其索引
        return m
def binary_search(nums:list[int],target:int)->int:
    n=len(nums)
    #求解问题f（0，n-1）
    return dfs(nums,target,0,n-1)

def erfen(nums,target):
    left,right=0,len(nums)-1
    while left<=right:
        mid=left+(right-left)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

def move(src:list[int],tar:list[int]):
    #移动一个圆盘
    #将圆盘放入tar顶部
    pan=src.pop()
    #将圆盘放入tar顶部
    tar.append(pan)
def dfs(i:int,src:list [int],buf:list[int],tar:list[int]):
    #求解汉诺塔问题f(i)
    #若src只剩下一个圆盘，则直接将其移到tar
    if i==1:
        move(src,tar)
        return
    #子问题f(i-1):将src顶部i-1个圆盘借助tar移到buf
    dfs(i-1,src,tar,buf)
    #子问题f(i-1):将buf顶部i-1个圆盘借助src移到tar
    move(src,tar)
    #子问题f（i-1）：将buf顶部i-1个圆盘借助src移到tar
    dfs(i-1,buf,src,tar)
def solve_hanota(A:list[int],B:list[int],C:list[int]):
    n=len(A)
    #将A顶部n个圆盘借助B移到C
    dfs(n,A,B,C)
