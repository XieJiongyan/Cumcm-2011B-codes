import numpy as np 

dis = np.loadtxt('data/dis.dat', delimiter = ',')

Plf_nodes = list(range(1, 21))

cro_nodes = list(range(21, 93))

car_ = {}
for ip in Plf_nodes:
    car_[ip] = []

print(car_)

for ic in cro_nodes:
    ip = np.argmin(dis[ic, Plf_nodes])
    # print(dis[ic, Plf_nodes])
    car_[Plf_nodes[ip]].append(ic)

for ip in car_:
    print("路口", ip, "管辖的路口有：", car_[ip])

print(dis[28][15])
print(dis[29, 15])