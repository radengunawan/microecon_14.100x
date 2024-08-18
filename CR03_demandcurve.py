# by Eka Gunawan
import matplotlib.pyplot as plt
import numpy as np

# Define the demand curve function
def demand_curve(P):
    return 3000 - P

# Define price values
P_values = np.linspace(0, 3000, 100)
Q_values = demand_curve(P_values)

# Plotting the demand curve
plt.figure(figsize=(7.5, 5))
plt.plot(P_values, Q_values, label=r'Demand Curve $Q = 3000 - P$', color='blue')
plt.axvline(x=1500, color='green', linestyle='--', label=r'Unit Elasticity $P = 1500$')
plt.axhline(y=1500, color='green', linestyle='--')
plt.scatter(1000, demand_curve(1000), color='red', zorder=5, label=r'Given Price $P = 1000$')

# Adding labels and title
plt.title('Demand Curve for Private Schools')
plt.xlabel('Price (P)')
plt.ylabel('Quantity Demanded (Q)')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()

