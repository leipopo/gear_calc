import math
import ezdxf
import matplotlib.pyplot as plt

def involute_point(base_radius, angle):
    """计算给定基圆半径和角度的渐开线点"""
    x = base_radius * (math.cos(angle) + angle * math.sin(angle))
    y = base_radius * (math.sin(angle) - angle * math.cos(angle))
    return x, y

def generate_involute_curve(diameter, pressure_angle, center=(0, 0), num_points=10000):
    """生成渐开线曲线的坐标点"""
    base_radius = diameter / 2 * math.cos(math.radians(pressure_angle))
    points = []
    for i in range(num_points):
        angle = i * (2 * math.pi / num_points)
        x, y = involute_point(base_radius, angle)
        points.append((x + center[0], y + center[1]))
    return points

def export_to_dxf(points, filename="involute_curve.dxf"):
    """将坐标点导出为DXF文件"""
    doc = ezdxf.new(dxfversion='R2010')
    msp = doc.modelspace()
    for i in range(len(points) - 1):
        msp.add_line(points[i], points[i + 1])
    doc.saveas(filename)

def plot_curve(points, diameter, pressure_angle, center):
    """使用matplotlib可视化渐开线曲线，并绘制基圆、节圆和压力角"""
    x_coords, y_coords = zip(*points)
    
    # 绘制渐开线曲线
    plt.plot(x_coords, y_coords, label='Involute Curve')
    
    # 绘制基圆
    base_radius = diameter / 2 * math.cos(math.radians(pressure_angle))
    base_circle = plt.Circle(center, base_radius, color='r', fill=False, linestyle='--', label='Base Circle')
    plt.gca().add_artist(base_circle)
    
    # 绘制节圆
    pitch_radius = diameter / 2
    pitch_circle = plt.Circle(center, pitch_radius, color='g', fill=False, linestyle='--', label='Pitch Circle')
    plt.gca().add_artist(pitch_circle)
    
    # 计算节圆与渐开线的交点
    intersection_angle = math.radians(pressure_angle)
    intersection_x, intersection_y = involute_point(base_radius, intersection_angle)
    intersection_x += center[0]
    intersection_y += center[1]
    
    # 绘制压力角
    pressure_angle_line_x = [center[0], intersection_x]
    pressure_angle_line_y = [center[1], intersection_y]
    plt.plot(pressure_angle_line_x, pressure_angle_line_y, color='b', linestyle='--', label='Pressure Angle')
    
    # 绘制法线
    normal_length = pitch_radius * 0.5
    normal_x = [intersection_x, intersection_x + normal_length * math.cos(intersection_angle)]
    normal_y = [intersection_y, intersection_y + normal_length * math.sin(intersection_angle)]
    plt.plot(normal_x, normal_y, color='m', linestyle='--', label='Normal Line')
    
    # 绘制切线
    tangent_length = pitch_radius * 0.5
    tangent_angle = intersection_angle + math.pi / 2
    tangent_x = [intersection_x, intersection_x + tangent_length * math.cos(tangent_angle)]
    tangent_y = [intersection_y, intersection_y + tangent_length * math.sin(tangent_angle)]
    plt.plot(tangent_x, tangent_y, color='c', linestyle='--', label='Tangent Line')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Involute Curve with Base Circle, Pitch Circle, Pressure Angle, Normal, and Tangent')
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()

# 示例参数
diameter = 100  # 分度圆直径
pressure_angle = 20  # 压力角
center = (0, 0)  # 基圆圆心坐标

# 生成渐开线曲线
points = generate_involute_curve(diameter, pressure_angle, center)

# 导出为DXF文件
export_to_dxf(points)

# 可视化渐开线曲线，并绘制基圆、节圆和压力角
plot_curve(points, diameter, pressure_angle, center)