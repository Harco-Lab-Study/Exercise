import matplotlib.pyplot as plt
from env import TicTacToeEnv
import random
import numpy as np


env = TicTacToeEnv()

fig, ax = plt.subplots()
plt.ion()
rendering=True

done = False


while not done:
    # Get Available Action    
    available_actions = np.where(env.board == 0)
    _i,_j = available_actions[0],available_actions[1]
    actions = [i*3+j for i,j in zip(_i,_j)]
    
    # Random Action Choosing
    action = random.choice(actions)
    print('current player : ', env.current_player)
    print(env.board)
    
    # Step
    _, reward, done, _ = env.step(action)
    if rendering == True:
        env.render(ax=ax)
        plt.pause(0.5)

    if reward == 1:
        print(f"Player {env.current_player} wins!")
        break
    elif env.is_full():
        print("It's a draw!")
        break

if rendering==True:
    plt.ioff()
    plt.show()
