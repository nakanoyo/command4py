import inspect
from .program import ProgramMeta
from .parsing import get_parser

def run(prog_class: ProgramMeta):
	prog = prog_class()
	parser = get_parser(prog)
	args = parser.parse_args()
	if not args.command_name:
		return
	command = getattr(prog, args.command_name)
	
	kw = {}
	for i, parameter in enumerate(inspect.signature(command.callback).parameters.values()):
		if hasattr(args, parameter.name):
			kw[parameter.name] = getattr(args, parameter.name)
	command(prog, **kw)
