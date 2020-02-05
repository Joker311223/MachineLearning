from PSO01ag import PSO
import matplotlib.pyplot as plt
import numpy as np


dim = 10000
size = 20
iter_num = 100
x_max = 10
max_vel = 0.5
itemLimit = 0.1


pso = PSO(dim, size, iter_num, x_max, max_vel, itemLimit)
fit_var_list, best_pos = pso.update(dim, x_max)
print("最优位置:" + str(best_pos))
print("最优解:" + str(fit_var_list[-1]))
plt.plot(np.linspace(0, iter_num, iter_num)[:np.size(fit_var_list)], fit_var_list, c="r", alpha=0.5)
plt.show()
