# An example of command use case

from command import Program, command, run


class MyProgram(Program):
	@command()
	def echo():
		pass
