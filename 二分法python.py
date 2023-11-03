#二分法  第一种
def second(list,item):
    low=0
    high=len(list)-1
    while low<=high:
        mid=(low+high)//2
        if item==list[mid]:
            return mid
        if item<list[mid]:
            high=mid-1
        else:
            low=mid+1
my_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
a=second(my_list,7)
print(a)

#二分法  第二种
def binary_search(list,item):
    low=0;
    high=len(list)-1
    while low<=high:
          mid=(high+low)//2
          guess=int(list[mid])
          if guess==item:
              return mid
          if guess>item:
              high=mid-1
          else:
              low=mid+1
my_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

a=binary_search(my_list,5)
print(a)