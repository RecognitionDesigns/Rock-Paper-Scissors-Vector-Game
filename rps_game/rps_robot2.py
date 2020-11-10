#!/usr/bin/env python3

import anki_vector
import time
import random
import sys
import os
import os.path
from PIL import Image, ImageDraw, ImageFont
from anki_vector.util import degrees, distance_mm, speed_mmps

duration_s = 4.0
good1 = 'Feedback_GoodRobot'
good2 = 'PounceWProxForward'
bad1 = 'Feedback_MeanWords'
bad2 = 'DriveEndAngry'
    
def main():
    robot1.behavior.say_text("Robot 2 Ready!")
    robot1.behavior.say_text("Rock, Paper, Scissors!")
    robot1choice()
    
def robot1choice():
    choice1 = random.randint(1,3)
    print(choice1)
    if choice1==1:
        robot1.behavior.say_text("rock!")
        f= open("game_data/robotchoice2.txt","w+")
        f.write("rock")
        f.close()
        time.sleep(2)
        rock1()
        
    if choice1==2:
        robot1.behavior.say_text("paper!")
        f= open("game_data/robotchoice2.txt","w+")
        f.write("paper")
        f.close()
        time.sleep(2)
        paper1()
        
    if choice1==3:
        robot1.behavior.say_text("scissor!")
        f= open("game_data/robotchoice2.txt","w+")
        f.write("scissors")
        f.close()
        time.sleep(2)
        scissor1()

def rock1():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    image_path = os.path.join(current_directory, "images", "rock.jpg")
    image_file = Image.open(image_path)
    screen_data = anki_vector.screen.convert_image_to_screen_data(image_file)
    robot1.behavior.set_head_angle(degrees(25.0))
    robot1.screen.set_screen_with_image_data(screen_data, duration_s)
    winner()

def paper1():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    image_path = os.path.join(current_directory, "images", "paper.jpg")
    image_file = Image.open(image_path)
    screen_data = anki_vector.screen.convert_image_to_screen_data(image_file)
    robot1.behavior.set_head_angle(degrees(25.0))
    robot1.screen.set_screen_with_image_data(screen_data, duration_s)
    winner()   
    
def scissor1():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    image_path = os.path.join(current_directory, "images", "scissor.jpg")
    image_file = Image.open(image_path)
    screen_data = anki_vector.screen.convert_image_to_screen_data(image_file)
    robot1.behavior.set_head_angle(degrees(25.0))
    robot1.screen.set_screen_with_image_data(screen_data, duration_s)
    winner()

def winner():
    rc1 = open("game_data/robotchoice1.txt", "r")
    if rc1.mode == 'r':
        robotchoice1 = rc1.read()
    
        rc2 = open("game_data/robotchoice2.txt", "r")
        if rc2.mode == 'r':
            robotchoice2 = rc2.read()
    
            if robotchoice1 == robotchoice2:
                robot1.behavior.say_text("Its a draw!")
                os.remove('game_data/winner.txt')
                sys.exit()
                
            if robotchoice1 == "rock" and robotchoice2 == "paper":
                robotWinner = "robot2"
                robot1.behavior.say_text((robotchoice2) + "beats" + (robotchoice1) + ", I Won!")
                robot1.anim.play_animation_trigger(good1)
#                f = open("game_data/winner.txt", "r")
#                if f.mode == 'r':
#                    contents = f.read()
##                    print (contents)
#                    if contents == robotWinner:
#                        robot1.behavior.say_text("you chose" + (contents))
#                        robot1.behavior.say_text("you were right!")
#                        robot1.anim.play_animation_trigger(good1)
#                        os.remove('game_data/winner.txt')
#                        robot1.disconnect()
#                        sys.exit()
#                    else:
#                        robot1.behavior.say_text("oh i'm sorry, you picked the wrong robot!")
#                        robot1.anim.play_animation_trigger(bad2)
#                        os.remove('game_data/winner.txt')
#                        robot1.disconnect()
#                        sys.exit()
                
            if robotchoice2 == "rock" and robotchoice1 == "paper":
                robotWinner = "robot1"
                robot1.behavior.say_text((robotchoice1) + "beats" + (robotchoice2))
                time.sleep(2)
                robot1.behavior.say_text("and I lost")
#                f = open("game_data/winner.txt", "r")
#                if f.mode == 'r':
#                    contents = f.read()
#                    print (contents)
#                    if contents == robotWinner:
#                        robot1.behavior.say_text("you chose" + (contents))
#                        robot1.behavior.say_text("you were right!")
#                        robot1.anim.play_animation_trigger(good2)
#                        os.remove('game_data/winner.txt')
#                        robot1.disconnect()
#                        sys.exit()
#                    else:
#                        robot1.behavior.say_text("oh i'm sorry, you picked the wrong robot!")
#                        robot1.anim.play_animation_trigger(bad1)
#                        os.remove('game_data/winner.txt')
#                        robot1.disconnect()
#                        sys.exit()
                
            if robotchoice1 == "scissors" and robotchoice2 == "paper":
                robotWinner = "robot1"
                robot1.behavior.say_text((robotchoice1) + "beats" + (robotchoice2))
                time.sleep(2)
                robot1.behavior.say_text("and I lost")
#                f = open("game_data/winner.txt", "r")
#                if f.mode == 'r':
#                    contents = f.read()
#                    print (contents)
#                    if contents == robotWinner:
#                        robot1.behavior.say_text("you chose" + (contents))
#                        robot1.behavior.say_text("you were right!")
#                        robot1.anim.play_animation_trigger(good1)
#                        os.remove('game_data/winner.txt')
#                        robot1.disconnect()
#                        sys.exit()
#                    else:
#                        robot1.behavior.say_text("oh i'm sorry, you picked the wrong robot!")
#                        robot1.anim.play_animation_trigger(bad2)
#                        os.remove('game_data/winner.txt')
#                        robot1.disconnect()
#                        sys.exit()
                
            if robotchoice2 == "scissors" and robotchoice1 == "paper":
                robotWinner = "robot2"
                robot1.behavior.say_text((robotchoice2) + "beats" + (robotchoice1) + ", I Won!")
                robot1.anim.play_animation_trigger(good2)
#                f = open("game_data/winner.txt", "r")
#                if f.mode == 'r':
#                    contents = f.read()
#                    print (contents)
#                    if contents == robotWinner:
#                        robot1.behavior.say_text("you chose" + (contents))
#                        robot1.behavior.say_text("you were right!")
#                        robot1.anim.play_animation_trigger(good1)
#                        os.remove('game_data/winner.txt')
#                        robot1.disconnect()
#                        sys.exit()
#                    else:
#                        robot1.behavior.say_text("oh i'm sorry, you picked the wrong robot!")
#                        robot1.anim.play_animation_trigger(bad2)
#                        os.remove('game_data/winner.txt')
#                        robot1.disconnect()
#                        sys.exit()
                
            if robotchoice1 == "rock" and robotchoice2 == "scissors":
                robotWinner = "robot1"
                robot1.behavior.say_text((robotchoice1) + "beats" + (robotchoice2))
                time.sleep(2)
                robot1.behavior.say_text("and I lost")
#                f = open("game_data/winner.txt", "r")
#                if f.mode == 'r':
#                    contents = f.read()
#                    print (contents)
#                    if contents == robotWinner:
#                        robot1.behavior.say_text("you chose" + (contents))
#                        robot1.behavior.say_text("you were right!")
#                        robot1.anim.play_animation_trigger(good2)
#                        os.remove('game_data/winner.txt')
#                        robot1.disconnect()
#                        sys.exit()
#                    else:
#                        robot1.behavior.say_text("oh i'm sorry, you picked the wrong robot!")
#                        robot1.anim.play_animation_trigger(bad2)
#                        os.remove('game_data/winner.txt')
#                        robot1.disconnect()
#                        sys.exit()
                
            if robotchoice2 == "rock" and robotchoice1 == "scissors":
                robotWinner = "robot2"
                robot1.behavior.say_text((robotchoice2) + "beats" + (robotchoice1) + ", I Won!")
                robot1.anim.play_animation_trigger(good1)
#                f = open("game_data/winner.txt", "r")
#                if f.mode == 'r':
#                    contents = f.read()
#                    print (contents)
#                    if contents == robotWinner:
#                        robot1.behavior.say_text("you chose" + (contents))
#                        robot1.behavior.say_text("you were right!")
#                        robot1.anim.play_animation_trigger(good2)
#                        os.remove('game_data/winner.txt')
#                        robot1.disconnect()
#                        sys.exit()
#                    else:
#                        robot1.behavior.say_text("oh i'm sorry, you picked the wrong robot!")
#                        robot1.anim.play_animation_trigger(bad1)
#                        os.remove('game_data/winner.txt')
#                        robot1.disconnect()
#                        sys.exit()
                        
robot1 = anki_vector.Robot('serial for robot 2')
robot1.connect()
main()

#Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>