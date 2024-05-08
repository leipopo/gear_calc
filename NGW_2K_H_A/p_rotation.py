# 该脚本用于计算NGW行星减速的齿轮安装偏转角度
import math

"""基本参数定义与传动比计算"""

# 模数与齿数定义
np = 5  # 行星轮数量
zs = 22  # 太阳轮齿数无太阳齿记为零
zp = 26  # 行星轮齿数
zr = 0  # 齿圈齿数无齿圈记为零

"""偏转角度计算：用于对阵列后齿廓进行旋转对位"""

for i in range(1, int(np / 2) + 1):
    if zs == 0:
        if zr == 0:
            print("无法计算")
            break
        else:
            n = 360 * i * zr
            d = np * zp
            # 求最简分数
            for j in range(1, 100):
                if n % j == 0 and d % j == 0:
                    n = n / j
                    d = d / j
            if d == 1:
                while n > 360:
                    n = n - 360
            print("分子为：", n)
            print("分母为：", d)
            print("若行星为顺时针旋转得到则为：-", n, "/", d)
            print("若行星为逆时针旋转得到则为：", n, "/", d)
    elif zr == 0:
        if zs == 0:
            print("无法计算")
            break
        else:
            n = 360 * i * zs
            d = np * zp
            for j in range(1, 100):
                if n % j == 0 and d % j == 0:
                    n = n / j
                    d = d / j
            if d == 1:
                while n > 360:
                    n = n - 360
            print("分子为：", n)
            print("分母为：", d)
            print("若行星为顺时针旋转得到则为：-", n, "/", d)
            print("若行星为逆时针旋转得到则为：", n, "/", d)
