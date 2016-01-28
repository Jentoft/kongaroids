import pyglet
from pyglet.window import key

class Kong:

	SPEED = 200

	def __init__(self, window, key_states, image):
		self.window = window
		self.key_states = key_states
		self.kong_sprite = pyglet.sprite.Sprite(image, x = 50, y = 50)
		self.kong_sprite.scale = 100/self.kong_sprite.width
		self.dx = 100
		self.dy = 100

	def draw(self):
		self.kong_sprite.draw()

	def update(self, dt):
		self.kong_sprite.x += self.dx * dt
		self.kong_sprite.y += self.dy * dt

		self.dx *= 0.99
		self.dy *= 0.99

		if self.key_states[key.UP]:
			self.dy += self.SPEED*dt
		if self.key_states[key.DOWN]:
			self.dy -= self.SPEED*dt
		if self.key_states[key.LEFT]:
			self.dx -= self.SPEED*dt
		if self.key_states[key.RIGHT]:
			self.dx += self.SPEED*dt

		min_y = 0
		max_y = self.window.height - self.kong_sprite.height
		min_x = 0
		max_x = self.window.width - self.kong_sprite.width

		if self.kong_sprite.y < min_y:
			self.kong_sprite.y = min_y
			self.dy *= -1
		if self.kong_sprite.y > max_y:
			self.kong_sprite.y = max_y
			self.dy *= -1
		if self.kong_sprite.x < min_x:
			self.kong_sprite.x = min_x
			self.dx *= -1
		if self.kong_sprite.x > max_x:
			self.kong_sprite.x = max_x
			self.dx *= -1