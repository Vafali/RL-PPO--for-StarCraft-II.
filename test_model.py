from stable_baselines3 import PPO
from sc2env import Sc2Env

# Define the path to the pre-trained model
LOAD_MODEL = "models/1647915989/2880000.zip"

# Create the SC2 environment
env = Sc2Env()

# Load the pre-trained model
model = PPO.load(LOAD_MODEL)

# Play the game loop
obs = env.reset()  # Reset the environment to start a new game
done = False
while not done:
    # Use the pre-trained model to predict an action based on the current observation
    action, _states = model.predict(obs)

    # Take the predicted action in the environment and get the resulting observation, rewards, done flag, and info
    obs, rewards, done, info = env.step(action)
