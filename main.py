import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgpic('turtle-img.gif')
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(fun=player.move_up, key="space")

scoreboard = Scoreboard()
car_manager = CarManager()
car_manager.hideturtle()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(player.speed)
    car_manager.cars_drive()

    if player.ycor() > 265:
        scoreboard.update_level()
        car_manager.level_up()
        player.speed /= 2
        player.goto(0, -280)

    for car in car_manager.cars_list:
        if (car.xcor() - 20 < player.xcor() < car.xcor() + 20
                and car.ycor() - 20 < player.ycor() < car.ycor() + 20):
            scoreboard.game_over()
            game_is_on = False

            print(player.ycor())
            print(car.ycor())
            print(round(player.xcor()), 4)
            print(car.xcor())
screen.exitonclick()
