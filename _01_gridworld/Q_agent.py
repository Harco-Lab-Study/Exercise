import numpy as np



class Q_Agent():
    def __init__(self, environment, epsilon=0.05,gamma=0.9,alpha=0.1):
        self.environment = environment
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        
        # Q_table 초기화
        self.q_table = {}
        # Q-table 초기화
        for x in range(self.environment.height):
            for y in range(self.environment.width):
                self.q_table[(x,y)] = {}
                for action in self.environment.actions:
                    self.q_table[(x,y)][action] = 0
        
        
        
    def action_choosing(self,available_actions):
        reward=0
        if np.random.uniform(0,1) < self.epsilon:
            action = available_actions[np.random.randint(0,len(available_actions))] # 4개중 하나 랜덤하게 택 1 
            
        else:
            # maximum q(s,a) pair selection
            # Q Value는 One-Step Ahead Search가 필요없음을 확인가능! -> 그저 Maximum한 값만을 선택하면 됨
            q_list = []
            for select_action in available_actions:
                q_list.append(self.q_table[self.environment.current_location][select_action])
            max_idx = np.where(np.array(q_list) == np.max(q_list))[0]
            if len(max_idx) > 1:
                action = available_actions[np.random.choice(max_idx)]
            else:
                action = available_actions[np.argmax(q_list)]
                
        return action,reward
    
    



    def learn(self, state, action, reward, next_state):
        if state not in self.q_table:
            self.q_table[state] = {}
            self.q_table[state][action] = 0
        if next_state not in self.q_table:
            self.q_table[next_state] = {}
            for action_ in self.environment.action_space:
                self.q_table[next_state][action_] = 0
        
        # Q Learning Update
        # Q(s,a) = (1-alpha)*Q(s,a) + alpha*(reward + gamma*max(Q(s',a')))
        
        """
        2023 05 19 문제
        Q 값 Update식 : Q(s,a) = Q(s,a) + alpha * ( reward + gamma*max( Q(s',a') ) - Q(s,a) ) => 벨만 최적방정식 으로 적혀있는데
        V와 Q에 대한 벨만 기대방정식으로 바꿔보기
        """
        self.q_table[state][action] = (1-self.epsilon)*self.q_table[state][action] + self.epsilon*(reward + self.gamma*np.max(list(self.q_table[next_state].values())))
        
        return self.q_table[state][action]
    