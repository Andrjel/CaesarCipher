import os


class Manager:
    """Class for managing caesar cipher application."""

    #  TODO: Make logger class
    def __init__(self):
        self.__menu_choices = {
            # TODO: Make Encrypt and Decrypt class
            "1": self.encrypt_submenu,
            "2": self.decrypt_submenu,
            # TODO: Make ShowResult method
            "3": "self.show_result",
            # TODO: Make Save and Load class, and make buffer
            "4": "self.save_buffer",
            "5": "self.load_buffer",
            "6": "self.exit",
        }
        self.__encrypt_submenu_choices = {
            "1": "self.encrypt_string",
            "2": "self.encrypt_from_file",
            "3": None,
        }
        self.__decrypt_submenu_choices = {
            "1": "self.decrypt_string",
            "2": "self.decrypt_from_file",
            "3": None,
        }
        self.menu_loop()

    def menu_loop(self) -> None:
        """Menu loop"""
        while True:
            os.system("cls")
            self.show_menu()
            if choice := self.get_user_choice(self.__menu_choices):
                self.__menu_choices[choice]()

    def show_menu(self) -> None:
        """Printing menu"""
        menu = """
    1. Encrypt
    2. Decrypt
    3. Show result
    4. Save buffer
    5. Load buffer
    6. Exit
        """
        print(menu)

    def encrypt_submenu(self) -> None:
        """Encrypt submenu"""
        while True:
            os.system("cls")
            self.encrypt_menu()
            if choice := self.get_user_choice(self.__encrypt_submenu_choices):
                if choice == "3":
                    break
                self.__encrypt_submenu_choices[choice]()

    def encrypt_menu(self) -> None:
        """Printing encrypt menu"""
        menu = """
    1. Encrypt string,
    2. Encrypt from file,
    3. Exit
        """
        print(menu)

    def decrypt_submenu(self) -> None:
        """Decrypt submenu"""
        while True:
            os.system("cls")
            self.decrypt_menu()
            if choice := self.get_user_choice(self.__decrypt_submenu_choices):
                if choice == "3":
                    break
                self.__decrypt_submenu_choices[choice]()

    def decrypt_menu(self) -> None:
        """Printing decrypt menu"""
        menu = """
    1. Decrypt string,
    2. Decrypt from file,
    3. Exit
        """
        print(menu)

    def get_user_choice(self, certain_menu: dict) -> int:
        """Getting user choice"""
        choice = input("Enter your choice: ")
        if choice in certain_menu.keys():
            return choice
        else:
            print("Wrong choice!")
            return None
