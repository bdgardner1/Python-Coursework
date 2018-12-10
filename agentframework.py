import random
class sheep_dog(): 
    def __init__ (self, agents, num_of_agents): #a sheepdog is created at the centre of the field
        self.x = 50
        self.y = 50
        self.agents = agents
        self.store = 500 # The sheepdog has '500' energy at the start
        self.num_of_agents = num_of_agents
    def move(self):
        if self.store > 20: #moving depletes the sheepdogs energy by 20
            if random.random() < 0.5: # sheepdog moves randomly
                self.x = (self.x + 3) % 100
            else:
               self.x = (self.x - 3) % 100
            if random.random() < 0.5:
                self.y = (self.y + 3) % 100
            else:
               self.y = (self.y - 3) % 100  
            self.store -= 3
    def herd_sheep(self,num_of_agents):
        for agent in self.agents:
            dist = self.distancetosheep(agent) # calculates how far the sheepdog is from the sheep
            print (dist)
            if dist < 10: #if within a certain distance of the sheep, the sheep returns to the centre
                agent.x = 50
                agent.y = 50
                self.num_of_agents -= 1
                self.store += 250 #sheepdog gains energy (treat from farmer)
                
    def distancetosheep(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
        
class Agent():
    def __init__(self, environment, agents): # sheep are created with random location
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.environment = environment 
        self.agents = agents
        self.store = 0 
    
                
    def move(self): # Sheep move randomly twice
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
           self.x = (self.x - 1) % 100
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
           self.y = (self.y - 1) % 100

    def eat(self): # Sheep either eat 10 units or whatever is left
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store = self.store + self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
    def share_with_neighbours(self,neighbourhood): # Sheep share with other sheep within a certain distance
       for agent in self.agents:
        dist = self.distance_between(agent) 
        if dist <= neighbourhood:
            sum = self.store + agent.store
            ave = sum /2
            self.store = ave
            agent.store = ave
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5