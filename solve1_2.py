import numpy as np 

dis = np.loadtxt('data/dis.dat', delimiter = ',')
print(dis[75, 78])
print(dis[1, 78])
print(dis[78, 75])
print(dis[1, 92])

Plf_nodes = list(range(1, 21))

import xlrd
data = xlrd.open_workbook('Problems/cumcm2011B附件2_全市六区交通网路和平台设置的数据表.xls') 
cross_ifm = data.sheet_by_name("全市区出入口的位置")
cross_nodes = cross_ifm.col_values(2, start_rowx = 1, end_rowx = 14)
cross_nodes = [int(x) for x in cross_nodes]
# cross_nodes = [0] + cross_nodes
# Cr_nodes = list(range(1, 14))
# print(Cr_nodes)
print(cross_nodes) 

import gurobipy as gp 
from gurobipy import GRB 

m = gp.Model("cuMcM_2011B")
x = m.addVars(Plf_nodes, cross_nodes, vtype = GRB.BINARY, name = "allocate")
d = m.addVars(Plf_nodes, vtype = GRB.CONTINUOUS, name = 'd')
D = m.addVar(vtype = GRB.CONTINUOUS, name = "max_Distance")

m.addConstrs((x.sum(i, '*') <= 1 for i in Plf_nodes), name = 'plf')
m.addConstrs((x.sum('*', k) == 1 for k in cross_nodes), name = 'crs')
m.addConstrs((d[i] == gp.quicksum(x[i, k] * dis[i, k] for k in cross_nodes) for i in Plf_nodes), name = 'midis')
m.addConstr((D == gp.max_(d)), name = 'd')

m.setObjective(D, GRB.MINIMIZE)
m.optimize()

for i in Plf_nodes:
    for k in cross_nodes:
        print(int(x[i, k].x), end = " ")
    print("in line ", i)

for i in Plf_nodes:
    for k in cross_nodes:
        if int(x[i, k].x >= 1e-6):
            print("服务平台 ", i, " 管理着路口 ", k)

print("最短时间:", D.x)
# print(dis[28, 15])
# print(dis[29, 15])
# print(dis[38, 16])