# An example of command use case

from command4py import Program, command, run


class MyProgram(Program):
	@command()
	def echo(self, value: str, end = "\n"):
		print(value, end="\n")

run(MyProgram)
