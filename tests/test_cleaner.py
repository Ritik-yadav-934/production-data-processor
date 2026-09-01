from src.cleaner import (
    clean_text,
    clean_number
)


def test_clean_text():

    result = clean_text(
        "   Spice Hub   "
    )

    assert result == "Spice Hub"


def test_clean_number():

    result = clean_number("254")

    assert result == 254.0


def test_invalid_number():

    result = clean_number("abc")

    assert result is None