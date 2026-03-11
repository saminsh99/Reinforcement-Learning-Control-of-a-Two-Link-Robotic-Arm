from stable_baselines3 import PPO
from two_link_env import TwoLinkArmEnv

env = TwoLinkArmEnv()

model = PPO(
    "MlpPolicy",
    env,
    verbose=1,
    learning_rate=3e-4,
    gamma=0.99
)

model.learn(total_timesteps=200000)

model.save("two_link_rl_agent")
