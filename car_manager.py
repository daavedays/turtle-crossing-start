from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.accelerate_cars = STARTING_MOVE_DISTANCE
        self.cars_list = self.make_cars()  # This variable stores the returned list of turtle objects,
        # that is created by the make_cars method. cars_list is later used in main.py and in making the objects move.

    @staticmethod
    def make_cars():
        """Produces 50 cars, scatters them randomly on the map. Saves each car instance in a list and returns list."""
        cars = []
        for i in range(50):
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.left(180)
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.goto(x=random.randint(300, 1000), y=random.randint(-250, 250))
            cars.append(new_car)
        return cars

    def cars_drive(self):
        """Takes each item in list cars[] iterates through each one and moves them forward by a set amount."""
        for car in self.cars_list:
            car.forward(STARTING_MOVE_DISTANCE)
            if car.xcor() < -300:
                car.setx(300)
                car.sety(random.randint(-250, 250))

    def level_up(self):
        self.accelerate_cars += MOVE_INCREMENT
