import random
import operator
import matplotlib.pyplot
import agentframework
import csv
environment = []
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:				# A list of rows
    newrow = []
    for value in row: 
        newrow.append(value)
    environment.append(newrow)
print (environment)

f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.


def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
        ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
     agents.append(agentframework.Agent(environment))

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        agents[i].move()
        agents[i].eat()

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
env_text = str(environment)
        
env_file = open('environment.txt','w')
env_file.write (env_text)
env_file.close()