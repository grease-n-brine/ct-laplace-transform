import matplotlib.pyplot as plt
import numpy as np

# System parameters

k_gain = 1.0
tau_time_constant = 2.0 # How sluggish the system is
dt = 0.1 # Size of time step
t_max = 1.0 # Total sim time

# Time array and initialize states

time = np.arrange(0, t_max, dt)
y = np.zeros_like(time)
u = np.ones_like(time) # step input, turns on at t=0

# Sim loop

for k in range(1, len(time)):
    # Euler's method derived from transfer function
    dy = (1.0 / tau_time_constant) * ((k_gain * u[k-1]) - y[k-1])
    y[k] = y[k-1] + (dy * dt)

