from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas

points = pandas.read_csv('trace2.csv')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

s = points['s'].values
b = points['b'].values
E = points['E'].values
p = points['p'].values


img = ax.scatter(s, b, E, c=p, alpha=0.8, marker='.', cmap=plt.hot(), s=500)
ax.legend()
ax.set_xlabel("s")
ax.set_ylabel("b")
ax.set_zlabel("E")

fig.colorbar(img)

plt.show()