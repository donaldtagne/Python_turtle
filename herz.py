"""
from turtle import*
from random import uniform

bgcolor("black")
tracer(50)

n=0
width=10
z=0.5
j = x= 1
ht()

while True:
    if j >= (n-1)*z+x:
        k=True
    if round (j, 2)==float(x):
        k=False
    goto(0, -80)
    begin_fill()
    seth(139)
    for i in range(623):
        color((uniform(0,1), uniform(0,1), uniform(0,1)))
        if i==312:
            lt(120)
        if i>=112 and i <=511:
            rt(1)
        fd(j)
        dot(width)
    if k:
        j-= z
    else:
        j += z
    penup()
    goto(-140, -150)
    color((uniform(0,1), uniform(0,1), uniform(0,1)))
    write("I LOVE YOU...BABY :)", font=("Arial", 20, "bold"))
done()







"""