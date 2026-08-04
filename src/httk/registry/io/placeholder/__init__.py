"""Import-light registry shim for the placeholder module."""

# Reader, writer, and format-adapter registrations belong under the reserved
# io tier. Add only the relevant lazy registration when the module grows.
# from httk.core.register import register_reader
#
# register_reader(
#     name="placeholder",
#     reader="httk.placeholder.io:load",  # lazy "module:callable" — must exist when uncommented
#     extensions=(".placeholder",),
# )
