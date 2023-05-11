
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
                # one Step Ahead Search중, max값을 가지는 action을 선택
                # 2개의 max값인경우, 최대값중 랜덤하게 선택 (은근히 구현할때 조심해야하는 부분. np.arg max를 쓰면 무조건 맨앞 인덱스를 반환하기 때문에..)
                max_idx = np.where(np.array(reward_list) == reward)[0]
                if len(max_idx) > 1:
                    action = action_list[np.random.choice(max_idx)]
                else:
                    action = action_list[np.argmax(reward_list)]
                    
                
        return action,reward

    """
    State Value는 One-Step-Ahead Search가 일반적으로 필요하다.
    그 다음 상태의 State Transition Probability를 보통은 알 수 없기 때문. (아래예제는.. 벽에 닿는지 정도만 Search하면 되는거고 나머지는 알 수 있는것이라 굳이 필요가 없음)
    그 다음 가장 Value가 높은 State Value가 무엇인지 안다고 하더라도, 어떤 행동을 해야 그 상태로 갈 수 있는지 모르기 때문.
    반면, Action Value는 이미 Action에 대한 고려가 진행된 상태로 수렴하기 때문에, 이러한 고려가 필요없다. 
    """
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
    
    
    
    """
    가치함수를 Update하는 부분 : Vt = Vt + alpha*(Rt+1 + gamma*Vt+1 - Vt)
    """
    def learning(self,old_state,new_state,reward,alpha=0.9):
        new_state_value = self.value_table[new_state[0],new_state[1]]
        self.value_table[old_state[0],old_state[1]] = self.value_table[old_state[0],old_state[1]] + alpha*(reward + self.gamma*new_state_value - self.value_table[old_state[0],old_state[1]])
        
    