import numpy as np
import matplotlib.pyplot as plt


def saveFig(plt):
    import os

    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, 'Properties/')
    file_name = "equal_vectors.png"

    # in case the directory does not exist, create a directory for saving figures.
    if not os.path.isdir(results_dir):
        os.makedirs(results_dir)

    plt.savefig(results_dir + file_name)


vec_1 = np.array([3, 3])

# Array for containing all vectors
vecs = np.array([vec_1])

# transpose and extract the number of rows as well as cols
rows, cols = vecs.T.shape

fig = plt.figure()
ax = plt.axes()

ax.arrow(0, 0, vecs[0, 0], vecs[0, 1], head_width=0.1, head_length=0.2, color='b')
ax.arrow(-1, -0, vecs[0, 0], vecs[0, 1], head_width=0.1, head_length=0.2, color='r')
ax.arrow(1, -1, vecs[0, 0], vecs[0, 1], head_width=0.1, head_length=0.2, color='k')

ax.annotate('A', (0, 2), fontsize=13, color='red')
ax.annotate('B', (2, 1.5), fontsize=13, color='blue')
ax.annotate('C', (3, 0.5), fontsize=13, color='black')

plt.plot(0, 0, 'ok')  # plot a black point denoting the origin
plt.plot(-1, 0, 'ok')
plt.plot(1, -1, 'ok')

plt.axis('equal')  # set the axes to the same scale
plt.xlim([-3, 5])  # set the x axis limits
plt.ylim([-2, 5])  # set the y axis limits
plt.grid(b=True, which='major')  # plot grid lines
saveFig(plt)
plt.show()
