class Command:
	# description describe the command
	# help describe the arguments that's received
	def __init__(self, callback, description = None, help = None):
		self.name = self.refine_name(callback.__name__)
		self.callback = callback
		self.description = description
		self.help = {} if help == None else help

	def refine_name(self, name: str):
		name = name.replace("_", "-")
		name = name.lower()
		return name

	@classmethod
	def create_command(cls, *a, **kw):
		def _command(callback):
			return cls(callback, *a, **kw)
		return _command

	def __call__(self, *args, **kwargs):
		return self.callback(*args, **kwargs)

command = Command.create_command