from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    section_list = []
    initial_position = [(0,0),(0,-20),(0,-40), (0,-60), (0,-80), (0,-100)]

    def __init__(self):
        for i in range (0,len(self.initial_position)-1):
            self.section_list.append(self.snakeSection(self.initial_position[i]))
        self.head = self.section_list[0]

    def snakeSection(self,position):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        return snake

    def add_section(self):
        tail = self.section_list[-1].position()
        self.section_list.append(self.snakeSection(tail))


    def snake_forward(self):
        for section in range(len(self.section_list)-1,0,-1):
            new_x = self.section_list[section-1].xcor()
            new_y = self.section_list[section-1].ycor()
            self.section_list[section].goto(new_x, new_y)
        self.section_list[0].forward(20)


    def snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def snake_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def eat_food(self, fruit):
        if (self.head.xcor()-fruit.xcoor >= 20) and (self.head.ycor()-fruit.ycoor>=20):
            return True

    def detect_collision_wall(self):
        if self.head.xcor() > 295 or self.head.xcor() < -295 or self.head.ycor() > 295 or self.head.ycor() < -295:
            return True

    def detect_collision_tail(self):
        for segment in range(1, len(self.section_list)-1):
            if self.head.distance(self.section_list[segment]) < 10:
                return True