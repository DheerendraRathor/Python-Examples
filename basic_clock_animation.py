"""
Animation of clock in python turtle

@author Dheerendra Rathor <dheeru.rathor14@gmail.com>
"""

from turtle import Turtle
from datetime import datetime, timedelta
from time import sleep

clock = Turtle()
hour = Turtle()
minute = Turtle()
second = Turtle()

turtles = [clock, hour, minute, second]

for turtle in turtles:
    turtle.speed(0)
    turtle.hideturtle()

def make_clock():
    clock.penup()
    clock.color('#1A237E')
    clock.left(90)
    font_settings = ('Arial', 32, 'bold')
    romans = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
    for roman in romans:
        clock.right(30)
        clock.forward(300)
        clock.write(roman, font=font_settings)
        clock.back(300)
    clock.pendown()


def setup_hour_hand():
    hour.pensize(10)
    hour.color('#283593')
    hour.home()
    hour.left(90)


def setup_minute_hand():
    minute.pensize(5)
    minute.color('#5C6BC0')
    minute.home()
    minute.left(90)


def setup_second_hand():
    second.home()
    second.left(90)
    second.pensize(1)
    second.color('#1A237E')


def get_current_time():
    now = datetime.now()
    hour = (now.hour % 12) * 30 + (now.minute / 2)
    minutes = now.minute * 6
    seconds = now.second * 6
    return (hour, minutes, seconds)


def start_clock():
    make_clock()
    setup_hour_hand()
    setup_minute_hand()
    setup_second_hand()

    hours, minutes, seconds = get_current_time()

    old_hours = -1
    old_minutes = -1

    for turtle in turtles:
        turtle.hideturtle()
        turtle.hideturtle()

    
    while True:    
        start_time = datetime.now()
        if hours != old_hours:
            hour.undo()
            hour.undo()
            hour.right(hours)
            hour.forward(100)

        if minutes != old_minutes:
            minute.undo()
            minute.undo()
            minute.right(minutes)
            minute.forward(200)

        second.undo()
        second.undo()
        second.right(seconds)
        second.forward(250)

        old_minutes = minutes
        old_hours = hours

        seconds += 6

        if seconds == 360:
            minutes += 1

        if minutes == 12:
            hours += 1

        seconds %= 360
        minutes %= 360
        hours %= 360
        end_time = datetime.now()
        time_delta = end_time - start_time
        sleep_seconds = 1 - time_delta.microseconds/1000000
        sleep(sleep_seconds)


if __name__ == '__main__':
    try:
        start_clock()
    except:
        pass
