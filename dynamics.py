import numpy as np

class TwoLinkDynamics:

    def __init__(self):

        self.l1 = 1.0
        self.l2 = 1.0

        self.m1 = 1.0
        self.m2 = 1.0

        self.g = 9.81

    def forward_kinematics(self, theta1, theta2):

        x = self.l1*np.cos(theta1) + self.l2*np.cos(theta1+theta2)
        y = self.l1*np.sin(theta1) + self.l2*np.sin(theta1+theta2)

        return np.array([x,y])

    def step(self, state, torque, dt):

        theta1, theta2, omega1, omega2 = state
        tau1, tau2 = torque

        omega1 += tau1 * dt
        omega2 += tau2 * dt

        theta1 += omega1 * dt
        theta2 += omega2 * dt

        return np.array([theta1,theta2,omega1,omega2])
