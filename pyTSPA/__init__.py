from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("pyTSPA_toolbox")
except PackageNotFoundError:
    __version__ = "0.0.2"

from .data import load_match_data, clean_data, data_profiling

__all__ = [
    "load_match_data",
    "clean_data",
    "data_profiling",
    "__version__",
]