#15-1 and #15-2
import matplotlib.pyplot as plt

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.autumn, s=40)
plt.title("Cubes", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Cubes of Values", fontsize=14)

plt.tick_params(axis='both', which='major')
plt.show()