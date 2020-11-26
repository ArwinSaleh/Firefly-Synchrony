from matplotlib.pyplot import colorbar
import numpy as np
from numpy.core.fromnumeric import size
import numpy.random as rnd
import matplotlib.pyplot as plt
plt.style.use('dark_background')

class Fireflies:
    def __init__(self, nr_agents, grid_length, nr_steps, velocity_range):
        self.nr_fireflies = nr_agents
        self.grid_length = grid_length
        self.fireflies = np.zeros((nr_agents, 1))
        self.x = np.random.randint(0, grid_length, nr_agents)
        self.y = np.random.randint(0, grid_length, nr_agents)
        self.velocities = np.zeros((self.nr_fireflies, 2))
        self.nr_steps = nr_steps
        self.velocity_range = velocity_range

    def initilialize_fireflies(self):
        for i in range(int(self.nr_fireflies/2)):
            self.fireflies[i] = 1

    def draw_fireflies(self):
        non_glowing_fireflies = np.where(self.fireflies == 0)[0]
        glowing_fireflies = np.where(self.fireflies == 1)[0]
        
        plt.clf()
        plt.plot(self.x[non_glowing_fireflies], self.y[non_glowing_fireflies], linestyle='none', marker='o', markersize=3, color='olive')
        plt.plot(self.x[glowing_fireflies], self.y[glowing_fireflies], linestyle='none', marker='o', markersize=3, color='yellow')
        plt.axis([0, self.grid_length, 0, self.grid_length])
        plt.draw()
        plt.pause(1)

    def update_velocities(self):
        self.velocities = np.random.randint(-self.velocity_range, self.velocity_range, size=(self.nr_fireflies, 2))
    
    def move_fireflies(self):
        self.x = np.add(self.x, self.velocities[:, 0])
        self.y = np.add(self.y, self.velocities[:, 1])
        
    def step(self):
        for i in range(self.nr_steps):
            self.update_velocities()
            self.move_fireflies()
            self.draw_fireflies()

def run_system():
    oscillators = Fireflies(nr_agents=100, grid_length=100, nr_steps=100, velocity_range=2)
    oscillators.initilialize_fireflies()
    oscillators.step()

run_system()