# 李佳朗
# 开发时间：2023
#回溯算法
def pre_order(root:TreeNode):
    if root is None:
        return
    #尝试
    path.append(root)
    if root.val==7:
        res.append(root)
    pre_order(root.left)
    pre_order(root.right)
    #回退
    path.pop()

# 在二叉树中搜索所有值为7的节点，请返回根节点到这些节点的路径
# 并要求路径中不包含值为3的节点。

def pre_order(root:TreeNode):
    #剪枝
    if root is None or root.val==3:
        return
    #尝试
    path.append(root)
    if root.val==7:
        #记录解
        res.append(list(path))
    pre_order(root.left)
    pre_order(root.right)
    #回退
    path.pop()

#全排列问题
def backtrack(
        state:list[int],choices:list[int],selected:list[bool],res:list[list[int]]
):
    #回溯算法：全排列I
    #当状态长度等于元素数量时，记录解
    if len(state)==len(choices):
        res.append(list(state))
        return
    #遍历所有选择
    for i ,choice in enumerate(choices):
        #剪枝：不允许重复选择元素
        if not selected[i]:
            #尝试：做出选择，更新状态
            selected[i]=True
            state.append(choice)
            #进行下一轮选择
            backtrack(state,choices,selected,res)
            #回退：撤销选择，恢复到之前的状态
            selected[i]=False
            state.pop()
def permutations_i(nums:list[int])->list[list[int]]:
    #全排列I
    res=[]
    backtrack(state=[],choices=nums,selected=[False]*len(numns),res=res)
    return res

def backtrack(
        state:list[int],choices:list[int],selected:list[bool],res:list[list[int]]
):
    #回溯算法，当状态长度等于元素数量时，记录解
        if len(state)==len(chioces):
            res.append(list(state))
            return
        #遍历所有选择
        duplicated=set[int]()
        for i,choice in enumerate(choices):
            #剪枝：不允许重复选择的元素且不允许重复相同的元素
            if not selected[i] and choice not in duplicated:
                #尝试：做出选择，更新状态
                duplicated.add(choice) #记录选择过的元素值
                selected[i]=True
                state.append(choice)
                #进行下一轮选择
                backtrack(state,choices,selected,res)
                #回退：撤销选择，恢复到之前的状态
                selected[i]=False
                state.pop()
def permutations_ii(nums:list[int])->list[list[int]]:
    res=[]
    backtrack(state=[],choices=nums,selected=[False]*len(nums),res=res)
    return res

def backtrsack(
        state:list[int],
        target:int,
        total:int,
        choices:list[int],
        res:list[list[int]]
):
    #回溯算法：子集和I
    #子集和等于target时，记录解
    if total==target:
        res.append(list(state))
        return
    #遍历所有选择
    for i in range(len(choices)):
        #剪枝：若子集和超过target,则跳过选择
        if total+choice[i]>target:
            continue
        #尝试：做出选择，更新元素和total
        state.append(choice[i])
        #进行下一轮选择
        backtrack(state,target,total+choice[i],choices,res)
        #回退：撤销选择，恢复到之前的状态
        state.pop()
def subset_sum_i_naive(nums:list[int],target:int)->list[list[int]]:
    #求解子集和I（包括重复子集）
    state=[]  #状态（子集）
    state=0 #子集和
    res=[] #结果列表（子集列表）
    backtrack(state,target,total,nums,res)
    return res

def backtrack(
        state:list[int],target:int,choices:list[int],start:int,res:list[list[int]]
):
    #回溯算法：子集和I
    #子集和等于target时，记录解
    if target==0:
        res.append(list(state))
        return
    #遍历所有选择
    #剪枝二：从start开始遍历，避免生成重复子集
    for i in range(start,len(choices)):
        #剪枝一：若子集和超过target,则直接结束循环
        #这是因为数组已排序，后边元素更大，子集和一定超过target
        if target-choice[i]<0:
            break
            #尝试：做出选择，更新target,start
        state.append(choice[i])
        #进行下一轮选择
        backtrack(state,target-choices[i],choices,i,res)
        #回退：撤销选择，恢复到之前的状态
        state.pop()
def subset_sum_i(nums:list[int],target:int)->list[list[int]]:
    #求解子集和I
    state=[]   #状态（子集）
    nums.sort()
    start=0
    res=[]
    backtrack(state,target,nums,start,res)
    return res

    if target == 0:
        res.append(list(state))
    return
#遍历所有选择
#剪枝二：从start开始遍历，避免生成重复子集
#剪枝三：从start开始遍历，避免重复选择同意元素
for i in range(start,len(choices)):
    #剪枝一：若子集和超过target,则直接结束循环
    #这是因为数组已排序，后边元素更大，子集和一定超过target
    if target-choices[i]<0:
        break
    #剪枝四：如果该元素与左边元素相等，说明该搜索分支重复，直接跳过
    if i>start and choices[i]==choices[i-1]:
        continue
    #尝试：做出选择，更新target，start
    state.append(choices[i])
    #进行下一轮选择
    backtrack(state,target-choices[i],choices,i+1,res)
    #回退：撤销选择，恢复到之前的状态
    state.pop()
def subset_sum_ii(nums:list[int],target:int)->list[list[int]]:
    #求解子集和II
    state=[]  #状态（子集）
    nums.sort() #对nums进行排序
    start=0 #遍历起始点
    res=[]   #结果列表（子集列表）
    backtrack(state.target,nums,start,res)
    return res

def backtrack(
        row:int,
        n:int,
        state:list[list[str]],
        res:list[list[list[str]]],
        cols:list[bool],
        diages1:list[bool],
        disage2:list[bool],
):
    #回溯算法：N皇后
    #当放置完所有行时，记录解
    if row==n:
        res.append([list(row) for row in state])
        return
    #遍历所有列
    for col in range(n):
        #计算该格子对应的主对角线和副对角线
        diag1=row-col+n-1
        diag2=row+col
        #剪枝：不允许该格子所在列，主对角线，副对角线上存在皇后
        if not cols[col] and not diags1[diag1] and not diags2[diag2]:
            #尝试：将皇后放置在该格子
            state[row][col]='Q'
            cols[col]=diags1[diag1]=diages2[diag2]=True
            #放置下一行
            backtrack(row+1,n,state,res,cols,diags1,diags2)
            #回退：将该格子恢复为空位
            state[row][col]="#"
            cols[col]=diags1[diag1]=diags2[diag2]=False
def n_queens(n:int)->list[list[list[str]]]:
    #求解N皇后
    #初始化n*n大小的棋盘，其中“Q”代表皇后，‘#’代表空位
    state=[['#'for _ in range(n)]for _ in range(n)]
    cols=[False]*n #记录列是否有皇后
    diags1=[False]*(2*n-1)  #记录主对角线上是否有皇后
    diags2=[False]*(2*n-1)  #记录副对角线上是否有皇后
    res=[]
    backtrack(0,n,state,res,cols,diags1,diags2)
    return res