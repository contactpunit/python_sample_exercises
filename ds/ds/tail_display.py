def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    lines = []
    with open(filepath) as f:
        for line in f:
            lines.append(line.strip())
    return lines[len(lines) - n:]