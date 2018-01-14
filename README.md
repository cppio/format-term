# format-term
ANSI escape codes in Python

## usage
`ansi(bold, underlined, inverse, foreground, background) => str`

By default `ansi()` does not actually change anything.
`bold`, `underlined`, and `inverse` can be set to `None` to signify no change, `True` to enable them, or `False` to disable them.
`foreground` and `background` can be set to an `int` in `colors` or `brightcolors`, or a `color` object for true color.

`reset()` will reset the terminal. It is equivalent to setting `bold`, `underlined`, and `inverse` to `False`, and setting `foreground` and `background` to `colors.default`.

### Convenience functions
`bold(string)`
`underlined(string)`
`inverse(string)`
`foreground(color, string)`
`background(color, string)`

These functions wrap a string and set the respective property.
