from die import Die

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
print(frequencies)