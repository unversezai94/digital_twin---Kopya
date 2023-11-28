import traci


class Junction:
    def __init__(self, junction_name, num_of_gphases):
        self.name = junction_name
        self.num_of_phases = num_of_gphases * 4
        self.green_phases, self.yellow_phases, self.red_phases = self.phase_creator()
        self.roads = self.get_roads()
        self.max_duration = [0,0,0,0]

    def phase_creator(self):
        green_phases = []
        yellow_phases = []
        red_phases = []
        for i in range(0,self.num_of_phases,4):
            yellow_phases.append(i)
            green_phases.append(i+1)
            yellow_phases.append(i+2)
            red_phases.append(i+3)
        
        return green_phases,yellow_phases,red_phases
    
    def get_roads(self):
        
        raw_edges = set(traci.trafficlight.getControlledLanes(f"TL_{self.name}"))
        processed_edges = set()

        for edge in raw_edges:
            clean_edge = edge.rsplit('_')[0]
            processed_edges.add(clean_edge)

        return processed_edges
    
    def phase_situation(self):
        phase = traci.trafficlight.getPhase(f"TL_{self.name}")
        if phase in self.green_phases:
            return "green"
        elif phase in self.yellow_phases:
            return "yellow"
        elif phase in self.red_phases:
            return "red"
        else:
            return "unknown"
        
        
    def get_remaining_green(self):
        remaining_green = traci.trafficlight.getNextSwitch(f"TL_{self.name}") - traci.simulation.getTime()
        return remaining_green
    
    def loop_list(self):
        loop_list = []
        for road in self.roads:
            loop_list.append(f"e{road}_0")
            loop_list.append(f"e{road}_1")
        return loop_list
    
    
    """
        [a,b]
        [a,b]
    
    
    """