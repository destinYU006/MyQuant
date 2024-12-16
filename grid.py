import numpy as np

#数据获取
max_1 =10
min_1 = 1
delt =max_1 -min_1

#设置网格等级和持仓量
count = np.arange(0,21,1)
price_m =  delt/20*count+1
holding_max = 100
holding_m = holding_max/20*count



print(price_m)
print(holding_m)
