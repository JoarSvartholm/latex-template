import matplotlib.pyplot as mpl
import numpy as np
import sys

k_Boltzmann = 8.6173303e-5 # eV/K

Temp_Si = (np.array([400, 1000]))
n_Si = np.array([1e19, 1e24])

Temp_Ge = (np.array([100, 800]))
n_Ge = np.array([1e6, 1e24])

Figure_nvsT_inv = mpl.Figure()
mpl.plot(1/Temp_Si, np.log(n_Si), 1/Temp_Ge, np.log(n_Ge))

p_Si_pfit = np.polyfit(np.log(n_Si), 1/Temp_Si, 1)
p_Si = (np.log(n_Si[1]) - np.log(n_Si[0]))/(1/Temp_Si[1] - 1/Temp_Si[0])
E_g_Si = -p_Si*(2*k_Boltzmann)

p_Ge_pfit = np.polyfit(np.log(n_Ge), 1/Temp_Ge, 1)
p_Ge = (np.log(n_Ge[1]) - np.log(n_Ge[0]))/(1/Temp_Ge[1] - 1/Temp_Ge[0])
E_g_Ge = -p_Ge*(2*k_Boltzmann)

print('Slope is:', p_Si, p_Ge)
print('Silicon band gap is: ', E_g_Si, 'eV')
print('Germanium band gap is: ', E_g_Ge, 'eV')


mpl.show()
sys.exit()
