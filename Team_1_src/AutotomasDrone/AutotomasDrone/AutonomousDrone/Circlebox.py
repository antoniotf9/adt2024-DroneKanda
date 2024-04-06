class boxcommand:
    from codrone_edu.drone import *

    def Box(self):


    drone = Drone()
    drone.pair()
    drone.takeoff()
    drone.move_forward(distance=15, units="in", speed=2)
    drone.turn_left(90)
    drone.move_forward(distance=15, units="in", speed=2)
    drone.turn_right(90)
    drone.move_backward(distance=12, units="in", speed=2)
    drone.turn_right(90)
    drone.move_forward(distance=15, units="in", speed=2)
    drone.land()
    drone.close()