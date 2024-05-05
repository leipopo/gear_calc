# Description: Calculate the closed loop tolerance of a system of parts
from matplotlib import pyplot as plt


class Part:
    def __init__(self, name, size, upper_deviation, lower_deviation, is_increase):
        self.name = name
        self.size = size
        self.upper_deviation = upper_deviation
        self.lower_deviation = lower_deviation
        self.is_increase = is_increase

    def __str__(self):
        return (
            f"{self.name} - Size: {self.size}, Upper Deviation: {self.upper_deviation}, "
            f"Lower Deviation: {self.lower_deviation}, Type: {'Increasing' if self.is_increase else 'Decreasing'}"
        )


def calculate_closed_loop_tolerance(parts):
    total_upper_deviation = sum(
        part.upper_deviation if part.is_increase else -part.lower_deviation
        for part in parts
    ).__round__(3)
    total_lower_deviation = sum(
        part.lower_deviation if part.is_increase else -part.upper_deviation
        for part in parts
    ).__round__(3)
    closed_loop_tolerance = round(total_upper_deviation - total_lower_deviation, 3)
    return closed_loop_tolerance, total_upper_deviation, total_lower_deviation


def visualize_closed_loop_tolerance(parts, img_width=16, img_height=10, m=20):
    increase_parts = [part for part in parts if part.is_increase]
    decrease_parts = [part for part in parts if not part.is_increase]

    closed_loop_deviation, total_upper_deviation, total_lower_deviation = (
        calculate_closed_loop_tolerance(parts)
    )

    increase_parts_total_length = sum(
        part.size + part.lower_deviation * m for part in increase_parts
    )
    # print(increase_parts_total_length)
    decrease_parts_total_length = sum(
        part.size + part.upper_deviation * m for part in decrease_parts
    )
    # print(decrease_parts_total_length)

    base_length = max(increase_parts_total_length, decrease_parts_total_length)
    closed_loop_line_place = (
        "upper"
        if increase_parts_total_length > decrease_parts_total_length
        else "lower"
    )
    closed_loop_color = "green" if total_lower_deviation >= 0 else "orange"
    # if increase_parts_total_length > decrease_parts_total_length:
    #     base_length = increase_parts_total_length
    #     closed_loop_color = "green"
    # else:
    #     base_length = decrease_parts_total_length
    #     closed_loop_color = "orange"

    drawing_width_percentage = 0.9  # 绘制宽度百分比
    increase_parts_length_percentage = list(
        (part.size + part.lower_deviation * m) / base_length * drawing_width_percentage
        for part in increase_parts
    )
    decrease_parts_length_percentage = list(
        (part.size + part.upper_deviation * m) / base_length * drawing_width_percentage
        for part in decrease_parts
    )

    plt.figure(figsize=(img_width, img_height))
    # 从左开始留白百分之五，开始用红色绘制增环零部件，然后用蓝色绘制减环零部件
    start_x = 0.05
    current_percentage = start_x
    partline_width = 3
    divline_width = 2
    partline_y_offset = 0.15
    divline_y_offset = 0.1
    divline_height = 0.2
    for i, part in enumerate(increase_parts):
        ##绘制起始分割线
        plt.plot(
            [current_percentage, current_percentage],
            [0.5 - divline_y_offset, 0.5 - divline_y_offset - divline_height],
            color="black",
            linewidth=divline_width,
        )
        ##绘制零部件
        plt.plot(
            [
                current_percentage,
                current_percentage + increase_parts_length_percentage[i],
            ],
            [0.5 - partline_y_offset, 0.5 - partline_y_offset],
            color="red",
            linewidth=partline_width,
        )
        text = f"{part.name}\nSize: {part.size}\nUpper Deviation: {part.upper_deviation}\nLower Deviation: {part.lower_deviation}"
        plt.text(
            current_percentage + increase_parts_length_percentage[i] / 2,
            0.5 - partline_y_offset - 0.15,
            text,
            ha="center",
        )
        current_percentage += increase_parts_length_percentage[i]
    # 绘制终止分割线
    plt.plot(
        [current_percentage, current_percentage],
        [0.5 - divline_y_offset, 0.5 - divline_y_offset - divline_height],
        color="black",
        linewidth=divline_width,
    )
    current_percentage = start_x
    for i, part in enumerate(decrease_parts):
        ##绘制起始分割线
        plt.plot(
            [current_percentage, current_percentage],
            [0.5 + divline_y_offset, 0.5 + divline_y_offset + divline_height],
            color="black",
            linewidth=divline_width,
        )
        plt.plot(
            [
                current_percentage,
                current_percentage + decrease_parts_length_percentage[i],
            ],
            [0.5 + partline_y_offset, 0.5 + partline_y_offset],
            color="blue",
            linewidth=partline_width,
        )
        # 添加部件名称和基准尺寸以及上下公差
        text = f"{part.name}\nSize: {part.size}\nUpper Deviation: {part.upper_deviation}\nLower Deviation: {part.lower_deviation}"
        plt.text(
            current_percentage + decrease_parts_length_percentage[i] / 2,
            0.5 + partline_y_offset + 0.05,
            text,
            ha="center",
        )
        current_percentage += decrease_parts_length_percentage[i]
    # 绘制终止分割线
    plt.plot(
        [current_percentage, current_percentage],
        [0.5 + divline_y_offset, 0.5 + divline_y_offset + divline_height],
        color="black",
        linewidth=divline_width,
    )

    # 绘制闭环公差
    plt.plot(
        (
            [
                start_x + sum(decrease_parts_length_percentage),
                start_x + drawing_width_percentage,
            ]
            if closed_loop_line_place == "upper"
            else [
                start_x + sum(increase_parts_length_percentage),
                start_x + drawing_width_percentage,
            ]
        ),
        (
            [0.5 + partline_y_offset, 0.5 + partline_y_offset]
            if closed_loop_line_place == "upper"
            else [0.5 - partline_y_offset, 0.5 - partline_y_offset]
        ),
        color=closed_loop_color,
        linewidth=partline_width,
    )
    text = f"Closed Loop Tolerance: {closed_loop_deviation}\nTotal Upper Deviation: {total_upper_deviation}\nTotal Lower Deviation: {total_lower_deviation}"
    plt.text(
        current_percentage
        + (start_x + drawing_width_percentage - current_percentage) / 2,
        0.5,
        text,
        ha="center",
    )

    # 绘制终止分割线
    plt.plot(
        [start_x + drawing_width_percentage, start_x + drawing_width_percentage],
        (
            [0.5 + divline_y_offset, 0.5 + divline_y_offset + divline_height]
            if closed_loop_line_place == "upper"
            else [0.5 - divline_y_offset, 0.5 - divline_y_offset - divline_height]
        ),
        color="black",
        linewidth=divline_width,
    )

    # plt.text(
    #     0.5,
    #     0.7,
    #     f"Closed Loop Tolerance: {closed_loop_deviation}",
    #     ha="center",
    #     fontsize=20,
    # )
    # 绘制

    plt.xlim(0, 1)
    plt.ylim(0, 1)
    # 隐藏坐标轴
    plt.axis("off")
    plt.title("Closed Loop Tolerance Visualization")
    plt.show()
    plt.waitforbuttonpress()
