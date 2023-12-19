# 李佳朗
# 开发时间：2023
#给定一个整数数组 nums 和一个目标元素 target ，
# 请在数组中搜索“和”为 target 的两个元素，并返回它们的数组索引。返回任意一个解即可。
def two_sum_brute_force(nums:list[int],target:int)->list[int]:
    #方法一，暴力枚举
    #两层循环，时间复杂度为O（n^2）
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return[i,j]
    return []

def two_sum_hash_table(nums:list[int],target:int)->list[int]:
    #方法二：辅助哈希表，空间复杂度O（n)
    dic=[]
    #单层循环，时间复杂度为O（n）
    for i in range(len(nums)):
        if target-nums[i] in dic:
            return[dic[target-nums[i]],i]
        dic[nums[i]]=i
    return []

def selection_sort(nums:list[int]):
    #选择排序
    n=len(nums)
    #外循环：未排序区间为[i,n-1]
    for i in range(i+1,n):
        if nums[j]<nums[k]:
            k=j  #记录最小元素的索引
            #将该最小元素与未排序区间内的最小元素
            k=i
            for j in range(i+1,n):
                if nums[j]<nums[k]:
                    k=j #记录最小元素的索引
            #将该最小元素与未排序区间的首个元素交换
            nums[i],nums[k]=nums[k],nums[i]

def bubble_sort(nums:list[int]):
    n=len(nums)#冒泡排序
    #外循环：未排序区间未[0,i]中的最大元素交换至该区间的最右端
    for i in range(n-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                #交换nums[j]与nums[j+1]
                nums[j],nums[j+1]=nums[j+1],nums[j]

def bubble_sort_with_flag(nums:list[int]):
    #冒泡排序（标准优化）
    n=len(nums)
    #外循环：未排序区间为[0,i]
    for i in range(n-1,0,-1):
        flag=False#初始化标志位
        #内循环：将未排序区间[0,i]中的最大元素交换至该区间的最右端
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1]
                flag=True #记录交换元素
        if not flag:
            break #此轮冒泡未交换任何元素，直接跳出

def insertion_sort(nums:list[int]):
    "插入排序"
    #外循环：已排序区间为[0,i-1]
    for i in range(1,len(nums)):
        base=nums[i]
        j=i-1
        #内循环：将base插入到已排序区间[0,i-1]中的正确位置
        while j>=0 and nums[j]>base:
            nums[j+1]=nums[j]  #将nums[j]向右移动一位
            j-=1
        nums[j+1]=base #将base赋值到正确的位置

#快排模板
def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)

#堆排序
def sift_down(nums:list[int],n:int,i:int):
    #堆的长度为n，从节点i开始，从顶至底堆化
    while True:
        #判断节点i，l，r中值最大的节点，记为ma
        l=2*i+1
        r=2*i+2
        ma=i
        if l<n and nums[l]>nums[ma]:
            ma=l
        if r<n and nums[r]>nums[ma]:
            ma=r
            #若节点i最大或索引l,r越界，则无须继续堆化，跳出
            if ma==i:
                break
                #交换两节点
            nums[i],nums[ma]=nums[ma],nums[i]
            #循环向下堆化
            i=ma
def heap_sort(nums:list[int]):
    #堆排序
    #建堆操作：堆化除叶节点以外的其他所有节点
    for i in range(len(nums)//2-1,-1,-1):
        #交换根节点与最右叶节点（交换首元素与尾元素）
        nums[0],nums[i]=nums[i],nums[0]
        #以根节点为起点，从顶至底进行堆化
        sift_down(nums,i,0)