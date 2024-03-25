import numpy as np
import matplotlib.pyplot as plt

T = 300 # K
k_B = 1.381e-23 # J K^{-1}


def density_of_states(lambda_wave):
    rho = (8*np.pi*k_B*T)/(lambda_wave)    
    return rho

def energy_distribution(lambda_wave, d_lambda):
    rho = density_of_states(lambda_wave)
    return rho * d_lambda

wavelengths = np.linspace(1e-9, 3e-8, 1000)
d_lambda = wavelengths[1] - wavelengths[0]
energy_distr = np.array([energy_distribution(lambda_wave, d_lambda) for lambda_wave in wavelengths])


plt.figure(figsize=(10, 6))
plt.plot(wavelengths * 1e9, energy_distr, label='Energy Distribution')  # converting meters to nanometers for the plot
plt.xlabel('Wavelength (nm)')
plt.ylabel('Energy Distribution (J/m^3/nm)')
plt.title('Energy Distribution per Wavelength')
plt.legend()
plt.grid(True)
plt.show()
