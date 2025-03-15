def rgb_to_ansi(r, g, b):
    if r == g == b:
        # Grayscale
        gray = int(round(0.2126 * r + 0.7152 * g + 0.0722 * b))
        if gray > 238:
            return 231
        else:
            return 232 + int(round(gray / 10.0))
    else:
        # Color cube
        return 16 + 36 * int(round(r / 255.0 * 5)) + 6 * int(round(g / 255.0 * 5)) + int(round(b / 255.0 * 5))

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def hex_to_ansi(hex_color):
    rgb = hex_to_rgb(hex_color)
    return rgb_to_ansi(*rgb)

ansi = rgb_to_ansi(112, 66, 20)
print(ansi)
print(f"\x1b[38;5;094mThis text is color {ansi}\033[0m")