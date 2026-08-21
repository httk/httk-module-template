# Test tiers

The template uses three test tiers so correctness, deeper coverage, and
performance work remain easy to run separately.

Tier 1 is the default merge-validation suite: `pytest` and `make test` should
finish in minutes and stay within roughly 8 GiB total RSS on a 16 GiB machine.
The default profile skips full-depth cases marked `extended`.

Tier 2 is the end-of-project suite. Run `make test-extended` after larger
implementation work; it includes every test case and should fit within a
roughly ten-minute budget. Both test tiers run under the
`python -m httk.core.memguard` process-group guard. Set
`HTTK_TEST_MAX_RSS_GB` to override a guard limit when diagnosing a failure.

Tier 3 is the opt-in benchmark tier. Run `make benchmarks` to execute the
small harness in `benchmarks/`; performance-purposed code belongs there, not
in `tests/`. Benchmark code is excluded from pytest discovery and is not run
by `make check` or `make ci`.
