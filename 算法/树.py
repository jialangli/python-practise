# 李佳朗
# 开发时间：2023
#树
#二叉树
class TreeNode:
    def __init__(self,val:int):
        self.val:int=val   #节点值
        self.left:TreeNode|None=None  #左子节点引用
        self.right:TreeNode|None=None #右子节点引用

#初始化二叉树，初始化节点
n1=TreeNode(val=1)
n2=TreeNode(val=2)
n3=TreeNode(val=3)
n4=TreeNode(val=4)
n5=TreeNode(val=5)
#构建节点之间的引用（指针）
n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5

#插入与删除节点
p=TreeNode(0)
#在n1->n2中间插入节点p
n1.left=p
p.left=n2
#删除节点p
n1.left=n2

def level_order(root:TreeNode|None)->list[int]:
    #层序遍历
    #初始化队列，加入根节点
    queue:deque[TreeNode]=deque()
    queue.append(root)
    #初始化一个列表，用于保存遍历序列
    res=[]
    while queue:
        node:TreeNode=queue.popleft() #队列出队
        res.append(node.val) #保存节点值
        if node.left is not None:
            queue.append(node.left)  #左子节点入队
        if node.right is not None:
            queue.append(node.right) #右子节点入队
    return res

def pre_order(root:TreeNode|None): #前序遍历
    if root is None:
        return
    #访问优先级：根节点->左子树->右子树
    res.append(root.val)
    pre_order(root=root.left)
    pre_order(root=root.right)
def in_order(root:TreeNode|None):
    #中序遍历
    if root is None:
        return
    #访问优先级：左子树->根节点->右子树
    in_order(root=root.left)
    res.append(root.val)
    in_order(root=root.right)

def post_order(root:TreeNode|None):
    #后序遍历
    if root is None:
        return
    #访问优先级：左子树->右子树->根节点
    post_order(root=root.left)
    post_order(root=root.right)
    res.append(root.val)

    #二叉树的数组表示
    #使用None来表示空位
    tree=[1,2,3,4,None,6,7,8,9,None,12,None,None,15]


class ArrayBinaryTree:
    #数组下的二叉树类,给定某节点，获取它的值、左（右）子节点、父节点。
    #获取前序遍历、中序遍历、后序遍历、层序遍历序列。
    def __init__(self,arr:list[int|None]):
        self._tree=list(arr)
    def size(self):#节点数量
        return len(self._tree)
    def val(self,i:int)->int:
        #获取索引为i节点的值
        #若索引越界，则返回None，代表空位
        if i<0 or i>=self.size():
            return None
        return self._tree[i]
    def left(self,i:int)->int|None:
        #获取索引为i节点的左子节点的索引
        return 2*i+1
    def right(self,i: int)->int|None:
        "获取索引为i节点的右子节点的索引"
        return 2*i+2
    def parent(self,i:int)->int|None:
        #获取索引为i节点的父节点的索引
        return(i-1)//2
    def level_order(self)->list[int]:#层序遍历
        self.res=[]
        for i in range(self.size()):#直接遍历数组
            if self.val(i) is not None:
                self.res.append(self.val(i))
        return self.res
    #深度优先遍历
    def dfs(self,i:int,order:str):
        if self.val(i) is None:
            return
        #前序遍历
        if order=="pre":
            self.res.append(self.val(i))
        self.dfs(self.left(i),order)

#二叉搜索树的查找操作
def search(self,num:int)->TreeNode|None:
    #查找节点
    cur=self._root
    #循环查找，越过叶节点后跳出
    while cur is not None:
        #目标节点在cur的右子树中
        if cur.val<num:
            cur=cur.right
        #目标节点在cur的左子树中
        elif cui.val<num:
            cur=cur.left
        #找到目标节点，跳出循环
        else:
            break
    return cur

#插入节点
def insert(self,num:int):
    #插入节点
    #若树为空，则初始化根节点
    if self._root is None:
        self._root=TreeNode(num)
        return
    #循环查找，越过叶节点后跳出
    cur,pre=self._root,None
    while cur is not None:
        #找到重复的节点，直接返回
        if cur.val==num:
            return
        pre=cur
        #插入位置在cur的左子树中
        if cur.val<num:
            cur=cur.right
            #插入位置在cur的左子树中
        else:
            cur=cur.left
    #插入节点
    node=TreeNode(num)
    if pre.val<num:
        pre.right=node
    else:
        pre.left=node

class TreeNode:
    def __init__(self,val:int):
        self.val:int=val #节点值
        self.height:int = 0 #节点高度
        self.left:TreeNode|None= None #左子节点引用
        self.right:TreeNode|None=None #右子节点引用

def height(self,node:TreeNode|None)->int:
    #获取节点高度，空节点高度为-1，叶节点高度为0
    if node is not None:
        return node.height
    return -1
def update_height(self,node:TreeNode|None):
    #更新节点高度
    #节点高度等于最高子树+1
    node.height=max([self.height(node.left),self.height(node.right)])+1

def balance_factor(self,node:TreeNode|None)->int:
    #获取平衡因子
    #空节点平衡因子为0
    if node is None:
        return 0
    #节点平衡因子=左子树高度-右子树高度
    return self.height(node.left)-self.height(node.right)

def right_rotate(self,node:TreeNode|None):
    child=node.left
    grand_child=child.right
    #以child为原点，将node向右旋转
    child.right=node
    node.left=grand_child
    #更新节点高度
    self.update_height(node)
    self.update_height(child)
    #返回旋转后子树的根节点
    return child
def left_rotate(self,node:TreeNode|None)->TreeNode|None:
    #左旋操作
    child=node.right
    grand_child=child.left
    #以child为原点，将node向左旋转
    child.left=node
    node.right=grand_child
    #更新节点高度
    self.update_height(node)
    self.update_height(child)
    #返回旋转后子树的根节点