import pytest

from ipv4_conversions import binary_to_ipv4, ipv4_to_binary


@pytest.mark.parametrize(
    "ipv4, expected",
    [
        ("0.0.0.0", "00000000.00000000.00000000.00000000"),
        ("255.255.255.255", "11111111.11111111.11111111.11111111"),
        ("192.168.1.1", "11000000.10101000.00000001.00000001"),
        ("10.0.0.5", "00001010.00000000.00000000.00000101"),
    ],
)
def test_ipv4_to_binary(ipv4, expected):
    assert ipv4_to_binary(ipv4) == expected


@pytest.mark.parametrize(
    "binary, expected",
    [
        ("00000000.00000000.00000000.00000000", "0.0.0.0"),
        ("11111111.11111111.11111111.11111111", "255.255.255.255"),
        ("11000000.10101000.00000001.00000001", "192.168.1.1"),
        ("00001010.00000000.00000000.00000101", "10.0.0.5"),
    ],
)
def test_binary_to_ipv4(binary, expected):
    assert binary_to_ipv4(binary) == expected


@pytest.mark.parametrize("octet", range(256))
def test_round_trip_each_octet(octet):
    ipv4 = f"{octet}.0.127.255"
    assert binary_to_ipv4(ipv4_to_binary(ipv4)) == ipv4
