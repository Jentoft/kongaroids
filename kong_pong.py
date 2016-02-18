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
paddleA = Paddle(window, key_states, paddle_image, 'A')
paddleB = Paddle(window, key_states, paddle_image, 'B')

def a_collision_detected():
	if (kong.kong_sprite.x <= paddleA.image.width) and ((paddleA.paddle_sprite.y <= (kong.kong_sprite.y + kong.kong_sprite.height)) and ((paddleA.paddle_sprite.y + paddleA.image.height) >= kong.kong_sprite.y)):
		print("collided with paddle A")
		return True
	return False

def b_collision_detected():
		if ((kong.kong_sprite.x + kong.kong_sprite.width) >= (window.width - paddleB.image.width)) and ((paddleB.paddle_sprite.y <= (kong.kong_sprite.y + kong.kong_sprite.height)) and ((paddleB.paddle_sprite.y + paddleB.image.height) >= kong.kong_sprite.y)):
			print("collided with paddle B")
			return True
		return False


def detect_collisions(objects):
	if a_collision_detected():
		return [objects[0], objects[2]]
	elif b_collision_detected():
		return [objects[1], objects[2]]
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
	detect_collisions([paddleA, paddleB, kong])

pyglet.clock.schedule_interval(update, 1/120)
pyglet.app.run()