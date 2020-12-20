from matplotlib.pyplot import colorbar
import numpy as np
from numpy.core.fromnumeric import size
import numpy.random as rnd
import matplotlib.pyplot as plt
import math
import cmath
#plt.style.use('dark_background')

class Fireflies:
    def __init__(self, nr_agents, grid_length, nr_steps, K, velocity_range=2):
        self.nr_fireflies = nr_agents
        self.grid_length = grid_length
        self.fireflies = np.zeros((nr_agents, 1))
        self.x = np.random.randint(0, grid_length, nr_agents)
        self.y = np.random.randint(0, grid_length, nr_agents)
        self.velocities = np.zeros((nr_agents, 2))
        self.nr_steps = nr_steps
        self.velocity_range = velocity_range
        self.theta = np.random.uniform(0, 1, size=(nr_agents, 1))
        self.current_step = 1
        self.theta_dot = np.random.uniform(
            -math.pi, math.pi, size=(nr_agents, 1))
        self.psi = np.sum(self.theta) / self.nr_fireflies
        self.K = K
        self.omega = np.random.normal(0, nr_agents, (nr_agents, 1))
        self.r = 0

    def initialize_fireflies(self):
        for i in range(int(self.nr_fireflies / 2)):
            self.fireflies[i] = 1

    def update_psi(self):
        self.psi = np.sum(self.theta) / self.nr_fireflies

    def draw_fireflies(self):
        '''
        non_glowing_fireflies = np.where(self.fireflies == 0)[0]
        glowing_fireflies = np.where(self.fireflies == 1)[0]

        plt.clf()
        plt.plot(
            self.x[non_glowing_fireflies],
            self.y[non_glowing_fireflies],
            linestyle='none',
            marker='o',
            markersize=3,
            color='olive')
        plt.plot(
            self.x[glowing_fireflies],
            self.y[glowing_fireflies],
            linestyle='none',
            marker='o',
            markersize=3,
            color='yellow')
            '''

        plt.cla()
        #plt.pcolor(np.random.rand(10,10),cmap='rainbow')
        plt.plot(np.cos(self.theta), np.sin(self.theta), linestyle='none', marker='.')
        plt.axis([-1.1, 1.1, -1.1, 1.1])
        plt.xlabel('cos(theta)')
        plt.ylabel('sin(theta)')
        plt.draw()
        plt.pause(0.00001)

    def update_velocities(self):
        self.velocities = np.random.randint(
            -self.velocity_range,
            self.velocity_range,
            size=(self.nr_fireflies, 2))

    def move_fireflies(self):
        self.x = np.add(self.x, self.velocities[:, 0])
        self.y = np.add(self.y, self.velocities[:, 1])
        self.x[np.where(self.x > self.grid_length)] = 0  # Periodic boundary
        self.x[np.where(self.x < 0)] = self.grid_length  # Periodic boundary
        self.y[np.where(self.y > self.grid_length)] = 0  # Periodic boundary
        self.y[np.where(self.y < 0)] = self.grid_length  # Periodic boundary

    def step(self, DRAW=False):
        for step in range(self.nr_steps):
            self.update_r()
            self.update_psi()
            for i in range(self.nr_fireflies):
                self.update_omega(i)
                self.update_theta(i)
            if DRAW:
                self.draw_fireflies()
            self.current_step += 1

    def update_omega(self, i):
        self.omega[i] = self.K * self.r * math.sin(self.theta[i])

    def update_theta(self, i):
        self.theta_dot[i] = self.omega[i] + self.K * self.r * math.sin(
            self.psi - self.theta[i])
        self.theta[i] += self.theta_dot[i]
      
    def update_r(self):
      #self.r = np.abs(np.sum(np.exp(1J*np.subtract(self.theta, self.psi)))) / self.nr_fireflies

      tmp = 0.0000000
      for i in range(self.nr_fireflies):
        tmp += cmath.exp(1J*(self.theta[i]-self.psi))
      self.r = abs(tmp) / self.nr_fireflies

def run_system():
    oscillators = Fireflies(
        nr_agents=1000, grid_length=100, nr_steps=10000, K=0.1)
    oscillators.initialize_fireflies()
    oscillators.step(DRAW=True)

run_system()
