# 此脚本用于计算NGWN减速器相啮合齿轮的基准齿廓的相对转速和转矩
"""
参考文献
行星齿轮传动设计 第二版 绕振纲
P195 ..."N_L=60*N_x*t"...
p208 ..."T_1=T_a/n_p"...
p209 ..."T_1=T_b/n_p/zb*zd"...
"""


def NGWN_H_av_t(
    m_1=0.23,
    m_2=0.235,
    z_s=9,
    d_s=None,
    z_p1=12,
    d_p1=None,
    z_r1=33,
    d_r1=None,
    z_p2=13,
    d_p2=None,
    z_r2=34,
    d_r2=None,
    N_p=3,
    t=0.005,
    n=10000,
):
    i_s_H = (1 + z_r1 / z_s) / (1 - (z_p2 * z_r1) / (z_p1 * z_r2))
    # 计算S和P1的理论啮合半径
    r_s = m_1 * z_s / 2 if d_s == None else d_s / 2
    # 计算P1的理论啮合半径
    r_p1 = m_1 * z_p1 / 2 if d_p1 == None else d_p1 / 2
    # 计算P2的理论啮合半径
    r_p2 = m_2 * z_p2 / 2 if d_p2 == None else d_p2 / 2
    # 计算R1的理论啮合半径
    r_r1 = m_1 * z_r1 / 2 if d_r1 == None else d_r1 / 2
    # 计算R2的理论啮合半径
    r_r2 = m_2 * z_r2 / 2 if d_r2 == None else d_r2 / 2
    # 计算双联行星中心距
    r_p1_p2 = (
        (
            (m_1 * z_p1 + m_1 * z_s) / 2
            + (m_2 * z_r2 - m_2 * z_p2) / 2
            + (m_1 * z_r1 - m_1 * z_p1) / 2
        )
        / 3
        if d_s == None or d_r1 == None or d_r2 == None or d_p1 == None or d_p2 == None
        else ((d_s + d_p1) / 2 + (d_r1 - d_p1) / 2 + (d_r2 - d_p2) / 2) / 3
    )
    # 计算S切向力
    F_p1_s = t / N_p / r_s
    # 计算S输入到P1的切向力
    F_s_p1 = -F_p1_s
    # print("F_s_p1",F_s_p1)
    # 计算R1切向力
    print("r_p1:", m_1, "*", z_p1, "/", 2, "=", r_p1)
    print("r_p2:", m_2, "*", z_p2, "/", 2, "=", r_p2)
    if r_p1 == r_p2:
        return (0, 0, 0, 0, 0)
    else:
        # F_r1_p1 = t * i_s_H / r_r2 / 3
        F_r1_p1 = (r_p1 + r_p2) / (r_p1 - r_p2) * F_s_p1
    F_p1_r1 = -F_r1_p1
    # 计算P1输入到R1的转矩
    t_p1_r1 = F_r1_p1 * r_p1
    # 计算P2切向力
    F_r2_p2 = F_r1_p1 + F_s_p1
    F_p2_r2 = -F_r2_p2
    # 计算P2输入到R2的转矩
    t_p2_r2 = F_r2_p2 * r_p2
    # t_p1p2_2 = F_s_p1 * r_p1 - F_r1_p1 * r_p1
    # print("t_p1p2:", t_p1p2)
    # print("t_p1p2_2:", t_p1p2_2)
    # 计算R1转矩
    t_r1 = F_p1_r1 * N_p * r_r1
    # 计算R2转矩
    t_r2 = -F_p2_r2 * N_p * r_r2

    i_s_H_N = z_s + z_r1
    i_s_H_D = z_s
    i_s_H = i_s_H_N / i_s_H_D
    for i in range(1, 100):
        if i_s_H_N % i == 0 and i_s_H_D % i == 0:
            i_s_H_N = i_s_H_N / i
            i_s_H_D = i_s_H_D / i
            i_s_H = i_s_H_N / i_s_H_D
            # print("减速比:", i_s_H_N, "/", i_s_H_D, "=", i_s_H)

    w_h_s = n - n / i_s_H
    w_h_p1 = w_h_s * z_s / z_p1

    return (
        w_h_s,
        w_h_p1,
        t,
        t_p1_r1,
        t_p2_r2,
    )


if __name__ == "__main__":
    w_h_s, w_h_p1, t, t_p1_r1, t_p2_r2 = NGWN_H_av_t()
    print("w_h_s:", w_h_s)
    print("w_h_p1:", w_h_p1)
    print("t:", t)
    print("t_p1_r1:", t_p1_r1)
    print("t_p2_r2:", t_p2_r2)
