# Build automation with python

from abc import abstractmethod
from command4py import Program, command, run
import shutil
from os import mkdir, listdir, system
from pathlib import Path


class Project(Program):

	ROOT = Path.cwd()
	SRCDIR = ROOT / "src"
	OUTDIR = ROOT / "bin"

	def prompt(self, command):
		system(command)

	@command(description="Creating a new project and delete the old one if exist in the same directory")
	def init(self):
		dependency_directories = [self.SRCDIR, self.OUTDIR]
		list_directories = [self.ROOT / x for x in listdir(self.ROOT)]

		print("This command will remake the following directories if exist")
		for dd in dependency_directories:
			print(dd)
		if input("Are you sure? [Y|N] ").lower() in ["n", "n"]:
			return

		for dd in dependency_directories:
			if dd in list_directories:
				shutil.rmtree(dd)
			mkdir(dd)

		print("Project created")

	@command(description="Build your source codes")
	def build(self):
		return self.on_build()

	@abstractmethod
	def on_build(self):
		pass

	@command(description="Clear the build directories")
	def clear(self):
		shutil.rmtree(self.OUTDIR)
		mkdir(self.OUTDIR)

	@command(description="Run the built application")
	def run(self):
		self.on_run()

	@abstractmethod
	def on_run(self):
		pass
