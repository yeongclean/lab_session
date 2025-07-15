import numpy as np
import matplotlib.pyplot as plt

# Load potential data
file_path = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/au_v_potential_1d.dat"
data = np.loadtxt(file_path, comments="#")
z = data[:, 0]  # z-axis in Bohr
potential = data[:, 1] * 13.6057  # Potential in eV (1 Ry = 13.6057 eV)

# Plot to find vacuum region
plt.plot(z, potential, label='Potential (eV)')
plt.xlabel('z (Bohr)')
plt.ylabel('Potential (eV)')
plt.axhline(y=np.max(potential), color='r', linestyle='--', label='Vacuum Level')
plt.legend()
plt.show()

# Extract vacuum potential
vacuum_potential = np.max(potential)
print(f"Vacuum Potential: {vacuum_potential:.4f} eV")