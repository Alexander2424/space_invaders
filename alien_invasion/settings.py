class Settings():
	"""A class to store all settings for alien invsasion."""

	def __init__(self):
		"""Initialise the game's static settings."""

		# Screen settings:
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_colour = (0, 0, 0)

		# Ship settings
		self.ship_limit = 2

		# Bullet settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_colour = 200, 200, 200
		self.bullets_allowed = 3
		
		#Alien settings
		self.fleet_drop_speed = 20

		# How quickly the game speeds up
		self.speedup_scale = 1.4
		# How quickly the alien point values increase
		self.score_scale = 1.5

		self.initialise_dynamic_settings()

	def initialise_dynamic_settings(self):
		"""Initialise settings that change throughout the game."""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1

		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		# Scoring.
		self.alien_points = 50

	def increase_speed(self):
		"""Increase speed settings and alien point values."""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)


