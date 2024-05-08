import sys
from pathlib import Path

current_file = Path(__file__)
package_path = current_file.parent.parent  # 假设 moduleA1 在 my_package/packageA 中
sys.path.append(str(package_path))

from others import Tolerance_Stackup as TS
import matplotlib.pyplot as plt

"""
example:

part_A1 = TS.Part("A1", 15, 0.1234, 0.056, True)
part_A2 = TS.Part("A2", 25, 0.1234, 0.056, True)
part_B1 = TS.Part("B1", 25, 0.56, -0.1234, False)
part_B2 = TS.Part("B2", 15, 0.56, -0.1234, False)

parts = [part_A1, part_A2, part_B1, part_B2]
closed_loop_tolerance, total_upper_deviation, total_lower_deviation = (
    TS.calculate_closed_loop_tolerance(parts)
)
print(f"Closed Loop Tolerance: {closed_loop_tolerance}")
print(f"Total Upper Deviation: {total_upper_deviation}")
print(f"Total Lower Deviation: {total_lower_deviation}")

TS.visualize_closed_loop_tolerance(parts)

"""

# NW_8513V0.1

## 外壳与行星架下部轴承配合位高度公差叠加
# part_housing = TS.Part("housing", 20.7, 0.04, 0.0, True)
# part_upper_planetary = TS.Part("upper_planetary", 6.7, 0.00, -0.06, False)
# part_lower_planetary = TS.Part("lower_planetary", 10, 0.0, -0.05, False)
# part_bearing=TS.Part("bearing",4,-0.0,-0.04,False)
# parts = [part_housing, part_upper_planetary, part_lower_planetary, part_bearing]
# TS.visualize_closed_loop_tolerance(parts)

## 齿圈与一级行星轮配合位公差叠加
# part_housing_1 = TS.Part("housing", 7.9, 0.04, 0.00, True)
# part_housing_ring = TS.Part("housing_ring", 6, 0.04, 0.0, True)
# part_ring = TS.Part("ring", 6, 0.0, -0.04, False)
# part_upper_planetary = TS.Part("upper_planetary", 6.7, 0.00, -0.06, False)
# part_lower_planetary_1 = TS.Part("lower_planetary", 8, 0.0, -0.02, False)
# part_p2 = TS.Part("p2", 6.9, 0.04, 0, True)
# parts = [
#     part_housing,
#     part_housing_ring,
#     part_ring,
#     part_upper_planetary,
#     part_lower_planetary,
#     part_p2,
# ]
# TS.visualize_closed_loop_tolerance(parts)

## 转子与定子配合
# part_stator = TS.Part("stator", 13/2, 0.2/2, -0.2/2, False)
# part_housing_2=TS.Part("housing",10.3,0.03,-0.03,False)
# part_upper_planetary_1=TS.Part("upper_planetary",3,0.04,0.0,False)
# part_bearing_1=TS.Part("bearing",4,-0.0,-0.04,True)
# part_sgear = TS.Part("sgear",18.8,0.03,0.0,True)
# part_sgear_bracket=TS.Part("sgear_bracket",3.5,0.04,0.0,True)
# part_rotator=TS.Part("rotator",13/2,0.05/2,-0.05/2,False)

# parts=[part_stator,part_housing_2,part_upper_planetary_1,part_bearing_1,part_sgear,part_sgear_bracket,part_rotator]
# TS.visualize_closed_loop_tolerance(parts)

## 码盘
part_housing_3 = TS.Part("housing",36.65,0.03,-0.03,True)
part_upper_planetary_1=TS.Part("upper_planetary",3,0.04,0.0,True)
part_cover=TS.Part("cover",2.45,0.05,0,False)
part_drive_pcb=TS.Part("drive_pcb",1.6,0.16,-0.16,False)
part_encoder_pcb=TS.Part("drive_pcb",1.6,0.16,-0.16,False)
part_RF_pcb=TS.Part("drive_pcb",1.6,0.16,-0.16,False)
part_pad_pcb=TS.Part("drive_pcb",1.6,0.16,-0.16,False)
part_bearing_1=TS.Part("bearing",4,-0.0,-0.04,False)
part_sgear = TS.Part("sgear",18.8,0.03,0.0,False)
part_sgear_bracket=TS.Part("sgear_bracket",4,0.06,0.0,False)
part_column_PCB=TS.Part("column_PCB",3,0.005,-0.005,False)
parts = [part_housing_3,part_upper_planetary_1,part_cover,part_drive_pcb,part_encoder_pcb,part_RF_pcb,part_pad_pcb,part_bearing_1,part_sgear,part_sgear_bracket,part_column_PCB]
TS.visualize_closed_loop_tolerance(parts)