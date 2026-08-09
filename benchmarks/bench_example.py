"""Run the small opt-in benchmark scaffold for the placeholder module."""

import argparse
import time
from collections.abc import Sequence

# Performance-purposed code belongs in benchmarks/, not tests/. This target is
# opt-in and is not part of either ``make check`` or ``make ci``.


def main(argv: Sequence[str] | None = None) -> int:
    """Run a trivial timed loop and report its elapsed time.

    :param argv: Command-line arguments, excluding the program name.
    :return: Zero on success.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--iterations", type=int, default=100_000)
    arguments = parser.parse_args(argv)

    started = time.perf_counter()
    total = 0
    for value in range(arguments.iterations):
        total += value
    elapsed = time.perf_counter() - started
    print(f"iterations={arguments.iterations} total={total} seconds={elapsed:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
