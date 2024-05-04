# 此脚本用于计算NGWN减速器相啮合齿轮的基准齿廓的相对转速和转矩
"""
参考文献
行星齿轮传动设计 第二版 绕振纲
P195 ..."N_L=60*N_x*t"...
p208 ..."T_1=T_a/n_p"...
p209 ..."T_1=T_b/n_p/zb*zd"...
"""
# 输入列表:一级模数，二级模数，s齿轮齿数，p1齿轮齿数，p2齿轮齿数，r1齿轮齿数，r2齿轮齿数，行星数，输入转速，输入转矩
# 输出列表:转化机构S转速，转化机构P转速，转化机构R1转速，转化机构R2转速，S转矩，P转矩，R1转矩，R2转矩
input_list = [0.23, 0.235, 9, 12, 13, 33, 34, 3, 10000, 0.005]


def NGWN_H_av_t(input_list):
    """
    计算NW型行星减速器的相啮合齿轮的基准齿廓的相对转速和转矩
    注意：
    1.使用此函数输出参数计算得到的s和r的寿命需要以三倍计算
    2.此函数中的转速准确，转矩可能由于变位和中心距变化而不准确
    :param input_list: 输入列表:[0]一级模数，[1]二级模数，[2]s齿轮齿数，[3]p1齿轮齿数，[4]p2齿轮齿数，[5]r1齿轮齿数，[6]r2齿轮齿数，[7]行星数，[8]输入转速，[9]输入转矩
    :return: 输出列表:[0]转化机构S转速，[1]转化机构P转速，[2]转化机构R1转速，[3]转化机构R2转速，[4]S转矩，[5]P转矩，[6]R1转矩，[7]R2转矩
    """
    # 输入列表
    m_s = m_p1 = m_r1 = input_list[0]
    m_p2 = m_r2 = input_list[1]
    z_s = input_list[2]
    z_p1 = input_list[3]
    z_p2 = input_list[4]
    z_r1 = input_list[5]
    z_r2 = input_list[6]
    N_p = input_list[7]
    n = input_list[8]
    t = input_list[9]
    # 计算S和P1的理论啮合半径
    r_s = m_s * z_s / 2
    # 计算P1的理论啮合半径
    r_p1 = m_p1 * z_p1 / 2
    # 计算P2的理论啮合半径
    r_p2 = m_p2 * z_p2 / 2
    # 计算R1的理论啮合半径
    r_r1 = m_r1 * z_r1 / 2
    # 计算R2的理论啮合半径
    r_r2 = m_r2 * z_r2 / 2
    # 计算双联行星中心距
    r_p1_p2 = (
        (m_p1 * z_p1 + m_s * z_s) / 2
        + (m_r2 * z_r2 - m_p2 * z_p2) / 2
        + (m_r1 * z_r1 - m_p1 * z_p1) / 2
    ) / 3
    # 计算S切向力
    F_p1_s = t / N_p / r_s
    # 计算P1切向力
    F_s_p1 = -F_p1_s
    # print("F_s_p1",F_s_p1)
    # 计算R1切向力
    F_r1_p1 = (r_p1 + r_p2) / (r_p1 - r_p2) * F_s_p1
    F_p1_r1 = -F_r1_p1
    # 计算P2切向力
    F_r2_p2 = F_r1_p1 + F_s_p1
    F_p2_r2 = -F_r2_p2
    # F_r2_p2_2 = 2 * r_p1 / (r_p1 - r_p2) * F_s_p1
    # print("F_r2_p2:", F_r2_p2)
    # print("F_r2_p2_2:", F_r2_p2_2)
    # 计算P1P2转矩
    t_p1p2 = F_r2_p2 * r_p2
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
            print("减速比:", i_s_H_N, "/", i_s_H_D, "=", i_s_H)

    w_h_s = n - n / i_s_H
    w_h_p1 = w_h_s * z_s / z_p1
    w_h_r1 = w_h_s * z_s / z_r1
    w_h_p2 = w_h_p1
    w_h_r2 = w_h_p2 * z_p2 / z_r2

    W_h_s = t * w_h_s
    W_h_p1 = t_p1p2 * w_h_p1 * N_p
    W_h_r1 = t_r1 * w_h_r1
    W_h_p2 = W_h_p1
    W_h_r2 = t_r2 * w_h_r2

    # print("S的H转速:", w_h_s, "S转矩:", t, "S功率:", W_h_s)
    # print("P1的H转速:", w_h_p1, "P1转矩:", t_p1p2, "P1功率:", W_h_p1)
    # print("R1的H转速:", w_h_r1, "R1转矩:", t_r1, "R1功率:", W_h_r1)
    # print("P2的H转速:", w_h_p2, "P2转矩:", t_p1p2, "P2功率:", W_h_p2)
    # print("R2的H转速:", w_h_r2, "R2转矩:", t_r2, "R2功率:", W_h_r2)
    return [w_h_s, w_h_p1, w_h_r1, w_h_r2, t, t_p1p2, t_r1, t_r2]


outputlist = NGWN_H_av_t(input_list)
