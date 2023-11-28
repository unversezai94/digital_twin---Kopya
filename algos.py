import traci

def uyarmali(junction_name,loop_list):
    traci.trafficlight.setProgram(f"TL_{junction_name.name}", "0")
    
    if junction_name.phase_situation() == "green":
        
        if traci.trafficlight.getPhase(f"TL_{junction_name.name}") == junction_name.green_phases[0]:
            if junction_name.get_remaining_green() == 1 and (traci.inductionloop.getLastStepVehicleNumber(f"e{loop_list[0]}_0") > 0 or traci.inductionloop.getLastStepVehicleNumber(f"e{loop_list[0]}_1") > 0):
                print("aaaaaaaa babam sağ daraf")
                traci.trafficlight.setPhaseDuration(f"TL_{junction_name.name}", 3)
                
        if traci.trafficlight.getPhase(f"TL_{junction_name.name}") == junction_name.green_phases[1]:
            if junction_name.get_remaining_green() == 1 and (traci.inductionloop.getLastStepVehicleNumber(f"e{loop_list[1]}_0") > 0 or traci.inductionloop.getLastStepVehicleNumber(f"e{loop_list[1]}_1") > 0):
                print("aaaaaaaa babam sol tarafı")
                traci.trafficlight.setPhaseDuration(f"TL_{junction_name.name}", 3)
                
        if traci.trafficlight.getPhase(f"TL_{junction_name.name}") == junction_name.green_phases[2]:
            if junction_name.get_remaining_green() == 1 and (traci.inductionloop.getLastStepVehicleNumber(f"e{loop_list[2]}_0") > 0 or traci.inductionloop.getLastStepVehicleNumber(f"e{loop_list[2]}_1") > 0):
                print("aaaaaaaa babam aşşası")
                traci.trafficlight.setPhaseDuration(f"TL_{junction_name.name}", 3)
        
        if traci.trafficlight.getPhase(f"TL_{junction_name.name}") == junction_name.green_phases[3]:
            if junction_name.get_remaining_green() == 1 and (traci.inductionloop.getLastStepVehicleNumber(f"e{loop_list[3]}_0") > 0 or traci.inductionloop.getLastStepVehicleNumber(f"e{loop_list[3]}_1") > 0):
                print("aaaaaaaa babam yukarsı")
                traci.trafficlight.setPhaseDuration(f"TL_{junction_name.name}", 3)