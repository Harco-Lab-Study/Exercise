import matplotlib.pyplot as plt
from env import gridworld
from agent import StateValue_Agent
import numpy as np


def play(environment , agent, trials = 10000, learn = False,ax=None):
    reward_list = []
    reward = 0
    for trial in range(trials):
        
        # 한번의 Try시에 거치는 단계들
        old_state = environment.current_location
        action,_ = agent.action_choosing(environment.actions)
        reward,_ = environment.make_step(action)
        new_state = environment.current_location
        
        grid_state_agent = environment.agent_on_map()
        
        # print('old_state : ',old_state)
        # print('Choosed Action : ',action)
        # print('그에대한 reward : ',reward)
        # print('new_state s` : ',new_state)
        # print(grid_state_agent)
        # print(agent.value_table)
        # print('----------')
        
        if ax is not None:
            ax[0].imshow(grid_state_agent, cmap='viridis', aspect='auto')
            ax[0].set_title('Grid State Agent')
            ax[1].clear()
            ax[1].imshow(agent.value_table, cmap='viridis', aspect='auto')
            ax[1].set_title('Agent Value Table')
            
            # show the values of the value table grid
            for i in range(agent.value_table.shape[0]):
                for j in range(agent.value_table.shape[1]):
                     ax[1].text(j, i, round(agent.value_table[i, j], 1),
                               ha="center", va="center", color="white", fontsize=8)
            
            plt.pause(0.0001)
        
        if learn == True:
            agent.learning(old_state,new_state,reward)
            
            
            
            





if __name__ == "__main__":
    environment = gridworld()
    agent = StateValue_Agent(environment,epsilon=0.05,gamma=0.9)

    render=True
    
    
    if render:
        fig, ax = plt.subplots(1, 2,figsize=(10,5))
    else:
        ax=None
    
    for i in range(50):
        environment.current_location = (4,np.random.randint(0,5))
        play(environment,agent,trials=10000,learn=True,ax=ax)
        print('ep : ',i,end='\r')
        
    print(np.round(agent.value_table,1))