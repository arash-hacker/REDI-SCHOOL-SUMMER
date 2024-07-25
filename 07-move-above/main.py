import pyglet
from pyglet.window import key

# Create a window
window = pyglet.window.Window(width=800, height=600, caption="Emoji Center")
# Load emoji as a sprite
emoji = pyglet.resource.image('emoji.png')
emoji_sprite = pyglet.sprite.Sprite(emoji)

X = window.width // 2 - emoji_sprite.width // 2
Y = window.height // 2 - emoji_sprite.height // 2


@window.event
def on_draw():
    global X, Y
    window.clear()
    # Calculate the center position
    emoji_sprite.x = X
    emoji_sprite.y = Y
    emoji_sprite.draw()


@window.event
def on_key_press(symbol, modifiers):
    global X, Y
    delta = 10
    if symbol == key.S:
        Y = Y-delta

    if symbol == key.W:
        Y = Y+delta

    if symbol == key.D:
        X = X+delta

    if symbol == key.A:
        X = X-delta

    if symbol == key.Q:  # Press 'Q' to quit the application
        pyglet.app.exit()


# Run the application
pyglet.app.run()
