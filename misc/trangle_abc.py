#设a,b,c是一个三角形的三条边，切满足，a+c+c=20,a+b>c,a+c>b,b+c>a,a>0,b>0,c>0,求a,b，c的解
#思路是这样的，让a从1变化到19，这是最外层循环，里面还有b从1变化到19，这是内层循环，然后让c从1变化到19
#如果满足条件则输出a，b，c的值即可。

count =0;
for a in range(1,19):
    for b in range(1,19):
        for c in range(1,19):
            if a+b+c==20 and a+b>c and a+c>b and b+c>a :
                count=count+1
                print(a,b,c)
print("共有{}种可能".format(count))