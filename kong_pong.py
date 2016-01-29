import pyglet
from pyglet.window import key
from pong_kong import Kong
from paddle import Paddle

window = pyglet.window.Window()
kong_image = pyglet.resource.image('King-Kong-psd24860.png')
paddle_image = pyglet.resource.image('empire_state_building.jpg')

key_states = key.KeyStateHandler()
window.push_handlers(key_states)

kong = Kong(window, key_states, kong_image)
paddleA = Paddle(window, key_states, paddle_image)

@window.event
def on_draw():
	window.clear()
	kong.draw()

def update(dt):
	kong.update(dt)

pyglet.clock.schedule_interval(update, 1/120)
pyglet.app.run()