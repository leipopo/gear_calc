# 此脚本用于遍历NW型行星减速器的参数空间，找到效率最高的设计方案，同时得出校核所需转速转矩

from prettytable import PrettyTable
from NW_efficiency_optimization import NW_E_OPT
from NW_uniform_distribution import NW_UD_JUDGEMENT
from NW_H_av_t import NW_H_av_t
import csv
import math

"基本参数与遍历范围设置"
n_p = 3  # 行星轮数量
m1 = 0.5  # 一级模数
m2 = 0.6  # 二级模数

min_zs = 12  # 太阳齿数下限
max_zs = 36  # 太阳齿数上限
min_zp2 = 15  # 二级行星齿数下限
max_rs_dp1 = 60  # 一级行星基准分度圆半径上限


min_i = 10  # 速比下限
max_i = 30  # 速比上限

max_dr = 50  # 齿圈基准分度圆直径上限
max_zr = int(max_dr / m2)  # 齿圈最大齿数
min_eta = 0.85  # 最小效率（确保效率不会太低）

n_input = 3000  # 输入额定转速
t_input = 2.1  # 输入额定转矩
t_input_peaks_ratio = 5  # 输入转矩峰值与额定值的比值

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
                if not NW_UD_JUDGEMENT(zs=zs, zp1=zp1, zp2=zp2, zr=zr, n_p=n_p):
                    continue
                if zr > max_zr:
                    continue
                i_s_H = (zs * zp2 + (zp1 * zr)) / (zs * zp2)
                if (i_s_H > max_i) or (i_s_H < min_i):
                    continue
                eta = NW_E_OPT(N_p=n_p, zs=zs, zp1=zp1, zp2=zp2, zr=zr)
                [ns_H, np_H, nr_H, ts, tp, tr] = NW_H_av_t(
                    [m1, m2, zs, zp1, zp2, zr, n_p, n_input, t_input]
                )
                if eta < min_eta:
                    continue
                results.append(
                    [
                        zs,
                        zp1,
                        zp2,
                        zr,
                        i_s_H,
                        eta,
                        ns_H,
                        np_H,
                        ts / n_p,
                        tp,
                        tp * t_input_peaks_ratio,
                    ]
                )

"""使用prettytable库输出结果"""

table = PrettyTable()
table.field_names = [
    "zs",
    "zp1",
    "zp2",
    "zr",
    "i_s_H",
    "eta",
    "ns_H",
    "np_H",
    "ts",
    "tp",
    "tp_peak",
]
for result in results:
    table.add_row(result)

print("原始表格：")
print(table)

"""将数据按效率从高到低排序"""
sorted_results = sorted(results, key=lambda x: x[5], reverse=True)
table_sorted = PrettyTable()
table_sorted.field_names = [
    "zs",
    "zp1",
    "zp2",
    "zr",
    "i_s_H",
    "eta",
    "ns_H",
    "np_H",
    "ts",
    "tp",
    "tp_peak",
]
for result in sorted_results:
    table_sorted.add_row(result)

print("\n效率降序表格：")
print(table_sorted)

"""将结果写入csv文件"""
with open(
    "2K-H(B)_(NW)/NW_output/NW_efficiency_optimization.csv", "w", newline=""
) as f:
    writer = csv.writer(f)
    writer.writerow(
        [
            "zs",
            "zp1",
            "zp2",
            "zr",
            "i_s_H",
            "eta",
            "ns_H",
            "np_H",
            "ts",
            "tp",
            "tp_peak",
        ]
    )
    writer.writerows(sorted_results)
