# Reinforcement-Learning-Control-of-a-Two-Link-Robotic-Arm
his project implements a reinforcement learning controller for a simulated two-link robotic arm. The objective of the agent is to drive the arm's end-effector to a predefined target position in a 2D plane.

## System State

The environment state is defined as:

[θ1, θ2, ω1, ω2]

Where:

θ = joint angle
ω = angular velocity

## Action Space

The agent controls the arm by applying torques to the two joints:

[τ1, τ2]
## Forward Kinematics

The end-effector position is computed using forward kinematics:

x = l1 cos(θ1) + l2 cos(θ1 + θ2)
y = l1 sin(θ1) + l2 sin(θ1 + θ2)
## Reward Function

The reward is defined as the negative distance between the end-effector and the target:

reward = − distance_to_target

This encourages the agent to minimize the distance to the target.

## Learning Algorithm

The agent is trained using Proximal Policy Optimization (PPO), a popular policy-gradient reinforcement learning algorithm.

During training the agent learns to:

Observe the system state

Apply joint torques

Reduce the distance to the target

After training, the learned policy can successfully guide the robotic arm toward the target position.
