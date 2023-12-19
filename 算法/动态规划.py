# 李佳朗
# 开发时间：2023
def backtrack(choices:list[int],state:int,n:int,res:list[int])->int:
    #回溯
    #当爬到第n阶时，方案数量+1
    if state==n:
        res[0]+=1
        #遍历所有选择
    for choice in choices:
        #剪枝：不允许越过第n阶
        if state+choice>n:
            continue
        #尝试：做出选择，更新状态
        backtrack(choices,state+choice,n,res)
        #回退
def climbing_stairs_backrack(n:int)->int:
    #爬楼梯：回溯
    choices=[1,2] # 可选择向上爬1阶或者2阶
    state=0 #从第0阶开始爬
    res=[0] #使用res[0]记录方案数量
    backtrack(choices,state,n,res)
    return res[0]

def dfs(i:int)->int:
    #搜索
    #已知dp[1]和dp[2]，返回之
    if i==1 or i==2:
        return i
    #dp[i]=dp[i-1]+dp[i-2]
    count=dfs(i-1)+dfs(i-2)
    return count
def climbing_stairs_dfs(n:int)->int:
    #爬楼梯：搜索
    return dfs(n)

def dfs(i:int,mem:list[int])->int:
    #记忆化搜索
    #已知dp[1] 和 dp[2]返回之
    if i==1 or i==2:
        return i
    #若存在记录dp[i],则直接返回之
    if mem[i]!=-1:
        return mem[i]
    #dp[i]=dp[i-1]+dp[i-2]
    count=dfs(i-1,mem)+dfs(i-2,mem)
    #记录dp[i]
    mem[i]=count
    return count
def climbing_stairs_dfs_mem(n:int)->int:
    #爬楼梯：记忆化搜索
    #mem[i] 记录爬到第i阶得方案总数，-1代表无记录
    mem=[-1]*(n+1)
    return dfs(n,mem)

#方法三：动态规划
def climbing_stairs_dp(n:int)->int:
    #爬楼梯：动态规划
    if n==1 or n==2:
        return 0
    #初始化dp表，用于存储子问题的解
    dp=[0]*(n+1)
    #初始化dp表，用于存储子问题的解
    dp[1],dp[2]=1,2
    #状态转移：从较小子问题逐步求解较大子问题
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
#空间优化
def climbing_stairs_dp_comp(n:int)->int:
    if n==1 or n==2:
         return n
    a,b=1,2
    for _ in range(3,n+1):
        a,b=b,a+b
    return b

def min_cost_climbing_stairs_dp(cost:list[int])->int:
    #爬楼梯最小代价：动态规划
    n=len(cost)-1 #cost为整数列表，n表示楼梯数
    if n==1 or n==2:
        return cost[n]
    #初始化dp表，用于存储子问题的解
    dp=[0]*(n+1)
    #初始状态：预设最小子问题的解
    dp[1],dp[2]=cost[1],cost[2]
    #状态转移：从较小子问题逐步求解较大子问题
    for i in range(3,n-1):
        dp[i]=min(dp[i-1],dp[i-2])+cost[i]
    #这里使用循环进行状态转移，从较小的子问题逐步求解较大的子问题。从第3个楼梯开始，
    # 每个楼梯的最小代价是其前两个楼梯中的最小代价加上当前楼梯的代价。
    return dp[n]

def min_cost_climbing_stairs_dp_comp(cost:list[int])->int:
    #爬楼梯最小代价：空间优化后的动态规划
    n=len(cost)-1
    if n==1 or n==2:
        return cost[n]
    a,b=cost[1],cost[2]
    for i in range(3,n+1):
        a,b=min(a,b)+cost[i]
    return b

def climbing_stairs_constraint_dp(n:int)->int:
    #带约束爬楼梯：动态规划
    if n==1 or n==2:
        return 1
    #初始化dp表，用于存储子问题的解
    dp=[[0]*3 for _ in range(n+1) ]
    #这里创建了一个二维列表dp，用于存储子问题的解。
    # 它的行数是n + 1，表示楼梯的数量，列数是3，
    # 分别表示状态1和状态2的解。
    #初始状态：预设最小问题的解
    dp[1][1],dp[1][2]=1,0
    dp[2][1],dp[2][2]=0,1
    #状态转移：从较小子问题逐步求解较大子问题
    # dp[2][1]表示楼梯数量为2时的状态1的解，即在倒数第二个楼梯选择状态2，爬到最后一个楼梯处，所以设置为0。
    # dp[2][2]表示楼梯数量为2时的状态2的解，即在倒数第二个楼梯选择状态1，再向上爬一个楼梯，所以设置为1。

    for i in range(3,n+1):
        dp[i][1]=dp[i-1][2]
        dp[i][2]=dp[i-2][1]+dp[i-2][2]
        #dp[i][1]表示在第i个楼梯处选择状态1时的解，即从状态2转移而来。
        # 我们将其设置为dp[i-1][2]，表示从上一个楼梯处选择状态2到达第i个楼梯的解。
        #dp[i][2]表示在第i个楼梯处选择状态2时的解，即从状态1或状态2转移而来。
        # 我们将其设置为dp[i-2][1] + dp[i-2][2]，表示从倒数第二个楼梯处选择状态1或状态2，再向上爬两个楼梯到达第i个楼梯的解。
    return dp[n][1]+dp[n][2]
    #最后，我们返回第n个楼梯的状态1和状态2的解之和，即带约束爬到楼顶的方式数。

#暴力最小路径
def min_path_sum_dfs(grid:list[list[int]],i:int,j:int)->int:
    #最小路径和：暴力搜索
    #若为左上角单元格，则终止搜索
    if i==0 and j==0:
        return grid[0][0]
    #若行列索引越界，则返回+∞代价
    if i<0 or j<0:
        return inf
    #计算从左上角到（i-1,j)和（i，j-1）的最小路径代价
    up=min_path_sum_dfs(grid,i-1,j)
    left=min_path_sum_dfs(grid,i,j-1)
    #返回从左上角（i，j）的最小路径代价
    return min(left,up)+grid[i][j]
#状态转移方程：dp[i,j]=min(dp[i-1,j],dp[i,j-1])+grid[i,j]


#最小路径和：记忆化搜索
def min_path_sum_dfs_mem(
        grid:list[list[int]],mem:list[list[int]],i:int,j:int
)->int:
    #若为左上角单元格，则终止搜索
    if i==0 and j==0:
        return grid[0][0]
    #若行列索引越界，则返回+∞代价
    if i<0 or j<0:
        return inf
    #若已有记录，则直接返回
    if mem[i][j]!=-1:
        return mem[i][j]
    这段代码用于检查记忆化数组mem中是否已经记录了当前位置(i, j)
    # 的计算结果，并在有记录的情况下直接返回结果，避免重复计算。
    # 在函数min_path_sum_dfs_mem中，记忆化数组mem被用来缓存已经计算过的子问题的最小路径和。
    # 初始时，数组的所有元素都被初始化为一个特殊值 - 1，表示该位置的计算结果尚未被记录。
    # 当函数进入到(i, j)这个位置时，它会首先检查mem[i][j]是否等于 - 1。
    # 如果等于 - 1，说明当前位置的计算结果尚未被记录，这意味着我们需要进行正常的计算过程。
    # 但如果mem[i][j]不等于 - 1，则表示当前位置的计算结果已经被记录过了，避免了重复计算。
    # 此时，函数可以直接返回mem[i][j]，作为当前位置的最小路径和。这样可以提高程序的效率，避免重复的递归计算。
    #左边和上边单元格的最小路径代价
    up=min_path_sum_dfs_mem(grid,mem,i-1,j)
    left=min_path_sum_dfs_mem(grid,mem,i,j-1)
    #记录并返回左上角到（i，j)的最小路径代价
    mem[i][j]=min(left,up)+grid[i][j]
    return mem[i][j]
#它在暴力搜索的基础上引入了一个额外的记忆化数组 mem，
# 用于记录已经计算过的子问题的结果。在函数的开始部分，
# 会检查 mem 中是否已有当前位置的计算结果。如果有，就直接返回记录的结果，避免了重复计算。
# 而如果没有，函数则会执行正常的搜索和计算过程，计算出子问题的最小路径和，并将结果记录在 mem 数组中。
# 这样，在后续的搜索过程中，如果再次遇到相同的子问题，直接从 mem 中获取即可，避免了重复计算，提高了效率。

def min_path_sum_dp(grid:list[list[int]])->int:
    #最小路径和：动态规划
    n,m=len(grid),len(grid[0])
    #初始化dp表
    dp=[[0]*m for _ in range(n)]
    dp[0][0]=grid[0][0]
    #状态转移：首行
    for j in range(1,m):
        dp[0][j]=dp[0][j-1]+grid[0][j]
    #状态转移，首列
    for i in range(1,n):
        dp[i][0]=dp[i-1][0]+grid[i][0]
    #状态转移：其余行和列
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j]=min(dp[i][j-1],dp[i-1][j])+grid[i][j]
    return dp[n-1][m-1]

def min_path_sum_dp_comp(grid: list[list[int]]) -> int:
    """最小路径和：空间优化后的动态规划"""
    n, m = len(grid), len(grid[0])
    # 初始化 dp 表
    dp = [0] * m
    # 状态转移：首行
    dp[0] = grid[0][0]
    for j in range(1, m):
        dp[j] = dp[j - 1] + grid[0][j]
    # 状态转移：其余行
    for i in range(1, n):
        # 状态转移：首列
        dp[0] = dp[0] + grid[i][0]
        # 状态转移：其余列
        for j in range(1, m):
            dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
    return dp[m - 1]


#0-1背包问题，暴力搜索
def knapsack_dfs(wgt:list[int],val:list[int],i:int,c:int)->int:
    #wgt：一个表示物品重量的整数列表。val：一个表示物品价值的整数列表。
    #i：当前考虑的物品索引。c：当前背包的剩余容量。
    #若已选完所有物品或背包无剩余容量，则返回价值0
    if i==0 or c==0:
        return 0
    #若超过背包容量，则只能选择不放入背包
    if wgt[i-1]>c:
        return knapsack_dfs(wgt,val,i-1,c)
    #计算不放入和放入物品i的最大价值
    no=knapsack_dfs(wgt,val,i-1,c)
    yes=knapsack_dfs(wgt,val,i-1,c-wgt[i-1])+val[i-1]
    #i-1 表示我们不考虑当前物品 i，而是继续考虑前一个物品的选择。
    #c 保持不变，表示维持当前背包的容量不变。
    #val[i - 1]表示当前物品的价值
    #c - wgt[i-1] 表示背包的剩余容量减去当前物品的重量，表示当前物品被放入背包后剩余的容量。
    #返回两种方案中价值更大的那一个
    return max(no,yes)

def knapsack_dfs_mem(
        wgt:list[int],val:list[int],mem:list[list[int]],i:int,c:int
)->int:
    #0-1背包：记忆化搜索
    #若已选完所有物品或背包无剩余容量，则返回价值0
    if i==0 or c==0:
        return 0
    #若已有记录，则直接返回
    if mem[i][c]!=-1:
        return mem[i][c]
    #若超过背包容量，则只能选择不放入背包
    if wgt[i-1]>c:
        return knapsack_dfs_mem(wgt,val,mem,i-1,c)
    #计算不放入和放入物品i的最大价值
    no=knapsack_dfs_mem(wgt,val,mem,i-1,c)
    yes=knapsack_dfs_mem(wgt,val,mem,i-1,c-wgt[i-1])+val[i-1]
    #记录并返回两种方案中价值更大的那一个
    mem[i][c]=max(no,yes)
    return mem[i][c]

def knapsack_dp(wgt:list[int],val:list[int],cap:int)->int:
    #0-1背包：动态规划
    n=len(wgt)
    #初始化dp表
    dp=[[0]*(cap+1) for _ in range(n+1)]
    #状态转移
    for i in range(1,n+1):
        for c in range(1,cap+1):
            if wgt[i-1]>c:
                #若超过背包容量，则不选物品i
                dp[i][c]=dp[i-1][c]
            else:
                #不选和选物品i这两种方案的较大值
                dp[i][c]=max(dp[i-1][c],dp[i-1][c-wgt[i-1]]+val[i-1])
    return dp[n][cap]

def knapsack_dp_comp(wgt:list[int],val:list[int],cap:int)->int:
    #0-1背包：空间优化后的动态规划
    n=len(wgt)
    #初始化dp表
    dp=[0]*(cap+1)
    #状态转移
    for i in range(1,n+1):
        #倒序遍历
        for c in range(cap,0,-1):
            if wgt[i-1]>c:
                #若超过背包容量，则不选物品i
                dp[c]=cp[c]
            else:
                #不选和选物品i这两种方案的较大值
                dp[c]=max(dp[c],dp[c-wgt[i-1]]+val[i-1])
    return dp[cap]

def unbounded_knapsack_dp(wgt:list[int],val:list[int],cap:int)->int:
    #完全背包：动态规划
    n=len(wgt)
    #初始化dp表
    dp=[[0]*(cap+1) for _ in range(n+1)]
    #状态转移
    for i in range(1,n+1):
        for c in range(1,cap+1):
            if wgt[i-1]>c:
                #若超过背包容量，则不选物品i
                dp[i][c]=dp[i-1][c]
            else:
                #不选和选物品i这两种方案的较大值
                dp[i][c]=max(dp[i-1][c],dp[i][c-wgt[i-1]]+val[i-1])
    return dp[n][cap]


#完全背包，动态规划空间优化
def unbounded_knapsack_dp_comp(wgt:list[int],val:list[int],cap:int)->int:
    n=len(wgt)
    #初始化dp表
    dp=[0]*(cap+1)
    #状态转移
    for i in range(1,cap+1):
        if wgt[i-1]>c:
            #若超过背包容量，则不选物品i
            dp[c]=dp[c]
        else:
            #不选和选物品i这两种方案的较大值
            dp[c]=max(dp[c],dp[c-wgt[i-1]]+val[i-1])
    return dp[cap]

def coin_change_dp(coins:list[int],amt:int)->int:
    #零钱兑换：动态规划
    n=len(coins)
    MAX=amt+1
    #初始化dp表
    dp=[[0]*(amt+1) for _ in range(n+1)]
    #状态转移：首行首列
    for a in range(1,amt+1):
        dp[0][a]=MAX
    #状态转移：其余行和列
    for i in range(1,n+1):
        for a in range(1,amt+1):
            if coins[i-1]>a:
                #若超过目标金额，则不选硬币i
                dp[i][a]=dp[i-1][a]
            else:
                #不选和选硬币i这两种方法的较小值
                dp[i][a]=min(dp[i-1][a],dp[i][a-coins[i-1]]+1)
    return dp[n][amt] if dp[n][amt]!=MAX else -1

def coin_change_dp_comp(coins: list[int], amt: int) -> int:
    """零钱兑换：空间优化后的动态规划"""
    n = len(coins)
    MAX = amt + 1
    # 初始化 dp 表
    dp = [MAX] * (amt + 1)
    dp[0] = 0
    # 状态转移
    for i in range(1, n + 1):
        # 正序遍历
        for a in range(1, amt + 1):
            if coins[i - 1] > a:
                # 若超过目标金额，则不选硬币 i
                dp[a] = dp[a]
            else:
                # 不选和选硬币 i 这两种方案的较小值
                dp[a] = min(dp[a], dp[a - coins[i - 1]] + 1)
    return dp[amt] if dp[amt] != MAX else -1

def coin_change_ii_dp(coins: list[int], amt: int) -> int:
    """零钱兑换 II：动态规划"""
    n = len(coins)
    # 初始化 dp 表
    dp = [[0] * (amt + 1) for _ in range(n + 1)]
    # 初始化首列
    for i in range(n + 1):
        dp[i][0] = 1
    # 状态转移
    for i in range(1, n + 1):
        for a in range(1, amt + 1):
            if coins[i - 1] > a:
                # 若超过目标金额，则不选硬币 i
                dp[i][a] = dp[i - 1][a]
            else:
                # 不选和选硬币 i 这两种方案之和
                dp[i][a] = dp[i - 1][a] + dp[i][a - coins[i - 1]]
    return dp[n][amt]

def coin_change_ii_dp_comp(coins: list[int], amt: int) -> int:
    """零钱兑换 II：空间优化后的动态规划"""
    n = len(coins)
    # 初始化 dp 表
    dp = [0] * (amt + 1)
    dp[0] = 1
    # 状态转移
    for i in range(1, n + 1):
        # 正序遍历
        for a in range(1, amt + 1):
            if coins[i - 1] > a:
                # 若超过目标金额，则不选硬币 i
                dp[a] = dp[a]
            else:
                # 不选和选硬币 i 这两种方案之和
                dp[a] = dp[a] + dp[a - coins[i - 1]]
    return dp[amt]

def edit_distance_dp(s:str,t:str)->int:
    #编辑距离：动态规划
    n,m=len(s),len(t)
    dp=[[0]*(m+1) for _ in range(n+1)]
    #状态转移：首行首列
    for i in range(1,n+1):
        dp[1][0]=i
    for j in range(1,m+1):
        d[0][j]=j
    #状态转移：其余行和列
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1]==t[j-1]:
                #若两字符相等，则直接跳过此两字符
                dp[i][j]=dp[i-1][j-1]
            else:
                #最小编辑步数=插入，删除，替换这三种操作的最小编辑步数+1
                dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
    return dp[n][m]

def edit_distance_dp_comp(s:str,t:str)->int:
    #编辑距离：空间优化后的动态规划
    n,m=len(s),len(t)
    dp=[0]*(m+1)
    #状态转移：首行
    for j in range(1,m+1):
        dp[j]=j
    #状态转移：其余行
    for j in range(1,n+1):
        #状态转移：首列
        leftup=dp[0] #暂存dp[i-1,j-1]
        dp[0]+=1
        #状态转移：其余列
        for j in range(1,m+1):
            temp=dp[j]
            if s[i-1]==t[j-1]:
                #若两字符相等，则直接跳过此两字符
                dp[j]=leftup
            else:
                #最小编辑步数=插入，删除，替换这三种操作的最小编辑步数+1
                dp[j]=min(dp[j-1],dp[j],leftup)+1
            leftup=temp #更新为下一轮的dp[i-1,j-1]
        return dp[m]