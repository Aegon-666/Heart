import turtle
import colorsys
import math 
import sys

screen = turtle.Screen()
screen.setup(width=950, height=950)
screen.bgcolor("#040008")
screen.title("Quantum love")
turtle.tracer(3)
t = turtle.Turtle()
t.speed(0)
t.width(1)
t.hideturtle()
hud = turtle.Turtle()
hud.speed(0)
hud.hideturtle()
hud.penup()

is_paused = False
heart_beat_speed = 3.0
num_ring = 18
twist_factor = 1.2
manifold_mode = 0 
palette_idx = 0
camera_distance = 420.0
master_time = 0.0
rot_x = 0.0
rot_y = 0.0
rot_z = 0.0