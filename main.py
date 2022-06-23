import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Turtle Crossing Capstone")
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.up, key="w")
screen.onkey(player.down, key="s")

car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # detect collision
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False


screen.exitonclick()
