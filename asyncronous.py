#! /usr/bin/env python3
import asyncio
from typing import Protocol, Any, Awaitable
from enum import Enum, auto
from dataclasses import dataclass

class Message_Type(Enum):
	SWITCH_ON = auto()
	SWITCH_OFF = auto()
	CHANGE_COLOR = auto()

@dataclass
class Message:
	msg_type: Message_Type
	data: str = ''

class Device(Protocol):
	async def connect(self) -> None:
		...
	async def disconnect(self) -> None:
		...
	async def send_message(self) -> None:
		...

class Bulb_Ligth_Device:
	async def connect(self) -> None:
		await asyncio.sleep(0.5)
		print("The device is connected")
	async def disconnect(self) -> None:
		await asyncio.sleep(0.5)
		print("The device is disconnected")
	async def send_message(self, msg: Message) -> None:
		await asyncio.sleep(0.5)
		print("The device is sending {msg}")

class Smart_Device:
	async def connect(self) -> None:
		await asyncio.sleep(0.5)
		print("The device is connected")
	async def disconnect(self) -> None:
		await asyncio.sleep(0.5)
		print("The device is disconnected")
	async def send_message(self, msg: Message) -> None:
		await asyncio.sleep(0.5)
		print("The device is sending {msg}")

async def run_sequence(*functions: Awaitable[Any]) -> None:
	for function in functions:
		await function

async def run_parallel(*functions: Awaitable[Any]) -> None:
	await asyncio.gather(*functions)

async def main() -> None:
	"""The main function"""
	
	print("==== Program running ====")
	smart_light = Smart_Device()
	bulb_light = Bulb_Ligth_Device()

	# await smart_light.connect()
	# await smart_light.send_message(Message(msg_type=Message_Type.SWITCH_ON))
	# await smart_light.disconnect()

	await run_sequence(
		run_parallel(
			smart_light.connect(),
			bulb_light.connect()
		),
		run_parallel(
			smart_light.send_message(Message(msg_type=Message_Type.SWITCH_ON)),
			bulb_light.send_message(Message(msg_type=Message_Type.SWITCH_ON))
		),
		run_parallel(
			smart_light.disconnect(),
			bulb_light.disconnect()
		)	
	)
	print("==== Program finished ====")

if __name__ == "__main__":
	asyncio.run(main())
