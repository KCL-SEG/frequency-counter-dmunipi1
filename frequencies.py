"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        if not isinstance(item, str):
            item = str(item)
        if item in frequencies:
            count = frequencies[item]
            count += 1
            frequencies.pop(item)
            frequencies[item] = count
        else:
            frequencies[item] = 1
    return frequencies
