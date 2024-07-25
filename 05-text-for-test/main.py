import pyglet
from pyglet import clock
from pyglet.window import key

# Create a window
window = pyglet.window.Window(width=800, height=600, caption="Emoji Center")

# List of emojis as text
emoji_texts = [':)', ':(', 'o_O', ':|', '><>', ':‑)',
               'Alex', ]  # Add your desired emojis here

# Current emoji index
current_index = 0

toggle = False
# Create a label for the emoji
emoji_label = pyglet.text.Label(
    emoji_texts[current_index],
    font_name='Arial',
    font_size=64,
    x=window.width // 2,
    y=window.height // 2,
    anchor_x='center',
    anchor_y='center'
)


def update_emoji(dt):
    global current_index, emoji_label, toggle
    if toggle == True:
        return
    current_index = (current_index + 1) % len(emoji_texts)
    emoji_label.text = emoji_texts[current_index]


@window.event
def on_draw():
    window.clear()
    emoji_label.draw()


@window.event
def on_key_press(symbol, modifiers):
    global toggle
    if symbol == key.S:  # Press 'S' to stop/start updates
        toggle = not toggle
    print("toggle is ", toggle)


# Schedule the update_emoji function to be called every second
clock.schedule_interval(update_emoji, 1)

# Run the application
pyglet.app.run()
