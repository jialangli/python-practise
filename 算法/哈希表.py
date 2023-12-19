# 李佳朗
# 开发时间：2023
hamp:dict={}
hmap[12836]='小哈'
hmap[15937]='小啰'
hmap[16750]='小算'
name:str=hamp[15937]
hamp.pop(10583)
name:str=hamp[15937]
hamp.pop(10503)
for key,value in hmap.keys():
    print(key,"->",value)   #单独遍历键key
for key in hmap.keys():
    print(key)
for value in hamp.values(): #单独遍历值 value
    print(value)
index=hash(key)%capacity
class Pair:
    def __init__(self,key:int,val:str):
        self.key=key
        self.val=val
class ArrayHashMap:
    def __init__(self):
        self.buckets:list[Pair|None]=[None]*100
        #初始化数组，包含100个桶
    def hash_func(self,key:int)->int:
        #"哈希函数"
        index=key%100
        return index
    def get(self,key:int)->str:
        index:int=self.hash_func(key)
        pair:Pair=self.buckets[index]
        if pair is None:
            return None
        return  pair.val  #查询操作
    def put(self,key:int,val:str):
        pair=Pair(key,val)
        index:int=self.hash_func(key)
        self.buckets[index]=pair
    def remove(self,key:int):#删除操作
        index:int=self.hash_func(key)
        #置为None,代表删除
        self.buckets[index]=None
    def entry_set(self)->list[Pair]:
        result:list[Pair]=[]#获取所有的键值对
        for pair in self.buckets:
            if pair is not None:
                result.append(pair)
        return result
    def key_set(self)->list[int]:
        result=[]#获取所有的键
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.key)
        return result
    def value_set(self)->list[str]:
        result=[]#获取所有值
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.val)
        return result
    def print(self):
        for pair in self.buckets:
            if pair is not None:#打印哈希表
                print(pair.key,"->",pair.val)
class HashMapChaining:
    def __init__(self):
        self.size=0   #键值对数量
        self.capacity=4#哈希表容量
        self.load_thres=2.0/3.0 # 触发扩容的负载因子阈值
        self.extend_ratio=2 #扩容倍数
        self.buckets=[[] for _ in range(self.capacity)]#桶数组
    def hash_func(self,key:int)->int:
        return key%self.capacity
    def load_facter(self)->float:
        return self.size/self.capacity
    def get(self,key:int)->str|None:
        index=self.hash_func(key)
        bucket=self.buckets[index]#查询操作
        #遍历桶，若找到key则返回对应val
        for pair in bucket:
            if pair.key==key:
                return pair.val
        #若未找到key则返回None
        return None
    def put(self,key:int,val:str):
        if self.load_factor()>self.load_thres:#当负载因子超过阈值时，执行扩容
            self.extend()
        index=self.hash_func(key)
        bucket=self.buckets[index]#遍历桶，若遇到指定key，则更新对应val并返回
        for pair in bucket:
            if pair.key==key:
                pair.val=val
                return
            #若无该key，则将键值对添加至尾部
        pair=Pair(key,val)
        bucket.append(pair)
        self.size+=1
    def remove(self,key:int):
        #删除操作
        index=self.hash_func(key)
        bucket=self.buckets[index]
        #遍历桶，从中删除键值对
        for pair in bucket:
            if pair.key==key:
                bucket.remove(pair)
                self.size-=1
                break
    def extend(self):
        #扩容哈希表
        #暂存原哈希表
        buckets=self.buckets
        #初始化扩容后的新哈希表
        self.capacity*=self.extend_ratio
        self.buckets=[[]for _ in range(self.capacity)]
        self.size=0
        #将键值对从原哈希表搬运至新哈希表
        for bucket in buckets:
            for pair in bucket:
                self.put(pair.key,pair.val)
    def print(self):
        #打印哈希表
        for bucket in self.buckets:
            res=[]
            for pair in bucket:
                res.append(str(pair.key)+"->"+pair.val)
            print(res)

def add_hash(key:str)->int:
    hash=0      #加法哈希
    modulus=1000000007
    for c in key:
        hash += ord(c)
    return hash % modulus
def mul_hash(key:str)->int:
    #乘法哈希
    hash=0
    modulus=1000000007
    for c in key:
        hash=31*hash+ord(c)
    return hash%modulus
def xor_hash(key:str)->int:
    hash=0 #异或哈希
    modulus=1000000007
    for c in key:
        hash^=ord(c)
    return hash%modulus
def rot_hash(key:str)->int:
    hash=0
    modulus=1000000007
    for c in key:
        hash=(hash<<4)^(hash>>28)^ord(c)
    return hash%modulus