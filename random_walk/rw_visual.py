import matplotlib.pyplot as plt
from random_walk import RandomWalk

#Make a random walk. Input  is the number of points to plot
#Can generate multiple walks until you quit
while True:
    rw = RandomWalk(1000000)
    rw.fill_walk()

    #Plot the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.get_cmap('YlGnBu'), edgecolors='none', facecolor='black', s=1)

    #Emphasize the starting and ending points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #Remove axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    #Show plot
    plt.show()

    keep_running = input("Make another? (y/n)")
    if keep_running == 'n':
        break