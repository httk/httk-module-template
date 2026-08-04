"""Small API example backed by the packaged element dataset."""

import logging

from .data import _example_dataset

_LOGGER = logging.getLogger(__name__)
# Modules under ``httk.*`` automatically participate in the httk reporting
# channel; see :mod:`httk.core.report`.


def atomic_number(symbol: str) -> int | None:
    """Return the atomic number for a noble-gas symbol, or ``None`` if unknown."""
    number = _example_dataset().data.get(symbol)
    if number is None:
        _LOGGER.warning("unknown element symbol %r", symbol)
    return number
