# Import necessary libraries
from sc2.bot_ai import BotAI
from sc2.data import Difficulty, Race
from sc2.main import run_game
from sc2.player import Bot, Computer
from sc2 import maps
from sc2.ids.unit_typeid import UnitTypeId
import random
import cv2
import math
import numpy as np
import sys
import pickle
import time

# Constants
SAVE_REPLAY = True
total_steps = 10000
steps_for_pun = np.linspace(0, 1, total_steps)
step_punishment = ((np.exp(steps_for_pun**3) / 10) - 0.1) * 10

# Define the IncrediBot class inheriting from BotAI
class IncrediBot(BotAI):
    async def on_step(self, iteration: int):
        # ... (Your main logic goes here)
        pass

        # Save observation and reward in a pickle file
        data = {"state": map, "reward": reward, "action": None, "done": False}
        with open('state_rwd_action.pkl', 'wb') as f:
            pickle.dump(data, f)

# Run the game
result = run_game(
    maps.get("2000AtmospheresAIE"),
    [Bot(Race.Protoss, IncrediBot()),
     Computer(Race.Zerg, Difficulty.Hard)],
    realtime=False,
)

# Calculate reward based on game result
if str(result) == "Result.Victory":
    rwd = 500
else:
    rwd = -500

# Write result to a file
with open("results.txt", "a") as f:
    f.write(f"{result}\n")

# Save final state and reward
map = np.zeros((224, 224, 3), dtype=np.uint8)
observation = map
data = {"state": map, "reward": rwd, "action": None, "done": True}
with open('state_rwd_action.pkl', 'wb') as f:
    pickle.dump(data, f)

# Clean up and exit
cv2.destroyAllWindows()
cv2.waitKey(1)
time.sleep(3)
sys.exit()
