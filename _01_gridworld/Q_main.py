import matplotlib.pyplot as plt
from env import gridworld
from Q_agent import Q_Agent
import numpy as np
import argparse




def play(environment , agent , trials = 5000 , learn = False , alpha=0.1, ax=None):
    global q_up
    global q_down
    global q_left
    global q_right
    

    for trial in range(trials):
        # 한번의 Try시에 거치는 단계들
        old_state = environment.current_location
        action,_ = agent.action_choosing(environment.actions)
        reward,_ = environment.make_step(action)
        new_state = environment.current_location
        
        grid_agent_position = environment.agent_on_map()
        
        q_up = []
        q_down = []
        q_left = []
        q_right = []
        q_table = agent.q_table

        for q in q_table:
            q_up.append(q_table[q]['UP'])
            q_down.append(q_table[q]['DOWN'])
            q_left.append(q_table[q]['LEFT'])
            q_right.append(q_table[q]['RIGHT'])
        
        Q_UP = np.array(q_up).reshape(5,5)
        Q_DOWN = np.array(q_down).reshape(5,5)
        Q_LEFT = np.array(q_left).reshape(5,5)
        Q_RIGHT = np.array(q_right).reshape(5,5)
        
        
        
        

        
        if learn == True:
            agent.learn(old_state,action,reward,new_state)
            
            
            
        if ax is not None:
            print(action)
            grid= (2,4)
            plt.subplot2grid(grid, (0, 0), colspan=2, rowspan=2)
            plt.title('Grid State Agent')
            plt.imshow(grid_agent_position, cmap='viridis', aspect='auto')
            plt.grid()
            
            
            plot_q(Q_UP,Q_DOWN,Q_LEFT,Q_RIGHT,idx=2)
            
            plt.pause(0.1)

                
          
def plot_q(Q_UP,Q_DOWN,Q_LEFT,Q_RIGHT,idx):    
    grid= (2,2+idx)
    plt.subplot2grid(grid, (0, 0+idx))
    plt.title('Q table UP')
    plt.imshow(Q_UP, cmap='viridis', aspect='auto')
    for i in range(environment.height):
        for j in range(environment.width):
                plt.text(j, i, np.round(Q_UP[i,j], 3),
                        ha="center", va="center", color="white", fontsize=8)
    
    plt.subplot2grid(grid, (1, 0+idx))
    plt.title('Q table DOWN')
    plt.imshow(Q_DOWN, cmap='viridis', aspect='auto')
    for i in range(environment.height):
        for j in range(environment.width):
                plt.text(j, i, np.round(Q_DOWN[i,j], 3),
                        ha="center", va="center", color="white", fontsize=8)
    
    plt.subplot2grid(grid, (0, 1+idx))
    plt.title('Q table LEFT')
    plt.imshow(Q_LEFT, cmap='viridis', aspect='auto')
    for i in range(environment.height):
        for j in range(environment.width):
                plt.text(j, i, np.round(Q_LEFT[i,j], 3),
                        ha="center", va="center", color="white", fontsize=8)
    
    plt.subplot2grid(grid, (1, 1+idx))
    plt.title('Q table RIGHT')
    plt.imshow(Q_RIGHT, cmap='viridis', aspect='auto')
    for i in range(environment.height):
        for j in range(environment.width):
                plt.text(j, i, np.round(Q_RIGHT[i,j], 3),
                        ha="center", va="center", color="white", fontsize=8)

    
           
            
            
            
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
    argparser.add_argument('-r','--render', default=True, help='render the environment',type=str2bool)
    argparser.add_argument('-g','--gamma', default=0.9, help='gamma value',type=float)
    argparser.add_argument('-e','--eps', default=0.1, help='epsilon value',type=float)
    argparser.add_argument('-a','--alpha', default=0.1, help='alpha value',type=float)
    argparser.add_argument('-I','--Iteration', default=5, help='Number of Episodes',type=int)
    argparser.add_argument('-T','--Trial', default=5000, help='Sampling per one Episode',type=int)
    
    args = argparser.parse_args()
    render = args.render
    gamma = args.gamma
    eps = args.eps
    alpha = args.alpha
    episodes = args.Iteration
    trials = args.Trial
    
    environment = gridworld()
    agent = Q_Agent(environment,epsilon=eps,gamma=gamma,alpha=alpha)
    
    
    
    if render:
        plt.figure(figsize=(10,5))
        ax=True
    else:
        ax=None
    
    for i in range(episodes):
        environment.current_location = (4,np.random.randint(0,5))
        play(environment,agent,trials=trials,learn=True,ax=ax,alpha=alpha)
        print(f'ep : {i} / {episodes}',end='\r')
        
    
    q_up = []
    q_down = []
    q_left = []
    q_right = []
    q_table = agent.q_table
    for q in q_table:
        q_up.append(q_table[q]['UP'])
        q_down.append(q_table[q]['DOWN'])
        q_left.append(q_table[q]['LEFT'])
        q_right.append(q_table[q]['RIGHT'])
        
    Q_UP = np.array(q_up).reshape(5,5)
    Q_DOWN = np.array(q_down).reshape(5,5)
    Q_LEFT = np.array(q_left).reshape(5,5)
    Q_RIGHT = np.array(q_right).reshape(5,5)
    plot_q(Q_UP,Q_DOWN,Q_LEFT,Q_RIGHT,idx=0)

    plt.show()