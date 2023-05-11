import matplotlib.pyplot as plt
from env import gridworld
from agent import StateValue_Agent
import numpy as np
import argparse

def play(environment , agent, trials = 10000, learn = False,ax=None,alpha=0.9):
    reward_list = []
    reward = 0
    for trial in range(trials):
        
        # 한번의 Try시에 거치는 단계들
        old_state = environment.current_location
        action,_ = agent.action_choosing(environment.actions)
        reward,_ = environment.make_step(action)
        new_state = environment.current_location
        
        grid_state_agent = environment.agent_on_map()

        
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
            
            plt.pause(0.1)
        
        if learn == True:
            print('Agent Location:',environment.current_location)
            print('Reward:',reward)
            agent.learning(old_state,new_state,reward,alpha=alpha)
            
            
            
            

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')



if __name__ == "__main__":
    
    
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--render', default=True, help='render the environment',type=str2bool)
    argparser.add_argument('--gamma', default=0.9, help='gamma value',type=float)
    argparser.add_argument('--eps', default=0.05, help='epsilon value',type=float)
    argparser.add_argument('--alpha', default=0.9, help='alpha value',type=float)
    
    args = argparser.parse_args()
    render = args.render
    gamma = args.gamma
    eps = args.eps
    alpha = args.alpha
    
    environment = gridworld()
    agent = StateValue_Agent(environment,epsilon=eps,gamma=gamma)
    
    
    
    if render:
        fig, ax = plt.subplots(1, 2,figsize=(10,5))
    else:
        ax=None
    
    for i in range(50):
        environment.current_location = (4,np.random.randint(0,5))
        play(environment,agent,trials=10000,learn=True,ax=ax,alpha=alpha)
        print('ep : ',i,end='\r')
        
    print(np.round(agent.value_table,1))