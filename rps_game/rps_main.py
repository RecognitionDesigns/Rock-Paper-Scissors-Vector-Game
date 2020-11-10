#!/usr/bin/env python3

import anki_vector
from anki_vector import behavior
import time
import random
import sys
import os
import os.path
from PIL import Image, ImageDraw, ImageFont
from anki_vector.util import degrees, distance_mm, speed_mmps
                        
def main():
    os.system('./sim_robots.sh')
    sys.exit()

robot1 = anki_vector.Robot('serial for robot 1')
robot2 = anki_vector.Robot('serial for robot 2')
robot1.connect()
robot2.connect()

robot1.behavior.say_text("Tap the back of the robot")
robot2.behavior.say_text("you think will win this round")

t_end = time.time() + 10
while time.time() < t_end:
    if robot1.touch.last_sensor_reading.is_being_touched:
        print("Robot 1 was tapped")
        f= open("game_data/winner.txt","w+")
        f.write("robot1")
        f.close()
        robot1.behavior.say_text("You tapped me!")
        main()
        
    if robot2.touch.last_sensor_reading.is_being_touched:
        print("Robot 2 was tapped")
        f= open("game_data/winner.txt","w+")
        f.write("robot2")
        f.close()
        robot2.behavior.say_text("You tapped me!")
        main()
    
if os.path.isfile('game_data/winner.txt') == False:
    print("No Robot tapped")
    robot1.behavior.say_text("You haven't tapped a robot!")
    sys.exit()
    
time.sleep(2.0)

robot1.disconnect()
robot2.disconnect()

#Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>