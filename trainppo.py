# Import necessary libraries
from stable_baselines3 import PPO
import os
from sc2env import Sc2Env
import time
from wandb.integration.sb3 import WandbCallback
import wandb

# Generate a unique model name based on current time
model_name = f"{int(time.time())}"

# Define directories for storing models and logs
models_dir = f"models/{model_name}/"
logdir = f"logs/{model_name}/"

# Configuration dictionary for logging
conf_dict = {
    "Model": "v19",
    "Machine": "Main",
    "policy": "MlpPolicy",
    "model_save_name": model_name
}

# Initialize WandB run for logging
run = wandb.init(
    project=f'SC2RLv6',
    entity="sentdex",
    config=conf_dict,
    sync_tensorboard=True,  # Auto-upload sb3's tensorboard metrics
    save_code=True  # Optional
)

# Create necessary directories if they don't exist
if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(logdir):
    os.makedirs(logdir)

# Initialize the StarCraft 2 environment
env = Sc2Env()

# Initialize the PPO model with the MlpPolicy and the environment
model = PPO('MlpPolicy', env, verbose=1, tensorboard_log=logdir)

# Training parameters
TIMESTEPS = 10000
iters = 0

# Training loop
while True:
    print("On iteration: ", iters)
    iters += 1
    
    # Train the model for a certain number of timesteps
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=f"PPO")
    
    # Save the model at the end of each iteration
    model.save(f"{models_dir}/{TIMESTEPS*iters}")
