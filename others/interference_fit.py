#  参考文献 GB/T 5371-2004 极限于配合 过盈配合的计算和选用
# 以下是机械属性
M = 3000  # 传递扭矩 N·mm
pi = 3.14159265  # 圆周率 无量纲
d_f = 8  # 接触直径 mm
l_f = 5 # 接触长度 mm
d_a = 12  # 孔零件外径 mm
d_i = 5 # 轴零件内径 mm

# 以下都是材料属性
mu = 0.17 # 摩擦系数 无量纲
v_a = 0.33 # 孔零件材料的泊松比 无量纲
v_i = 0.29 # 轴零件材料的泊松比 无量纲
E_a = 70000  # 孔零件的弹性模量 N/mm^2
E_i = 210000  # 轴零件的弹性模量 N/mm^2
sigma_s_a = 160  # 孔零件的屈服极限 N/mm^2
sigma_s_i = 800  # 轴零件的屈服极限 N/mm^2


p_f_min = 2 * M / (pi * d_f ** 2 * l_f * mu) # 传递负荷所需的最小结合力
q_a = d_f/d_a  # 孔零件直径直径比 无量纲
q_i = d_i/d_f  # 轴零件直径比 无量纲
C_a = (1 + q_a**2)/(1 - q_a ** 2) + v_a
C_i = (1 + q_i**2)/(1 - q_i ** 2) + v_i
e_a_min = p_f_min * d_f / E_a * C_a  # 孔零件传递负荷所需的最小直径变化量 mm
e_i_min = p_f_min * d_f / E_i * C_i  # 轴零件传递负荷所需的最小直径变化量 mm
delta_c_min = e_a_min+e_i_min  # 传递负荷所需的最小有效过盈量 mm

a = (1-q_a**2)/(3+q_a**4)**0.5
b = (1-q_a**2)/(1+q_a**2)
p_fa_max = a * sigma_s_a  # 孔零件不产生塑性形变所允许的最大结合压力 N/mm^2
c = (1 - q_i**2)/2
p_fi_max = c * sigma_s_i  # 轴零件不产生塑性形变所允许的最大结合压力 N/mm^2
p_f_max = min(p_fa_max, p_fi_max)  # 轴孔配合不产生塑性形变所允许的最大结合压力 N/mm^2
e_a_max = p_f_max * d_f / E_a * C_a  # 孔零件不产生塑性形变所允许的最大直径变化了 mm
e_i_max = p_f_max * d_f / E_i * C_i  # 轴零件不产生塑性形变所允许的最大直径变化了 mm
delta_c_max = e_a_max + e_i_max  # 轴孔配合不产生塑性形变所允许的最大有效过盈量 N/mm^2
print("传递负荷所需的最小有效过盈量(mm):", delta_c_min)
print("轴孔配合不产生塑性形变所允许的最大有效过盈量(mm):", delta_c_max)