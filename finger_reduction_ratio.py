z_s=8
z_p=14
z_r=37
theta_MCP=100

#行星轮系减速比
def P_reduction_ratio(z_s,z_p,z_r):
    return 1+(z_r/z_s)
#计算系统等效传动比
def equivalent_transmission_ratio(z_s,z_p,z_r,x_MCP,x_PIP_DIP):
    return x_MCP/P_h*P_reduction_ratio(z_s,z_p,z_r)*360*(x_MCP+x_PIP_DIP)/x_MCP/theta_MCP

for i in range(12,21):
    x_MCP=i
    for j in range(4,21):
        x_PIP_DIP=j
        for k in range(2,5):
            P_h=k
            print("x_MCP:",x_MCP,"x_PIP_DIP:",x_PIP_DIP,"P_h:",P_h,"等效传动比：",equivalent_transmission_ratio( z_s,z_p,z_r,x_MCP,x_PIP_DIP), "杆组等效传动率：",equivalent_transmission_ratio( z_s,z_p,z_r,x_MCP,x_PIP_DIP)/P_reduction_ratio(z_s,z_p,z_r)/((x_MCP)/P_h))


