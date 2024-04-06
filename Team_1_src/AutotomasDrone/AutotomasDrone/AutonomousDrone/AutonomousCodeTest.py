#  This is a sample Python script.
from codrone_edu.drone import *
from Matlanding import Red1, Red2, Green1, Green2, Blue1, Blue2
import
situation = input("What Scenario:" )

## Press Shift+F10 to execute it or replace it with your code.
## Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#Array Senarios Dice 3M == BM takeoff to RM land
#Array Senarios Dice 4M == BM takeoff to GM land


#Array Senarios Dice 1C == RC takeoff to BC land
#Array Senarios Dice 3C == BC takeoff to RC land



drone = Drone()
drone.pair()
colors = drone.get_colors()

if colors[1] == "Red":
    drone.set_drone_LED(255, 0, 0, 100)
    if situation == "R1":
        Drone1m = Red1.drone1m()
        Drone1m.scenario1()
    if situation == "R2":
        Drone2m = Red2.drone2m()
        Drone1m.scenario2()
elif colors[1] == "Blue":
    if situation == "B1":
        Drone3m = Blue1.drone5m()
        Drone3m.scenario3()
    if situation == "B2":
        Drone4m = Blue2.drone6m()
        Drone4m.scenario4()
    drone.set_drone_LED(0, 0, 255, 100)
elif colors[1] == "Green":
    drone.set_drone_LED(0, 255, 0, 100)
    if situation == "G1":
        Drone5m = Green1.drone5m()
        Drone5m.scenario5()
    if situation == "G2":
        Drone6m = Green2.drone6m()
        Drone6m.scenario6()
print(colors)
drone.close


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


