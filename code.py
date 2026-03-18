import numpy as np
import matplotlib.pyplot as plt

# --- Styling ---
SMALL_SIZE = 14
MEDIUM_SIZE = 16
BIGGER_SIZE = 18

plt.rc('font', size=SMALL_SIZE)
plt.rc('axes', titlesize=SMALL_SIZE)
plt.rc('axes', labelsize=MEDIUM_SIZE)
plt.rc('xtick', labelsize=SMALL_SIZE)
plt.rc('ytick', labelsize=SMALL_SIZE)
plt.rc('legend', fontsize=SMALL_SIZE)
plt.rc('figure', titlesize=BIGGER_SIZE)

def calculate_ppv(prevalence, sensitivity, specificity):
    true_pos = sensitivity * prevalence
    false_pos = (1 - specificity) * (1 - prevalence)
    return true_pos / (true_pos + false_pos)

# -- Parameters --
prevalences_log = np.logspace(np.log10(0.00001), np.log10(0.5), 1000)
prevalences_lin = np.linspace(0.00001, 0.5, 1000)

specificities = [0.99, 0.999, 0.9999, 0.99999]
sensitivity = 0.99

# Color Palette
colors = ['darkcyan', 'crimson', 'orange', 'mediumorchid']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

for spec, color in zip(specificities, colors):
    # Plotting on Log Scale
    ppv_log = calculate_ppv(prevalences_log, sensitivity, spec)
    ax1.plot(prevalences_log * 100, ppv_log * 100, 
             label=f'Spec: {spec*100:.3f}%', color=color, linewidth=3)

    # Plotting on Linear Scale
    ppv_lin = calculate_ppv(prevalences_lin, sensitivity, spec)
    ax2.plot(prevalences_lin * 100, ppv_lin * 100, 
             label=f'Spec: {spec*100:.3f}%', color=color, linewidth=3)

for ax in [ax1, ax2]:
    ax.axvline(x=5, color='black', linestyle='--', alpha=0.4, 
               label='Example Prevalence (5%)')
    ax.set_ylabel('Prob. of Actual Infection (%)')
    ax.legend(frameon=False)

# Log Plot
ax1.set_xscale('log')
ax1.set_xlabel('Infection Prevalence (%) (Log Scale)')

# Linear Plot
ax2.set_xlabel('Infection Prevalence (%) (Linear Scale)')

plt.tight_layout()
plt.savefig('plot_log_vs_lin.pdf', dpi=600)
plt.show()
