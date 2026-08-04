"""Show packaged data loading and collected httk diagnostics."""

from httk.core.report import collect_reports, configure_reporting

from httk.placeholder import atomic_number

# Applications opt into console diagnostics.
configure_reporting()

# The first API call loads the packaged dataset lazily.
print(f"He has atomic number {atomic_number('He')}.")

# Servers can collect the same report records for a response or task result.
with collect_reports() as collection:
    print(f"Unknown symbol result: {atomic_number('Xx')}")

for record in collection.records:
    print(f"Collected {record.levelname}: {record.getMessage()}")
