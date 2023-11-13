class Cipher:
    @staticmethod
    def encrypt(text: str) -> str:
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                encrypted_char = chr(
                    (ord(char) + 13 - ascii_offset) % 26 + ascii_offset
                )
            else:
                encrypted_char = char
            encrypted_text += encrypted_char
        return encrypted_text

    @staticmethod
    def decrypt(encrypted_text: str) -> str:
        decrypted_text = ""
        for char in encrypted_text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                decrypted_char = chr(
                    (ord(char) - 13 - ascii_offset) % 26 + ascii_offset
                )
            else:
                decrypted_char = char
            decrypted_text += decrypted_char
        return decrypted_text
