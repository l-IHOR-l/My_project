import turtle
from turtle import Turtle, Screen

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
HALL_HEADER = 150
FONT_SIZE = 20

ROW = 5
COLUMN = 5

main_screen = Screen()
main_screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
main_screen.setworldcoordinates(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
main_screen.title("Cinema")

turtle.Screen().bgcolor('#fc8803')

main_turtle = Turtle()
main_turtle.hideturtle()
main_turtle.speed(0)
main_turtle.penup()

main_write = Turtle()
main_write.hideturtle()
main_write.speed(0)
main_write.penup()

free = Turtle()
free.hideturtle()
free.speed(0)
free.penup()

cell_width = SCREEN_WIDTH / COLUMN
cel_height = (SCREEN_HEIGHT - HALL_HEADER) / ROW

seat_radius = (cel_height * 0.8) / 2

x = cell_width / 2
y = (cel_height / 2) - seat_radius


seats = {}

for r in range(ROW):
    for c in range(COLUMN):
        seats[(x, y)] = False
        x += cell_width
    x = cell_width / 2
    y += cel_height

print(seats)

def write_free_seats():
    main_screen.tracer(0)
    main_write.clear()
    main_write.setposition(10, SCREEN_HEIGHT - (FONT_SIZE * 2))
    main_write.pendown()
    free_seats = len(seats.values()) - sum(seats.values())
    main_write.write(f'Free: {free_seats}', font=('arial',FONT_SIZE,'bold'))
    main_write.penup()
    main_screen.tracer(1)

def write_sold_seats():
    main_screen.tracer(False)
    free.clear()
    free.setposition(10, SCREEN_HEIGHT - (FONT_SIZE * 4))
    free.pendown()
    free_seats = sum(seats.values())
    free.write(f'Sold: {free_seats}', font=('arial',FONT_SIZE,'bold'))
    free.penup()
    main_screen.tracer(True)



def draw(x, y, color='steel blue'):
    main_turtle.setposition(x, y)
    main_turtle.pendown()
    main_turtle.begin_fill()
    main_turtle.circle(seat_radius)
    main_turtle.fillcolor(color)
    main_turtle.end_fill()
    main_turtle.penup()




def get_seat(x, y):
    for seat_x, seat_y in seats:
        distance = ((x - seat_x) ** 2 + (y - (seat_y + seat_radius)) ** 2) ** 0.5
        if distance <= seat_radius:
            return seat_x,seat_y


def book_seat(x, y):
    seat_coord = get_seat(x,y)
    if seat_coord:
        seats[seat_coord] = True
        draw(*seat_coord, color='tomato')
        write_sold_seats()
        write_free_seats()

def test(x, y):
    seat_coord = get_seat(x,y)
    if seat_coord:
        seats[seat_coord] = False
        draw(*seat_coord, color='steel blue')
        write_free_seats()
        write_sold_seats()


main_screen.tracer(False)
for seat in seats:
    draw(*seat)
main_screen.tracer(True)
write_free_seats()
write_sold_seats()
main_screen.onclick(book_seat)
main_screen.onclick(test, btn=3)
main_screen.mainloop()
