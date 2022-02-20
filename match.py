#! /usr/bin/python3.10
from __future__ import annotations
from typing import List
from dataclasses import dataclass 

import shlex

def run_command(command: str) -> None:
	match command:
		case "quit":
			print("quiting program")
			quit()
		case "reset":
			print("reseting the system")
		case other:
			print(f"Unknown command {command!r}")

def run_command_v2(command: str) -> None:
	match command.split():
		case ["load", filename]:
			print(f"Loading the file: {filename}")
		case ["save", filename]:
			print(f"Saving the file: {filename}")
		case ["quit"|"exit"|"bye", *rest] if "--force" or "-f" in rest:
			print(" Force SIGTERM quiting")
			quit()
		case ["quit"|"exit"|"bye"]:
			print("Quiting")
			quit()
		case _:
			print(f"Unknown command {command!r}")

def run_command_v3(command: Command) -> None:
	match command:
		case Command(command="load", arguments=[filename]):
			print(f"Loading the file: {filename}")
		case Command(command="save", arguments=[filename]):
			print(f"Saving the file: {filename}")

		# caveats of match: Order matters
		# so the first match will be executed first
		case Command(command="quit"|"exit"|"bye", arguments=["--force" |"-f", *rest]):
			print(" Force SIGTERM quiting")
			quit()
		case Command(command="quit"|"exit"|"bye"):
			print("Quiting")
			quit()
		
		case _:
			print(f"Unknown command {command!r}")

@dataclass
class Command():
	"""Commands to be executed"""
	command: str
	arguments: List[str]

def main() -> None:
	"""Main function """

	while True:
		# command = input("$ ")
		# run_command(command)
		# run_command_v2(command)

		command, *arguments = shlex.split(input("$ "))
		run_command_v3(Command(command=command, arguments=arguments))


if __name__ == '__main__':
	main()
