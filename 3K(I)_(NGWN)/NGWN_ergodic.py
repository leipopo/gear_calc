# 该脚本用于遍历计算3K(I)型行星减速器的参数空间，找到效率最高的设计方案，同时得出校核所需转速转矩

from prettytable import PrettyTable
from NGWN_efficiency_optimization import NGWN_E_OPT
from NGWN_H_av_t import NGWN_H_av_t
import math
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

n_p = 5  # 行星轮数量
m1 = 0.6  # 一级模数
m2 = 0.6  # 二级模数


min_zs = 21  # 太阳齿数下限
max_zs = 30  # 太阳齿数上限
min_zp1 = 12  # 一级行星齿数下限
min_zp2 = 12  # 二级行星齿数下限
min_i = 24  # 速比下限
max_i = 30  # 速比上限

h_r_D = 2  # 齿根到齿外圆的距离
max_dr1 = 53  # 一级齿圈外径圆直径上限
max_zr1 = int((max_dr1 - h_r_D * 2 - m1 * 1.25 * 2) / m1)  # 一级齿圈最大齿数
max_dr2 = 53  # 二级齿圈外径圆直径上限
max_zr2 = int((max_dr2 - h_r_D * 2 - m2 * 1.25 * 2) / m2)  # 二级齿圈最大齿数
min_eta = 0.90  # 最小效率（确保效率不会太低）

n_input = 3000  # 输入额定转速
t_input = 2.1  # 输入额定转矩
t_input_peaks_ratio = 5  # 输入转矩峰值与额定值的比值

results = []  # 初始化结果表格

"""遍历开始"""
for zs in range(min_zs, max_zs + 1):
    for zp1 in range(min_zp1, int(zs * 6.464) + 1):  # 行星轮干涉条件
        for zr1 in range(zs + 2 * zp1, zs + 2 * zp1 + n_p + 1):
            if zp1 < min_zp1:
                continue
            if (zs + zr1) % n_p == 0:
                for zr2 in range(
                    int((min_zs + min_zp1) * m1 / m2 + min_zp2), max_zr2 + 1
                ):
                    if (zr1 > max_zr1) or (zr2 > max_zr2):  # 限定齿圈最大齿数
                        continue
                    zp2 = int(zr2 - m1 / m2 * (zs + zp1))
                    if zp2 < min_zp2:
                        continue
                    if (zp2 * zr1) / (zp1 * zr2) == 1:  # 判定减速比不能无穷大
                        continue
                    # print(zs, zp1, zp2, zr1, zr2)
                    eta_forward, eta_backward = NGWN_E_OPT(
                        zs=zs, zp1=zp1, zp2=zp2, zr1=zr1, zr2=zr2
                    )
                    ns_H, np_H, ts, tp1, tp2 = NGWN_H_av_t(
                        m_1=m1,
                        m_2=m2,
                        z_s=zs,
                        z_p1=zp1,
                        z_p2=zp2,
                        z_r1=zr1,
                        z_r2=zr2,
                        N_p=n_p,
                        t=t_input,
                        n=n_input,
                    )
                    i = (1 + zr1 / zs) / (1 - (zp2 * zr1) / (zp1 * zr2))
                    # print(zs, zp1, zp2, zr1, zr2)
                    # print(i)
                    # print(eta_forward)
                    # print(eta_backward)
                    if max_i > abs(i) > min_i:  # 限定速比范围
                        # print(zs, zp1, zp2, zr1, zr2)
                        if eta_forward > min_eta:  # 限定效率
                            formatted_result = [
                                round(x, 4)
                                for x in [
                                    zs,
                                    zp1,
                                    zr1,
                                    zp2,
                                    zr2,
                                    i,
                                    eta_forward,
                                    eta_backward,
                                    ts / n_p,
                                    ns_H,
                                    tp1,
                                    tp2,
                                    np_H,
                                    tp2 * t_input_peaks_ratio,
                                ]
                            ]
                            results.append(formatted_result)

"""使用prettytable打印结果"""

pt = PrettyTable()
pt.field_names = [
    "齿数s",
    "齿数p1",
    "齿数r1",
    "齿数p2",
    "齿数r2",
    "传动比",
    "正向效率",
    "逆向效率",
    "S转矩",
    "S的H转速",
    "P1转矩",
    "P2转矩",
    "P的H转速",
    "P上的峰值转矩",
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
    "齿数r1",
    "齿数p2",
    "齿数r2",
    "传动比",
    "正向效率",
    "逆向效率",
    "S转矩",
    "S的H转速",
    "P1转矩",
    "P2转矩",
    "P的H转速",
    "P上的峰值转矩",
]
for result in sorted_results:
    pt_sorted.add_row(result)

print("\n正向效率降序表格:")
print(pt_sorted)

# 准备保存CSV文件
with open(
    "3K(I)_(NGWN)/NGWN_output/NGWN_efficiency_optimization.csv", "w", newline=""
) as csvfile:
    writer = csv.writer(csvfile)
    # 写入标题行
    writer.writerow(pt_sorted.field_names)

    # 写入表格数据
    for result in sorted_results:
        writer.writerow(result)

print("CSV文件已保存")
