def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    if any(map(lambda x: x> 255 or x< 0, rgb)):
        raise ValueError()
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2]).upper()


print(rgb_to_hex((123, 0, 0)))