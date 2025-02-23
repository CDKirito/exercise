import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 创建一个RandomWalk实例
rw = RandomWalk(50000)
rw.fill_walk()

# 绘制随机漫步图
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9))
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
ax.set_aspect('equal')

# 突出起点和终点
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

# 隐藏坐标轴
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()