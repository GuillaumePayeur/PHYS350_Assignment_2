# Guillaume Payeur
import numpy as np
import matplotlib.pyplot as plt

# Setting constants
R = 1
k = 1

# Creating the a grid with the position of the charges
points = np.linspace(-R,R,100)
x_grid,y_grid = np.meshgrid(points,points)
x, y = np.ravel(x_grid), np.ravel(y_grid)
z = 0*x

# Creating a grid with the charge of the charges
q_grid = np.exp(-(x_grid**2 + y_grid**2)/(2*R**2))
q = np.ravel(q_grid)

# Function to compute the potential at a point r=(0,y,z).
def Potential(r,x,y,z,q):
    V = np.zeros((r.shape[1]))
    for i in range(r.shape[1]):
        for j in range(len(x)):
            dx = r[0][i] - x[j]
            dy = r[1][i] - y[j]
            dz = r[2][i] - z[j]
            d = np.sqrt(dx**2 + dy**2 + dz**2)

            V[i] += q[j]/d
    return V

# Creating a grid to make a plot on the yz plane
plt_size = 200
points = np.linspace(-2*R, 2*R, plt_size)
y_grid_plt, z_grid_plt = np.meshgrid(points,points)
y_plt, z_plt = np.ravel(y_grid_plt), np.ravel(z_grid_plt)
x_plt = 0*y_plt

# Creating an array containing the values of the potential
r = np.array([x_plt,y_plt,z_plt])
V = Potential(r,x,y,z,q)
V = np.reshape(V, (plt_size,plt_size))
plt.imshow(V, extent=[-2*R,2*R,-2*R,2*R])
plt.xlabel('y')
plt.ylabel('z')
plt.title('Electric potential on the yz plane')
plt.colorbar()
plt.show()
