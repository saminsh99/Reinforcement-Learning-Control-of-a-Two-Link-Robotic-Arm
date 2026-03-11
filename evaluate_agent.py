from stable_baselines3 import PPO
from two_link_env import TwoLinkArmEnv

env = TwoLinkArmEnv()

model = PPO.load("two_link_rl_agent")

obs = env.reset()

for i in range(500):

    action, _ = model.predict(obs)

    obs, reward, done, _ = env.step(action)

    print("state:", obs, "reward:", reward)

    if done:
        print("Target reached")
        break
