import pyglet
from pyglet.window import key

class Paddle:
	def __init__(self, window, key_states, image, identifier):
		self.window = window
		self.key_states = key_states
		if identifier == 'A':
			position_x = 0;
		else:
			position_x = self.window.width - 20
		self.paddle_sprite = pyglet.sprite.Sprite(image, x = position_x, y = (self.window.height/2 - 50))
		self.paddle_sprite.scale = 20/self.paddle_sprite.width

	def draw(self):
		self.paddle_sprite.draw()