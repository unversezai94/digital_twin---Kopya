import traci

def uyarmali(junction,phase,loop):
    traci.trafficlight.setProgram(f"TL_{junction.name}", "0")
    if junction.get_remaining_green() == 1 and (traci.inductionloop.getLastStepVehicleNumber(f"e{loop}_0") > 0 or traci.inductionloop.getLastStepVehicleNumber(f"e{loop}_1") > 0):
        # set 3 seconds for current phase
        traci.trafficlight.setPhaseDuration(f"TL_{junction.name}", 3)
        
        if junction.timer  == 0 :
            junction.timer = traci.simulation.getTime()
        else:
            if traci.simulation.getTime() - junction.timer > junction.max_green:
                traci.trafficlight.setPhase(f"TL_{junction.name}", phase+1)
                junction.timer = 0
                