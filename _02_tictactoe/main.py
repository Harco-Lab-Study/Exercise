import matplotlib.pyplot as plt
from env import TicTacToeEnv
import random
from Q_agent import Some_Q_Agent


env = TicTacToeEnv()
agent = Some_Q_Agent(env)


fig, ax = plt.subplots()
plt.ion()
rendering=True
done = False







"""
Edit the code below to make your own agent

X Agent와 O Agent를 각각 만들어서 서로 학습시키는 것도 가능!
혹은 하나의 에이전트만을 사용해 학습하는 것도 가능!
(정답은 없습니다)
"""

while True:
    env.reset()
    while not done:
        action = agent.get_action(env.board.tobytes())
        observation, reward, done, _ = env.step(action)
        
        
        if rendering == True:
            env.render(ax=ax)
            plt.pause(0.001)

        if reward == 1:
            print(f"Player {env.current_player} wins!")
            break
        elif env.is_full():
            print("It's a draw!")
            break

    done = False
    if rendering == True:
        plt.ion()
        plt.show()
       