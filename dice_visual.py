from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

#Create two dice
die = Die(6)
die2 = Die(10)

#Roll and store results as a list
results = []
for roll_num in range(50_000):
    result = die.roll() + die2.roll()
    results.append(result)

#Counting how many times each number is rolled
frequencies = []
max_result = die.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config  = {'title': 'Result', 'dtick':1}
y_axis_config = {'title': 'Frequency of Result'}
layout = Layout(title='Rolling a D6 and a D10 50,000 Times!',
                xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': layout}, filename='d10d6.html')