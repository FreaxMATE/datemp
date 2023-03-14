#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots()

data = np.loadtxt('data/linear-regression.txt')
i = data[:, 0]
u = data[:, 1]
r = u/i

fit_range = r[0:10]
fit_values = u[0:10]

fit = np.polyfit(fit_range, fit_values, 1)
r_indiscrete = np.linspace(0, 18, 100)
fit_function = np.poly1d(fit)
axes.plot(r_indiscrete, fit_function(r_indiscrete), lw=1, label=r'Linfit (Steigung $' + str(round(fit[0], 1)) +  r'$ $' + r'\frac{V}{k\Omega})$')


axes.plot(r, u, '.', label='Ausgangsspannung')

plt.axvline(x=r[41], color='tab:green', linestyle=(0, (5, 5)), lw=1, label=r'$R_{Grenz} =' + r'$ $' + str(round(r[41], 1)) + r'$ $' + ' k\Omega$')

axes.set_xlabel(r'Widerstand ' + r'$R_{poti}$' + r' $(k\Omega)$')
axes.set_ylabel(r'Spannung ' + r'$I$ ' + '$(V)$')


axes.legend()
axes.grid(linestyle='--')
plt.savefig("figures/linear-regression.png",dpi=300)







