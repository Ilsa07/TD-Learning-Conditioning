# Temporal Difference Learning - Conditioning
This project illustrates classical conditioning with Temporal Difference (TD) learning. In each trial, a stimulus, lets say bell, is presented at t=5 and a reward, some good food, is presented at t=20, at the end of the trial. The model learns to associate the stimulus with the reward. While the code runs the program updates the simulation_live.png image, which depicts the TD error and the value function across each trial. It can be seen that the as the algorithm is learning, the value function approaches the first time the stimulus is presented and when it finished learning it reaches it.

### Value Function
The value function is calculated witht the following equation w are the weights and x is the input.

![value_function](https://latex.codecogs.com/gif.latex?%5Chat%7BV%7D%28t%29%20%3D%20%5Csum_i%20%5Cbold%7Bw%7D_i%20%5Cbold%7Bx%7D_i%20%28t%29)

### TD Error
The TD error is calculated with the following equation where r(t) is the reqard at the current time step.

![error](https://latex.codecogs.com/gif.latex?%5Cdelta%20%28t%29%20%3D%20r%28t%29%20&plus;%20%5Cgamma%20%5Chat%7BV%7D%28t&plus;1%29%20-%20%5Chat%7BV%7D%28t%29)

### Weight Update
The weight update is given by the following equation where alpha is the learning rate and x is the stimulus.

![weight_update](https://latex.codecogs.com/gif.latex?%5CDelta%20w_i%20%3D%20%5Calpha%20%5Csum_t%20x_i%20%28t%29%20%5Cdelta%20%28t%29)

## Getting Started
1. Clone the project and create a virtual environment
1. install the required packages in the virtual environment
      ```
      pip3 install -r requirements.txt
      ```
