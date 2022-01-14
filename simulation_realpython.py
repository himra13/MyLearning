"""
Learning from https://realpython.com/simpy-simulating-with-python/
pip install numpy==1.19.3 # to fix windows error
"""

import simpy
import statistics
import random
import numpy as np

# Set up Environment
env=simpy.Environment()

# Assume there's checkpoint_run()
env.process(checkpoint_run(env, num_booths, check_time, passenger_arrival))

# Submit running
env.run(until=10) #minutes

# play
# min_=input('Please select minimum value: ')
# max_=input('Please select maximum value: ')
# print(f"The minimum is {min_}")
# print(f"The maximum is {max_}")
# print(np.random.randint(min_,max_))

wait_times=[]

class Theater(object):
    """
    Simpy works in minutes, that why check ticket has to be in minute
    """
    def __init__(self, env, num_cashiers, num_ushers, num_servers):
        self.env = env # environment object to schedule and process events
        self.cashier=simpy.Resource(env, num_cashiers)
        self.usher=simpy.Resource(env, num_ushers)
        self.server=simpy.Resource(env, num_servers)
        
    def purchase_ticket(self, moviegoer):
        yield self.env.timeout(np.random.randint(1,3))
    
    def check_ticket(self, moviegoer):
        yield self.env.timeout(3/60)
    
    def food_selling(self, moviegoer):
        yield self.env.timeout(random.randint(1,5)) #continuous uniform
        
    # def go_to_movies(env, moviegoer, theater)
        