# *httk-[placeholder]*

*httk-[placeholder]* is a [*httk₂*](https://github.com/httk/httk2) module
template for [placeholder functionality]. Replace the placeholder namespace
and description as the module takes shape.

When instantiating the template, rename in all of:

- every `placeholder` occurrence in tracked files (`git grep placeholder`),
  including the package directories `src/httk/placeholder/` and
  `src/httk/registry/placeholder/` and the dataset identifier
  `"httk.placeholder.example_dataset"`;
- the bracketed `httk-[placeholder]` forms in this file (remove the brackets);
- the repository URL/name itself (this file and `.github/` reference the
  repository only implicitly, but `docs/versioning.toml` and `pyproject.toml`
  carry the distribution name).

## Description

This template starts a small httk module with packaged data and report-channel
diagnostics.

## Install

```console
python -m pip install httk-placeholder
```

For local development:

```console
python -m pip install -e ".[dev,docs]"
```

## Development

Use `make check` for formatting, type checks, and the default test profile.
Use `make ci` for the extended test profile as well. The default profile skips
tests marked `extended`; run `make test-extended` to select them explicitly.

## Reporting

Library code logs with `logging.getLogger(__name__)`, which places modules
under the `httk.*` reporting hierarchy. Applications call
`httk.core.report.configure_reporting` for console output; servers can collect
records per task with `httk.core.report.collect_reports`.

## Packaged datasets

Package data through `httk.core.DatasetLoader` and load it lazily on
first access. A plain JSON document yields `.data` with `.meta`/`.index` set
to `None`; a structured JSON-LD document yields `.meta` and, when it declares
indices, `.index`.

## Registry

When the module exposes a loader, adapter, command, provider, record, or schema,
add an import-light shim under the matching `httk.registry` tier. The template
includes an inactive loader example:

```python
# from httk.core.register import register_loader
#
# register_loader(
#     name="placeholder",
#     loader="httk.placeholder.io:load",  # lazy "module:callable" — must exist when uncommented
#     extensions=(".placeholder",),
# )
```

For entry-type schemas, use `register_entry_type_definition`; property schemas
use `register_property_definition`. See the
[httk-core documentation index](https://docs.httk.org/httk-core/) for registry
tiers, identity rules, and module layout.
