import pytest

from src.cipher import Cipher


@pytest.mark.parametrize(
    "text, expected_result",
    [
        ("xyz", "klm"),
        ("XYZ", "KLM"),
        ("abc", "nop"),
        ("123", "123"),
        ("abc", "nop"),
        ("", ""),
        ("ążźśćół", "ążźśćół"),
        ("./,;!@#$%", "./,;!@#$%"),
    ],
)
def test_encrypt_should_correct_text_for_letters_from_the_end_of_alphabet(
    text, expected_result
):
    actual_result = Cipher.encrypt(text)

    assert expected_result == actual_result
