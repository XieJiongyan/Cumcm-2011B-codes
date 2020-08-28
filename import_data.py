import xlrd
import numpy as np 

data = xlrd.open_workbook('Problems/cumcm2011B附件2_全市六区交通网路和平台设置的数据表.xls') 
sheets_name = data.sheet_names() 
print(sheets_name) 

node_information = data.sheet_by_name("全市交通路口节点数据")
print(node_information)
print(node_information.name, node_information.nrows, node_information.ncols)

Nodes = node_information.nrows
node_xplace = node_information.col_values(1, start_rowx = 1)
node_yplace = node_information.col_values(2, start_rowx = 1)
print(len(node_xplace)) 
print("Nodes:", Nodes)
node_xplace = [0] + node_xplace
node_yplace = [0] + node_yplace
print(len(node_xplace))

edge_ifm = data.sheet_by_name("全市交通路口的路线")
start_edge = edge_ifm.col_values(0, start_rowx = 1)
start_edge = [int(x) for x in start_edge]
to_edge = edge_ifm.col_values(1, start_rowx = 1)
to_edge = [int(x) for x in to_edge]
print(to_edge)
print(len(to_edge))
Edges = len(to_edge)
print("Edges", Edges)

inf = 1e9
dis = inf * np.ones((Nodes, Nodes))
print(type(dis))
for i, j in zip(start_edge, to_edge):
    dis[i][j] = np.sqrt((node_xplace[i] - node_xplace[j]) ** 2 + (node_yplace[i] - node_yplace[j]) ** 2)
    dis[j][i] = dis[i][j]
print(dis[1][1])
print(dis[1][75])
print(dis[75][1])

a_size = 93
for k in range(1, a_size): 
    for i in range(1, a_size): 
        for j in range(1, a_size): 
            if dis[i][k] + dis[k][j] < dis[i][j]:
                dis[i][j] = dis[i][k] + dis[k][j]

for i in range(dis.shape[0]):
    for j in range(dis.shape[1]):
        dis[i][j] /= 10
        
print(dis[75, 78])
print(dis[1, 78])
print(dis[78, 75])
print(dis[1, 92])


np.savetxt("data/dis.dat", dis, fmt = '%f', delimiter = ',')


plf = list(range(1, 21))
print(type(plf))
print(plf)