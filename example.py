#!/usr/bin/env python

import rvo23d

timeStep = 1/60.
neighborDist = 1.5
maxNeighbors = 5
timeHorizon = 1.5
radius = 2
maxSpeed = 0.4
velocity = (1, 1, 1)

sim = rvo23d.PyRVOSimulator(timeStep, neighborDist, maxNeighbors, timeHorizon, radius, maxSpeed, velocity)

a0 = sim.addAgent((0, 0, 0), neighborDist, maxNeighbors, timeHorizon, radius, maxSpeed, (0, 0, 0))
a1 = sim.addAgent((1, 0, 0), neighborDist, maxNeighbors, timeHorizon, radius, maxSpeed, (0, 0, 0))
a2 = sim.addAgent((1, 1, 0), neighborDist, maxNeighbors, timeHorizon, radius, maxSpeed, (0, 0, 0))
a3 = sim.addAgent((0, 1, 0), neighborDist, maxNeighbors, timeHorizon, radius, maxSpeed, (0, 0, 0))


# Set preferred velocities
sim.setAgentPrefVelocity(a0, (1, 1, 0))
sim.setAgentPrefVelocity(a1, (-1, 1, 0))
sim.setAgentPrefVelocity(a2, (-1, -1, 0))
sim.setAgentPrefVelocity(a3, (1, -1, 0))

print('Simulation has %i agents in it.' %
      (sim.getNumAgents()))

print('Running simulation')

for step in range(20):
    sim.doStep()

    positions = ['(%5.3f, %5.3f, %5.3f)' % sim.getAgentPosition(agent_no) for agent_no in (a0, a1, a2, a3)]
    print('step=%2i  t=%.3f  %s' % (step, sim.getGlobalTime(), '  '.join(positions)))

