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
    time.sleep(0.1)
    snake.move()

    # collision parameters
    # food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_b.sb_refresh()
    # wall
    if snake.head.xcor() > 281 or snake.head.xcor() < -281 or snake.head.ycor() > 281 or snake.head.ycor() < -281:
        score_b.game_over()
        game_on = False

    # tail
    for segments in snake.segment[1:]:
        if snake.head.distance(segments) < 10:
            game_on = False
            score_b.game_over()

screen.exitonclick()
