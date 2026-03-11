import gym
from gym import spaces
import numpy as np

class TwoLinkArmEnv(gym.Env):

    def __init__(self):
        super(TwoLinkArmEnv, self).__init__()

        # state = [theta1, theta2, omega1, omega2]
        high = np.array([np.pi, np.pi, 5.0, 5.0], dtype=np.float32)

        self.observation_space = spaces.Box(-high, high)

        # action = torque for two joints
        self.action_space = spaces.Box(
            low=np.array([-2.0, -2.0]),
            high=np.array([2.0, 2.0]),
            dtype=np.float32
        )

        self.dt = 0.05

        self.l1 = 1.0
        self.l2 = 1.0

        self.state = None

        self.target = np.array([1.5, 1.5])

    def reset(self):

        theta1 = np.random.uniform(-0.1,0.1)
        theta2 = np.random.uniform(-0.1,0.1)

        omega1 = 0
        omega2 = 0

        self.state = np.array([theta1,theta2,omega1,omega2])

        return self.state

    def step(self, action):

        theta1, theta2, omega1, omega2 = self.state

        torque1, torque2 = action

        # simple dynamics
        omega1 += torque1 * self.dt
        omega2 += torque2 * self.dt

        theta1 += omega1 * self.dt
        theta2 += omega2 * self.dt

        self.state = np.array([theta1,theta2,omega1,omega2])

        x = self.l1*np.cos(theta1) + self.l2*np.cos(theta1+theta2)
        y = self.l1*np.sin(theta1) + self.l2*np.sin(theta1+theta2)

        end_effector = np.array([x,y])

        dist = np.linalg.norm(end_effector - self.target)

        reward = -dist

        done = dist < 0.1

        return self.state, reward, done, {}
