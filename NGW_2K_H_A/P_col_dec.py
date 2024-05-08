import math


def detector_col_dec(m=0.235, n_p=3, zs=0, zp=13, zr=34):
    if zs == 0:
        if zr == 0:
            return False
        else:
            if m * zp + m * 1 * 2 + 0.5 * m < 2 * (zr - zp) * m / 2 * math.sin(
                math.pi / n_p
            ):
                return True
            else:
                return False
    elif zr == 0:
        if zs == 0:
            return False
        else:
            if m * zp + m * 1 * 2 + 0.5 * m < 2 * (zs + zp) * m / 2 * math.sin(
                math.pi / n_p
            ):
                return True
            else:
                return False
    return False


# if detector_col_dec() == False:
#     print("OK")
# else:
#     print("NG")
