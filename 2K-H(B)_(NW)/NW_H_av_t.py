# 此脚本用于计算NW减速器相啮合齿轮的基准齿廓的相对转速和转矩
"""
参考文献
行星齿轮传动设计 第二版 绕振纲
P195 ..."N_L=60*N_x*t"...
p208 ..."T_1=T_a/n_p"...
p209 ..."T_1=T_b/n_p/zb*zd"...
"""


def NW_H_av_t(
    m_1=0.55,
    m_2=0.75,
    z_s=18,
    d_s=None,
    z_p1=45,
    d_p1=None,
    z_p2=15,
    d_p2=None,
    z_r=63,
    d_r=None,
    N_p=3,
    t=2.1,
    n=3000,
):

    # 计算S和P1的理论啮合半径
    r_s = m_1 * z_s / 2 if d_s == None else d_s / 2
    # 计算P1的理论啮合半径
    r_p1 = m_1 * z_p1 / 2 if d_p1 == None else d_p1 / 2
    # 计算P2的理论啮合半径
    r_p2 = m_2 * z_p2 / 2 if d_p2 == None else d_p2 / 2
    # 计算R的理论啮合半径
    r_r = m_2 * z_r / 2 if d_r == None else d_r / 2
    # 计算双联行星中心距
    r_p1_p2 = (
        ((m_1 * z_p1 + m_1 * z_s) / 2 + (m_2 * z_r - m_2 * z_p2) / 2) / 2
        if d_s == None or d_r == None or d_p1 == None or d_p2 == None
        else ((d_s + d_p1) / 2 + (d_r - d_p2) / 2) / 2
    )
    # 计算S切向力
    F_s_p1 = t / N_p / r_s
    # 计算P1切向力
    F_p1_s = -F_s_p1
    # 计算P2切向力
    F_r_p2 = r_p1 / r_p2 * F_s_p1
    # print("F_s_p1:", F_s_p1)
    # print("F_r_p2:", F_r_p2)
    # 计算P1P2转矩
    t_p1p2 = F_r_p2 * r_p2
    # print("P1P2转矩:", t_p1p2)
    t_p1p2 = F_s_p1 * r_p1
    # print("P1转矩:", t_p1p2)
    # 计算行星架切向力
    F_H_p1p2 = -(F_s_p1 + F_r_p2)
    # 计算行星架转矩
    t_H_p1p2 = F_H_p1p2 * r_p1_p2 * N_p
    t_p1p2_H = -t_H_p1p2
    # 计算R切向力
    F_p2_r = r_p1 * t / N_p / r_p2 / r_s
    # F_r_p2 = -F_p2_r
    # 计算R转矩
    t_r_p2 = N_p * r_r * F_p2_r

    # print("行星架转矩:", t_p1p2_H)
    # print("r转矩:", t_r_p2)

    # 减速比
    i_s_H_N = z_s * z_p2 + (z_p1 * z_r)
    i_s_H_D = z_s * z_p2
    i_s_H = i_s_H_N / i_s_H_D
    # 求最简分数
    for i in range(2, int(i_s_H) + 1):
        if i_s_H_N % i == 0 and i_s_H_D % i == 0:
            i_s_H_N = i_s_H_N / i
            i_s_H_D = i_s_H_D / i
            i_s_H = i_s_H_N / i_s_H_D

    w_h_s = n - n / i_s_H
    w_h_p = w_h_s / z_p1 * z_s

    return w_h_s, w_h_p, t, t_p1p2


outputlist = NW_H_av_t()
