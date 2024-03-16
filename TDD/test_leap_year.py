"""Test cases for the leap year function."""

# Standard library

# 3rd party library
import pytest

# Project library
from main.leap_year import is_leap_year


# ----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "year, expected",
    [
        (2000, True),      # Case 1: Divisible by 400
        (2020, True),      # Case 2: Divisible by 4 but not by 100
        (1900, False),     # Case 3: Divisible by 100 but not by 400
        (2021, False),     # Case 4: Not divisible by 4
    ]
)
def test_is_leap_year(year, expected):
    """Check if the given year is a leap year."""
    # Arrange
    # Act
    result = is_leap_year(year)

    # Assert
    assert result == expected
