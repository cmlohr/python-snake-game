from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#191919")
screen.title("PySnake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_b = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()


    # collision parameters
    if snake.head.distance(food) < 15:
        food.refresh()
        score_b.sb_refresh()

screen.exitonclick()
