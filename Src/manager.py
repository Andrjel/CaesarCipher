import os
from src.cipher import Cipher
from src.submain import Buffer, SingleSession
from src.file_handler import FileHandler


class Manager:
    """Class for managing caesar cipher application."""

    def __init__(self):
        """Constructor"""
        self.__buffer = Buffer()
        self.__file_handler = FileHandler()
        self.__is_running = True
        self.__menu_choices = {
            "1": self.encrypt,
            "2": self.decrypt,
            "3": self.show_result,
            "4": self.save_buffer,
            "5": self.load_buffer,
            "6": self.__buffer.clear_buffer,
            "7": self.exit,
        }
        self.menu_loop()

    def menu_loop(self) -> None:
        """Menu loop"""
        while self.__is_running:
            os.system("cls")
            self.show_menu()
            if choice := self.get_user_choice():
                self.__menu_choices.get(choice, self.show_error)()

    def show_menu(self) -> None:
        """Printing menu"""
        menu = """
    1. Encrypt Text
    2. Decrypt Text
    3. Show Result
    4. Save to File
    5. Load from File
    6. Clear buffer
    7. Exit
        """
        print(menu)

    def get_user_choice(self) -> str:
        """Getting user choice"""
        return input("Enter your choice: ")

    def show_error(self) -> None:
        print("Wrong choice!")

    def encrypt(self) -> None:
        os.system("cls")
        text = input("Enter text to encrypt: ")
        encrypted_text = Cipher.encrypt(text)
        self.__buffer.add_to_buffer(SingleSession(text, encrypted_text, "encrypt"))
        print("Text encrypted successfully!")

    def decrypt(self) -> None:
        os.system("cls")
        text = input("Enter text to decrypt: ")
        decrypted_text = Cipher.decrypt(text)
        self.__buffer.add_to_buffer(SingleSession(text, decrypted_text, "decrypt"))
        print("Text decrypted successfully!")

    def save_buffer(self) -> None:
        os.system("cls")
        file_path = input("Enter file path: ")
        self.__file_handler.write_to_file(file_path, self.__buffer.get_buffer_data())
        print("Buffer saved successfully!")

    def load_buffer(self) -> None:
        os.system("cls")
        file_path = input("Enter file path: ")
        self.__buffer.clear_buffer()
        data = self.__file_handler.read_from_file(file_path)
        if data:
            for session in data["data"]:
                text_before = session["text_before_operation"]
                text_after = session["text_after_operation"]
                operation = session["operation"]
                session_time_stamp = session["session_time_stamp"]
                self.__buffer.add_to_buffer(
                    SingleSession(
                        text_before, text_after, operation, session_time_stamp
                    )
                )
        else:
            print("Buffer is empty!")
            return
        print("Buffer loaded successfully!")

    def show_result(self) -> None:
        print(self.__buffer)

    def exit(self) -> None:
        if self.__buffer.get_buffer_data():
            user_choice = input("Do you want to save your data? (y/n): ")
            if user_choice == "y":
                self.save_buffer()
        self.__is_running = False
        print("Goodbye!")
