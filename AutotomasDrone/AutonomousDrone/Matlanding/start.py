from codrone_edu.drone import Drone
from codrone_edu.drone import *
import dronesc1
import dronesc2
import dronesc3
import dronesc4
import dronesc5
import dronesc6
#import colorprediction
#import ColorCallTest

# Step 1 - Pair Drone & Define Variables
#drone = Drone()
#drone.pair()
#drone.set_drone_LED(255, 255, 255, 100)
Scenario1 = dronesc1.scenario1()
Scenario2 = dronesc2.scenario2()
Scenario3 = dronesc3.scenario3()
Scenario4 = dronesc4.scenario4()
Scenario5 = dronesc5.scenario5()
Scenario6 = dronesc6.scenario6()
#TestClrPred = colorprediction.colorpredict()
#TestClrCalib = colorcalibration.colorcalibrate()
# Step 2 - Detect Color of Mat Before Takeoff
# Step 3 - Change LED Color of Drone
# Step 4 - Identify Scenario (c = cube, m = mat)
#   Sc1 (Takeoff Red Land Blue)/1c(bonus) or 1m
#   Sc2 (Takeoff Red Land Green)/2m
#   Sc3 (Takeoff Blue Land Red)/3c(bonus) or 3m
#   Sc4 (Takeoff Blue Land Green)/4m
#   Sc5 (Takeoff Green Land Blue)/5c(bonus) or 5m
#   Sc6 (Takeoff Green Land Red)/6c(bonus) or 6m
# Step 5 - Place Code
# Calibration Seq
#TestClrCalib.clrcalib()
if __name__ == '__main__':
   # TestClrPred.dronepairing()
    # print("About to change color!")
    # TestClrPred.colortoled()
    # print("Color should be changed!")
    # input("Press enter to sense and change LED color")
    print("# = Scenario, c = cube landing, m = mat landing")
    print("Options: 1c, 1m, 2m, 3c, 3m, 4m, 5c, 5m, 6c, 6m, predict, calibrate, exit")
    scenario = input("Enter Scenario:")
    if scenario == "1m":
        Scenario1.dronescen1m()
    #elif scenario == "calibrate":
    # ColorCallTest.callingcolors(drone)
    #elif scenario == "predict":
    # TestClrPred.colortoled()
    elif scenario == "1c":
        Scenario1.dronescen1c()
    elif scenario == "2m":
        Scenario2.dronescen2m()
    elif scenario == "3m":
        Scenario3.dronescen3m()
    elif scenario == "3c":
        Scenario3.dronescen3c()
    elif scenario == "4m":
        Scenario4.dronescen4m()
    elif scenario == "5m":
        Scenario5.dronescen5m()
    elif scenario == "5c":
        Scenario5.dronescen5c()
    elif scenario == "6m":
        Scenario6.dronescen6m()
    elif scenario == "6c":
        Scenario6.dronescen6c()
    elif scenario == "exit":
        print("Shutting down...")
        exit()