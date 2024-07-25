import pyglet
from pyglet.window import key

# Create a window
window = pyglet.window.Window(width=800, height=600, caption="Emoji Center")
# Load emoji as a sprite
# Add your emoji image filenames here
emoji_images = ['up.png', 'down.png', 'left.png', 'right.png']
emoji_sprites = [pyglet.sprite.Sprite(
    pyglet.resource.image(img)) for img in emoji_images]
current_index = 0
emoji_sprite = emoji_sprites[current_index]
X = window.width // 2 - emoji_sprite.width // 2
Y = window.height // 2 - emoji_sprite.height // 2


@window.event
def on_draw():
    global X, Y, emoji_sprite
    window.clear()
    emoji_sprite.x = X
    emoji_sprite.y = Y
    emoji_sprite.draw()


@window.event
def on_key_press(symbol, modifiers):
    global X, Y, emoji_sprite
    delta = 10
    if symbol == key.S:  # Down
        emoji_sprite = emoji_sprites[1]
        Y = Y-delta

    if symbol == key.W:  # Up
        emoji_sprite = emoji_sprites[0]
        Y = Y+delta

    if symbol == key.D:  # Right
        emoji_sprite = emoji_sprites[3]
        X = X+delta

    if symbol == key.A:  # Left
        emoji_sprite = emoji_sprites[2]
        X = X-delta

    if symbol == key.Q:  # Press 'Q' to quit the application
        pyglet.app.exit()


# Run the application
pyglet.app.run()
