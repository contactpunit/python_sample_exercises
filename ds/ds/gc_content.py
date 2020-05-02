from collections import Counter


def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    c = Counter(sequence.lower())
    total = sum([c[char] for char in 'atgc'])
    gc = sum([c[char] for char in 'gc'])
    return round(gc * 100 / total, 2)
