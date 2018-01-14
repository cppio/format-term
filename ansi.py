from collections import namedtuple

colors = namedtuple("colors", "black red green yellow blue magenta cyan white default")(0, 1, 2, 3, 4, 5, 6, 7, 9)
brightcolors = namedtuple("brightcolors", "black red green yellow blue magenta cyan white")(60, 61, 62, 63, 64, 65, 66, 67)
color = namedtuple("color", "r g b")
del namedtuple

def ansi(*, bold=None, underlined=None, inverse=None, foreground=None, background=None):
    params = []
    if bold is not None:
        assert isinstance(bold, bool)
        params.append("1" if bold else "22")
    if underlined is not None:
        assert isinstance(underlined, bool)
        params.append("4" if underlined else "24")
    if inverse is not None:
        assert isinstance(inverse, bool)
        params.append("7" if inverse else "27")
    if foreground is not None:
        if isinstance(foreground, color):
            assert isinstance(foreground.r, int) and isinstance(foreground.g, int) and isinstance(foreground.b, int) and 0 <= foreground.r < 256 and 0 <= foreground.g < 256 and 0 <= foreground.b < 256
            params.extend(str(i) for i in (38, 2) + foreground)
        else:
            assert foreground in colors or foreground in brightcolors
            params.append(str(foreground + 30))
    if background is not None:
        if isinstance(background, color):
            assert isinstance(background.r, int) and isinstance(background.g, int) and isinstance(background.b, int) and 0 <= background.r < 256 and 0 <= background.g < 256 and 0 <= background.b < 256
            params.extend(str(i) for i in (48, 2) + background)
        else:
            assert background in colors or background in brightcolors
            params.append(str(background + 40))
    if len(params) > 0:
        return "\x1b[" + ";".join(params) + "m"
    return ""

def reset():
    ansi(bold=False, underlined=False, inverse=False, foreground=colors.default, background=colors.default)

def bold(string):
    return ansi(bold=True) + string + ansi(bold=False)

def underlined(string):
    return ansi(underlined=True) + string + ansi(underlined=False)

def inverse(string):
    return ansi(inverse=True) + string + ansi(inverse=False)

def foreground(color, string):
    return ansi(foreground=color) + string + ansi(foreground=colors.default)

def background(color, string):
    return ansi(background=color) + string + ansi(background=colors.default)
