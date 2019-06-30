'''
    Author: David Garcia Fernandez
    Date: 29/6/2019
'''
import matplotlib.pyplot as plt
import numpy as np

final1 = []
final2 = []
for c in range(256):
    for d in range(256):
        final1.append(c)
        final2.append(d)

C = np.array([[255, int(final1[i]), int(final2[i])] for i in range(len(final1))])

fig, ax = plt.subplots(1, figsize=(10, 6))
fig.suptitle('RGB Colors, R = 255', y=0.96, size=16)

ax.scatter(final1, final2, c=C/255.0)
ax.set_xlabel("G", color="#00FF00", size=14)
ax.set_ylabel("B", color="#0000FF", size=14)
plt.show()


