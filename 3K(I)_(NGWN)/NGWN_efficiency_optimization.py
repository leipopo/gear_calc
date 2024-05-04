# 该脚本用于遍历计算NGWN型行星减速在不同齿数下的效率
import math

"""
参考文献
行星齿轮传动设计 第二版 绕振纲P157表6-2、p151公式6-37
"""


def NGWN_E_OPT(
    epsilon1=1,
    epsilon2=1,
    epsilon3=1,
    f_m=0.06,
    N_p=3,
    zs=9,
    zp1=12,
    zp2=13,
    zr1=33,
    zr2=34,
):
    """
    计算3K(I)型行星减速器的效率
    符号定义
    -----------
    太阳齿: s
    一级行星: p1
    二级行星: p2
    一级齿圈: r1
    二级齿圈: r2
    齿数: z
    -----------
    :param epsilon1: s与p1的重合度
    :param epsilon2: p1与r1的重合度
    :param epsilon3: p2与r2的重合度
    :param f_m: 啮合摩擦系数
    :param N_p: 行星轮数
    :param zs: 太阳齿数
    :param zp1: 一级行星齿数
    :param zp2: 二级行星齿数
    :param zr1: 一级齿圈齿数
    :param zr2: 二级齿圈齿数
    :return: 3K(I)型行星减速器的正向驱动效率和反向驱动效率
    """
    # 一级s_p1啮合损失系数
    # psai_m_x_1 = (
    #     2 * math.pi * f_m * (1 / zs + 1 / zp1) * (1 - epsilon1 + 0.5 * epsilon1**2)
    # )
    # psai_m_x_1_2 = math.pi / 2 * epsilon1 * f_m * (1 / zs + 1 / zp1)  # 太阳轮和一级行星
    # 一级p1_r1啮合损失系数
    # psai_m_x_2 = (
    #     2 * math.pi * f_m * (1 / zp1 - 1 / zr1) * (1 - epsilon2 + 0.5 * epsilon2**2)
    # )
    psai_m_x_2_2 = (
        math.pi / 2 * epsilon2 * f_m * (1 / zp1 - 1 / zr1)
    )  # 一级行星和一级齿圈
    # 一级p1_r1啮合损失系数
    # psai_m_x_3 = (
    #     2 * math.pi * f_m * (1 / zp2 - 1 / zr2) * (1 - epsilon3 + 0.5 * epsilon3**2)
    # )
    psai_m_x_3_2 = (
        math.pi / 2 * epsilon3 * f_m * (1 / zp2 - 1 / zr2)
    )  # 二级行星和二级齿圈

    # 总啮合损失系数
    psai_m_x_23 = (psai_m_x_2_2 + psai_m_x_3_2) * N_p

    print("齿数", zs, zp1, zp2, zr1, zr2)
    # print("一级s_p1啮合损失系数", psai_m_x_1)
    # print("一级s_p1啮合损失系数2", psai_m_x_1_2)
    # print("一级p1_r1啮合损失系数", psai_m_x_2)
    print("一级p1_r1啮合损失系数2", psai_m_x_2_2)
    # print("一级p1_r1啮合损失系数", psai_m_x_3)
    print("二级p2_r2啮合损失系数2", psai_m_x_3_2)
    print("总啮合损失系数", psai_m_x_23)
    # 效率
    i_s_r2 = (1 + zr1 / zs) / (1 - (zp2 * zr1) / (zp1 * zr2))
    print("i_s_r2", i_s_r2)
    p = zr1 / zs
    # print("p", p)
    if zr1 >= zr2:
        eta_forward = 0.98 / (1 + abs(i_s_r2 / (1 + p) - 1) * psai_m_x_23)  # zr1>zr2
        eta_backward = 0.98 * (1 - abs(i_s_r2 / (1 + p)) * psai_m_x_23)  # zr1>zr2
    else:
        eta_forward = 0.98 / (1 + abs(i_s_r2 / (1 + p)) * psai_m_x_23)  # zr2>zr1
        eta_backward = 0.98 * (1 - abs(i_s_r2 / (1 + p) + 1) * psai_m_x_23)  # zr2>zr1
    print("正向驱动效率", eta_forward)
    print("反向驱动效率", eta_backward)

    return [eta_forward, eta_backward]


# N_P = 3
# Z_S = 18
# Z_P1 = 45
# Z_P2 = 15
# Z_R = 63
# print(NW_E_OPT())
