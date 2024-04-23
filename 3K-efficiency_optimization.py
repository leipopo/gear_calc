# 该脚本用于遍历计算3K(I)型行星减速在不同齿数下的效率
import math
from prettytable import PrettyTable
import csv

"""
符号定义
-----------
太阳齿：s
一级行星：p1
二级行星：p2
一级齿圈：r1
二级齿圈：r2
-----------
模数：m
齿数：z
"""

"基本参数与遍历范围设置"

n_p = 3  # 行星轮数量
m1 = 0.25  # 一级模数
m2 = 0.25  # 二级模数

min_delta_zr = -8  # 齿数差下限
max_delta_zr = 10
min_delta_zp = -4
max_delta_zp = +4

min_zs = 7  # 太阳齿数下限
max_zs = 12  # 太阳齿数上限
min_i = 25  # 速比下限
max_i = 30  # 速比上限

max_zr = 40  # 齿圈最大齿数（确保模数不会太低）
min_eta = 0.80  # 最小效率（确保效率不会太低）

results = []  # 初始化结果表格

"""遍历开始"""
for zs in range(min_zs, max_zs + 1):
    for zp1 in range(zs, int(zs * 6.464)):  # 行星轮干涉条件
        zr1 = zs + 2 * zp1
        if (zs + zr1) % n_p == 0:
            for delta_zr in range(min_delta_zr, max_delta_zr + 1):
                zr2 = zr1 + delta_zr
                if max(zr1, zr2) >= max_zr:  # 限定齿圈最大齿数
                    continue
                for delta_zp in range(min_delta_zp, max_delta_zp + 1):
                    zp2 = zp1 + delta_zp
                    if (zp2 * zr1) / (zp1 * zr2) == 1:  # 判定减速比不能无穷大
                        continue

                    """减速比计算"""
                    i = (1 + zr1 / zs) / (1 - (zp2 * zr1) / (zp1 * zr2))
                    p = zr1 / zs
                    """啮合效率计算"""
                    # 各啮合齿轮副重合度输入
                    epsilon_s_p1 = 1  # 太阳轮和一级行星
                    epsilon_p1_r1 = 1  # 一级行星和一级齿圈
                    epsilon_p2_r2 = 1  # 二级行星和二级齿圈
                    # 啮合摩擦系数
                    fm = 0.05
                    # 功率损失系数
                    psai_s_p1 = (
                        math.pi / 2 * epsilon_s_p1 * fm * (1 / zs + 1 / zp1)
                    )  # 太阳轮和一级行星
                    psai_p1_r1 = (
                        math.pi / 2 * epsilon_p1_r1 * fm * (1 / zp1 - 1 / zr1)
                    )  # 一级行星和一级齿圈
                    psai_p2_r2 = (
                        math.pi / 2 * epsilon_p2_r2 * fm * (1 / zp2 - 1 / zr2)
                    )  # 二级行星和二级齿圈
                    psai_r1_r2 = psai_p1_r1 + psai_p2_r2  # 总损失系数
                    if delta_zr >= 0:
                        eta_forward = 0.98 / (
                            1 + abs(i / (1 + p)) * psai_r1_r2
                        )  # zr2>zr1
                        eta_backward = 0.98 * (
                            1 - abs(i / (1 + p) + 1) * psai_r1_r2
                        )  # zr2>zr1
                    else:
                        eta_forward = 0.98 / (
                            1 + abs(i / (1 + p) - 1) * psai_r1_r2
                        )  # zr1>zr2
                        eta_backward = 0.98 * (
                            1 - (abs(i / (1 + p)) * psai_r1_r2)
                        )  # zr1>zr2
                    if max_i > abs(i) > min_i:  # 限定速比范围
                        if eta_forward > min_eta:  # 限定效率
                            formatted_result = [
                                round(x, 3)
                                for x in [
                                    zs,
                                    zp1,
                                    zp2,
                                    zr1,
                                    zr2,
                                    i,
                                    eta_forward,
                                    eta_backward,
                                ]
                            ]
                            results.append(formatted_result)

"""使用prettytable打印结果"""

pt = PrettyTable()
pt.field_names = [
    "齿数s",
    "齿数p1",
    "齿数p2",
    "齿数r1",
    "齿数r2",
    "传动比",
    "正向效率",
    "逆向效率",
]
for result in results:
    pt.add_row(result)  # 将元组转换为列表，以便prettytable处理

print("原始筛选表格:")
print(pt)

"""根据效率从高到低排序"""

sorted_results = sorted(results, key=lambda x: x[6], reverse=True)  # 根据正向效率排序

pt_sorted = PrettyTable()
pt_sorted.field_names = [
    "齿数s",
    "齿数p1",
    "齿数p2",
    "齿数r1",
    "齿数r2",
    "传动比",
    "正向效率",
    "逆向效率",
]
for result in sorted_results:
    pt_sorted.add_row(result)

print("\n正向效率降序表格:")
print(pt_sorted)

# 准备保存CSV文件
with open("results.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # 写入标题行
    writer.writerow(pt_sorted.field_names)

    # 写入表格数据
    for result in sorted_results:
        writer.writerow(result)

print("CSV文件已保存")
