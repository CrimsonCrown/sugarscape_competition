"""
Sugarscape Constant Growback Model
================================

Replication of the model found in Netlogo:
Li, J. and Wilensky, U. (2009). NetLogo Sugarscape 2 Constant Growback model.
http://ccl.northwestern.edu/netlogo/models/Sugarscape2ConstantGrowback.
Center for Connected Learning and Computer-Based Modeling,
Northwestern University, Evanston, IL.
"""

import mesa

from .agents import SsAgent, SsAgent2, Sugar


class SugarscapeCg(mesa.Model):
    """
    Sugarscape 2 Constant Growback
    """

    verbose = True  # Print-monitoring

    def gettotalmass(self):
        agentmass = 0.0
        for agent in self.schedule.agents:
            if type(agent) is SsAgent:
                agentmass=agentmass+agent.weightgain
        return agentmass

    def getaveragemass(self):
        agentmass = self.gettotalmass()/self.schedule.get_type_count(SsAgent)
        return agentmass

    def __init__(self, width=50, height=50, initial_population=100, initial_population2=50):
        self.initial_population2=initial_population2
        """
        Create a new Constant Growback model with the given parameters.

        Args:
            initial_population: Number of population to start with
        """

        # Set parameters
        self.width = width
        self.height = height
        self.initial_population = initial_population

        self.schedule = mesa.time.RandomActivationByType(self)
        self.grid = mesa.space.MultiGrid(self.width, self.height, torus=False)
        self.datacollector = mesa.DataCollector(
            {"SsAgent": lambda m: m.schedule.get_type_count(SsAgent),
            "SsAgentMass": lambda m: self.gettotalmass(),
            "SsAgentMassAvg": lambda m: self.getaveragemass()}
        )

        # Create sugar
        import numpy as np

        sugar_distribution = np.genfromtxt("sugarscape_cg/sugar-map.txt")
        for _, x, y in self.grid.coord_iter():
            max_sugar = sugar_distribution[x, y]
            sugar = Sugar((x, y), self, max_sugar)
            self.grid.place_agent(sugar, (x, y))
            self.schedule.add(sugar)

        # Create agent:
        for i in range(self.initial_population):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            sugar = self.random.randrange(6, 25)
            metabolism = self.random.randrange(2, 4)
            vision = self.random.randrange(1, 6)
            ssa = SsAgent((x, y), self, False, sugar, metabolism, vision)
            self.grid.place_agent(ssa, (x, y))
            self.schedule.add(ssa)

        # Create agent competitor:
        for i in range(self.initial_population2):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            vision = self.random.randrange(1, 6)
            ssa = SsAgent2((x, y), self, False, vision)
            self.grid.place_agent(ssa, (x, y))
            self.schedule.add(ssa)

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        self.schedule.step()
        # collect data
        self.datacollector.collect(self)

    def run_model(self, step_count=200):

        for i in range(step_count):
            self.step()
