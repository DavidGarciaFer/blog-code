"""
    Author: David Garcia Fernandez
    Date: 19/7/2019
    Description: Creates a video file called 'animation.avi'
    with an example of the Method 1 to find Colinear points
    exaplained in https://davidgarciafer.github.io/Colinear-Points/.
    Animation stops if a line is found.
"""
import cv2 as cv
import numpy as np

n_points = 5  # Number of points

rate = 100
width, height = 1000, 800
canvas = np.zeros((height, width, 3), np.uint8)

yellow = (3, 186, 252)
gray = (85, 65, 50)
green = (80, 215, 20)
blue = (225, 155, 30)

# Creating a random set of points
x_values = [np.random.randint(width) for i in range(n_points)]
y_values = [np.random.randint(height) for i in range(n_points)]
colors = [x_values[i] + y_values[i] for i in range(n_points)]

out = cv.VideoWriter('animation.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (width, height))


def draw(p, q1, q2, line=False):
    """
    Creates a new frame and adds it to a global variable called out (VideoWriter).

    Args:
        p (tuple of int): Coordinates of reference point.
        q1 (tuple of int): Coordinates of second point.
        q2 (tuple of int): Coordinates of third point.
        line (:obj:`bool`, default=False): Indicates if a line has been found.

    Returns:
        (bool): True if the algorithm has finished, else False.
    """
    cv.rectangle(canvas, (0, 0), (width, height), gray, -1)
    for i in range(len(x_values)):
        point = (x_values[i], y_values[i])
        cv.circle(canvas, point, 3, blue, -1)

    cv.circle(canvas, p, 5, green, -1)
    cv.circle(canvas, q1, 5, green, -1)
    cv.circle(canvas, q2, 5, green, -1)

    color = yellow if line is True else green
    cv.line(canvas, p, q1, color, 1)
    cv.line(canvas, p, q2, color, 1)
    cv.line(canvas, q1, q2, color, 1)

    out.write(canvas)
    if line:
        for i in range(20):
            out.write(canvas)
        return True
    return False


def method_1():
    size = len(x_values)
    x_segments = []
    y_segments = []
    for i in range(size):
        x1, y1 = x_values[i], y_values[i]
        for j in range(size):
            if i == j:
                continue
            x2, y2 = x_values[j], y_values[j]
            for k in range(size):
                if i == k or j == k:
                    continue
                x3, y3 = x_values[k], y_values[k]
                ret = draw((x1, y1), (x2, y2), (x3, y3))
                if ret is True:
                    return
                if x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) == 0:
                    x_segments += [x1, x2, x1, x3]
                    y_segments += [y1, y2, y1, y3]
                    ret = draw((x1, y1), (x2, y2), (x3, y3), line=True)
                    if ret is True:
                        return
    return x_segments, y_segments


method_1()
cv.destroyAllWindows()
out.release()