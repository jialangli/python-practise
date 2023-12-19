# 李佳朗
# 开发时间：2023
def coin_change_greedy(coins:list[int],amt:int)->int:
    #零钱找零：贪心
    #假设coins列表有序,剩余金额amt,count硬币数量
    i=len(coins)-1
    count=0
    #循环进行贪心选择，直到无剩余金额
    while amt>0:
        #找到小于且最接近剩余金额的硬币
        while i>0 and coins[i]>amt:
            i-=1
            #选择coins[i]
        amt-=coins[i]
        count+=1
        #若未找到可行方案，则返回-1
        return count if amt==0 else -1
#一些典型的贪心算法问题:
# 硬币找零问题：在某些硬币组合下，贪心算法总是可以得到最优解。
# 区间调度问题：假设你有一些任务，每个任务在一段时间内进行，你的目标是完成尽可能多的任务。如果每次都选择结束时间最早的任务，那么贪心算法就可以得到最优解。
# 分数背包问题：给定一组物品和一个载重量，你的目标是选择一组物品，使得总重量不超过载重量，且总价值最大。如果每次都选择性价比最高（价值 / 重量）的物品，那么贪心算法在一些情况下可以得到最优解。
# 股票买卖问题：给定一组股票的历史价格，你可以进行多次买卖，但如果你已经持有股票，那么在卖出之前不能再买，目标是获取最大利润。
# 霍夫曼编码：霍夫曼编码是一种用于无损数据压缩的贪心算法。通过构建霍夫曼树，每次选择出现频率最低的两个节点合并，最后得到的霍夫曼树的带权路径长度（编码长度）最小。
# Dijkstra 算法：它是一种解决给定源顶点到其余各顶点的最短路径问题的贪心算法。

class Item:
    #物品
    def __init__(self,w:int,v:int):
        self.w=w #物品重量
        self.v=v #物品价值
def fractional_knapsack(wgt:list[int],val:list[int],cap:int)->int:
    #分数背包：贪心
    #创造物品列表，包含两个属性：重量，价值
    items=[Item(w,v) for w,v in zip(wgt,val)]
    #按照单元价值item.v/item.w 从高到低进行排序
    items.sort(key=lambda item:item.v/item.w,reverse=True)
    #将物品对象列表按照单位价值从高到低进行排序。
    #reverse=True将单位价值高的物品放在排序后的列表的前面。
    #循环贪心选择
    res=0
    for item in items:
        if item.w<=cap:
            #若剩余容量充足，则将当前物品整个装进背包
            res+=item.v
            cap-=item.w
        else:
            #若剩余容量不足，则将当前物品的部分装进背包
            res+=(item.v/item.w)*cap
            #已无剩余容量，因此跳出循环
            break
    return res

def dmax_capacity(ht:list[int])->int:
    #最大容量：贪心
    #初始化i，j分列数组两端
    i,j=0,len(ht)-1
    #初始化最大容量为0
    res=0
    #循环贪心选择，直至两板相遇
    while i<j:
        #更新最大容量
        cap=min(ht[i],ht[j]*(j-1))
        res=max(res,cap)
        #向内移动短板
        if ht[i]<ht[j]:
            i+=1
        else:
            j-=1
    return res

def max_product_cutting(n:int)->int:
    #最大切分乘法：贪心
    #当n<=3时，必须切分出一个1
    if n<=3:
        return 1*(n-1)
    #贪心地切出3，a为3的个数，b为余数
    a,b=n//3,n%3
    if b==1:
        #当余数为1时。将一对1*3转化为2*2
        return int(math.pow(3,a-1))*2*2
    if b==2:
        #当余数为2时，不做处理
        return int(math.pow(3,a))*2
    #当余数为0时，不做处理
    return int(math.pow(3,a))