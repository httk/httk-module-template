"""Packaged example data loaded lazily through :class:`httk.core.DatasetLoader`.

The example is plain JSON, so its loader yields ``.data`` with ``.meta`` and
``.index`` set to ``None``; a structured JSON-LD document yields ``.meta`` and,
when it declares indices, ``.index``.
"""

import atexit
from contextlib import ExitStack
from functools import cache
from importlib.resources import as_file, files
from pathlib import Path

from httk.core import DatasetLoader

# Structured JSON-LD documents additionally expose ``.meta`` and ``.index``.
_RESOURCES = ExitStack()
atexit.register(_RESOURCES.close)


@cache
def _resource_path(name: str) -> Path:
    """Return a filesystem path for a packaged data file."""
    return _RESOURCES.enter_context(as_file(files(__package__).joinpath(name)))


@cache
def _example_dataset() -> DatasetLoader:
    """Declare the example dataset without reading it yet."""
    return DatasetLoader("httk.placeholder.example_dataset", _resource_path("example_dataset.json.gz"))
