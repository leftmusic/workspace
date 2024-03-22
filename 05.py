n = int(input())
num = input().split()
list=[]
for i in num:
    list.append(int(i))
gap = []
for i in range(1,n):
    gap.append(list[i]-list[i-1])
print(max(gap))