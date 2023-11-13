from dataclasses import dataclass, asdict
from typing import List
from datetime import datetime


@dataclass
class SingleSession:
    encrypted_data: str
    decrypted_data: str
    operation: str
    session_time_stamp: datetime = datetime.now().strftime("%Y%m%d%H%M%S")

    def get_data_for_buffer(self) -> dict:
        return asdict(self)


class Buffer:
    def __init__(self):
        self.__buffer: List[SingleSession] = []

    def add_to_buffer(self, data: SingleSession) -> None:
        self.__buffer.append(data.get_data_for_buffer())

    def __str__(self):
        return str(self.__buffer)
