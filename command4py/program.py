from .command import Command

class DefaultConfig:
	description = None


class ProgramMeta(type):
	def __new__(cls, name: str, bases: tuple, attrs: dict, **kw):
		super_new = super().__new__
		commands = []
		for _, attr in attrs.items():
			if isinstance(attr, Command):
				commands.append(attr)

		config_class = attrs.pop("Config", DefaultConfig)
		config = config_class()
	
		config.commands = commands
		if not hasattr(config, "name"):
			setattr(config, "name", name)
			attrs["_config"] = config

		return super_new(cls, name, bases, attrs, **kw)


class Program(metaclass=ProgramMeta):
	def __getitem__(self, __k):
		return getattr(self._config, __k)