import random
import operator
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import csv
environment = []
neighbourhood = 20
num_of_agents = 10
num_of_foxes = 3
num_of_iterations = 1000
agents = []
foxes = []

f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:				# A list of rows
    newrow = []
    for value in row: 
        newrow.append(value)
    environment.append(newrow)


f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.
fig = matplotlib.pyplot.figure(figsize=(7,7))
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)
# Make the agents.
for i in range(num_of_agents):
     agents.append(agentframework.Agent(environment, agents))

# Move the agents.
for i in range(num_of_foxes):
    foxes.append(agentframework.Fox(agents, num_of_agents))

for j in range(num_of_iterations):
        
    def update(frame_number):
 
        fig.clear()  
    
        for i in range(num_of_agents):
            random.shuffle(agents[i].agents)
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
        
        for i in range(num_of_foxes):
            foxes[i].move()
            foxes[i].hunt_sheep(num_of_agents)
            
        for i in range(num_of_agents):
            matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
            matplotlib.pyplot.xlim(0, 99)
            matplotlib.pyplot.ylim(0, 99)
            matplotlib.pyplot.imshow(environment)
            
        for i in range(num_of_foxes):
            matplotlib.pyplot.scatter(foxes[i].x,foxes[i].y, color='black')
            matplotlib.pyplot.xlim(0, 99)
            matplotlib.pyplot.ylim(0, 99)
            matplotlib.pyplot.imshow(environment)

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)

matplotlib.pyplot.show()

print (neighbourhood)


env_text = str(environment)
env_file = open('environment.txt','w')
env_file.write (env_text)
env_file.close()