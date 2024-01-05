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
    """Main game loop, where the logic of the game is being handled.
       The collisions with the obstacles, their motion, the turtles motion, and the difficulty level."""
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
screen.exitonclick()
