from abc import ABCMeta
from .command import Command

class DefaultConfig:
	description = None


class ProgramMeta(ABCMeta):
	def __new__(cls, name: str, bases: tuple, attrs: dict, **kw):
		super_new = super().__new__
		commands = []
		
		# Get the commands if exist in the attributes
		for attr in attrs.values():
			if isinstance(attr, Command):
				commands.append(attr)
		default_meta_class = DefaultMeta

		for base in bases:
			# accumulate all the commands from the base classes
			commands += base._meta.commands
			if hasattr(base, "Meta"):
				default_meta_class = getattr(base, "Meta")
				break
		meta_class = attrs.pop("Meta", default_meta_class)
		meta_attr = meta_class()
	
		meta_attr.commands = commands
		if not hasattr(meta_attr, "name"):
			setattr(meta_attr, "name", name)
			attrs["_meta"] = meta_attr

		return super_new(cls, name, bases, attrs, **kw)



class Program(metaclass=ProgramMeta):
	def __getitem__(self, __k):
		return getattr(self._meta, __k)
