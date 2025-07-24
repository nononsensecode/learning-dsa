import pytest

from src.two_pointer.compress import compress, compress_two_pointer


@pytest.mark.parametrize(
    "s, expected",
    [
        ("ccaaatsss", "2c3at3s"),
        ("ssssbbz", "4s2bz"),
        ("ppoppppp", "2po5p"),
        ("nnneeeeeeeeeeeezz", "3n12e2z"),
        (
            "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",
            "127y",
        ),
    ],
)
def test_compress(s: str, expected: str):
    assert compress(s) == expected
    assert compress_two_pointer(s) == expected
