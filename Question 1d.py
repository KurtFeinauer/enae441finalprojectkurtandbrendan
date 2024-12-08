import numpy as np
import matplotlib.pyplot as plt

# Load the structured array
data = np.load('Project-Measurements-Easy.npy', allow_pickle=True)

# Extract columns (adjust column names/index if needed)
tvec = data[:, 0]  # Assuming time is in the first column
ivec = data[:, 1]  # Station ID
rhovec = data[:, 2]  # Range
rhodotvec = data[:, 3]  # Range rate

# Define colors for stations
colors = ['blue', 'red', 'green']

# Define a smaller marker size
marker_size = 10

# Create scatter plot for time vs range
plt.figure(figsize=(10, 5))
for station_id in range(3):  # Station IDs are 0, 1, 2
    mask = ivec == station_id
    plt.scatter(tvec[mask], rhovec[mask], label=f'DSN {station_id}', color=colors[station_id], s=marker_size)

plt.title('Time vs Range')
plt.xlabel('Time (t)')
plt.ylabel('Range (ρ)')
plt.legend()
plt.grid(True)

# Create scatter plot for time vs range rate
plt.figure(figsize=(10, 5))
for station_id in range(3):  # Station IDs are 0, 1, 2
    mask = ivec == station_id
    plt.scatter(tvec[mask], rhodotvec[mask], label=f'DSN {station_id}', color=colors[station_id], s=marker_size)

plt.title('Time vs Range Rate')
plt.xlabel('Time (t)')
plt.ylabel('Range Rate (ρ̇)')
plt.legend()
plt.grid(True)

# Show plots
plt.show()

