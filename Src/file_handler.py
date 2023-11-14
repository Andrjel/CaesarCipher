import json


class FileHandler:
    @staticmethod
    def read_from_file(file_path: str) -> str:
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"File {file_path} not found!")

    @staticmethod
    def write_to_file(file_path: str, data: str) -> None:
        _data = {"data": data}
        with open(file_path, "w") as file:
            json.dump(_data, file, indent=4)

    @staticmethod
    def append_to_file(file_path: str, data: str) -> None:
        loaded_data = FileHandler.read_from_file(file_path)
        new_data = loaded_data["data"] + data
        FileHandler.write_to_file(file_path, new_data)

    @staticmethod
    def clear_file(file_path: str) -> None:
        with open(file_path, "w") as file:
            json.dump({"data": ""}, file, indent=4)
