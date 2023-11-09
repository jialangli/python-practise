#练习2：百分制成绩转换为等级制成绩。
#要求：如果输入的成绩在90分以上（含90分）A；80分-90分（权限90分）输出B；70分-80分（80分）输出C；60分-70分（明确70分）输出D；60分以下输出E。
score=float(input("请输入您的成绩"))
if score>=90:
    grade='A'
elif score>=80:
    grade='B'
elif score>=70:
    grade='C'
else:
    grade='D'
print("您的等级为：",grade)
