import random
class Fox():
    def __init__ (self, agents, num_of_agents):
        self.x = 50
        self.y = 50
        self.agents = agents
        self.store = 500
        self.num_of_agents = num_of_agents
    def move(self):
        if self.store > 20:
            if random.random() < 0.5:
                self.x = (self.x + 2) % 100
            else:
               self.x = (self.x - 2) % 100
            if random.random() < 0.5:
                self.y = (self.y + 2) % 100
            else:
               self.y = (self.y - 2) % 100  
            self.store -= 2
    def hunt_sheep(self,num_of_agents):
        for agent in self.agents:
            dist = self.distancetosheep(agent)
            print (dist)
            if dist < 10:
                agent.x = 50
                agent.y = 50
                self.num_of_agents -= 1
                self.store += 250
                
    def distancetosheep(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
        
class Agent():
    def __init__(self, environment, agents):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.environment = environment
        self.agents = agents
        self.store = 0 # We'll come to this in a second.
    
                
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
           self.x = (self.x - 1) % 100
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
           self.y = (self.y - 1) % 100

    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store = self.store + self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
    def share_with_neighbours(self,neighbourhood):
       for agent in self.agents:
        dist = self.distance_between(agent) 
        if dist <= neighbourhood:
            sum = self.store + agent.store
            ave = sum /2
            self.store = ave
            agent.store = ave
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5