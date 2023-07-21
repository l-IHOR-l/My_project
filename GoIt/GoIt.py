import turtle
def fibo(n):
    if n in (1,2):
        return 1
    if not n:
       return 0
    return fibo(n-2) + fibo(n-1)


print(fibo(8))
t = turtle.Turtle()


for i in range(20):
    f = fibo(i)
    for i in range(4):
        t.forward(f)
        t.left(90)
    t.circle(f, 90)

turtle.mainloop()