"""
Animation of clock in python turtle

@author Dheerendra Rathor <dheeru.rathor14@gmail.com>
"""

from turtle import Turtle

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
    clock.left(90)
    font_settings = ('Arial', 16, 'bold')
    for i in range(1, 13):
        clock.right(30)
        clock.forward(300)
        clock.write(i, font=font_settings)
        clock.back(300)
    clock.pendown()


def setup_hour_hand():
    hour.pensize(10)
    hour.color('blue')
    hour.home()
    hour.left(90)


def setup_minute_hand():
    minute.pensize(5)
    minute.color('green')
    minute.home()
    minute.left(90)


def setup_second_hand():
    second.home()
    second.left(90)
    second.pensize(1)
    second.color('red')


def start_clock():
    make_clock()
    setup_hour_hand()
    setup_minute_hand()
    setup_second_hand()

    hours = 0
    minutes = 0
    seconds = 0

    old_hours = -1
    old_minutes = -1

    for turtle in turtles:
        turtle.hideturtle()
        turtle.hideturtle()

    while True:
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

        seconds += 1

        if seconds == 360:
            minutes += 1

        if minutes == 12:
            hours += 1

        seconds %= 360
        minutes %= 360
        hours %= 360


if __name__ == '__main__':
    try:
        start_clock()
    except:
        pass
