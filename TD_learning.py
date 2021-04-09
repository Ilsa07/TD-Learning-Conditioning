import numpy as np
import matplotlib.pyplot as plt
import time 


# Simulation Parameters
# *********************
Trials = 100                # Number of trials
Time = 20                   # Trial length
reward_time = 20            # Time of the reward
cue_time = 5                # Time of the Cue
end_cue_time = 20           # Enf of the cue at the end of the simulation
cue_duration = end_cue_time - cue_time + 1  # The duration of the cue

# Model Parameters
# ****************
v = []                      # Initialise the value function
w = np.zeros(cue_duration)  # Initialise the weights
r = np.zeros(Time)          # Initialise a reward of 1 to the last time point
r[-1] = 1
gamma = 1                   # Discount factor
alpha = 0.6                 # Learning rate
# Initialise the cue matrix as 16 x 20 
x = np.eye(cue_duration)    
for i in range(4):
    x = np.insert(x, 0, np.zeros(cue_duration), axis=0)                   


# Run the Simulation
# ******************
for i in range(Trials):
    # Update the value function
    sub_v = []
    for iterator in range(Time):
        sub_v.append(w.dot(x[iterator]))

    v.append(sub_v)

    # Calculate the error
    error_vector = []
    for t in range(Time):
        try:
            td_error = r[t] + gamma * v[-1][t+1] - v[-1][t]
            error_vector.append(td_error)
        except:
            td_error = r[t] - v[-1][t]
            error_vector.append(td_error)
    
    # Update the Weights
    delta_w = []
    for element in x.transpose():
        sub_delta = np.sum(element*error_vector)
        delta_w.append(sub_delta)

    w = np.add(w, delta_w)

    # Plot the Value Function and the Error
    # *************************************
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle("Simulation Results Accross Training Iterations")
    ax1.plot(v[-1])
    ax1.set(xlabel='Time')
    ax1.set(ylabel='Value')
    ax1.set_title('Value Function over Iterations')

    ax2.plot(error_vector)
    ax2.set(xlabel='Time')
    ax2.set(ylabel='Error value')
    ax2.set_title('Error over Iterations')
    plt.savefig('simulation_live.png')
    time.sleep(0.3)

    # Stop if the weights are no longer updating
    if np.sum(delta_w) == 0:
        break
