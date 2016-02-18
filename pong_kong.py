import pyglet
from pyglet.window import key

class Kong:

	SPEED = 200

	def __init__(self, window, key_states, image):
		self.window = window
		self.key_states = key_states
		self.kong_sprite = pyglet.sprite.Sprite(image, x = (self.window.width/2 -50), y = (self.window.height/2 - 50))
		self.kong_sprite.scale = 100/self.kong_sprite.width
		self.dx = 150
		self.dy = 150

	def draw(self):
		self.kong_sprite.draw()

	def update(self, dt, a_position, b_position):
		self.kong_sprite.x += self.dx * dt
		self.kong_sprite.y += self.dy * dt

		min_y = 0
		max_y = self.window.height - self.kong_sprite.height
		min_x = 0
		max_x = self.window.width - self.kong_sprite.width - 20

		if self.kong_sprite.y < min_y:
			self.dy *= -1
			self.kong_sprite.y *=-1
		if self.kong_sprite.y > max_y:
			self.kong_sprite.y = 2 * max_y - self.kong_sprite.y
			self.dy *= -1
		# if self.kong_sprite.x < min_x:
		# 	self.kong_sprite.x *= -1
		# 	self.dx *= -1
		# if self.kong_sprite.x > max_x:
		# 	self.kong_sprite.x = 2*max_x - self.kong_sprite.x
		# 	self.dx *= -1