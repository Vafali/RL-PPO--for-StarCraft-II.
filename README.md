# Reinforcement Learning for StarCraft II with Stable Baselines3

This repository contains code that demonstrates how to use the Stable Baselines3 library to perform reinforcement learning in the context of the StarCraft II video game using the Sc2Env environment.

## Requirements

Before running the code, ensure you have the following components installed:

- Python 3.6 or later
- [StarCraft II](https://github.com/Blizzard/s2client-proto) installed on your machine
- [Python-SC2](https://github.com/Dentosal/python-sc2) library
- [Stable Baselines3](https://github.com/DLR-RM/stable-baselines3) library

You can install the required Python packages using the following command:

```bash
pip install sc2env stable-baselines3
```

## Usage

1. **Setup StarCraft II Environment**: Make sure you have StarCraft II installed on your machine. You can download and install the game from the [official website](https://starcraft2.com/).

2. **Clone the Repository**: Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/your-repo-name.git
```

3. **Modify the Model Path**: Open the `play_game_with_model.py` file and modify the `LOAD_MODEL` variable to point to the path of your pre-trained model's zip file.

4. **Run the Code**: Execute the script `play_game_with_model.py` to run the pre-trained model in the StarCraft II environment:

```bash
python play_game_with_model.py
```

This script will load the specified pre-trained model using Stable Baselines3's PPO implementation and use it to play the StarCraft II game in the provided environment. The model will make predictions for actions at each step and interact with the environment based on these predictions.

## Understanding the Code

- `play_game_with_model.py`: This script demonstrates how to load a pre-trained model using Stable Baselines3 and use it to play the StarCraft II game in the `Sc2Env` environment. It initializes the environment, loads the model, and then runs the game loop, predicting actions and interacting with the environment.

- `Sc2Env`: This class defines a custom environment that follows the OpenAI Gym interface. It provides the `step` and `reset` methods required by the Gym interface. The environment allows you to interact with the StarCraft II game and receive observations, rewards, and other information.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the functionality, feel free to submit a pull request.

## License

This repository is licensed under the MIT License. You are free to use, modify, and distribute the code as long as you retain the license and attribute the original authors.

## Acknowledgments

- This code is inspired by the Stable Baselines3 library and the Python-SC2 library, which enable reinforcement learning in the StarCraft II environment.
- Thanks to the contributors and maintainers of both libraries for their efforts in making this kind of research and experimentation possible.

## Disclaimer

This project is developed for educational and research purposes. The authors are not responsible for any misuse of the provided code. Use it responsibly and ensure compliance with the terms and conditions of the StarCraft II game.

---

Feel free to customize the README file further to match your specific repository structure and information.