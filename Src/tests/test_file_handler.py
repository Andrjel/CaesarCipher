import unittest
import json
from src.file_handler import FileHandler


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.txt"

    def tearDown(self):
        # Usunięcie pliku po zakończeniu testów
        try:
            with open(self.file_path, "r"):
                pass
            # Plik istnieje, usuwamy go
            FileHandler.clear_file(self.file_path)
        except FileNotFoundError:
            pass

    def test_read_from_file(self):
        # Tworzymy sztuczne dane do zapisania w pliku
        test_data = {"data": "test"}
        with open(self.file_path, "w") as file:
            json.dump(test_data, file, indent=4)

        # Testujemy czy dane odczytane z pliku są poprawne
        result = FileHandler.read_from_file(self.file_path)
        self.assertEqual(result, test_data)

    def test_read_from_nonexistent_file(self):
        # Testujemy sytuację, gdy plik nie istnieje
        with self.assertRaises(FileNotFoundError):
            FileHandler.read_from_file("nonexistent_file.txt")

    def test_write_to_file(self):
        # Tworzymy sztuczne dane do zapisania w pliku
        test_data = "test"
        expected_data = {"data": test_data}

        # Testujemy czy dane zapisane do pliku są poprawne
        FileHandler.write_to_file(self.file_path, test_data)
        with open(self.file_path, "r") as file:
            result = json.load(file)
        self.assertEqual(result, expected_data)

    def test_append_to_file(self):
        # Tworzymy sztuczne dane do zapisania w pliku
        initial_data = {"data": "initial"}
        with open(self.file_path, "w") as file:
            json.dump(initial_data, file, indent=4)

        # Testujemy czy dane dołączone do pliku są poprawne
        additional_data = " additional"
        expected_data = {"data": "initial additional"}
        FileHandler.append_to_file(self.file_path, additional_data)
        with open(self.file_path, "r") as file:
            result = json.load(file)
        self.assertEqual(result, expected_data)

    def test_clear_file(self):
        # Tworzymy sztuczne dane do zapisania w pliku
        test_data = {"data": "test"}
        with open(self.file_path, "w") as file:
            json.dump(test_data, file, indent=4)

        # Testujemy czy plik zostaje wyczyszczony
        FileHandler.clear_file(self.file_path)
        with open(self.file_path, "r") as file:
            result = json.load(file)
        self.assertEqual(result, {"data": ""})


if __name__ == "__main__":
    unittest.main()
