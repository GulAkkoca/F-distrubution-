import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f

# Data initialization and variance calculations
photometric = np.array([16, 17, 25, 26, 32, 34, 38, 40, 42])
photographic = np.array([14, 16, 24, 28, 32, 35, 37, 42, 43, 45, 47])
var_photometric = np.var(photometric, ddof=1)
var_photographic = np.var(photographic, ddof=1)
F_ratio = var_photometric / var_photographic
df_photometric = len(photometric) - 1
df_photographic = len(photographic) - 1
alpha = 0.05
critical_value_low = f.ppf(alpha / 2, df_photometric, df_photographic)
critical_value_high = f.ppf(1 - alpha / 2, df_photometric, df_photographic)

# Print results
if var_photometric / var_photographic == 1:
    print("Variances are equal.")
else:
    print("Variances are not equal.")

if F_ratio < critical_value_low or F_ratio > critical_value_high:
    print("Reject null hypothesis. There is a significant difference in variability between the two methods.")
else:
    print("Fail to reject null hypothesis. There is no significant difference in variability between the two methods.")
print("F-ratio:", F_ratio)
print("Critical values for F-test:", critical_value_low, "and", critical_value_high)

# Plotting the F-distribution
x = np.linspace(0.01, 5, 1000)
f_dist = f.pdf(x, df_photometric, df_photographic)
plt.plot(x, f_dist, label='F-distribution')

# Shading the critical regions
x_critical_low = np.linspace(0.01, critical_value_low, 100)
y_critical_low = f.pdf(x_critical_low, df_photometric, df_photographic)
plt.fill_between(x_critical_low, y_critical_low, color='red', alpha=0.5, label='Critical Region (Lower)')
x_critical_high = np.linspace(critical_value_high, 5, 100)
y_critical_high = f.pdf(x_critical_high, df_photometric, df_photographic)
plt.fill_between(x_critical_high, y_critical_high, color='red', alpha=0.5, label='Critical Region (Upper)')

# Adding labels and legend
plt.xlabel('F-value')
plt.ylabel('Density')
plt.title('F-distribution with Critical Regions')
plt.legend()

# Displaying the plot
plt.show()
