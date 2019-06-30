"""
    Author: David Garcia Fernandez
    Date: 29/6/2019
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Initial parameters
x0, y0, z0 = 255, 0, 0
radius = 100
res = 200

# Defining parameter spaces
phi_values = np.linspace(0, np.pi, res)
theta_values = np.linspace(0, 2 * np.pi, res)

# Color coordinates will be stored here
r, g, b = [], [], []

for phi in phi_values:
    for theta in theta_values:
        # Calculating the coordinates of the point
        x = x0 + radius * np.cos(theta) * np.sin(phi)
        y = y0 + radius * np.sin(theta) * np.sin(phi)
        z = z0 + radius * np.cos(phi)

        # Checking if the point is inside the RGB space
        if x >= 0 and x < 255 \
                  and y >= 0 and y < 255 \
                  and z >= 0 and z < 255:
            r.append(x)
            g.append(y)
            b.append(z)

# Preparing the array of colors
C = np.array([[int(r[i]), int(g[i]), int(b[i])] for i in range(len(r))])

# Plotting the graph
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Axis limits
ax.set_xlim3d(0, 255)
ax.set_ylim3d(0, 255)
ax.set_zlim3d(0, 255)

# Axis labels and colors
ax.set_xlabel('R', color='#FF0000')
ax.set_ylabel('G', color='#00FF00')
ax.set_zlabel('B', color='#0000FF')

# Title
plt.title('RGB Color Frontier\nRadius = ' + str(int(radius)), y=1.05)

ax.scatter(r, g, b, c =C/255.0)

# Initial position
ax.view_init(elev=30., azim=135)
plt.show()