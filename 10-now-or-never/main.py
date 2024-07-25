import pyglet
from pyglet.window import key
from random import random
# Create a window
window = pyglet.window.Window(width=800, height=600, caption="Emoji Center")
# Load emoji as a sprite
# Add your emoji image filenames here
heart = pyglet.sprite.Sprite(pyglet.resource.image('heart.png'))
emoji_images = ['up.png', 'down.png', 'left.png', 'right.png']
emoji_sprites = [pyglet.sprite.Sprite(
    pyglet.resource.image(img)) for img in emoji_images]
current_index = 0
emoji_sprite = emoji_sprites[current_index]
X = window.width // 2 - emoji_sprite.width // 2
Y = window.height // 2 - emoji_sprite.height // 2
####
delta = 10
global_symbol = None
game_over_label = pyglet.text.Label(
    'GAME OVER',
    font_name='Arial',
    font_size=64,
    color=(255, 0, 0, 255),
    x=window.width // 2,
    y=window.height // 2,
    anchor_x='center',
    anchor_y='center'
)

game_win_label = pyglet.text.Label(
    'You Won!',
    font_name='Arial',
    font_size=64,
    color=(0, 255, 0, 255),
    x=window.width // 2,
    y=window.height // 2,
    anchor_x='center',
    anchor_y='center'
)


def restart():
    for spider in spiders:
        spider.x = random()*window.width
        spider.y = random()*window.height
        spider.scale = 2
        # spider.rotation = random()*180
    heart.x = random()*window.width
    heart.y = random()*window.height
    heart.scale = 1.1
    # heart.rotation = random()*180


spiders = [pyglet.sprite.Sprite(
    pyglet.resource.image(img)) for img in ['spider.png']*5]
restart()


@window.event
def on_draw():
    global X, Y, emoji_sprite, game_win_label, game_over_label, global_symbol
    window.clear()
    emoji_sprite.x = X
    emoji_sprite.y = Y
    emoji_sprite.draw()
    for spider in spiders:
        spider.draw()

    heart.draw()

    threshold = 20
    if global_symbol == key.S:  # Down
        emoji_sprite = emoji_sprites[1]
        Y = Y-delta

    if global_symbol == key.W:  # Up
        emoji_sprite = emoji_sprites[0]
        Y = Y+delta

    if global_symbol == key.D:  # Right
        emoji_sprite = emoji_sprites[3]
        X = X+delta

    if global_symbol == key.A:  # Left
        emoji_sprite = emoji_sprites[2]
        X = X-delta
    # print('X: ', emoji_sprite.x, heart.x, abs(emoji_sprite.x-heart.x))
    # print('Y: ', emoji_sprite.y, heart.y, abs(emoji_sprite.y-heart.y))
    if abs(emoji_sprite.x-heart.x) < threshold and abs(emoji_sprite.y-heart.y) < threshold:
        game_win_label.draw()
    for spider in spiders:
        if abs(emoji_sprite.x-spider.x) < threshold and abs(emoji_sprite.y-spider.y) < threshold:
            game_over_label.draw()


def heart_beat(dt):
    if (heart.scale == 1.0):
        heart.scale = 1.1
    else:
        heart.scale = 1.0


key_states = key.KeyStateHandler()
window.push_handlers(key_states)


@window.event
def on_key_press(symbol, modifiers):
    global global_symbol
    print('key pressed:', symbol)
    global X, Y, emoji_sprite
    global_symbol = symbol
    if symbol == key.R:  # restart
        restart()
    if symbol == key.Q:  # Press 'Q' to quit the application
        pyglet.app.exit()


@window.event
def on_key_release(symbol, modifiers):
    global global_symbol
    global_symbol = None
    pass  # Can be used for additional logic when keys are released


pyglet.clock.schedule_interval(heart_beat, 1/10)
# Run the application
pyglet.app.run()
