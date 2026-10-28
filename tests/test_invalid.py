import re

import pytest

from ipv4_conversions import binary_to_ipv4, ipv4_to_binary


@pytest.mark.parametrize(
    "invalid, expected_in_message",
    [
        ("", "empty"),
        ("192.168.1", "four decimal octets"),
        ("192.168.1.256", "outside the range 0-255"),
        ("192.168.a.1", "not a decimal octet"),
        ("192..1.1", "not a decimal octet"),
    ],
)
def test_ipv4_to_binary_invalid_input(invalid, expected_in_message):
    with pytest.raises(ValueError, match=re.escape(expected_in_message)):
        ipv4_to_binary(invalid)


@pytest.mark.parametrize(
    "invalid, expected_in_message",
    [
        ("", "empty"),
        ("11000000.10101000.00000001", "four 8-bit binary octets"),
        ("1100000.10101000.00000001.00000001", "exactly 8 bits"),
        ("11000000.10101000.0000000a.00000001", "invalid character"),
    ],
)
def test_binary_to_ipv4_invalid_input(invalid, expected_in_message):
    with pytest.raises(ValueError, match=re.escape(expected_in_message)):
        binary_to_ipv4(invalid)
