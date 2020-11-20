from matplotlib.pyplot import colorbar
import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt
plt.style.use('dark_background')

class Fireflies:
    def __init__(self, nr_agents, grid_length):
        self.nr_fireflies = nr_agents
        self.grid_length = grid_length
        self.fireflies = np.zeros((nr_agents, 1))
        self.x = np.random.randint(0, grid_length, nr_agents)
        self.y = np.random.randint(0, grid_length, nr_agents)

    def initilialize_fireflies(self):
        for i in range(int(self.nr_fireflies/2)):
            self.fireflies[i] = 1

    def draw_fireflies(self):
        non_glowing_fireflies = np.where(self.fireflies == 0)[0]
        glowing_fireflies = np.where(self.fireflies == 1)[0]

        plt.plot(self.x[non_glowing_fireflies], self.y[non_glowing_fireflies], linestyle='none', marker='o', markersize=3, color='olive')
        plt.plot(self.x[glowing_fireflies], self.y[glowing_fireflies], linestyle='none', marker='o', markersize=3, color='yellow')
        plt.show()

oscillators = Fireflies(nr_agents=1000, grid_length=100)
oscillators.initilialize_fireflies()
oscillators.draw_fireflies()