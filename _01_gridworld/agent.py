
import numpy as np


class StateValue_Agent():
    def __init__(self, environment, epsilon=0.05,gamma=0.9):
        self.environment = environment
        self.value_table = np.zeros( (environment.width , environment.height) )
        self.value_table = environment.grid
        self.epsilon = epsilon
        self.gamma = gamma
        
    
    def action_choosing(self,available_actions):
        reward = 0
        if np.random.uniform(0,1) < self.epsilon:
            action = available_actions[np.random.randint(0,len(available_actions))] # 4개중 하나 랜덤하게 택 1 
        else:
            action_list = []
            reward_list = []
            for select_action in available_actions:
                # print(select_action)
                reward, action = self.for_one_step_search(select_action)
                action_list.append(action)
                reward_list.append(reward)
                reward = max(reward_list)
                action = action_list[np.argmax(reward_list)] # one Step Ahead Search중 Max값
            
        return action,reward
    
    def for_one_step_search(self,action):
        reward=0
        location_search = self.environment.current_location
        x = location_search[0]
        y = location_search[1]
        
        
        if action == 'UP':
            if location_search[0]>0:
                location_search = (location_search[0]-1,location_search[1])
                reward = self.value_table[location_search]
            
        elif action == 'DOWN':
            if location_search[0]<4:
                location_search = (location_search[0]+1,location_search[1])
                reward = self.value_table[location_search]
            
        elif action == 'LEFT':
            if location_search[1]>0:
                location_search = (location_search[0],location_search[1]-1)
                reward = self.value_table[location_search]

        elif action == 'RIGHT':
            if location_search[1]<4:
                location_search = (location_search[0],location_search[1]+1)
                reward = self.value_table[location_search]
        
        return reward,action
    
    
    
    def learning(self,old_state,new_state,reward):
        new_state_value = self.value_table[new_state[0],new_state[1]]
        
        
        self.value_table[old_state[0],old_state[1]] = reward + self.gamma*new_state_value