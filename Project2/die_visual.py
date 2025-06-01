import pygal
import matplotlib.pyplot as plt
from die import Die

#create a D6
die_1 = Die(6)
die_2 = Die(6)


#Make some rolls, and store resutls in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll() 
    results.append(result)

#analyze the results
frequencies = []
max_result = die_1.num_sides * die_2.num_sides 
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#visualize the results
hist = pygal.Bar()
hist.title = "Results of rolling three D6s 1000 times."
hist.x_labels = [str(x) for x in range(1, max_result+1)]
hist._x_title = "Result"
hist._y_title = "Frequency of Results"

hist.add('D6 * D6', frequencies)
hist.render_to_file('die_visual.svg')

x_values = [x for x in range (1, max_result+1)]
plt.scatter(x_values, frequencies, s=10)
plt.show()

print(frequencies)