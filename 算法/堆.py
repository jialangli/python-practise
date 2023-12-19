# 李佳朗
# 开发时间：2023
#初始化小顶堆
min_heap,flag=[],1
#初始化大顶堆
max_heap,flag=[],-1
#python的heapq模块默认实现小顶堆
#考虑将“元素取负”后再入堆，这样就可以将大小关系颠倒，从而实现大顶堆
#在本示例中，flag=1时对应小顶堆，flag=-1时对应大顶堆
#元素入堆
heapq.heappush(max_heap,flag*1)
heapq.heappush(max_heap,flag*3)
heapq.heappush(max_heap,flag*2)
heapq.heappush(max_heap,flag*5)
heapq.heappush(max_heap,flag*4)

#获取堆顶元素
peek:int=flag*max_heap[0]  #5
#堆顶元素出堆
#出堆元素会形成一个从大到小的序列
val=flag*heapq.heappop(max_heap)  #5
val=flag*heapq.heappop(max_heap)  #4
val=flag*heapq.heappop(max_heap)  #3
val=flag*heapq.heappop(max_heap)  #2
val=flag*heapq.heappop(max_heap)  #1
#获取堆大小
size:int=len(max_heap)
#判断堆是否为空
is_empty:bool=not max_heap
#输入列表并建堆
min_heap:list[int]=[1,3,2,5,4]
heapq.heapify(min_heap)
def left(self,i:int)->int:
    #获取左子节点索引
    return 2*i+1
def right(self,i:int)->int:
    #获取右子节点索引
    return 2*i+2
def parent(self,i:int)->int:
    #获取父节点索引
    return(i-1)//2# 向下整除
def peek(self)->int:
    #访问堆顶元素
    return self.max_heap[0]

def push(self,val:int):
    #元素入堆
    #添加节点
    self.max_heap.append(val)
    # 从低至顶堆化
    self.sift_up(self.size()-1)
def sift_up(self,i:int):
    #从节点开始，从底至顶堆化
    while True:
        #获取节点i的父节点
        p=self.parent(i)
        #当“越过根节点”或“节点无须修复”时，结束堆化
        if p<0 or self.max_heap[i]<=self.max_heap[p]:
            break
        #交换两节点
        self.swap(i,p)
        #循环向上堆化
        i=p


#元素出堆
def pop(self)->int:
    "元素出堆"
    #判空处理
    if self.is_empty():
        raise IndexError("堆为空")
    #交换根节点与最右叶节点（交换首元素与尾元素）
    self.swap(0,self.size()-1)
    # 删除节点
    val=self.max_heap.pop()
    #从顶至底堆化
    self.sift_down(0)
    #返回堆顶元素
    return val
def sift_down(self,i:int):
    #从节点i开始，从顶至底堆化
    while True:
        l,r,ma=self.left(i),self.right(i),i
        if l<self.size() and self.max_heap[l]>self.max_heap[ma]:
            ma=l
        if r<self.size() and self.max_heap[l]>self.max_heap[ma]:
            ma=r
        #若节点i最大或索引l,r越界，则无须继续堆化，跳出
        if ma==i:
            break
        #交换两节点
        self.swap(i,ma)
        # 循环向下堆化
        i=ma

def top_k_heap(nums:list[int],k:int)->list[int]:
    #基于堆查找数组中最大的k个元素
    #初始化小顶堆
    heap=[]
    #将数组的前k个元素入堆
    for i in range(k):
        heapq.heappush(heap,nums[i])
        #从第k+1个元素开始，保持堆的长度为k
    for i in range(k,len(nums)):
        #若当前元素大于堆顶元素，则将堆顶元素出堆，当前元素入堆
        if nums[i]>heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap,nums[i])
    return heap