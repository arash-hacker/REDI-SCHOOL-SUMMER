from math import cos, sin
import math
import pyglet
from pyglet import shapes
from datetime import datetime


w = 600
window = pyglet.window.Window(w, w)
batch = pyglet.graphics.Batch()
fps_display = pyglet.window.FPSDisplay(window=window)

circle1 = shapes.Circle(w/2, w/2, w//2, color=(50, 225, 30), batch=batch)
circle2 = shapes.Circle(w/2, w/2, w//2-10, color=(0, 0, 0), batch=batch)

fac_second = 360//60
fac_minute = 360//60
fac_hour = 360//12


def update(dt):
    global sec_handle, min_handle, hour_handle

    current_time = datetime.now().strftime("%H:%M:%S")
    hour, minute, second = current_time.split(":")
    second = int(second)
    minute = int(minute)
    hour = int(hour)
    hour = hour - 12 if hour > 12 else hour
    # print("Current Time =", hour, minute, second)
    sec_handle = shapes.Line(w/2, w/2,
                             w/2+(w/2-10)*sin(math.radians(second*fac_second)),
                             w/2+(w/2-10)*cos(math.radians(second*fac_second)),
                             width=3, color=(0, 0, 255), batch=batch)
    min_handle = shapes.Line(w/2, w/2,
                             w/2+(w/2-15)*sin(math.radians(minute*fac_minute)),
                             w/2+(w/2-15)*cos(math.radians(minute*fac_minute)),
                             width=6, color=(0, 255, 0), batch=batch)
    hour_handle = shapes.Line(w/2, w/2,
                              w/2+(w/2-30)*sin(math.radians(hour*fac_hour)),
                              w/2+(w/2-30)*cos(math.radians(hour*fac_hour)),
                              width=15, color=(255, 0, 0), batch=batch)


pyglet.clock.schedule_interval(update, 1/60)


@window.event
def on_draw():
    window.clear()
    batch.draw()
    fps_display.draw()


pyglet.app.run()
