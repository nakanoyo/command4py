from command4py import Program, command, run


class MyProgram(Program):
	@command()
	# value is a positional argument so you just need to pass it
	# end is an optional argument an will be translated as --end or -e in the command line
	def echo(self, value: str, end = "\n"):
		print(value, end=end)

run(MyProgram)
