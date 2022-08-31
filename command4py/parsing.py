import inspect
from argparse import ArgumentParser

from .utils import *

def get_parser(program):
	kwargs = {
		"description" : program["description"]
	}
	kwargs = eliminate_none_items(kwargs)
	parser = ArgumentParser(**kwargs)
	subparsers = parser.add_subparsers(title="Commands", description="List of available commands", dest="command_name")

	for command in program["commands"]:
		# Creating the command parser
		kwargs = {
			"help" : command.description,
		}
		kwargs = eliminate_none_items(kwargs)
		command_parser = subparsers.add_parser(command.name, **kwargs)
		
		# Getting the configuration and adding it to the command parser
		used_shorthands = []
		parameters = inspect.signature(command.callback).parameters

		for i, parameter in enumerate(parameters.values()):
			# Just skip the first parameter because it's usually self
			if i == 0:
				continue

			names = [parameter.name]
			configs = {}


			# Checking if the arguments is optional or required
			if parameter.default != inspect._empty:
				configs["metavar"] = ""
				names[0] = "--" + parameter.name
				shorthand = names[0][0]
				if shorthand not in used_shorthands:
					names.append("-" + parameter.name[0])
				configs["default"] = parameter.default

				# Checking if the parameter has help
				if command.help and parameter.name in command.help:
					configs["help"] = command.help[parameter.name]

			# ToDo: Add the type conversion feature by checking the annotations and add it to the configs
			command_parser.add_argument(*names, **configs)
	return parser
