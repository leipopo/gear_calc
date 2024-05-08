import math

"""
参考文献
行星齿轮传动设计 第二版 绕振纲
P38
"""


def NW_UD_JUDGEMENT(zs, zp1, zp2, zr, n_p):
    """
    判断NW的行星是否能均布
    :param zs: 太阳齿数
    :param zp1: 一级行星齿数
    :param zp2: 二级行星齿数
    :param zr: 齿圈齿数
    :param n_p: 行星轮数量
    :return: 均布返回True，否则返回False
    """
    if (zs % n_p != 0) or (zr % n_p != 0):
        if zs % n_p != 0:
            E_A = zs / n_p
            for i in range(1, 100):
                if ((zs + zr) / n_p + (1 + zp2 / zp1) * (E_A + i - zs / n_p) == i) and (
                    (zs + zr) / n_p + (1 + zp2 / zp1) * (E_A - i - zs / n_p) == i
                ):
                    return True
            return False
        else:
            E_A = math.ceil(zs / n_p)
            for i in range(0, 100):
                if ((zs + zr) / n_p + (1 - zp2 / zp1) * (E_A + i - zs / n_p) == i) and (
                    (zs + zr) / n_p + (1 - zp2 / zp1) * (E_A - i - zs / n_p) == i
                ):
                    return True
            return False
    else:
        return True
