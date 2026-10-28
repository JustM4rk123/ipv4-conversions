from bin_dec_conversions import binary_to_decimal, decimal_to_binary


def ipv4_to_binary(ipv4: str) -> str:
    """Convert a dotted-decimal IPv4 address to four 8-bit binary octets."""
    if not ipv4:
        raise ValueError("The input is empty. Enter an IPv4 address with four octets")

    octets = ipv4.split(".")
    if len(octets) != 4:
        raise ValueError(
            f"'{ipv4}' is not a valid IPv4 address: exactly four decimal octets are required"
        )

    binary_octets = []
    for octet in octets:
        if not octet or not octet.isascii() or not octet.isdigit():
            raise ValueError(
                f"'{ipv4}' is not a valid IPv4 address: "
                f"'{octet}' is not a decimal octet"
            )

        decimal = int(octet)
        if decimal > 255:
            raise ValueError(
                f"'{ipv4}' is not a valid IPv4 address: "
                f"octet '{octet}' is outside the range 0-255"
            )
        binary_octets.append(decimal_to_binary(decimal, 8))

    return ".".join(binary_octets)


def binary_to_ipv4(binary: str) -> str:
    """Convert four dotted 8-bit binary octets to a dotted-decimal IPv4 address."""
    if not binary:
        raise ValueError("The input is empty. Enter four 8-bit binary octets")

    octets = binary.split(".")
    if len(octets) != 4:
        raise ValueError(
            f"'{binary}' is not a valid IPv4 binary address: "
            "exactly four 8-bit binary octets are required"
        )

    decimal_octets = []
    for octet in octets:
        if len(octet) != 8:
            raise ValueError(
                f"'{binary}' is not a valid IPv4 binary address: "
                f"octet '{octet}' must contain exactly 8 bits"
            )
        decimal_octets.append(str(binary_to_decimal(octet)))

    return ".".join(decimal_octets)
