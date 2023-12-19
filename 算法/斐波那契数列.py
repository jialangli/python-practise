# 李佳朗
# 开发时间：2023
#效率低下的斐波那契数列
def digui(n):
    if n<=1:
        return n
    else:
        return digui(n-2)+digui(n-1)
print(digui(10))

#效率高的斐波那契数列
def good_digui(n):
    if n<=1:
        return (n,0)
    else:
        (a,b)=good_digui(n-1)
        return(a+b,a)