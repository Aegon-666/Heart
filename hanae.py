import turtle
import math

# --- الإعدادات ---
screen = turtle.Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("Quantum Love")
screen.colormode(255)
turtle.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# متغير التحكم بالدوران
rotation_angle = 0

# --- دالة الرسم ---
def draw_heart(scale, angle):
    for i in range(200):
        teta = i * 0.1
        x = scale * (16 * math.sin(teta)**3)
        y = scale * (13 * math.cos(teta) - 5 * math.cos(2*teta) - 2 * math.cos(3*teta) - math.cos(4*teta))
        
        rot_x = x * math.cos(angle) - y * math.sin(angle)
        rot_y = x * math.sin(angle) + y * math.cos(angle)
        
        t.goto(rot_x, rot_y)
        if i == 0: t.pendown()
        else: t.pendown()
    t.penup()

# --- دالة الحركة (بديلة لـ while True) ---
def animate():
    global rotation_angle
    t.clear()
    
    # رسم القلوب
    for i in range(15):
        draw_heart(10 + i * 1.5, rotation_angle + (i * 0.2))
    
    screen.update()
    rotation_angle += 0.05
    
    # استدعاء الدالة مرة أخرى بعد 10 مللي ثانية
    screen.ontimer(animate, 10)

# بدء الحركة
animate()
turtle.mainloop()