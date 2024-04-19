#将输入的维氏硬度，布氏硬度，洛氏硬度进行转换
import math

def hardness_conv():
    print("1.维氏硬度转换")
    print("2.布氏硬度转换")
    print("3.洛氏硬度转换")
    choice = int(input("请选择转换类型："))
    if choice == 1:
        HV = float(input("请输入维氏硬度："))
        HB = (HV +10.5)/1.05
        print("转换后的布氏硬度为：",HB)
        # 洛氏硬度计算（国标）
        if HV > 520 :
            HRC = (100*HV-15100)/(HV+223)
            print("国标对应洛氏硬度：",HRC,"误差±1HRC")
        elif HV > 200 and HV <= 520:
            HRC = (100*HV-13700)/(HV+223)
            print("国标对应洛氏硬度：",HRC,"误差±1HRC")
        else:
            print("国标无对应洛氏硬度")
        # 洛氏硬度压痕分析计算
        HRC = 99.6 - math.sqrt((1585324-658*HV)*HV)
        print("压痕分析对应洛氏硬度：",HRC,"误差±0.1HRC")
    elif choice == 2:
        HB = float(input("请输入布氏硬度："))
        HV = HB/1.05-10.5
        print("转换后的维氏硬度为：",HV,"误差±3HV")
        HRC = 52.76-math.sqrt((103500000-218600*HB)*HB*HB)
        print("压痕分析对应洛氏硬度：",HRC,"误差±0.1HRC")
    elif choice == 3:
        HRC = float(input("请输入洛氏硬度："))
        # 使用HK作为中间量进行计算
        HK = 0.1663021*(HRC**2)-2.6482344*HRC+239.71320
        HV = 3033*HK/(3066/(62.5555/(1088-HK)+0.9077)+math.fabs(HK-355))
        print("转换后的维氏硬度为：",HV,"误差比较大建议查表")
        HB = 1.05*(HV+10.5)
        print("转换后的布氏硬度为：",HB)
hardness_conv()
# 请将其转换为函数hardness_conv，实现维氏硬度、布氏硬度、洛氏硬度的转换