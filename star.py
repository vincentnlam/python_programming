# Python program to draw star 
# using Turtle Programming 
import turtle 
star = turtle.Turtle() 
star.speed(10)

star.right(75) 
star.forward(100) 

for i in range(120): 
	star.right(124) 
	star.forward(200) 
	
turtle.done() 
