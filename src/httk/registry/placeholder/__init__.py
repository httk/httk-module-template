"""Import-light registry shim for the placeholder module."""

# The four registry tiers are loaders, CLI commands, entry providers/records,
# and schemas. Add only the relevant lazy registration when the module grows.
# from httk.core.register import register_loader
#
# register_loader(
#     name="placeholder",
#     loader="httk.placeholder.io:load",  # lazy "module:callable" — must exist when uncommented
#     extensions=(".placeholder",),
# )
