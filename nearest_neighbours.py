import numpy as np
import matplotlib.pyplot as plt


# Overview:
# Randomly splits data points withing a given range n.
# Finds nearest neighbors of the chosen point and plots it.

# Randomly distributes n data points
def random_distribution(n):
    plt.figure(1)
    plt.xlim([0, n])
    plt.ylim([0, n])
    data = 0 + (n - 0) * np.random.random([2, n])
    xdata = data[0, :]
    ydata = data[1, :]
    plt.plot(xdata, ydata, 'ro')
    plt.show()
    return data


# Finds root mean square distance between data points and finds nearest neighbors
def nearest_neighbors(n):
    dis_parameter = int(0.2 * n)
    data = random_distribution(n)
    dist = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            x1 = data[0, i]
            x2 = data[0, j]
            y1 = data[1, i]
            y2 = data[1, j]
            dist[i, j] = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    calc_matrix = np.zeros([n, n])
    for k in range(n):
        for l in range(n):
            if dist[k, l] < dis_parameter and dist[k, l] > 0:
                calc_matrix[k, l] = 1

    N = int(input('enter the node number = '))
    near_neighbors = calc_matrix[N - 1, :]
    plt.plot(data[0, N - 1], data[1, N - 1], 'ko')
    for i in range(0, n):
        if near_neighbors[i] == 1:
            print('neighbours are: ', i + 1)
            plt.plot([data[0, N - 1], data[0, i]], [data[1, N - 1], data[1, i]])

    plt.show()


if __name__ == '__main__':
    nearest_neighbors(100)
