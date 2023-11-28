from junction import Junction
from algos import uyarmali
import traci

class Simulation:
    def __init__(self,junction_array):
        self.num_junction = len(junction_array)
        self.junctions = self.junction_creator(junction_array)
        self.sumo_cmd = ["sumo-gui", "-c", "3_junction.sumocfg","--no-warnings"]
        traci.start(self.sumo_cmd)

    def junction_creator(self,junction_array):
        junctions = []
        for junction in junction_array:
            junctions.append(Junction(junction,4))
        junctions[0].loop_list = {1:'k2k1',5:'w1k1',9:'s1k1',13:'n1k1'}
        junctions[1].loop_list = {1:'k3k2',5:'k1k2',9:'s2k2',13:'n2k2'}
        junctions[2].loop_list = {1:'e1k3',5:'k2k3',9:'s3k3',13:'n3k3'} 
        return junctions
    
    def run(self):
        
        while traci.simulation.getMinExpectedNumber() > 0:
            for junction in self.junctions:
                phase = self._get_phase(junction)
                if phase not in junction.loop_list:
                    continue
                else:
                    loop = junction.loop_list[phase]
                    uyarmali(junction,phase,loop)
            traci.simulationStep()
    
    
    def _simulate(self,steps_todo):
        while steps_todo > 0:
            traci.simulationStep()
            steps_todo -= 1
            
    def _get_phase(self,junction):
        junction.curent_phase = traci.trafficlight.getPhase(f"TL_{junction.name}")
        phase = traci.trafficlight.getPhase(f"TL_{junction.name}")
        if phase in junction.green_phases:
            return phase
    
        
Simulation(['K1','K2','K3']).run()