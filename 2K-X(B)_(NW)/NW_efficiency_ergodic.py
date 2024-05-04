from prettytable import PrettyTable
from NW_efficiency_optimization import NW_E_OPT
from NW_uniform_distribution import NW_UD_JUDGEMENT
from NW_H_av_t import NW_H_av_t
import csv
import math

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

n_input = 3000  # 输入转速
t_input = 10  # 输入转矩

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
                results.append([zs, zp1, zp2, zr, i_s_H, eta, ns_H, np_H, ts, tp])

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
]
for result in results:
    table.add_row(result)

print("原始表格：")
print(table)

"""将数据按效率从高到低排序"""
sorted_results = sorted(results, key=lambda x: x[-1], reverse=True)
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
]
for result in sorted_results:
    table_sorted.add_row(result)

print("\n效率降序表格：")
print(table_sorted)

"""将结果写入csv文件"""
with open(
    "2K-X(B)_(NW)/NW_output/NW_efficiency_optimization.csv", "w", newline=""
) as f:
    writer = csv.writer(f)
    writer.writerow(
        ["zs", "zp1", "zp2", "zr", "i_s_H", "eta", "ns_H", "np_H", "ts", "tp"]
    )
    writer.writerows(sorted_results)