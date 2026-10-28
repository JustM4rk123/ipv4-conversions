import argparse
import sys

import questionary

from .core import binary_to_ipv4, ipv4_to_binary


def main():
    parser = argparse.ArgumentParser(prog="ipv4-conversions")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-d",
        "--to-decimal",
        dest="to_decimal",
        metavar="BINARY",
        type=str,
        help="Convert a binary IPv4 address to dotted-decimal notation",
    )
    group.add_argument(
        "-b",
        "--to-binary",
        dest="to_binary",
        metavar="DECIMAL",
        type=str,
        help="Convert a dotted-decimal IPv4 address to binary",
    )

    args = parser.parse_args()

    if args.to_decimal is not None:
        try:
            result = binary_to_ipv4(args.to_decimal)
        except ValueError as e:
            parser.error(str(e))
        print(f"The dotted-decimal equivalent of {args.to_decimal} is: {result}")
    elif args.to_binary is not None:
        try:
            result = ipv4_to_binary(args.to_binary)
        except ValueError as e:
            parser.error(str(e))
        print(f"The binary equivalent of {args.to_binary} is: {result}")
    else:
        conversion = questionary.select(
            "Which conversion do you want to perform?",
            choices=[
                "Binary address to dotted decimal",
                "Dotted decimal to binary address",
                "Exit",
            ],
        ).ask()

        match conversion:
            case "Binary address to dotted decimal":
                while True:
                    try:
                        binary = input(
                            "Insert four dotted 8-bit binary octets: "
                        ).strip()
                        print(
                            f"The dotted-decimal equivalent of {binary} is: "
                            f"{binary_to_ipv4(binary)}"
                        )
                    except ValueError as e:
                        print(f"Invalid input: {e}")
                    else:
                        break
            case "Dotted decimal to binary address":
                while True:
                    try:
                        ipv4 = input("Insert a dotted-decimal IPv4 address: ").strip()
                        print(
                            f"The binary address equivalent of {ipv4} is: "
                            f"{ipv4_to_binary(ipv4)}"
                        )
                    except ValueError as e:
                        print(f"Invalid input: {e}")
                    else:
                        break
            case "Exit":
                sys.exit("Program terminated")


if __name__ == "__main__":
    main()
