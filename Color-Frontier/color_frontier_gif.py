"""
    Author: David Garcia Fernandez
    Date: 29/6/2019
    Visit: https://ndres.me/post/matplotlib-animated-gifs-easily/
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import imageio

x0, y0, z0 = 255, 0, 0
res = 200

def plot_for_offset(radius, azim):
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

    C = np.array([ [int(r[i]), int(g[i]), int(b[i])] for i in range(len(r))])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim3d(0, 255)
    ax.set_ylim3d(0, 255)
    ax.set_zlim3d(0, 255)
    ax.set_xlabel('R', color='#FF0000')
    ax.set_ylabel('G', color='#00FF00')
    ax.set_zlabel('B', color='#0000FF')
    plt.title('RGB Color Frontier\nRadius = ' + str(int(round(radius, 0))), y = 1.05)
    ax.scatter(r, g, b, c=C/255.0)
    ax.view_init(elev=30., azim=azim)
    # plt.show()
    fig.canvas.draw()  # draw the canvas, cache the renderer
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    return image


# Defining radius possible values
radius = np.linspace(1, 435, 100)
radius = list(radius) + list(radius)[::-1]

# Defining rotation angle values
azim = np.linspace(135, 170, 50)
azim = list(azim) + list(azim)[::-1]
azim2 = np.linspace(135, 100, 50)
azim = azim + list(azim2) + list(azim2)[::-1]

# Generating gif
kwargs_write = {'fps':1.0, 'quantizer':'nq'}
imageio.mimsave('./colors.gif', [plot_for_offset(radius[i], azim[i]) for i in range(200)], fps=10)