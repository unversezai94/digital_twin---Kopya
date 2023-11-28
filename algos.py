import traci

def uyarmali(junction,phase,loop):
    traci.trafficlight.setProgram(f"TL_{junction.name}", "0")
    if junction.get_remaining_green() == 1 and (traci.inductionloop.getLastStepVehicleNumber(f"e{loop}_0") > 0 or traci.inductionloop.getLastStepVehicleNumber(f"e{loop}_1") > 0):
        print("aaaaaaaa babam sağ daraf")
        # set 3 seconds for current phase
        traci.trafficlight.setPhaseDuration(f"TL_{junction.name}", 3)
        junction.counter += 3
        if junction.counter >= junction.max_green:
            junction.counter = 0
            junction.current_phase += 1
            if junction.current_phase >= junction.num_of_phases:
                junction.current_phase = 0
            traci.trafficlight.setPhase(f"TL_{junction.name}", junction.current_phase)
        