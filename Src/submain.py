from dataclasses import dataclass, asdict
from typing import List
from datetime import datetime


@dataclass
class SingleSession:
    text_before_operation: str
    text_after_operation: str
    operation: str
    session_time_stamp: datetime = datetime.now().strftime("%Y/%m/%d_%H:%M:%S")

    def get_data_for_buffer(self) -> dict:
        return asdict(self)


class Buffer:
    def __init__(self):
        self.__buffer: List[SingleSession] = []

    def add_to_buffer(self, data: SingleSession) -> None:
        self.__buffer.append(data.get_data_for_buffer())

    def clear_buffer(self) -> None:
        self.__buffer.clear()

    def get_buffer_data(self) -> List[SingleSession]:
        return self.__buffer

    def __str__(self):
        returned_string = ""
        for data in self.__buffer:
            for k, v in data.items():
                returned_string += f"{k}: {v}\n"
            returned_string += "\n"
        return returned_string
