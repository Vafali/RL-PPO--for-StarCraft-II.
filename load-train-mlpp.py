# Activate your virtual environment
# $ source ~/Desktop/sc2env/bin/activate

from stable_baselines3 import PPO
from sc2env import Sc2Env
import time
from wandb.integration.sb3 import WandbCallback
import wandb
import os

LOAD_MODEL = "models/1647915989/1647915989.zip"

# Create a StarCraft II environment
env = Sc2Env()

# Load the pre-trained model
model = PPO.load(LOAD_MODEL, env=env)

# Define a name for the new model based on the current timestamp
model_name = f"{int(time.time())}"

# Directories for saving models and logs
models_dir = f"models/{model_name}/"
logdir = f"logs/{model_name}/"

# Configuration dictionary for logging with WandB
conf_dict = {
    "Model": "load-v16s",
    "Machine": "Puget/Desktop/v18/2",
    "policy": "MlpPolicy",
    "model_save_name": model_name,
    "load_model": LOAD_MODEL
}

# Initialize WandB run for tracking
run = wandb.init(
    project=f'SC2RLv6',
    entity="sentdex",
    config=conf_dict,
    sync_tensorboard=True,  # Auto-upload sb3's tensorboard metrics
    save_code=True,  # Save source code
)

# Define the number of timesteps for each learning iteration
TIMESTEPS = 10000
iters = 0

# Continuously train the model
while True:
    print("On iteration:", iters)
    iters += 1
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=f"PPO")
    
    # Save the model after each iteration
    model.save(f"{models_dir}/{TIMESTEPS * iters}")
