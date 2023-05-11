import gymnasium as gym
import panda_gym
import time

# env = gym.make('PandaReach-v3', render_mode="human")
env = gym.make('PandaReachJointsDense-v3', render_mode="rgb_array",renderer="OpenGL")
observation, info = env.reset()

for _ in range(1000):
    action = env.action_space.sample() # random action
    observation, reward, terminated, truncated, info = env.step(action)
    print(reward)
    time.sleep(0.04) # for visualization 
    if terminated or truncated:
        observation, info = env.reset()

env.close()