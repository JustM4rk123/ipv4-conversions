from importlib.metadata import PackageNotFoundError, version

from .core import binary_to_ipv4, ipv4_to_binary

try:
    __version__ = version("ipv4-conversions")
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = ["__version__", "binary_to_ipv4", "ipv4_to_binary"]
