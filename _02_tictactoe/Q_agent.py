import numpy as np


class Some_Q_Agent:
    def __init__(self, env,episodes=1000, gamma=0.9, epsilon=0.01):
        self.env = env
        self.q_table = {}
        self.visit_counts = {}
        self.action_space = env.action_space
        self.episodes = episodes
        self.gemma = gamma
        self.epsilon = epsilon
    
        
        
    def get_action(self, observation):
        if observation not in self.q_table:
            self.q_table[observation] = np.zeros(self.action_space.n)
            self.visit_counts[observation] = np.zeros(self.action_space.n)
        
        
        
        # Check which spaces are available, Epsilon greedy Policy
        available_actions = np.where(self.env.board == 0)
        _i,_j = available_actions[0],available_actions[1]
        available_actions = [i*3+j for i,j in zip(_i,_j)]
        if np.random.random() > self.epsilon:
            # Of the nine possible actions, select the space that the players did not put
            available_q = self.q_table[observation][available_actions]
            # if there are multiple max values, select one randomly
            if np.sum(available_q == np.max(available_q)) > 1:
                max_idx = np.where(available_q == np.max(available_q))[0]
                max_action = [available_actions[i] for i in max_idx]
                action = np.random.choice(max_action)
            else:
                action = available_actions[np.where(available_q == np.max(available_q))[0][0]]
        else:
            # Of the nine possible actions, select the space that the players did not put
            action = np.random.choice(available_actions)
            
        return action
    
    
    
    
    def update(self, observation, action, reward):
        """
        Write Your Own Agent's Update Rule Here
        """
        
        
    def rotate_board(self, board):
        """
        By Rotating the States, we can reduce the number of states
        """
    
    def symmetrize(self, observation, action, reward):
        """
        By Symmetrizing the States, we can reduce the number of states
        """