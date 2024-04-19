# 该脚本用于计算行星减速的齿轮安装偏转角度
import math

'''基本参数定义与传动比计算'''

# 模数与齿数定义
np = 3  # 行星轮数量
zs = 8  # 太阳轮齿数
zp = 14  # 一级行星轮齿数
zr= 37 # 二级齿数

'''偏转角度计算：用于对阵列后齿廓进行旋转对位'''

N=360*(zr%np)
D=np*zp

theta_rotate = N/D

print("分子为：",N)
print("分母为：",D)
print("若行星为顺时针旋转得到则为：-",N,"/",D)
print("若行星为逆时针旋转得到则为：",N,"/",D)
print("行星轮系减速比：",1-(zr/zs))