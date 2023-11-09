#练习3：输入三条边长，如果能构成三角形就计算周长和面积。
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a+b>c and a+c>b and b+c>a:
    C=a+b+c
    p = (a + b + c) / 2
    S=(p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("三角形的周长为：",C)
    print("三角形的面积为：",S)
else:
    print("不构成三角形")