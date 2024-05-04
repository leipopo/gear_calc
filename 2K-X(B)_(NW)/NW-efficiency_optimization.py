# 该脚本用于遍历计算2Z-X(B)型(NM)行星减速在不同齿数下的效率
import math
from prettytable import PrettyTable
import csv

"""
符号定义
-----------
太阳齿：s
一级行星：p1
二级行星：p2
齿圈：r
-----------
模数：m
齿数：z
"""


def NW_E_OPT(
    epsilon1=1.05, epsilon2=1.2, f_m=0.06, N_p=3, zs=18, zp1=45, zp2=15, zr=63
):
    """
    计算NW型行星减速器的效率
    :param epsilon1: s与p1的重合度
    :param epsilon2: p2与r的重合度
    :param f_m: 啮合摩擦系数
    :param N_p: 行星轮数
    :param zs: 太阳齿数
    :param zp1: 一级行星齿数
    :param zp2: 二级行星齿数
    :param zr: 齿圈齿数
    :return: NW型行星减速器的效率
    """
    # 一级啮合损失系数
    phi_m_x_1 = (
        2 * math.pi * f_m * (1 / zs + 1 / zp1) * (1 - epsilon1 + 0.5 * epsilon1**2)
    )
    # 二级啮合损失系数
    phi_m_x_2 = (
        2 * math.pi * f_m * (1 / zp2 - 1 / zr) * (1 - epsilon2 + 0.5 * epsilon2**2)
    )
    # 总啮合损失系数
    phi_m_x = (phi_m_x_1 + phi_m_x_2) * N_p
    # 效率
    eta = 1 - (zr * zp1 / (zs * zp2 + zr * zp1)) * phi_m_x
    return eta


# N_P = 3
# Z_S = 18
# Z_P1 = 45
# Z_P2 = 15
# Z_R = 63
# print(NW_E_OPT())


"基本参数与遍历范围设置"
n_p = 3  # 行星轮数量
m1 = 0.55  # 一级模数
m2 = 0.75  # 二级模数

min_zs = 18  # 太阳齿数下限
max_zs = 27  # 太阳齿数上限
min_zp2 = 15  # 二级行星齿数下限
max_rs_dp1 = 60  # 一级行星半径上限


min_i = 10  # 速比下限
max_i = 13  # 速比上限

max_dr = 50  # 齿圈最大基准分度圆直径
max_zr = int(max_dr / m2)  # 齿圈最大齿数
min_eta = 0.85  # 最小效率（确保效率不会太低）

results = []  # 初始化结果表格

for zs in range(min_zs, max_zs + 1):
    max_zp1 = int((max_rs_dp1 - m1 * zs / 2) / m1)
    for zp1 in range(min_zp2, min(int(zs * 6.464), max_zp1) + 1):
        for zp2 in range(min_zp2, zp1):
            for zr in range(
                int((zs * m1 + zp1 * m1 + zp2 * m2) / m2),
                int((zs * m1 + zp1 * m1 + zp2 * m2) / m2) + 4,
            ):
                # 判断是否均布
                if (zs % n_p != 0) or (zr % n_p != 0):
                    if zs % n_p != 0:
                        E_A = zs / n_p
                        for i in range(1, 100):
                            if (zs + zr) / n_p + (1 - zp2 / zp1) * (
                                E_A + i - zs / n_p
                            ) != i and (zs + zr) / n_p + (1 - zp2 / zp1) * (
                                E_A - i - zs / n_p
                            ) != i:
                                continue
                    else:
                        E_A = math.ceil(zs / n_p)
                        for i in range(0, 100):
                            if (zs + zr) / n_p + (1 - zp2 / zp1) * (
                                E_A + i - zs / n_p
                            ) != i and (zs + zr) / n_p + (1 - zp2 / zp1) * (
                                E_A - i - zs / n_p
                            ) != i:
                                continue
                if zr > max_zr:
                    continue
                i_s_H = (zs * zp2 + (zp1 * zr)) / (zs * zp2)
                if (i_s_H > max_i) or (i_s_H < min_i):
                    continue
                eta = NW_E_OPT(N_p=n_p, zs=zs, zp1=zp1, zp2=zp2, zr=zr)
                if eta < min_eta:
                    continue
                results.append([zs, zp1, zp2, zr, i_s_H, eta])

"""使用prettytable库输出结果"""

table = PrettyTable()
table.field_names = ["zs", "zp1", "zp2", "zr", "i_s_H", "eta"]
for result in results:
    table.add_row(result)

print("原始表格：")
print(table)

"""将数据按效率从高到低排序"""
sorted_results = sorted(results, key=lambda x: x[-1], reverse=True)
table_sorted = PrettyTable()
table_sorted.field_names = ["zs", "zp1", "zp2", "zr", "i_s_H", "eta"]
for result in sorted_results:
    table_sorted.add_row(result)

print("\n效率降序表格：")
print(table_sorted)

"""将结果写入csv文件"""
with open("NW_efficiency_optimization.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["zs", "zp1", "zp2", "zr", "i_s_H", "eta"])
    writer.writerows(sorted_results)
