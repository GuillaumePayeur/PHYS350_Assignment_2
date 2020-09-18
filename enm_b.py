# Guillaume Payeur
import numpy as np
import matplotlib.pyplot as plt

# Setting constants
R = 1
k = 1

# Creating the a grid with the position of the charges
points = np.linspace(-R,R,500)
x_grid,y_grid = np.meshgrid(points,points)
x, y = np.ravel(x_grid), np.ravel(y_grid)
z = 0*x

# Creating a grid with the charge of the charges
q = np.ones(x.shape)/(500*500)

# Function to compute E_z at a point r=(0,0,z)
def E_z(z_array,x,y,z,q):
    E = np.zeros((z_array.shape[0]))
    for i in range(z_array.shape[0]):
        for j in range(len(x)):
            dx = 0 - x[j]
            dy = 0 - y[j]
            dz = z_array[i] - z[j]
            d3 = (dx**2 + dy**2 + dz**2)**(3/2)

            E[i] += q[j]*dz/d3
    return E

# Plotting E_z versus z for small z
z_array = np.linspace(0.02,0.1,50)
E_array = E_z(z_array,x,y,z,q)
plt.style.use('seaborn-whitegrid')
plt.xlabel('z')
plt.ylabel('E_z')
plt.title('E_z versus z')
plt.plot(z_array,E_array)
plt.show()
