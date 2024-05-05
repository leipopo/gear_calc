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
part_housing = TS.Part("housing", 20.7, 0.02, 0.0, True)
part_upper_planetary = TS.Part("upper_planetary", 6.7, 0.00, -0.05, False)
part_lower_planetary = TS.Part("lower_planetary", 10, 0.0, -0.05, False)
parts = [part_housing, part_upper_planetary, part_lower_planetary]
TS.visualize_closed_loop_tolerance(parts)
