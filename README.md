# 主要内容
## 2K-H(A)_(NGW)
目前主要包含两个脚本，一是对齿圈和太阳齿齿数不为行星数整数倍的行星均布时所需转动相位进行计算的脚本，二是计算行星的H转速和太阳对地转速的比值的脚本。

## 2K-H(B)_(NW)
1. NW_efficiency_optimization.py是对NW的效率进行计算的脚本，可以单独使用，但也被NW_erigidc.py调用。
2. NW_H_av_t.py是对NW校核所需的太阳齿转速和转矩，行星转速和转矩进行计算的脚本，可以单独使用，但也被NW_erigidc.py调用。单独使用时可以直接输入节圆直径参数得到较为准确的转速和转矩。
3. NW_SU_T.py是根据8513V0.1的标准对结构件尺寸链进行计算并可视化的脚本。
4. NW_uniform_distribution.py是对NW是否均布进行判断的脚本，被NW_erigidc.py调用。
5. NW_erigidc.py是对NW在有限参数空间内进行遍历的脚本，输出以最优估计效率为目标的最优齿数组合，并输出用于齿轮强度校核的粗略参数。

## 3K(I)_(NGWN)
1. NGWN_efficiency_optimization.py是对NGWN的效率进行计算的脚本，可以单独使用，但也被NGWN_erigidc.py调用。
2. NGWN_H_av_t.py是对NGWN校核所需的太阳齿转速和转矩，行星转速和转矩进行计算的脚本，可以单独使用，但也被NGWN_erigidc.py调用。单独使用时可以直接输入节圆直径参数得到较为准确的转速和转矩。
3. NGWN_erigidc.py是对NGWN在有限参数空间内进行遍历的脚本，输出以最优估计效率为目标的最优齿数组合，并输出用于齿轮强度校核的粗略参数。

## others
1. hardening_conv.py是用于硬度转换的脚本
2. interference_fit.py是用于计算过盈配合量的脚本
3. Tolerance_Stackup.py是用于计算尺寸链并可视化的脚本