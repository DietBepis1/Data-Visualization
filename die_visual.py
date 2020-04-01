from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

#Create a D6
die = Die(6)

#Roll and store results as a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#Counting how many times each number is rolled
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config  = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
layout = Layout(title='Results of Rolling One D6 1000 times',
                xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': layout}, filename='d6.html')