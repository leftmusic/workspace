print('输入：')
renshu = int(input('请输入人数：'))
jg,yx = 0,0
for i in range(renshu):
    cj = int(input('请输入'))
    if cj >60:
        jg+=1
        if cj >85:
            yx+=1
print(f'{round(jg/renshu*100)}%\n{round(jg/renshu*100)}%')