from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Creating the gui
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# While the game is active
# we need to refresh the screen
# and slow down the snake

game_is_on = True

while game_is_on:
    screen.update()
    if scoreboard.score < 5:
        time.sleep(0.1)
    else:
        time.sleep(0.05)    
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    # Detect collision with the wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    # if the head of the snake collide with the rest of it's body
    # trigger game_over

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()    

screen.exitonclick()