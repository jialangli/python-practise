#冒泡排序
def bubblesort(a):
    n=len(a)
    for i in range(n-1,-1,-1):
       for j in range(0,i):
           if a[j]>a[j+1]:
             a[j],a[j+1]=a[j+1],a[j]
    return a
number=[2,3,6,4,10,9,8]
result=bubblesort(number)
print(result)
