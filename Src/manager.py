import os


class Manager:
    """Class for managing caesar cipher application."""

    def __init__(self):
        self.__is_running = True
        self.__menu_choices = {
            "1": "self.encrypt",
            "2": "self.decrypt",
            "3": "self.show_result",
            "4": "self.save_buffer",
            "5": "self.load_buffer",
            "6": "clear buffer",
            "7": "self.exit",
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

    def get_user_choice(self) -> int:
        """Getting user choice"""
        return input("Enter your choice: ")

    def show_error(self):
        print("Wrong choice!")
