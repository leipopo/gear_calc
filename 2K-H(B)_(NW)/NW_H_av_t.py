# 此脚本用于计算NW减速器相啮合齿轮的基准齿廓的相对转速和转矩
"""
参考文献
行星齿轮传动设计 第二版 绕振纲
P195 ..."N_L=60*N_x*t"...
p208 ..."T_1=T_a/n_p"...
p209 ..."T_1=T_b/n_p/zb*zd"...
"""
# 输入列表:一级模数，二级模数，s齿轮齿数，p1齿轮齿数，p2齿轮齿数，r齿轮齿数，行星数，输入转速，输入转矩
# 输出列表:转化机构S转速，转化机构P转速，转化机构R转速，S转矩，P转矩，R转矩
input_list = [0.55, 0.75, 18, 45, 15, 63, 3, 3000, 10]


def NW_H_av_t(input_list):
    """
    计算NW型行星减速器的相啮合齿轮的基准齿廓的相对转速和转矩
    注意：
    1.使用此函数输出参数计算得到的s和r的寿命需要以三倍计算
    2.此函数中的转速准确，转矩可能由于变位和中心距变化而不准确
    :param input_list: 输入列表:[0]一级模数，[1]二级模数，[2]s齿轮齿数，[3]p1齿轮齿数，[4]p2齿轮齿数，[5]r齿轮齿数，[6]行星数，[7]输入转速，[8]输入转矩
    :return: 输出列表:[0]转化机构S转速，[1]转化机构P转速，[2]转化机构R转速，[3]S转矩，[4]P转矩，[5]R转矩
    """
    # 输入列表
    m_s = m_p1 = input_list[0]
    m_p2 = m_r = input_list[1]
    z_s = input_list[2]
    z_p1 = input_list[3]
    z_p2 = input_list[4]
    z_r = input_list[5]
    n_p = input_list[6]
    n = input_list[7]
    t = input_list[8]
    # 计算S和P1的理论啮合半径
    r_s = m_s * z_s / 2
    # 计算P1的理论啮合半径
    r_p1 = m_p1 * z_p1 / 2
    # 计算P2的理论啮合半径
    r_p2 = m_p2 * z_p2 / 2
    # 计算R的理论啮合半径
    r_r = m_r * z_r / 2
    # 计算双联行星中心距
    r_p1_p2 = ((m_p1 * z_p1 + m_s * z_s) / 2 + (m_r * z_r - m_p2 * z_p2) / 2) / 2
    # 计算S切向力
    F_s_p1 = t / n_p / r_s
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
    t_H_p1p2 = F_H_p1p2 * r_p1_p2 * n_p
    t_p1p2_H = -t_H_p1p2
    # 计算R切向力
    F_p2_r = r_p1 * t / n_p / r_p2 / r_s
    # F_r_p2 = -F_p2_r
    # 计算R转矩
    t_r_p2 = n_p * r_r * F_p2_r

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
    # print("减速比:", i_s_H_N, "/", i_s_H_D, "=", i_s_H)
    # print("Tb_i:", (i_s_H - 1) * t)
    w_h_s = n - n / i_s_H
    w_h_p = w_h_s / z_p1 * z_s
    w_h_r = w_h_p / z_r * z_p2

    # W_s = t * w_h_s
    # W_p1_3 = t_p1p2 * w_h_p * 3
    # W_r = t_r_p2 * w_h_r
    # W_H = t_p1p2_H * n / i_s_H
    # print("S的H转速:", w_h_s, "S转矩:", t, "S功率:", w_h_s * t)
    # print("P1的H转速:", w_h_p1, "P1转矩:", t_p1p2, "三个P1的功率:", W_p1_3)
    # print("R的H转速:", w_h_r, "R转矩:", t_r_p2, "R功率:", W_r)
    # print("H的转速:", n / i_s_H, "H转矩:", t_p1p2_H, "H功率:", W_H)

    # print("按圆周力计算的行星架输出转矩:", t_p1p2_H)
    # print("按减速比计算的行星架输出转矩:", i_s_H * t)

    return [w_h_s, w_h_p, w_h_r, t, t_p1p2, t_r_p2]

    # print(F_s_p1, F_r_p2, F_H_p1p2, F_s_p1 + F_r_p2 + F_H_p1p2)


outputlist = NW_H_av_t(input_list)
