import matplotlib.pyplot as plt
import pygal

from random_walk import RandomWalk


#make a random walk and plot the points.
rw = RandomWalk(5000)
rw.fill_walk()

#set plot size to fill screen
plt.figure(dpi=128, figsize=(10,6))

point_numbers = list(range(rw.num_points))
plt.plot(rw.x_values, rw.y_values, linewidth=.5)

#emphasize start and end
plt.scatter(0,0, c='green', edgecolors='none', s=20)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=20)

#remove axes
plt.gca().get_xaxis().set_visible(False)
plt.gca().get_yaxis().set_visible(False)

plt.show()
