import pandas
import matplotlib.pyplot as plt
import numpy

def normalize(data): # min-max
    n_data = list()
    for i in data:
        n_data.append((i - data.min()) / (data.max() - data.min()))
    return numpy.array(n_data)

X, Y, Z = numpy.meshgrid(numpy.linspace(0, 1, 93), numpy.linspace(0, 1, 93), numpy.linspace(0, 1, 93))

lin_reg = 0.432 - 0.022 * X - 0.098 * Y + 0.59 * Z

kw = {
    'vmin': lin_reg.min(),
    'vmax': lin_reg.max(),
    'levels': numpy.linspace(lin_reg.min(), lin_reg.max(), 10),
}

fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(111, projection='3d')

_ = ax.contourf(
    X[:, :, 0], Y[:, :, 0], lin_reg[:, :, -1],
    zdir='z', offset=Z.max(), **kw
)
_ = ax.contourf(
    X[0, :, :], lin_reg[0, :, :], Z[0, :, :],
    zdir='y', offset=0, **kw
)
C = ax.contourf(
    lin_reg[:, -1, :], Y[:, -1, :], Z[:, -1, :],
    zdir='x', offset=X.max(), **kw
)
# --


xmin, xmax = X.min(), X.max()
ymin, ymax = Y.min(), Y.max()
zmin, zmax = Z.min(), Z.max()
ax.set(xlim=[xmin, xmax], ylim=[ymin, ymax], zlim=[zmin, zmax])

edges_kw = dict(color='0.4', linewidth=1, zorder=1e3)
ax.plot([xmax, xmax], [ymin, ymax], 0, **edges_kw)
ax.plot([xmin, xmax], [ymin, ymin], 0, **edges_kw)
ax.plot([xmax, xmax], [ymin, ymin], [zmin, zmax], **edges_kw)

ax.set_xlabel('City MPG, vol./len.')
ax.set_ylabel('Highway MPG, vol./len.')
ax.set_zlabel('Power, hp')

ax.view_init(15, 270)

colorbar = fig.colorbar(C, ax=ax, shrink=0.5, aspect=10)
colorbar.set_label("Price, $ cond.")
plt.suptitle("4D heatmap for linear regression")
plt.show()