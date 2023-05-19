import numpy as np

class gridworld:
    def __init__(self, width = 5 , height = 5):
        self.width = width
        self.height = height
        self.grid = np.zeros((self.width,self.height))
        self.current_location = (4,np.random.randint(0,5))
        # self.current_location = (2,2)
        
        self.reward_position_1 = (0,1)
        self.reward_position_2 = (0,3)
        
        # State Value 의 경우, 아래와같은 작업이 필요함! (Reward랑은 다른개념인데 한번 생각해보기)
        self.grid[self.reward_position_1] = 100
        self.grid[self.reward_position_2] = 50
        
        self.actions = np.array(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        
    # For Debugging
    def agent_on_map(self):
        self.grid = np.zeros(( self.height, self.width))
        self.grid[ self.current_location[0], self.current_location[1]] = 1
        
        

        return self.grid
        
        
    def get_reward(self , location):
        if location == self.reward_position_1:
            return 10
        elif location == self.reward_position_2:
            return 5
        else:
            return 0
    
        
    def make_step(self,action):
        reward=0
        before_location = self.current_location
        x = before_location[0]
        y = before_location[1]

        
        
        
        if action == 'UP':
            if self.current_location[0]>0:
                self.current_location = (self.current_location[0]-1,self.current_location[1])
                reward = self.get_reward(self.current_location)
                if self.current_location == (0,1):
                    self.current_location = (4,1)
                elif self.current_location == (0,3):
                    self.current_location = (3,3)
            
            # 벽에 부딪히면 -50점
            elif self.current_location[0]==0:
                reward=-50

            
        elif action == 'DOWN':
            if self.current_location[0]<4:
                self.current_location = (self.current_location[0]+1,self.current_location[1])
                reward = self.get_reward(self.current_location)
                if self.current_location == (0,1):
                    self.current_location = (4,1)
                elif self.current_location == (0,3):
                    self.current_location = (3,3)
            
            # 벽에 부딪히면 -50점
            elif self.current_location[0]==4:
                reward=-50

            
        elif action == 'LEFT':
            if self.current_location[1]>0:
                self.current_location = (self.current_location[0],self.current_location[1]-1)
                reward = self.get_reward(self.current_location)
                if self.current_location == (0,1):
                    self.current_location = (4,1)
                elif self.current_location == (0,3):
                    self.current_location = (3,3)
                    
            # 벽에 부딪히면 -50점
            elif self.current_location[1]==0:
                reward=-50

            
        elif action == 'RIGHT':
            if self.current_location[1]<4:
                self.current_location = (self.current_location[0],self.current_location[1]+1)
                reward = self.get_reward(self.current_location)
                if self.current_location == (0,1):
                    self.current_location = (4,1)
                elif self.current_location == (0,3):
                    self.current_location = (3,3)
                    
            # 벽에 부딪히면 -50점
            elif self.current_location[1]==4:
                reward=-50

        # print(action)
        return reward,action
    