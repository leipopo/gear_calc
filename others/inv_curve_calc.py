import math
import ezdxf
import matplotlib.pyplot as plt

def involute_point(base_radius, angle, initial_angle=0):
    """计算给定基圆半径和角度的渐开线点，并控制起始点与基圆圆心连线的角度"""
    total_angle = angle + initial_angle
    x = base_radius * (math.cos(total_angle) + angle * math.sin(total_angle))
    y = base_radius * (math.sin(total_angle) - angle * math.cos(total_angle))
    return x, y

def generate_involute_curve(diameter, pressure_angle, initial_angle=0, center=(0, 0), point_spacing=0.0005, end_angle=math.pi/4):
    """生成渐开线曲线的坐标点，并确保相邻点的连线距离相等"""
    points = []
    base_radius = diameter / 2 * math.cos(math.radians(pressure_angle))
    angle = 0
    while angle <= end_angle:
        x, y = involute_point(base_radius, angle, initial_angle)
        points.append((x + center[0], y + center[1]))
        angle += point_spacing / base_radius
    return points

def export_to_dxf(points, filename="involute_curve.dxf",linetype="CONTINUOUS", degree=3):
    """将坐标点导出为DXF文件"""
    doc = ezdxf.new(dxfversion='R2010')
    msp = doc.modelspace()
    # 确保线型在DXF文档中定义
    if linetype not in doc.linetypes:
        doc.linetypes.new(linetype, dxfattribs={'description': 'Custom linetype', 'pattern': [0.2, 0.2]})
    
    # 使用 SPLINE 创建拟合线，并设置样条曲线的阶数
    msp.add_spline(points, dxfattribs={'linetype': linetype}, degree=degree)
    doc.saveas(filename)

def plot_curve(points, diameter, pressure_angle, center,initial_angle):
    """使用matplotlib可视化渐开线曲线，并绘制基圆、节圆和压力角"""
    x_coords, y_coords = zip(*points)
    
    # 绘制渐开线曲线
    plt.plot(x_coords, y_coords, linestyle='dotted', label='Involute Curve')
    
    # 绘制基圆
    base_radius = diameter / 2 * math.cos(math.radians(pressure_angle))
    base_circle = plt.Circle(center, base_radius, color='r', fill=False, linestyle='dashed', label='Base Circle')
    plt.gca().add_patch(base_circle)
    
    # 绘制分度圆
    pitch_circle = plt.Circle(center, diameter / 2, color='g', fill=False, linestyle='dashed', label='Pitch Circle')
    plt.gca().add_patch(pitch_circle)
    
    # 绘制压力角线
    pressure_angle_rad = math.radians(pressure_angle)
    plt.plot([center[0], center[0] + involute_point(base_radius, math.tan(pressure_angle_rad), initial_angle)[0]],
             [center[1], center[1] + involute_point(base_radius, math.tan(pressure_angle_rad), initial_angle)[1]],
             color='b', linestyle='dashed', label='Pressure Angle')
    
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.show()

# 主函数
def main():
    diameter = 100  # 分度圆直径
    center = (-diameter, 0)  # 分度圆圆心位置
    pressure_angle = 20  # 分度圆压力角
    initial_angle = 0  # 渐开线起始角度
    end_angle = math.pi / 4  # 渐开线滚动角度
    point_spacing = 0.0005  # 输出线条精度

    # 生成渐开线曲线
    points = generate_involute_curve(diameter, pressure_angle, initial_angle, center, point_spacing, end_angle)
    
    # 可视化渐开线曲线
    plot_curve(points, diameter, pressure_angle, center,initial_angle)
    
    # 导出DXF文件
    export_to_dxf(points, "involute_curve.dxf")

if __name__ == "__main__":
    main()