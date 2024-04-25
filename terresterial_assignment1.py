import numpy as np
import matplotlib.pyplot as plt


# define function of Planck's radiation law
def planck(wavelength, temperature):
    h = 6.62607015e-34  # Planck constant
    c = 299792458  # Light speed
    k = 1.380649e-23  # Boltzmann constant
    return (2*h*c**2) / (wavelength**5 * (np.exp(h*c/(wavelength*k*temperature)) - 1))


# set parameters
wavelength = np.logspace(-1, 3, 1000)  # (unit: μm)
temperatures = [5900, 4000, 3000, 1000, 500, 300]  # (unit: K)


# plot a figure
plt.figure(figsize=(6, 4))
for temp in temperatures:
    spectral_radiance = planck(wavelength * 1e-6, temp)
    plt.plot(wavelength, spectral_radiance, label=f'{temp}[K]', linewidth=1.5)

plt.xlabel('Wavelength (μm)')
plt.ylabel('Spectral radiance (W⋅m$^{-2}$⋅sr$^{-1}$⋅μm$^{-1}$)')
plt.title('Blackbody radiation spectrum (log scale plot)')
plt.xscale('log')
plt.yscale('log')
plt.xlim(0.1, 10**3)
plt.ylim(1e4, 1e15)
plt.grid(True, which='both', linestyle='-', linewidth=0.5, color='#888888', alpha=0.5)
plt.xticks([0.1, 1, 10, 100, 1000], ['0', '1', '10', '100', '1000'])
plt.yticks([1e4, 1e7, 1e11, 1e15], ['$10^{4}$', '$10^{7}$', '$10^{11}$', '$10^{15}$'])
plt.tick_params(axis='both', which='major', labelsize=10)
plt.tick_params(axis='both', which='minor', labelsize=8)

plt.legend(loc='upper right', fontsize=10)
plt.tight_layout()
plt.show()