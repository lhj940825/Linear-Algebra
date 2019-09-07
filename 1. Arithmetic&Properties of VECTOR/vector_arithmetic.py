import numpy as np
import matplotlib.pyplot as plt

vec_1 = np.array([1, 1])
vec_2 = np.array([-2, 2])

vec_3 = vec_1 + vec_2

# Array for containing all vectors
vecs = np.array([vec_1, vec_2, vec_3])

# transpose and extract the number of rows as well as cols
rows, cols = vecs.T.shape

colors = ['r', 'k', 'b']  # set color of vectors
labels = ['vector 1', 'vector 2', 'vector 3']

# 1.1: codes in order to plot the three example vectors
fig = plt.figure()
ax = plt.axes()

for i, l in enumerate(range(0, cols)):
    # draw vectors with initialized arguments
    ax.arrow(0, 0, vecs[i, 0], vecs[i, 1], head_width=0.1, head_length=0.2, color=colors[i], label=labels[i])

ax.annotate('vector 1', (vec_1[0] + 0.3, vec_1[1]), fontsize=13, color='red')
ax.annotate('vector 2', (vec_2[0] + 0.2, vec_2[1]), fontsize=13, color='black')
ax.annotate('vector 3', (vec_3[0] + 0.3, vec_3[1]), fontsize=13, color='blue')

plt.plot(0, 0, 'ok')  # plot a black point denoting the origin
plt.axis('equal')  # set the axes to the same scale
plt.xlim([-3, 5])  # set the x axis limits
plt.ylim([-2, 5])  # set the y axis limits
plt.grid(b=True, which='major')  # plot grid lines
plt.savefig('vector arithmetic-plus-(1)')
plt.show()

# 1.2: codes in order to plot the vector operation '+'
fig = plt.figure()
ax = plt.axes()

for i, l in enumerate(range(0, cols)):

    # draw vectors with initialized arguments
    if labels[i] == 'vector 1':
        # vecs[1,0] and vecs[1, 1] denote the position of 'vector 2'
        ax.arrow(vecs[1, 0], vecs[1, 1], vecs[i, 0], vecs[i, 1], head_width=0.1, head_length=0.1, color=colors[i],
                 label=labels[i])
    else:
        ax.arrow(0, 0, vecs[i, 0], vecs[i, 1], head_width=0.1, head_length=0.2, color=colors[i], label=labels[i])

ax.annotate('vector 1', (vec_2[0] - 0.4, vec_2[1] + 0.8), fontsize=13, color='red')
ax.annotate('vector 2', (vec_2[0] + 0.2, vec_2[1]), fontsize=13, color='black')
ax.annotate('vector 3', (vec_3[0] + 0.3, vec_3[1]), fontsize=13, color='blue')

plt.plot(0, 0, 'ok')  # plot a black point denoting the origin
plt.axis('equal')  # set the axes to the same scale
plt.xlim([-3, 5])  # set the x axis limits
plt.ylim([-2, 5])  # set the y axis limits
plt.grid(b=True, which='major')  # plot grid lines
plt.savefig('vector arithmetic-plus-(2)')
plt.show()

# 1.3: codes in order to plot the three example vectors

# define example vectors
vec_1 = np.array([1, 1])
vec_2 = np.array([-2, 2])

vec_3 = vec_1 - vec_2

# Array for containing all vectors
vecs = np.array([vec_1, vec_2, vec_3])
fig = plt.figure()
ax = plt.axes()

for i, l in enumerate(range(0, cols)):
    # draw vectors with initialized arguments
    ax.arrow(0, 0, vecs[i, 0], vecs[i, 1], head_width=0.1, head_length=0.2, color=colors[i], label=labels[i])

ax.annotate('vector 1', (vec_1[0] + 0.3, vec_1[1]), fontsize=13, color='red')
ax.annotate('vector 2', (vec_2[0] + 0.2, vec_2[1]), fontsize=13, color='black')
ax.annotate('vector 3', (vec_3[0] + 0.3, vec_3[1]), fontsize=13, color='blue')

plt.plot(0, 0, 'ok')  # plot a black point denoting the origin
plt.axis('equal')  # set the axes to the same scale
plt.xlim([-5, 5])  # set the x axis limits
plt.ylim([-5, 5])  # set the y axis limits
plt.grid(b=True, which='major')  # plot grid lines
plt.savefig('vector arithmetic-minus-(1)')
plt.show()

# 1.4: codes in order to plot the vector operation '-'

vec_1 = np.array([1, 1])
vec_2 = np.array([-2, 2])

vec_3 = vec_1 - vec_2

# Array for containing all vectors
vecs = np.array([vec_1, vec_2, vec_3])

fig = plt.figure()
ax = plt.axes()

# draw the vector 1
ax.arrow(-vecs[1, 0], -vecs[1, 1], vecs[0, 0], vecs[0, 1], head_width=0.1, head_length=0.2, color=colors[0])

# draw the minus vector 2(reversed)
ax.arrow(0, 0, -vecs[1, 0], -vecs[1, 1], head_width=0.1, head_length=0.2, color=colors[1])

# draw the vector 3 denoting vector 1 subtracted by vector 2
ax.arrow(0, 0, vecs[2, 0], vecs[2, 1], head_width=0.1, head_length=0.2, color=colors[2])

ax.annotate('vector 1', (-vecs[1, 0] + 0.3, -vecs[1, 1] - 0.5), fontsize=13, color='red')
ax.annotate('- vector 2', (-vec_2[0] - 1.5, -vec_2[1] + 0.3), fontsize=13, color='black')
ax.annotate('vector 3', (vec_3[0] - 1, vec_3[1] + 0.5), fontsize=13, color='blue')

plt.plot(0, 0, 'ok')  # plot a black point denoting the origin
plt.axis('equal')  # set the axes to the same scale
plt.xlim([-5, 5])  # set the x axis limits
plt.ylim([-5, 5])  # set the y axis limits
plt.grid(b=True, which='major')  # plot grid lines
plt.savefig('vector arithmetic-minus-(2)')
plt.show()
