import pyglet
from pyglet.window import key

class Paddle:
	SPEED = 5

	def __init__(self, window, key_states, image, identifier):
		self.window = window
		self.key_states = key_states
		self.identifier = identifier
		self.image = image
		self.image.height = 100
		self.image.width = 20
		if identifier == 'A':
			position_x = 0;
		else:
			position_x = self.window.width - 20
		self.paddle_sprite = pyglet.sprite.Sprite(image, x = position_x, y = (self.window.height/2 - 50))

	def draw(self):
		self.paddle_sprite.draw()

	def update(self):
		if self.identifier == 'A':
			if self.key_states[key.UP]:
				self.paddle_sprite.y += self.SPEED
			if self.key_states[key.DOWN]:
				self.paddle_sprite.y -= self.SPEED
		else:
			if self.key_states[key.A]:
				self.paddle_sprite.y += self.SPEED
			if self.key_states[key.D]:
				self.paddle_sprite.y -= self.SPEED

		y_min = 0
		y_max = self.window.height - self.paddle_sprite.height

		if self.paddle_sprite.y < y_min:
			self.paddle_sprite.y = y_min
		if self.paddle_sprite.y > y_max:
			self.paddle_sprite.y = y_max

		return self.paddle_sprite.y