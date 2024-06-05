# 该脚本用于计算NGW行星减速器太阳转速和行星齿轮在转换机构中的转速之间的关系
z_s = 18  # 太阳齿数
z_p = 45  # 行星齿数
z_r = 108  # 齿圈齿数

if z_r == 0 and z_s != 0 and z_p != 0:
    z_r = z_s+z_p*2
    N = z_s * (z_p - z_r) - z_p * z_s
    D = z_p * (z_s + z_r)
    for j in range(1, 100):
        
        if N % j == 0 and D % j == 0:
            N = N / j
            D = D / j
        
    for j in range(1, 100):
        if N % j == 0 and D % j == 0:
            N = N / j
            D = D / j
            
    for j in range(1, 100):
        if N % j == 0 and D % j == 0:
            N = N / j
            D = D / j
    print("N:", N)
    print("D:", D)

elif z_s == 0 and z_r != 0 and z_p != 0:
    z_s = z_r-z_p*2
    N = z_s * (z_p - z_r) - z_p * z_s
    D = z_p * (z_s + z_r)
    for j in range(1, 100):
        if N % j == 0 and D % j == 0:
            N = N / j
            D = D / j
        
    for j in range(1, 100):
        if N % j == 0 and D % j == 0:
            N = N / j
            D = D / j
            
    for j in range(1, 100):
        if N % j == 0 and D % j == 0:
            N = N / j
            D = D / j

    print("N:", N)
    print("D:", D)
elif z_p !=0 and z_r!=0 and z_s!=0:
    N = z_s * (z_p - z_r) - z_p * z_s
    D = z_p * (z_s + z_r)
    for j in range(1, 100):
        if N % j == 0 and D % j == 0:
            N = N / j
            D = D / j
        
    for j in range(1, 100):
        if N % j == 0 and D % j == 0:
            N = N / j
            D = D / j
            
    for j in range(1, 100):
        if N % j == 0 and D % j == 0:
            N = N / j
            D = D / j

    print("N:", N)
    print("D:", D)
else:
    print("输入错误")
    

