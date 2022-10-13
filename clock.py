from turtle import *
import turtle as tur
import datetime
import time

def draw_clock(): #Currently color doesn't matter
    tur.bgpic("sora_clock.png")

def draw_hand(angle, radius, width, color):   
    tur.pencolor(color) # Sets the outline
    tur.pensize(4)
    tur.penup()
    tur.home()
    tur.fillcolor(color)
    tur.begin_fill()
    tur.left(90)
    tur.right(angle)
    tur.forward(radius)
    tur.pendown()
    tur.left(150)
    tur.forward(width)
    tur.home()
    tur.left(90)
    tur.right(angle)
    tur.penup()
    tur.forward(radius)
    tur.pendown()
    tur.right(150)
    tur.forward(width)
    tur.home()
    tur.end_fill()

def main():
    radius = 450 # Currently manually inputted , should update to auto detect best radius
    tur.speed(0)
    tur.hideturtle()
    tur.title("Clock Face")
    draw_clock()
    curr_time = datetime.datetime.now().time() # Gets the current time

    tur.title(curr_time.strftime("Themed Clock for %H:%M"))
    draw_hand(curr_time.minute * 6, radius * .85, radius // 10, "blue")
    draw_hand(((curr_time.hour + curr_time.minute / 60) % 12) * 30, radius * .55, radius // 10, "purple")

    while True: #Have to force close the program if we want it to close
        new_time=datetime.datetime.now().time()

        if curr_time.minute != new_time.minute:
            tur.clear()
            tur.title(new_time.strftime("Themed Clock for %H:%M"))
            draw_hand(new_time.minute * 6, radius * .9, radius // 10, "blue")
            draw_hand(((new_time.hour + new_time.minute / 60) % 12) * 30, radius * .6, radius // 10, "purple")
            curr_time=new_time
        time.sleep(50) # Sleeps the program for most of a minute as no calculations need to be done
main()