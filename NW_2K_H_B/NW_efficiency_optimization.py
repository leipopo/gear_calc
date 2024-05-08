# 该脚本用于遍历计算2K-H(B)型(NM)行星减速在不同齿数下的效率
import math

"""
参考文献
行星齿轮传动设计 第二版 绕振纲P150表6-1、p151公式6-37
"""


def NW_E_OPT(
    epsilon1=1.05, epsilon2=1.2, f_m=0.06, N_p=3, zs=18, zp1=45, zp2=15, zr=63
):
    """
    计算NW型行星减速器的效率
    符号定义
    -----------
    太阳齿: s
    一级行星: p1
    二级行星: p2
    齿圈: r
    -----------
    齿数: z
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
    psai_m_x_1 = (
        # 2 * math.pi * f_m * (1 / zs + 1 / zp1) * (1 - epsilon1 + 0.5 * epsilon1**2)
        math.pi
        / 2
        * epsilon1
        * f_m
        * (1 / zs + 1 / zp1)
    )
    # 二级啮合损失系数
    psai_m_x_2 = (
        # 2 * math.pi * f_m * (1 / zp2 - 1 / zr) * (1 - epsilon2 + 0.5 * epsilon2**2)
        math.pi
        / 2
        * epsilon2
        * f_m
        * (1 / zp2 - 1 / zr)
    )
    # 总啮合损失系数
    psai_m_x = (psai_m_x_1 + psai_m_x_2) * N_p
    # 效率
    eta = 1 - (zr * zp1 / (zs * zp2 + zr * zp1)) * psai_m_x
    return eta


# N_P = 3
# Z_S = 18
# Z_P1 = 45
# Z_P2 = 15
# Z_R = 63
# print(NW_E_OPT())
