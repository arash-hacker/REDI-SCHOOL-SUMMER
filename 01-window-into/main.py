import pyglet
from pyglet.window import key

# Create a window
window = pyglet.window.Window(width=800, height=600, caption="Window")

# Load emoji as a sprite


@window.event
def on_draw():
    window.clear()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.Q:  # Press 'Q' to quit the application
        pyglet.app.exit()


# Run the application
pyglet.app.run()
