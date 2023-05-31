import matplotlib.pyplot as plt
from env import TicTacToeEnv
import random
import numpy as np


env = TicTacToeEnv()

fig, ax = plt.subplots()
plt.ion()
rendering=True

done = False

def Random_Agent(board):
    available_actions = np.where(board == 0)
    _i,_j = available_actions[0],available_actions[1]
    available_actions = [i*3+j for i,j in zip(_i,_j)]
    action = random.choice(available_actions)
    return action





while not done:
    # Random Action Choosing
    action = Random_Agent(env.board)

    # Step
    _, reward, done, _ = env.step(action)
    if rendering == True:
        env.render(ax=ax)
        plt.pause(0.5)

    print('current player : ', env.current_player)
    print(env.board)


    # Winner Check
    if reward == 1:
        print(f"Player {env.current_player} wins!")
        break
    elif env.is_full():
        print("It's a draw!")
        break

if rendering==True:
    plt.ioff()
    plt.show()
