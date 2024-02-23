from turtle import Screen
from snake import Snake
from fruit import Fruit
from score import Score
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
fruit = Fruit()
score = Score()

game_is_on = True

screen.listen()
screen.onkey(key = "Up", fun = snake.snake_up)
screen.onkey(key = "Down", fun = snake.snake_down)
screen.onkey(key = "Left", fun = snake.snake_left)
screen.onkey(key = "Right", fun = snake.snake_right)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_forward()
    if snake.head.distance(fruit) < 15:
        fruit.refresh()
        score.update_score()
        snake.add_section()
    if snake.detect_collision_wall():
        score.game_over()
        game_is_on: False
        break
    if snake.detect_collision_tail():
        score.game_over()
        game_is_on: False
        break

screen.exitonclick()