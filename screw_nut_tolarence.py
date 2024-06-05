from prettytable import PrettyTable
import math
import statistics
from fractions import Fraction

# 国标GB/T 5796.4-2022
# 中径公差带 内螺纹H 外螺纹c和e
# 内螺纹小径和大径公差带H基本偏差为0
# 外螺纹小径和大径公差带h基本偏差为0，与中径无关

P = 1
D = 3
N = 2
Accuracy_class = 7#精度等级7,8,9




#将圆整到R40优先数系得最临近值
def R40(value): 
    # print(value)
    n = 40
    log10_value = math.log10(abs(value))
    k_ceil = math.ceil(log10_value*n)
    k_floor = math.floor(log10_value*n)

    r40_value_ceil = 10**(k_ceil/n)*value/abs(value)
    r40_value_floor = 10**(k_floor/n)*value/abs(value)
    
    if value<0:
        r40_value = r40_value_ceil
    else:
        r40_value = r40_value_ceil
        
    # print(r40_value_ceil,r40_value_floor)
    
    return r40_value

#求相邻优先数系两值的几何平均数
def R_Geometric_Mean(begin_exp, step_exp,tar_value):
    # print(begin_exp, step_exp, tar_value)
    log10_value = math.log10(1/begin_exp*1/step_exp*abs(tar_value))
    # print(log10_value)
    k_ceil = math.ceil(log10_value)
    k_floor = math.floor(log10_value)
    # print(k_ceil,k_floor)
    R_ceil = 10**(begin_exp+k_ceil*step_exp)
    R_floor = 10**(begin_exp+k_floor*step_exp)
    
    R_mean = statistics.geometric_mean([R_ceil,R_floor])
    # print(R_ceil,R_floor)
    
    
    return R_mean
    
# print(R_Geometric_Mean(6/40,12/40,D))


#基本偏差
EI_H = 0
es_h = 0
if(P<=2):
    es_e=-(125+11*P)
elif(P>2 and P<=3):
    es_e=-(50+11*P)
elif(P>3 and P<=4):
    es_e=-47.49*(P**0.5)
elif(P>4 ):
    es_e=-(5+94.12*(P**0.5))
    
#顶径公差
##外螺纹大径公差
T_d1 = 0.63*(180*(P**(2/3))-3.15/(P**(1/2)))
##内螺纹小径公差
T_D1 = 0.63*(230*(P**(Fraction(7, 10))))

#中径公差
##外螺纹中径公差
d = R_Geometric_Mean(6/40,12/40,D)
print(d)
if Accuracy_class == 7:
    T_d2 = 1.25*(90*(P**(0.4))*(d**(0.1)))
elif Accuracy_class == 8:
    T_d2 = 1.6*(90*(P**(0.4))*(d**(0.1)))
elif Accuracy_class == 9:
    T_d2 = 2*(90*(P**(0.4))*(d**(0.1)))
else:
    print('精度等级错误')
    
# print(T_d2)
    
if N == 1:
    T_d2 = T_d2
elif N == 2:
    T_d2 = 1.12*T_d2
elif N == 3:
    T_d2 = 1.25*T_d2
elif N == 4:
    T_d2 = 1.4*T_d2
elif N >= 5:
    T_d2 = 1.6*T_d2
else:
    print('N错误')

##内螺纹中径公差
D = R_Geometric_Mean(6/40,12/40,D)

if Accuracy_class == 7:
    T_D2 = 1.7*(90*(P**(0.4))*D**(0.1))
elif Accuracy_class == 8:
    T_D2 = 2.12*(90*(P**(0.4))*D**(0.1))
elif Accuracy_class == 9:
    T_D2 = 2.65*(90*(P**(0.4))*D**(0.1))
    
if N == 1:
    T_D2 = T_D2
elif N == 2:
    T_D2 = 1.12*T_D2
elif N == 3:
    T_D2 = 1.25*T_D2
elif N == 4:
    T_D2 = 1.4*T_D2
elif N >= 5:
    T_D2 = 1.6*T_D2
else:
    print('N错误')
    
# print(T_D2_7)

#外螺纹小径公差
T_d3 = 1.25*T_d2 + abs(es_e)

# results = PrettyTable()
# results.field_names = ["内螺纹小径上差", "内螺纹小径下差", "内螺纹中径上差", "内螺纹中径下差", "内螺纹大径上差", "内螺纹大径下差", "外螺纹小径上差", "外螺纹小径下差", "外螺纹中径上差", "外螺纹中径下差", "外螺纹大径上差", "外螺纹大径下差"]
# # results.add_row([round(R40(T_D1),3), 0, round(R40(T_D2),3), 0, 0, 0, 0, round(R40(T_d1),3), 0, round(R40(T_d2),3), 0, round(R40(T_d3),3)])
# results.add_row([round(T_D1,3), 0, round(T_D2,3), 0, 0, 0, 0, round(T_d3,3), 0, round(T_d2,3), 0, round(T_d1,3)])
# # results.add_row(T_D1, 0, T_D2, 0, 0, 0, 0, T_d1, 0, T_d2, 0, T_d3)
# print(results)

results_innerscrew= PrettyTable()
results_innerscrew.field_names = ["内螺纹小径上差", "内螺纹小径下差", "内螺纹中径上差", "内螺纹中径下差", "内螺纹大径上差", "内螺纹大径下差"]
results_innerscrew.add_row([round(R40(T_D1),3), 0, round(R40(T_D2),3), 0, 0,0])

results_externalscrew = PrettyTable()
results_externalscrew.field_names = ["外螺纹小径上差", "外螺纹小径下差", "外螺纹中径上差", "外螺纹中径下差", "外螺纹大径上差", "外螺纹大径下差"]
results_externalscrew.add_row([0, -round(R40(T_d3),3), round(R40(es_e),3), -round(R40(T_d2-es_e),3), 0, -round(R40(T_d1),3)])

print(results_innerscrew)
print(results_externalscrew)

