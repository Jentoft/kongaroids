import pyglet
from pyglet.window import key
from pong_kong import Kong
from paddle import Paddle

aScore = 0
bScore = 0

window = pyglet.window.Window()
kong_image = pyglet.resource.image('King-Kong-psd24860.png')
paddle_image = pyglet.resource.image('empire_state_building.jpg')

key_states = key.KeyStateHandler()
window.push_handlers(key_states)

kong = Kong(window, key_states, kong_image)
paddleA = Paddle(window, key_states, paddle_image, 'A')
paddleB = Paddle(window, key_states, paddle_image, 'B')

def a_collision_detected():
	return (kong.kong_sprite.x <= paddleA.image.width) and ((paddleA.paddle_sprite.y <= (kong.kong_sprite.y + kong.kong_sprite.height)) and ((paddleA.paddle_sprite.y + paddleA.image.height) >= kong.kong_sprite.y))

def b_collision_detected():
	return ((kong.kong_sprite.x + kong.kong_sprite.width) >= (paddleB.paddle_sprite.x)) and ((paddleB.paddle_sprite.y <= (kong.kong_sprite.y + kong.kong_sprite.height)) and ((paddleB.paddle_sprite.y + paddleB.image.height) >= kong.kong_sprite.y))

def wall_collision_detected():
	return (kong.kong_sprite.x <= 0) or ((kong.kong_sprite.x + kong.kong_sprite.width) >= (window.width - 20))

def handle_collisions():
	global aScore
	global bScore
	if a_collision_detected():
		kong.dx *= -1
		kong.kong_sprite.x = 2 * paddleA.image.width - kong.kong_sprite.x
	elif b_collision_detected():
		kong.dx *= -1
		kong.kong_sprite.x = 2 * paddleB.paddle_sprite.x - 2*kong.kong_sprite.width - kong.kong_sprite.x
	elif wall_collision_detected():
		if kong.kong_sprite.x <= 0:
			bScore += 1
		else:
			aScore += 1
		print("A: {}     B: {}".format(aScore, bScore))
		kong.reset()
	else:
		return []

@window.event
def on_draw():
	window.clear()
	paddleA.draw()
	paddleB.draw()
	kong.draw()

def update(dt):
	a_position = paddleA.update()
	b_position = paddleB.update()
	kong.update(dt, a_position, b_position)
	handle_collisions()

pyglet.clock.schedule_interval(update, 1/160)
pyglet.app.run()