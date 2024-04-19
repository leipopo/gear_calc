z_s = 8 #太阳齿数
z_p = 14 #行星齿数
z_r = 37 #齿圈齿数

N=z_s*(z_p-z_r)-z_p*z_s
D=z_p*(z_s+z_r)

print("N:",N)
print("D:",D)