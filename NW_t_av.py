# 此脚本用于计算NW减速器相啮合齿轮的基准齿廓的相对转速和转矩
# 输入列表：一级模数，二级模数，s齿轮齿数，p1齿轮齿数，p2齿轮齿数，r齿轮齿数，行星数，输入转速，输入转矩
# 输出列表：齿轮P1相对齿轮S的转速，齿轮P2相对齿轮R的转速，齿轮P1的转矩，齿轮P2的转矩，齿轮R的转矩
input_list = [0.55, 0.75, 18, 45, 15, 63, 3, 3000, 10]


def gear_torque(input_list):
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
    # 计算行星架切向力
    F_H_p1p2 = -(F_s_p1 + F_r_p2)
    # 计算行星架转矩
    t_H_p1p2 = F_H_p1p2 * r_p1_p2 * n_p
    t_p1p2_H = -t_H_p1p2
    # 计算R切向力
    F_p2_r = r_p1 * t / n_p / r_p2 / r_s
    F_r_p2 = -F_p2_r
    # 计算R转矩
    t_r_p2 = n_p * r_r * F_p2_r

    print("行星架转矩：", t_p1p2_H)
    print("r转矩：", t_r_p2)

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
    print("减速比：", i_s_H_N, "/", i_s_H_D, "=", i_s_H)
    print("Tb_i:", (i_s_H - 1) * t)


gear_torque(input_list)
