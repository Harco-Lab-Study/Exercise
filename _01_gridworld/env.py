import numpy as np

class gridworld:
    def __init__(self, width = 5 , height = 5):
        self.width = width
        self.height = height
        self.grid = np.zeros((self.width,self.height))
        self.current_location = (4,np.random.randint(0,5))
        # self.current_location = (2,2)
        
        self.grid[0,1] = 10
        self.grid[0,3] = 2
        
        self.actions = np.array(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        
    # For Debugging
    def agent_on_map(self):
        self.grid = np.zeros(( self.height, self.width))
        self.grid[ self.current_location[0], self.current_location[1]] = 1
        
        self.grid[0,1] = 10
        self.grid[0,3] = 5
        return self.grid
        
        
    def get_reward(self , location):
        # print('location : ',location)
        # print('reward : ',self.grid[location[0],location[1]])
        return self.grid[location[0],location[1]]
    
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

            
        elif action == 'DOWN':
            if self.current_location[0]<4:
                self.current_location = (self.current_location[0]+1,self.current_location[1])
                reward = self.get_reward(self.current_location)
                if self.current_location == (0,1):
                    self.current_location = (4,1)
                elif self.current_location == (0,3):
                    self.current_location = (3,3)

            
        elif action == 'LEFT':
            if self.current_location[1]>0:
                self.current_location = (self.current_location[0],self.current_location[1]-1)
                reward = self.get_reward(self.current_location)
                if self.current_location == (0,1):
                    self.current_location = (4,1)
                elif self.current_location == (0,3):
                    self.current_location = (3,3)

            
        elif action == 'RIGHT':
            if self.current_location[1]<4:
                self.current_location = (self.current_location[0],self.current_location[1]+1)
                reward = self.get_reward(self.current_location)
                if self.current_location == (0,1):
                    self.current_location = (4,1)
                elif self.current_location == (0,3):
                    self.current_location = (3,3)

        # print(action)
        return reward,action
    