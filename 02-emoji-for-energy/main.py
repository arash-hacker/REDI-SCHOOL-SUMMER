import pyglet

# Create a window
window = pyglet.window.Window(width=800, height=600, caption="Emoji Center")

# Load emoji as a sprite
emoji = pyglet.resource.image('emoji.png')
emoji_sprite = pyglet.sprite.Sprite(emoji)


@window.event
def on_draw():
    window.clear()
    # Calculate the center position
    emoji_sprite.x = window.width // 2 - emoji_sprite.width // 2
    emoji_sprite.y = window.height // 2 - emoji_sprite.height // 2
    emoji_sprite.draw()


# Run the application
pyglet.app.run()
