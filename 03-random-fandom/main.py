import pyglet
from pyglet import clock

# Create a window
window = pyglet.window.Window(width=800, height=600, caption="Emoji Center")

# List of emoji images
# Add your emoji image filenames here
emoji_images = ['emoji1.png', 'emoji2.png', 'emoji3.png']
emoji_sprites = [pyglet.sprite.Sprite(
    pyglet.resource.image(img)) for img in emoji_images]

# Current emoji index
current_index = 0


def update_emoji(dt):
    global current_index
    current_index = (current_index + 1) % len(emoji_sprites)


@window.event
def on_draw():
    window.clear()
    current_sprite = emoji_sprites[current_index]
    # Calculate the center position
    current_sprite.x = window.width // 2 - current_sprite.width // 2
    current_sprite.y = window.height // 2 - current_sprite.height // 2
    current_sprite.draw()


# Schedule the update_emoji function to be called every second
clock.schedule_interval(update_emoji, 1.0)

# Run the application
pyglet.app.run()
