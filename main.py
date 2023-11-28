import traci
from junction import Junction
import random
import traci.constants as tc
from algos import uyarmali
import sumolib

sumo_cmd = ["sumo-gui", "-c", "3_junction.sumocfg","--no-warnings"]

traci.start(sumo_cmd)

j_1 = Junction("K1",4)
j_2 = Junction("K2",4)
j_3 = Junction("K3",4)


a = ['k2k1','w1k1','s1k1','n1k1']
b = ['k3k2','k1k2','s2k2','n2k2']
c = ['e1k3','k2k3','s3k3','n3k3']

"""
{'s1k1', 'k2k1', 'n1k1', 'w1k1'} -> {k2k1,w1k1,s1k1,n1k1} -> {ek2k1,ew1k1,es1k1,en1k1}
{'s2k2', 'k3k2', 'n2k2', 'k1k2'}
{'s3k3', 'k2k3', 'e1k3', 'n3k3'}
"""

while traci.simulation.getMinExpectedNumber() > 0:
    
    uyarmali(j_1,a)
    uyarmali(j_2,b)
    uyarmali(j_3,c)
    
    traci.simulationStep()
    
    
traci.close()